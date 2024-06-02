import numpy as np

from .utils import to_result, insert_placeholder


class MultL1(object):

    """
    乘法（非负） a*b
    """

    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
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
        return MultL1(self._lb, self._ub+1).generate(num)


class MultL3(object):

    """
    乘法填空（非负） a×?=c 或 ?×b =c
    """
    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
        arr[:, 1] = arr[:, 0] * arr[:, 1]
        ops = [['× __ =']] * num
        return to_result(arr, ops)

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
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

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        arr[:, 1] = arr[:, 0] * arr[:, 1]
        ops = [['× __ =']] * num
        return to_result(arr, ops, skip={0, 1})

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        arr[:, 1] = arr[:, 0] * arr[:, 1]
        ops = [['=']] * num
        res = to_result(arr, ops, skip={1})
        return ['__ × ' + res[i] for i in range(num)]

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL5(object):
    """
    除法基础（非负） c÷a
    注意：除数为0没有剔除，这是Feature。
    """

    def __init__(self, lb=0, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
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
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
        arr[:, 0] = arr[:, 0] * arr[:, 1]
        ops = [['÷ __ =']] * num
        return to_result(arr, ops)

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
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

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        arr[:, 0] = arr[:, 0] * arr[:, 1]
        ops = [['÷ __ =']] * num
        return to_result(arr, ops, skip={0, 1})

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        ops = [['=']] * num
        res = to_result(arr, ops, skip={1})
        return ['__ ÷ ' + res[i] for i in range(num)]

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL9(object):
    """
    四则运算 a×b+c×d 或 a×b-c×d
    abcd是一位数。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['×', '+', '×', '=']
            else:
                ops[i] = ['×', '-', '×', '=']
        return to_result(arr, ops)


class MultL10(object):
    """
    四则运算 a×?+c×d=e 或 a×b-?×d=e
    abcd是一位数。
    """

    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        a, b, c, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        e = a * b + c * d
        arr = np.array([a, c, d, e]).T
        ops = [['× __ + ', '×', '=']] * num
        return to_result(arr, ops, skip={0, 3})

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        a, b, c, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        e = a * b - c * d
        arr = np.array([a, b, d, e]).T
        ops = [['×', '- __ ×', '=']] * num
        return to_result(arr, ops, skip={0, 3})

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL11(object):
    """
    四则运算 a×b+c÷d 或 a×b-c÷d
    abd是一位数。
    """

    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        a, b, e, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        c = d * e
        arr = np.array([a, b, c, d]).T
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['×', '+', '÷', '=']
            else:
                ops[i] = ['×', '-', '÷', '=']
        return to_result(arr, ops, skip={0})


class MultL12(object):
    """
    四则运算填空 a×?+c÷d=e 或 a×b-c÷?=e 或 a×b+?÷d=e
    abd是一位数。
    注意：除数为0没有剔除，这是Feature。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        a, b, f, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        c = f * d
        e = a * b + f
        arr = np.array([a, c, d, e]).T
        ops = [['× __ +', '÷', '=']] * num
        return to_result(arr, ops, skip={0, 3})

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        a, b, f, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        c = f * d
        e = a * b - f
        arr = np.array([a, b, c, e]).T
        ops = [['×', '-', '÷ __ =']] * num
        return to_result(arr, ops, skip={0, 3})

    def _gen3(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 4))
        a, b, f, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        e = a * b + f
        arr = np.array([a, b, d, e]).T
        ops = [['×', '+ __ ÷', '=']] * num
        return to_result(arr, ops, skip={0, 3})

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num) + self._gen3(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL13(object):
    """
    四则运算 (a+b)×c 或 a×(b+c)
    abc是一位数。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        arr = np.random.randint(self._lb, self._ub+1, (num, 2))
        a, c = arr[:, 0], arr[:, 1]
        b = np.random.randint(0, self._ub+1, num)
        arr = np.array([a, b, c]).T
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['+', '×', '=']
            else:
                ops[i] = ['-', '×', '=']
        return to_result(arr, ops, skip={0}, cc=[(0, 2)])

    def _gen2(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        a, b = arr[:, 0], arr[:, 1]
        c = np.random.randint(0, self._ub + 1, num)
        arr = np.array([a, b, c]).T
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            if z > 0.5:
                ops[i] = ['×', '+', '=']
            else:
                ops[i] = ['×', '-', '=']
        return to_result(arr, ops, skip={0, 1}, cc=[(2, 4)])

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL14(object):
    """
    四则填空 (a+?)×c=d 或 (a+b)×?=d
    abcd是一位数。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        # (a +?)×c = d
        arr = np.random.randint(self._lb, self._ub + 1, (num, 3))
        a, b, c = arr[:, 0], arr[:, 1], arr[:, 2]
        d = (a + b) * c
        ops = [[]] * num
        for i in range(num):
            ops[i] = ['+', '×', '=']
            z = np.random.rand()
            if z > 0.5:
                ops[i][0] = '-'
        arr = np.array([a, c, d]).T
        arr = insert_placeholder(arr, 1)
        return to_result(arr, ops, skip={0, 3}, cc=[(0, 2)])

    def _gen2(self, num):
        # (a + b)×?=d
        arr = np.random.randint(self._lb, self._ub + 1, (num, 3))
        a, b, c = arr[:, 0], arr[:, 1], arr[:, 2]
        d = (a + b) * c
        ops = [[]] * num
        for i in range(num):
            ops[i] = ['+', '×', '=']
            if b[i] < 0:
                b[i] *= -1
                ops[i][0] = '-'
        arr = np.array([a, b, d]).T
        arr = insert_placeholder(arr, 2)
        return to_result(arr, ops, skip={0, 3}, cc=[(0, 2)])

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL15(object):
    """
    四则运算 (a+b)×(c+d)
    abcd是一位数。
    """

    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 4))
        ops = [[]] * num
        for i in range(num):
            z = np.random.rand()
            op1 = '+' if z > 0.5 else '-'
            z = np.random.rand()
            op2 = '+' if z > 0.5 else '-'
            ops[i] = [op1, '×', op2, '=']
        return to_result(arr, ops, skip={0, 2}, cc=[(0, 2), (4, 6)])


