import numpy as np

from .utils import to_result


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


class AddL1(object):
    """
    加法 a+b
    """
    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['+', '=']] * num
        return to_result(arr, ops)


class AddL2(object):
    """
    减法（结果为非负）a-b
    """
    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(0, self._ub, (num, 2))
        for i in range(len(arr)):
            if arr[i][0] < arr[i][1]:
                arr[i] = [arr[i][1], arr[i][0]]
        ops = [['-', '=']] * num
        return to_result(arr, ops)


class AddL3(object):
    """
    加减法 a+b 或 a-b（结果非负）
    """
    def __init__(self, ub=20):
        self._m1 = AddL1(ub)
        self._m2 = AddL2(ub)

    def generate(self, num):
        res0 = self._m1.generate(num) + self._m2.generate(num)
        indices = np.random.randint(0, len(res0), num)
        return [res0[i] for i in indices]


class AddL4(object):
    """
    连加法 a+b+c
    """

    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [['+', '+', '=']] * num
        return to_result(arr, ops)


class AddL5(object):
    """
    连减法 a-b-c（结果非负）
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
        return to_result(arr, ops)


class AddL6(object):
    """
    连加 a+b+c 或 连减 a-b-c（结果非负）
    """

    def __init__(self, ub=30):
        self._m4 = AddL4(ub)
        self._m5 = AddL5(ub)

    def generate(self, num):
        res0 = self._m4.generate(num) + self._m5.generate(num)
        indices = np.random.randint(0, len(res0), num)
        return [res0[i] for i in indices]


class AddL7(object):
    """
    连加减法 a+b-c 或 a-b+c 或 a+b+c（结果非负）
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
        return to_result(arr, ops)


class AddL8(object):
    """
    负数相加 - a - b
    """

    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr1 = _gen_add_arr(-self._ub // 2, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub // 2, 1, num)
        arr = map(lambda a: [a[0][0], a[1][0]], zip(arr1, arr2))
        ops = [['-', '=']] * num
        return to_result(arr, ops, skip={0})


class AddL9(object):
    """
    减法 a-b, -a+b
    """
    def __init__(self, ub=30):
        self._ub = ub

    def _generate1(self, num):
        # a-b
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['-', '=']] * num
        return to_result(arr, ops)

    def _generate2(self, num):
        # -a+b
        arr1 = _gen_add_arr(-self._ub, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub, 1, num)
        arr = map(lambda a: [a[0][0], a[1][0]], zip(arr1, arr2))
        ops = [['+', '=']] * num
        return to_result(arr, ops, skip={0})

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res = res1 + res2
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class AddL10(object):
    """
    加法、减法：-a-b, -a+b, a-b
    """
    def __init__(self, ub=30):
        self._ub = ub

    def _generate1(self, num):
        # -a-b
        arr1 = _gen_add_arr(-self._ub // 2, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub // 2, 1, num)
        arr = map(lambda a: [a[0][0], a[1][0]], zip(arr1, arr2))
        ops = [['-', '=']] * num
        return to_result(arr, ops, skip={0})

    def _generate2(self, num):
        # -a+b
        arr1 = _gen_add_arr(-self._ub, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub, 1, num)
        arr = map(lambda a: [a[0][0], a[1][0]], zip(arr1, arr2))
        ops = [['+', '=']] * num
        return to_result(arr, ops, skip={0})

    def _generate3(self, num):
        # a-b
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['-', '=']] * num
        return to_result(arr, ops)

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res3 = self._generate3(num)
        res = res1 + res2 + res3
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class AddL11(object):
    """
    连加法 a-b-c, -a-b-c
    """
    def __init__(self, ub=30):
        self._ub = ub

    def _generate1(self, num):
        # a-b-c
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [['-', '-', '=']] * num
        return to_result(arr, ops)

    def _generate2(self, num):
        # -a-b-c
        arr = _gen_add_arr(0, self._ub, 3, num)
        arr[:, 0] = arr[:, 0] * -1
        ops = [['-', '-', '=']] * num
        return to_result(arr, ops, skip={0})

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res = res1 + res2
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class AddL12(object):
    """
    连加减法 a+b-c 或 a-b+c
    """
    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [[]] * num
        for i in range(len(arr)):
            z = np.random.rand()
            ops[i] = ['+', '-', '='] if z < 0.3 else ['-', '+', '=']
        return to_result(arr, ops)


