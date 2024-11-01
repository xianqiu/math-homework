import numpy as np

from .utils import to_content, gen_ops, gen_arr, insert_placeholder


class FracL1(object):
    """
    加减法 a+b, a-b, ab是分数，非负
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='frac')
        ops = gen_ops(m=num, n=1, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops)


class FracL2(object):
    """
    连加减 a+b-c, a-b+c, abc是分数，非负
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=0, ub=self.ub,
                      dtype='frac')
        ops = gen_ops(m=num, n=2, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops)


class FracL3(object):
    """
    加减法填空 a @ __ @ b=c, @ in {+,-} , abc是分数, 占位符位置随机
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=0, ub=self.ub,
                      dtype='frac')
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=2, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops)


class FracL4(object):
    """
    乘法 a×b=, ab是分数
    """
    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                      dtype='frac')
        ops = [['×', '=']] * num
        return to_content(arr, ops)


class FracL5(object):
    """
    除法 a÷b=, ab是分数
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                      dtype='frac')
        ops = [['÷', '=']] * num
        return to_content(arr, ops)


class FracL6(object):
    """
    乘除法 a×b÷c=, a÷b×c=, abc是分数
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='frac')
        ops = gen_ops(m=num, n=2, chars={'×', '÷'}, has_eq=True)
        return to_content(arr, ops)


class FracL7(object):
    """
    乘除法填空 a@?@b=c, @ in {×,÷}, abc是分数，占位符位置随机
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='frac')
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=2, chars={'×', '÷'}, has_eq=True)

        return to_content(arr, ops, skip={0, 3})


class FracL8(object):
    """
    四则运算 a@b@c@d=, @ in {+,-,×,÷}
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='frac')
        ops = gen_ops(m=num, n=3, chars={'+', '-', '×', '÷'}, has_eq=True)

        return to_content(arr, ops)


class FracL9(object):
    """
    四则填空 a@__@b@c=d, @ in {+,-,×,÷}, 占位符位置随机
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='frac')
        # 随机插入占位符'__'
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=3, chars={'+', '-', '×', '÷'}, has_eq=True)

        return to_content(arr, ops, skip={0, 4})

class FracL10(object):
    """
    加减法 a+b=, a-b=, ab是1位小数
    """
    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1)
        ops = gen_ops(m=num, n=1, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops)

class FracL11(object):
    """
    加减法 a @ b @ c=, @ in {+, -} abc是小数
    """
    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1)
        ops = gen_ops(m=num, n=2, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops)


class FracL12(object):
    """
    加减法填空 a@b@__=c, @ in {+, -} abc是两位小数，占位符位置随机
    """
    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=2)
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=2, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops, skip={0, 3})


class FracL13(object):
    """
    乘法 a×b=, ab是1位小数
    """
    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1)
        ops = [['×', '=']] * num

        return to_content(arr, ops)


class FracL14(object):
    """
    除法 a÷b=, b是1位小数
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        bc = np.array(gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                     dtype='float', dec=1))
        b, c = bc[:, 0], bc[:, 1]
        a = np.round(b * c, 2)
        arr = np.array([a, b]).T
        ops = [['÷', '=']] * num

        return to_content(arr, ops)


class FracL15(object):
    """
    乘除法 a×b÷c=, ac是1位小数
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        acd = np.array(gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1))
        a, c, d = acd[:, 0], acd[:, 1], acd[:, 2]
        b = np.round(c * d, 2)
        arr = np.array([a, b, c]).T
        ops = [['×', '÷', '=']] * num

        return to_content(arr, ops)


class FracL16(object):
    """
    乘除法填空 a×b÷__=c, ac是1位小数，占位符位置随机
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        acd = np.array(gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                               dtype='float', dec=1))
        a, c, d = acd[:, 0], acd[:, 1], acd[:, 2]
        b = np.round(c * d, 2)
        arr = np.array([a, b, c]).T
        arr = arr.tolist()
        arr = insert_placeholder(arr)
        ops = [['×', '÷', '=']] * num

        return to_content(arr, ops, skip={0, 3})


class FracL17(object):
    """
    四则运算 a@b@c@d=, @ in {+,-,×,÷}
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1)
        ops = gen_ops(m=num, n=3, chars={'+', '-', '×', '÷'}, has_eq=True)

        for i in range(num):
            for j in range(3):
                if ops[i][j] == '÷':
                    arr[i][j] *= arr[i][j+1]
                    arr[i][j] = np.round(arr[i][j], 2)
                    break

        return to_content(arr, ops)


class FracL18(object):
    """
    四则填空 a@?@b@c=d, @ in {+,-,×,÷}, abcd是小数，占位符位置随机
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1)
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=3, chars={'+', '-', '×', '÷'}, has_eq=True)

        for i in range(num):
            for j in range(3):
                if ops[i][j] == '÷' and arr[i][j] != '__' and arr[i][j+1] != '__':
                    arr[i][j] *= arr[i][j+1]
                    arr[i][j] = np.round(arr[i][j], 2)
                    break

        return to_content(arr, ops, skip={0, 4})