class MultL16(object):
    """
    四则填空 (a+?)×(c+d)=e 或 (a+b)×(?+d)=e
    abcd是一位数。
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def _gen1(self, num):
        # (a+?)×(c+d)=e
        arr = np.random.randint(self._lb, self._ub + 1, (num, 4))
        a, b, c, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        ops = [[]] * num
        e = (a + b) * (c + d)
        for i in range(num):
            ops[i] = ['+', '×', '+', '=']
            z = np.random.rand()
            if z > 0.5:
                ops[i][0] = '-'
            if d[i] < 0:
                d[i] *= -1
                ops[i][2] = '-'
        arr = np.array([a, c, d, e]).T
        arr = insert_placeholder(arr, 1)
        return to_result(arr, ops, skip={0, 2, 4}, cc=[(0, 2), (4, 6)])

    def _gen2(self, num):
        # (a+b)×(?+d)=e
        arr = np.random.randint(self._lb, self._ub + 1, (num, 4))
        a, b, c, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        ops = [[]] * num
        e = (a + b) * (c + d)
        for i in range(num):
            ops[i] = ['+', '×', '+', '=']
            if b[i] < 0:
                b[i] *= -1
                ops[i][0] = '-'
            if d[i] < 0:
                d[i] *= -1
                ops[i][2] = '-'
        arr = np.array([a, b, d, e]).T
        arr = insert_placeholder(arr, 2)
        return to_result(arr, ops, skip={0, 2, 4}, cc=[(0, 2), (4, 6)])

    def generate(self, num):
        res = self._gen1(num) + self._gen2(num)
        indices = np.random.randint(0, len(res), num)
        return [res[i] for i in indices]


class MultL17(object):
    """
    连乘 a×b×c，abc是1位数
    """
    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 3))
        ops = [['×', '×', '=']] * num
        return to_result(arr, ops, skip={0})


class MultL18(object):
    """
    连乘填空 ?×b×c=d 或 a×?×c=d 或 a×b×?=d
    abc是1位数
    """

    def __init__(self, lb=-9, ub=9):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 3))
        a, b, c = arr[:, 0], arr[:, 1], arr[:, 2]
        d = a * b * c
        arr = np.array([b, c, d]).T
        arr1 = insert_placeholder(arr, 0)
        arr2 = insert_placeholder(arr, 1)
        arr3 = insert_placeholder(arr, 2)
        arr = arr1 + arr2 + arr3
        indices = np.random.randint(0, len(arr), num)
        arr = [arr[i] for i in indices]
        ops = [['×', '×', '=']] * num
        return to_result(arr, ops, skip={0, 3})


class MultL19(object):
    """
    乘法 a×b
    ab是两位数
    """

    def __init__(self, lb=-30, ub=30):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        ops = [['×', '=']] * num
        return to_result(arr, ops, skip={0})


class MultL20(object):
    """
    乘法填空 a×?=c 或 ?×b=c
    ab是两位数
    """

    def __init__(self, lb=-30, ub=30):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        a, b = arr[:, 0], arr[:, 1]
        c = a * b
        ops = [['×', '=']] * num
        arr = np.array([b, c]).T
        arr1 = insert_placeholder(arr, 0)
        arr2 = insert_placeholder(arr, 1)
        arr = arr1 + arr2
        indices = np.random.randint(0, len(arr), num)
        arr = [arr[i] for i in indices]
        return to_result(arr, ops, skip={0, 2})


class MultL21(object):
    """
    除法 a÷b
    b是两位数
    """

    def __init__(self, lb=-30, ub=30):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        b, c = arr[:, 0], arr[:, 1]
        a = b * c
        arr = np.array([a, b]).T
        ops = [['÷', '=']] * num
        return to_result(arr, ops, skip={0})


class MultL22(object):
    """
    除法填空 a÷?=c 或 ?÷b=c
    bc是两位数
    """

    def __init__(self, lb=-30, ub=30):
        self._lb = lb
        self._ub = ub

    def generate(self, num):
        arr = np.random.randint(self._lb, self._ub + 1, (num, 2))
        b, c = arr[:, 0], arr[:, 1]
        a = b * c
        ops = [['÷', '=']] * num
        arr = np.array([a, c]).T
        arr1 = insert_placeholder(arr, 1)
        arr = np.array([b, c]).T
        arr2 = insert_placeholder(arr, 0)
        arr = arr1 + arr2
        indices = np.random.randint(0, len(arr), num)
        arr = [arr[i] for i in indices]
        return to_result(arr, ops, skip={0, 2})