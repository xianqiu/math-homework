__all__ = ['MathL1', 'MathL2', 'MathL3', 'MathL4',
           'MathL5', 'MathL6', 'MathL7', 'MathL8',
           'MathL9', 'MathL10', 'MathL11', 'MathL12',
           ]

import numpy as np


def _to_result(arr, ops):
    """
    把公式格式化成字符串
    :param arr: 二维数组，每一行代表公式的数字，例如 [a, b]
    :param ops: 二维数组，每一行代表公式的操作，例如 [+, =]
    :return: str list，例如 ['a1 + b1 = ', 'a2 + b2 = ']
    """
    res = []
    for row, op in zip(arr, ops):
        comb = []
        for i in range(len(row)):
            comb.append(str(int(row[i])))
            if i < len(op):
                comb.append(op[i])
        res.append(' '.join(comb))
    return res


def _gen_add_arr(lb, ub, k, num):
    """ 生成二维数组。
    1、每行 k 个数，用来相加，结果不大于 ub。
    2、数组一共 num 行。
    3、每个数不超过 ub，不低于lb。
    """
    arr = np.random.randint(lb, ub, (num, k))
    for i in range(len(arr)):
        if sum(arr[i]) > ub:
            arr[i] = np.floor(arr[i] / k)
    return arr


class MathL1(object):
    """
    L1：加法 a+b
    """
    def __init__(self, lb=0, ub=20):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 2, num)
        ops = [['+', '=']] * num
        return _to_result(arr, ops)


class MathL2(object):
    """
    L2：减法（结果为非负）a-b
    """
    def __init__(self, lb=0, ub=20):
        self._lb = lb
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
    def __init__(self, lb=0, ub=20):
        self._m1 = MathL1(lb, ub)
        self._m2 = MathL2(lb, ub)

    def generate(self, num):
        res0 = self._m1.generate(num) + self._m2.generate(num)
        indices = np.random.randint(0, len(res0), num)
        return [res0[i] for i in indices]


class MathL4(object):
    """
    L4：连加法 a+b+c
    """

    def __init__(self, lb=0, ub=30):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 3, num)
        ops = [['+', '+', '=']] * num
        return _to_result(arr, ops)


class MathL5(object):
    """
    L5：连减法 a-b-c（结果非负）
    """

    def __init__(self, lb, ub):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        b = [0] * num
        for i in range(len(arr)):
            if arr[i][0] < arr[i][1]:
                arr[i] = [arr[i][1], arr[i][0]]
                b[i] = np.random.randint(self._lb, arr[i][0] - arr[i][1])
        arr = np.insert(arr, 2, values=b, axis=1)
        ops = [['-', '-', '=']] * num
        return _to_result(arr, ops)


class MathL6(object):
    """
    L6：连加 a+b+c 或 连减 a-b-c（结果非负）
    """

    def __init__(self, lb=0, ub=30):
        self._m4 = MathL4(lb, ub)
        self._m5 = MathL5(lb, ub)

    def generate(self, num):
        res0 = self._m4.generate(num) + self._m5.generate(num)
        indices = np.random.randint(0, len(res0), num)
        return [res0[i] for i in indices]


class MathL7(object):
    """
    L7：连加减法 a+b-c 或 a-b+c 或 a+b+c（结果非负）
    """

    def __init__(self, lb=0, ub=40):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 3, num)
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
    L8: 减法 a - b（结果可以为负）
    """
    def __init__(self, lb=0, ub=30):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 2, num)
        ops = [['-', '=']] * num
        return _to_result(arr, ops)


class MathL9(object):
    """
    L9: 连加减法 a+b-c 或 a-b+c （结果可以为负）
    """
    def __init__(self, lb=0, ub=40):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 3, num)
        ops = [['']] * num
        for i in range(len(arr)):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['+', '-', '=']
            else:
                ops[i] = ['-', '+', '=']
        return _to_result(arr, ops)


class MathL10(object):
    """
    L10: 加法填空 a+?=b （?非负）
    """
    def __init__(self, lb=0, ub=40):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 2, num)
        for i in range(len(arr)):
            if arr[i][0] > arr[i][1]:
                arr[i] = [arr[i][1], arr[i][0]]
        ops = [['+ __ =']] * num
        return _to_result(arr, ops)


class MathL11(object):
    """
    L11: 减法填空 a-?=b （?非负）
    """
    def __init__(self, lb=0, ub=40):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 2, num)
        for i in range(len(arr)):
            if arr[i][0] < arr[i][1]:
                arr[i] = [arr[i][1], arr[i][0]]
        ops = [['- __ =']] * num
        return _to_result(arr, ops)


class MathL12(object):
    """
    L12: 加减法填空 a+?=b 或 a-?=b（?允许为负）
    """
    def __init__(self, lb=0, ub=40):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = _gen_add_arr(self._lb, self._ub, 2, num)
        ops = [['']] * num
        for i in range(len(arr)):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['- __ =']
            else:
                ops[i] = ['+ __ =']
        return _to_result(arr, ops)

