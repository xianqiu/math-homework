__all__ = [
    'MultL1', 'MultL2', 'MultL3', 'MultL4', 'MultL5',
    'MultL6', 'MultL7', 'MultL8', #'MultL9', 'MultL10'
]

import numpy as np

from .utils import to_result


class MultL1(object):

    """
    乘法（非负） a*b
    """

    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        ops = [['×', '=']] * num
        return to_result(arr, ops)


class MultL2(object):

    """
    乘法 a*b
    """

    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        return MultL1(self._lb, self._ub).generate(num)


class MultL3(object):

    """
    乘法填空（非负） a×?=c 或 ?×b =c
    """
    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        arr[:, 1] = arr[:, 0] * arr[:, 1]
        ops = [['× __ =']] * num
        return to_result(arr, ops)

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        arr[:, 1] = arr[:, 0] * arr[:, 1]
        ops = [['=']] * num
        res = to_result(arr, ops)
        return ['__ × ' + res[i] for i in range(num)]

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL4(object):
    """
    乘法填空 a×?=c 或 ?×b =c
    """

    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        return MultL3(self._lb, self._ub).generate(num)


class MultL5(object):
    """
    除法基础（非负） c÷a
    注意：除数为0没有剔除，这是Feature。
    """

    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        arr[:, 0] = arr[:, 0] * arr[:, 1]
        ops = [['÷', '=']] * num
        return to_result(arr, ops)


class MultL6(object):
    """
    除法基础 c÷a
    注意：除数为0没有剔除，这是Feature。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        return MultL5(self._lb, self._ub).generate(num)


class MultL7(object):
    """
    除法填空（非负）c÷?=b 或 ?÷a=b
    注意：除数为0没有剔除，这是Feature。
    """

    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        arr[:, 0] = arr[:, 0] * arr[:, 1]
        ops = [['÷ __ =']] * num
        return to_result(arr, ops)

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub, (num, 2))
        ops = [['=']] * num
        res = to_result(arr, ops)
        return ['__ ÷ ' + res[i] for i in range(num)]

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL8(object):
    """
    除法填空 c÷?=b 或 ?÷a=b
    注意：除数为0没有剔除，这是Feature。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        return MultL7(self._lb, self._ub).generate(num)


