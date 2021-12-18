__all__ = ['MathL1', 'MathL2', 'MathL3', 'MathL4',
           'MathL5', 'MathL6', 'MathL7', 'MathL8',
           'MathL9',  'MathL10', 'MathL11', 'MathL12',
           'MathL13', 'MathL14', 'MathL15', 'MathL16',
           'MathL17', 'MathL18', 'MathL19', 'MathL20',
           'MathL21', 'MathL22', 'MathL23', 'MathL24',
           'MathL25', 'MathL26', 'MathL27'
           ]

import numpy as np


def _to_result(arr, ops, wrap=True, skip=None):
    """
    把公式格式化成字符串
    :param arr: 二维数组，每一行代表公式的数字，例如 [a, b]
    :param ops: 二维数组，每一行代表公式的操作，例如 [+, =]
    :param wrap: 自动加括号，例如 a + (-b)
    :return: str list，例如 ['a1 + b1 = ', 'a2 + b2 = ']
    """
    if skip is None:
        skip = {}
    res = []
    for row, op in zip(arr, ops):
        comb = []
        for i in range(len(row)):
            if wrap and row[i] < 0 and i not in skip:
                comb.append('(' + str(int(row[i])) + ')')
            else:
                comb.append(str(int(row[i])))
            if i < len(op):
                comb.append(op[i])
        res.append(' '.join(comb))
    return res


def _gen_add_arr(lb, ub, k, num):
    """ 生成二维数组。
    1、每行 k 个数，用来相加，绝对值不大于 ub。
    2、数组一共 num 行。
    3、每个数不超过 ub，不低于lb。
    """
    arr = np.random.randint(lb, ub, (num, k))
    for i in range(len(arr)):
        if abs(sum(arr[i])) > ub:
            arr[i] = np.floor(arr[i] / k)
    return arr


class MathL1(object):
    """
    L1：加法 a+b
    """
    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['+', '=']] * num
        return _to_result(arr, ops)


class MathL2(object):
    """
    L2：减法（结果为非负）a-b
    """
    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(0, self._ub, (num, 2))
        for i in range(len(arr)):
            if arr[i][0] < arr[i][1]:
                arr[i] = [arr[i][1], arr[i][0]]
        ops = [['-', '=']] * num
        return _to_result(arr, ops)


class MathL3(object):
    """
    L3：加减法 a+b 或 a-b（结果非负）
    """
    def __init__(self, ub=20):
        self._m1 = MathL1(ub)
        self._m2 = MathL2(ub)

    def generate(self, num):
        res0 = self._m1.generate(num) + self._m2.generate(num)
        indices = np.random.randint(0, len(res0), num)
        return [res0[i] for i in indices]


class MathL4(object):
    """
    L4：连加法 a+b+c
    """

    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [['+', '+', '=']] * num
        return _to_result(arr, ops)


class MathL5(object):
    """
    L5：连减法 a-b-c（结果非负）
    """

    def __init__(self, ub):
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(0, self._ub, (num, 2))
        b = [0] * num
        for i in range(len(arr)):
            if arr[i][0] < arr[i][1]:
                arr[i] = [arr[i][1], arr[i][0]]
                b[i] = np.random.randint(0, arr[i][0] - arr[i][1])
        arr = np.insert(arr, 2, values=b, axis=1)
        ops = [['-', '-', '=']] * num
        return _to_result(arr, ops)


class MathL6(object):
    """
    L6：连加 a+b+c 或 连减 a-b-c（结果非负）
    """

    def __init__(self, ub=30):
        self._m4 = MathL4(ub)
        self._m5 = MathL5(ub)

    def generate(self, num):
        res0 = self._m4.generate(num) + self._m5.generate(num)
        indices = np.random.randint(0, len(res0), num)
        return [res0[i] for i in indices]


