import numpy as np

from .utils import to_content, gen_arr, gen_ops, insert_placeholder


class AddL1(object):
    """
    加法 a+b, ab非负
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int')
        ops = [['+', '=']] * num
        return to_content(arr, ops)


class AddL2(object):
    """
    减法（结果为非负）a-b, ab非负
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):

        bc = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int'))
        b, c = bc[:, 0], bc[:, 1]
        a = b + c
        arr = np.array([a, b]).T
        ops = [['-', '=']] * num
        return to_content(arr, ops)


class AddL3(object):
    """
    加减法 a+b 或 a-b（结果非负）, ab非负
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):

        arr = []
        ops = []

        for i in range(num):
            if np.random.random() < 0.5:
                arr_item = gen_arr(m=1, n=2, lb=0, ub=self.ub,
                                   dtype='int')[0]
                op_item = ['+', '=']
            else:
                b, c = gen_arr(m=1, n=2, lb=0, ub=self.ub,
                                   dtype='int')[0]
                a = b + c
                arr_item = [a, b]
                op_item = ['-', '=']
            arr.append(arr_item)
            ops.append(op_item)

        return to_content(arr, ops)


class AddL4(object):
    """
    连加 a+b+c, ab非负
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=0, ub=self.ub,
                           dtype='int')
        ops = [['+', '+', '=']] * num
        return to_content(arr, ops)


class AddL5(object):
    """
    连减 a-b-c（结果非负）, abc非负
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        bcd = np.array(gen_arr(m=num, n=3, lb=0, ub=self.ub,
                dtype='int'))
        b, c, d = bcd[:, 0], bcd[:, 1], bcd[:, 2]
        a = b + c + d
        arr = np.array([a, b, c]).T
        ops = [['-', '-', '=']] * num
        return to_content(arr, ops)


class AddL6(object):
    """
    连加 a+b+c 或 连减 a-b-c（结果非负）, abc非负
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = []
        ops = []

        for i in range(num):
            if np.random.random() < 0.5:
                arr_item = gen_arr(m=1, n=3, lb=0, ub=self.ub,
                                   dtype='int')[0]
                op_item = ['+', '+', '=']
            else:
                b, c, d = gen_arr(m=1, n=3, lb=0, ub=self.ub,
                               dtype='int')[0]
                a = b + c + d
                arr_item = [a, b, c]
                op_item = ['-', '-', '=']
            arr.append(arr_item)
            ops.append(op_item)

        return to_content(arr, ops)


class AddL7(object):
    """
    连加减法 a+b-c （结果非负） 或 a-b+c （结果非负）或 a+b+c, abc非负
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):

        arr = []
        ops = []

        for i in range(num):
            temp = gen_arr(m=1, n=3, lb=0, ub=self.ub,
                                   dtype='int')[0]
            r = np.random.random()
            if r < 0.35:
                # a + b - c
                a, c, d = temp
                b = c + d
                arr_item = [a, b, c]
                op_item = ['+', '-', '=']
            elif r < 0.7:
                # a - b + c
                b, c, d = temp
                a = b + d
                arr_item = [a, b, c]
                op_item = ['-', '+', '=']
            else:
                arr_item = temp
                op_item = ['+', '+', '=']
            arr.append(arr_item)
            ops.append(op_item)

        return to_content(arr, ops)


class AddL8(object):
    """
    负数相加 -a-b, ab非负
    """

    def __init__(self):
        self.ub = 15

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                      dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                      dtype='int')

        arr = np.hstack((a, b))
        ops = [['-', '=']]* num

        return to_content(arr, ops)


class AddL9(object):
    """
    减法 a-b, -a+b, ab非负
    """
    def __init__(self):
        self.ub = 15

    def _gen1(self, num):
        # a-b
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                    dtype='int')
        ops = [['-', '=']] * num
        return to_content(arr, ops)

    def _gen2(self, num):
        # -a+b
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=-1,
                      dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a,b))
        ops = [['+', '=']] * num

        return to_content(arr, ops)

    def generate(self, num):
        half = num // 2
        res = self._gen1(half) + self._gen2(num-half)
        np.random.shuffle(res)
        return res


class AddL10(object):
    """
    加法、减法：-a-b, -a+b, a-b, ab非负
    """
    def __init__(self):
        self.ub = 15

    def _gen1(self, num):
        # -a-b
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=-1,
                    dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a,b))
        ops = [['-', '=']] * num
        return to_content(arr, ops)

    def _gen2(self, num):
        # -a+b
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=-1,
                    dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a, b))
        ops = [['+', '=']] * num
        return to_content(arr, ops)

    def _gen3(self, num):
        # a-b
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                    dtype='int')
        ops = [['-', '=']] * num
        return to_content(arr, ops)

    def generate(self, num):
        k = num // 3
        res = self._gen1(k) + self._gen2(k) + self._gen3(num- 2 * k)
        np.random.shuffle(res)

        return res


class AddL11(object):
    """
    连减 a-b-c, -a-b-c, abc非负
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                    dtype='int')
        bc = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a, bc))
        ops = [['-', '-', '=']] * num

        return to_content(arr, ops)


