import numpy as np

from .utils import to_content, gen_arr, gen_ops, add_chars

class FuncL1(object):
    """
    ab 是整数, n 是 整数/分数/小数
    f(x) = ax + b
    f(n) =
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):

        ab = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x)"]] * num, ab))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num

        n1 = gen_arr(m=num//3+1, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        n2 = gen_arr(m=num//3+1, n=1, lb=-self.ub, ub=self.ub, dtype='float', dec=1)
        n3 = gen_arr(m=num//3+1, n=1, lb=-self.ub, ub=self.ub, dtype='frac')

        n = n1 + n2 + n3
        np.random.shuffle(n)
        n = n[0: num]
        arr2 = [[f"f({val[0]})"] for val in n]
        ops2 = [["="]] * num

        arr = []
        for p in zip(arr1, arr2):
            arr.append(p[0])
            arr.append(p[1])

        ops = []
        for p in zip(ops1, ops2):
            ops.append(p[0])
            ops.append(p[1])

        return to_content(arr, ops)