class AddL13(object):
    """
    连加减法 -a+b-c 或 -a-b+c
    """
    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        arr1 = _gen_add_arr(-self._ub // 2, 0, 1, num)
        arr2 = _gen_add_arr(0, self._ub, 2, num)
        arr = np.c_[arr1, arr2]
        ops = [[]] * num
        for i in range(len(arr)):
            z = np.random.rand()
            ops[i] = ['+', '-', '='] if z < 0.5 else ['-', '+', '=']
        return to_result(arr, ops, skip={0})


class AddL14(object):
    """
    负负得正 a+(-b) 或 a-(-b)
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr1 = _gen_add_arr(0, self._ub // 2, 1, num)
        arr2 = _gen_add_arr(-self._ub // 2, -1, 1, num)
        arr = np.c_[arr1, arr2]
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '='] if z > 0.5 else ['-', '=']
        return to_result(arr, ops)


class AddL15(object):
    """
    负负得正 -a+(-b) 或 -a-(-b)
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(-self._ub, 0, 2, num)
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '='] if z > 0.5 else ['-', '=']
        return to_result(arr, ops, skip={0})


class AddL16(object):
    """
    a+b+c, abc可以带负号
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+', '+', '=']] * num
        return to_result(arr, ops, skip={0})


class AddL17(object):
    """
    加法填空 a+?=b
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['+ __ =']] * num
        return to_result(arr, ops)


class AddL18(object):
    """
    减法填空 a-?=b
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 2, num)
        ops = [['- __ =']] * num
        return to_result(arr, ops)


class AddL19(object):
    """
    加减法填空 a+?=b 或 a-?=b
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
        return to_result(arr, ops)


class AddL20(object):
    """
    加后填空 a+b+?=c 或 a+b-?=c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+', '+ __ ='] if z < 0.4 else ['+', '- __ =']
        return to_result(arr, ops)


class AddL21(object):
    """
    加法填空、减法填空 -a + ? = b 或 -a - ? = b
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
        return to_result(arr, ops, skip={0})


class AddL22(object):
    """
    加减法填空 a-b+?=c 或 a-b-?=c
    """

    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['-', '+ __ ='] if z < 0.5 else ['-', '- __ =']
        return to_result(arr, ops)


class AddL23(object):
    """
    加减法填空 -a-b+?=c 或 -a-b-?=c
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
        return to_result(arr, ops, skip={0})


class AddL24(object):
    """
    加减法填空 -a+b+?=c 或 -a+b-?=c
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
        return to_result(arr, ops, skip={0})


class AddL25(object):
    """
    加减法填空 -a+b+?=-c 或 -a-b+?=-c
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

        return to_result(arr, ops, skip={0, 2})


class AddL26(object):
    """
    中间填空 a+?+b=c 或 a-?-b=c
    """
    def __init__(self, ub=40):
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(0, self._ub, 3, num)

        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            ops[i] = ['+ __ +', '='] if z < 0.5 else ['- __ -', '=']

        return to_result(arr, ops)


class AddL27(object):
    """
    中间填空 -a+?+b=-c 或 -a-?-b=c
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

        return to_result(arr, ops, skip={0, 2})


class AddL28(object):
    """
    a+b+?=c 或 ?+a+b=c 或 a+?+b=c, abc可以带负号
    """
    def __init__(self, ub=40):
        self._ub = ub

    def _generate1(self, num):
        # a+b+?=c
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+', '+ __ =']] * num
        return to_result(arr, ops, skip={0, 2})

    def _generate2(self, num):
        # ?+a+b=c
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+', '=']] * num
        res = to_result(arr, ops, skip={2})
        return ['__ + ' + res[i] for i in range(num)]

    def _generate3(self, num):
        # a+?+b=c
        arr = _gen_add_arr(-self._ub, self._ub, 3, num)
        ops = [['+ __ +', '=']] * num
        return to_result(arr, ops, skip={0, 2})

    def generate(self, num):
        res1 = self._generate1(num)
        res2 = self._generate2(num)
        res3 = self._generate3(num)
        res = res1 + res2 + res3
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]