class MathL7(object):
    """
    L7：连加减法 a+b-c 或 a-b+c 或 a+b+c（结果非负）
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [['']] * num
        for i in range(len(arr)):
            if arr[i][0] >= arr[i][1]:
                ops[i] = ['-', '+', '=']
            elif arr[i][1] >= arr[i][2]:
                ops[i] = ['+', '-', '=']
            else:
                ops[i] = ['+', '+', '=']
        return _to_result(arr, ops)


class MathL8(object):
    """
    L8: 减法 a - b
    """
    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['-', '=']] * num
        return _to_result(arr, ops)


class MathL9(object):
    """
    L9: 加法、减法：-a-b, -a+b, a-b
    """
    def __init__(self, ub=30):
        self._ub = ub

    def _generate1(self, num):
        # -a-b
        arr1 = _gen_add_arr(-self._ub//2, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub//2, 1, num)
        arr = map(lambda a: [a[0][0], a[1][0]], zip(arr1, arr2))
        ops = [['-', '=']] * num
        return _to_result(arr, ops, skip={0})

    def _generate2(self, num):
        # -a+b
        arr1 = _gen_add_arr(-self._ub, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub, 1, num)
        arr = map(lambda a: [a[0][0], a[1][0]], zip(arr1, arr2))
        ops = [['+', '=']] * num
        return _to_result(arr, ops, skip={0})

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res3 = MathL8(self._ub).generate(num)
        res = res1 + res2 + res3
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MathL10(object):
    """
    L10: 连加法 a-b-c, -a-b-c
    """
    def __init__(self, ub=30):
        self._ub = ub

    def _generate1(self, num):
        # a-b-c
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [['-', '-', '=']] * num
        return _to_result(arr, ops)

    def _generate2(self, num):
        # -a-b-c
        arr = _gen_add_arr(0, self._ub, 3, num)
        arr[:, 0] = arr[:, 0] * -1
        ops = [['-', '-', '=']] * num
        return _to_result(arr, ops, skip={0})

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res = res1 + res2
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MathL11(object):
    """
    L11: 连加减法 a+b-c 或 a-b+c
    """
    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [[]] * num
        for i in range(len(arr)):
            z = np.random.rand()
            ops[i] = ['+', '-', '='] if z < 0.3 else ['-', '+', '=']
        return _to_result(arr, ops)


class MathL12(object):
    """
    L12: 连加减法 -a+b-c 或 -a-b+c
    """
    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr1 = _gen_add_arr(-self._ub//2, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub, 2, num)
        arr = np.c_[arr1, arr2]
        ops = [[]] * num
        for i in range(len(arr)):
            z = np.random.rand()
            ops[i] = ['+', '-', '='] if z < 0.5 else ['-', '+', '=']
        return _to_result(arr, ops, skip={0})


class MathL13(object):
    """
    L13: 负负得正 a+(-b) 或 a-(-b)
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr1 = _gen_add_arr(0, self._ub//2, 1, num)
        arr2 = _gen_add_arr(-self._ub//2, -1, 1, num)
        arr = np.c_[arr1, arr2]
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '='] if z > 0.5 else ['-', '=']
        return _to_result(arr, ops)


class MathL14(object):
    """
    L14: 负负得正 -a+(-b) 或 -a-(-b)
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(-self._ub, 0, 2, num)
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '='] if z > 0.5 else ['-', '=']
        return _to_result(arr, ops, skip={0})


class MathL15(object):
    """
    L15: a+b+c, abc可以带负号
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+', '+', '=']] * num
        return _to_result(arr, ops, skip={0})


class MathL16(object):
    """
    L16: 加法填空 a+?=b
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['+ __ =']] * num
        return _to_result(arr, ops)


class MathL17(object):
    """
    L17: 减法填空 a-?=b
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['- __ =']] * num
        return _to_result(arr, ops)


class MathL18(object):
    """
    L18: 加减法填空 a+?=b 或 a-?=b
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['']] * num
        for i in range(len(arr)):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['- __ =']
            else:
                ops[i] = ['+ __ =']
        return _to_result(arr, ops)


class MathL19(object):
    """
    L19: 加后填空 a+b+?=c 或 a+b-?=c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '+ __ ='] if z < 0.4 else ['+', '- __ =']
        return _to_result(arr, ops)


class MathL20(object):
    """
    L20: 加法填空、减法填空 -a + ? = b 或 -a - ? = b
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr1 = _gen_add_arr(-self._ub, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub, 1, num)
        arr = np.c_[arr1, arr2]
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+ __ ='] if z < 0.4 else ['- __ =']
        return _to_result(arr, ops, skip={0})


class MathL21(object):
    """
    L21: 加减法填空 a-b+?=c 或 a-b-?=c
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['-', '+ __ ='] if z < 0.5 else ['-', '- __ =']
        return _to_result(arr, ops)


class MathL22(object):
    """
    L22: 加减法填空 -a-b+?=c 或 -a-b-?=c
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        arr[:, 0] = arr[:, 0] * -1
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['-', '+ __ ='] if z < 0.5 else ['-', '- __ =']
        return _to_result(arr, ops, skip={0})


class MathL23(object):
    """
    L23：加减法填空 -a+b+?=c 或 -a+b-?=c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        arr[:, 0] = arr[:, 0] * -1
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '+ __ ='] if z < 0.5 else ['+', '- __ =']
        return _to_result(arr, ops, skip={0})


class MathL24(object):
    """
    L24：加减法填空 -a+b+?=-c 或 -a-b+?=-c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        arr[:, 0] = arr[:, 0] * -1
        arr[:, 2] = arr[:, 2] * -1

        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '+ __ ='] if z < 0.5 else ['-', '+ __ =']

        return _to_result(arr, ops, skip={0, 2})


class MathL25(object):
    """
    L25：中间填空 a+?+b=c 或 a-?-b=c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)

        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+ __ +', '='] if z < 0.5 else ['- __ -', '=']

        return _to_result(arr, ops)


class MathL26(object):
    """
    L26：中间填空 -a+?+b=-c 或 -a-?-b=c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        arr[:, 0] = arr[:, 0] * -1
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+ __ +', '='] if z < 0.5 else ['- __ -', '=']
            if np.random.rand() < 0.5:
                arr[i][2] = arr[i][2] * -1

        return _to_result(arr, ops, skip={0, 2})


class MathL27(object):
    """
    L27：a+b+?=c 或 ?+a+b=c 或 a+?+b=c, abc可以带负号
    """
    def __init__(self, ub=40):
        self._ub = ub

    def _generate1(self, num):
        # a+b+?=c
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+', '+ __ =']] * num
        return _to_result(arr, ops, skip={0, 2})

    def _generate2(self, num):
        # ?+a+b=c
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+', '=']] * num
        res = _to_result(arr, ops, skip={2})
        return ['__ + ' + res[i] for i in range(num)]

    def _generate3(self, num):
        # a+?+b=c
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+ __ +', '=']] * num
        return _to_result(arr, ops, skip={0, 2})

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res3 = self._generate3(num)
        res = res1 + res2 + res3
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]