class AddL12(object):
    """
    连加减 a+b-c 或 a-b+c, abc非负
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=0, ub=self.ub,
                dtype='int')
        ops = gen_ops(m=num, n=2, chars=['+', '-'], has_eq=True)

        return to_content(arr, ops)


class AddL13(object):
    """
    连加减法 -a+b-c 或 -a-b+c, abc非负
    """
    def __init__(self):
        self.ub = 10

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=-1,
                    dtype='int')
        bc = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a, bc))
        ops = gen_ops(m=num, n=2, chars=['+', '-'], has_eq=True)

        return to_content(arr, ops)


class AddL14(object):
    """
    负负得正 a+(-b) 或 a-(-b), ab非负
    """
    def __init__(self):
        self.ub = 20

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        b = gen_arr(m=num, n=1, lb=-self.ub, ub=-1,
                    dtype='int')
        arr = np.hstack((a, b))
        ops = gen_ops(m=num, n=1, chars=['+', '-'], has_eq=True)

        return to_content(arr, ops)


class AddL15(object):
    """
    负负得正 -a+(-b) 或 -a-(-b), ab非负
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=-1,
                    dtype='int')
        ops = gen_ops(m=num, n=1, chars=['+', '-'], has_eq=True)

        return to_content(arr, ops)


class AddL16(object):
    """
    a+b+c, abc可以带负号
    """

    def __init__(self):
        self.ub = 15

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['+', '+', '=']] * num
        return to_content(arr, ops)


class AddL17(object):
    """
    加法填空 a+__=b, __+a=b ab非负
    """
    def __init__(self):
        self.ub = 40

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int')
        arr = insert_placeholder(arr)
        ops = [['+', '=']] * num
        return to_content(arr, ops)


class AddL18(object):
    """
    减法填空 a-__=b, __-a=b, ab非负
    """
    def __init__(self):
        self.ub = 40

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int')
        arr = insert_placeholder(arr)
        ops = [['-', '=']] * num
        return to_content(arr, ops)


class AddL19(object):
    """
    加减法填空 a+__=b 或 a-__=b, ab非负
    """
    def __init__(self):
        self.ub = 40

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int')
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=1, chars=['+', '-'], has_eq=True)
        return to_content(arr, ops)


class AddL20(object):
    """
    加减法填空 a @ __ = c, @ in {+,-}, abc非负，占位符位置随机
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int')
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=1, chars=['+', '-'], has_eq=True)
        return to_content(arr, ops)


class AddL21(object):
    """
    加法填空、减法填空 -a+__=b 或 -a-__=b, ab非负
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                    dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a, b))
        ops = gen_ops(m=num, n=1, chars=['+ __ =', '- __ ='])

        return to_content(arr, ops)


class AddL22(object):
    """
    加减法填空 a @ b @ __ = d @ in {+, -}, abd非负
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=0, ub=self.ub,
                      dtype='int')
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=2, chars=['+', '-'], has_eq=True)

        return to_content(arr, ops)


class AddL23(object):
    """
    加减法填空 a-b+__=c, a可以为负, 占位符位置随机
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                    dtype='int')
        bc = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                     dtype='int')
        arr = np.hstack((a, bc))
        arr = insert_placeholder(arr.tolist())
        ops = [['-', '+', '=']] * num

        return to_content(arr, ops)


class AddL24(object):
    """
    填空 a@b@__=d, @ in {+,-} abd可负
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int')
        arr = insert_placeholder(arr)
        ops = gen_ops(m=num, n=2, chars={'+', '-'}, has_eq=True)

        return to_content(arr, ops, skip={0, 3})