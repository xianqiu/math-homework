import numpy as np

from .utils import to_content, gen_arr, gen_ops, add_chars, add_sep


class FuncL1(object):
    """
    ab 是整数, n 是 整数/分数/小数
    f(x) = ax + b
    f(n) =
    """
    pageCapacity = 14

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

        content = to_content(arr, ops)
        content = add_sep(content, gap=2, page_capacity=self.pageCapacity)

        return content


class FuncL2(object):

    """ 解方程：abcde是整数
    f(x) = ax + b
    cf(x) + dx = e
    """

    pageCapacity = 14

    def __init__(self):
        self.ub = 30

    def generate(self, num):

        ab = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x)"]] * num, ab))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num

        cde = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = add_chars(cde, ["f(x)", "x"])
        ops2 = [["+", "="]] * num

        arr = []
        for p in zip(arr1, arr2):
            arr.append(p[0])
            arr.append(p[1])

        ops = []
        for p in zip(ops1, ops2):
            ops.append(p[0])
            ops.append(p[1])

        content = to_content(arr, ops)
        content = add_sep(content, gap=2, page_capacity=self.pageCapacity)

        return content


class FuncL3(object):

    """ 解方程: abcv是整数
    f(x) = ax + b
    g(x) = c/x + v
    df(x) + xg(x) = 0
    """

    pageCapacity = 15

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr1 = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x)"]] * num, arr1))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num

        arr2 = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["g(x)"]] * num, arr2))
        arr2 = add_chars(arr2, ["", "/x"])
        ops2 = [["=", "+"]] * num

        d = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        arr3 = np.hstack((d, [["xg(x)"]] * num, [["0"]]*num))
        arr3 = add_chars(arr3, ["f(x)"])
        ops3 = [["+", "="]] * num

        arr = []
        for p in zip(arr1, arr2, arr3):
            arr.append(p[0])
            arr.append(p[1])
            arr.append(p[2])

        ops = []
        for p in zip(ops1, ops2, ops3):
            ops.append(p[0])
            ops.append(p[1])
            ops.append(p[2])

        content = to_content(arr, ops)
        content = add_sep(content, gap=3, page_capacity=self.pageCapacity)

        return content


class FuncL4(object):

    """ 解方程: acd是整数, u是正整数
    f(x) = ax^2
    g(x) = x/u
    f(x) / g(x) = cx + d
    """

    pageCapacity = 15

    def __init__(self):
        self.ub = 30

    def generate(self, num):

        arr1 = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x)"]] * num, arr1))
        arr1 = add_chars(arr1, ["", "x^2"])
        ops1 = [["="]] * num

        arr2 = gen_arr(m=num, n=1, lb=0, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["g(x)", "x"]] * num, arr2))
        ops2 = [["=", "/"]] * num

        cd = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr3 = np.hstack(([["f(x) / g(x)"]] * num, cd))
        arr3 = add_chars(arr3, ["", "x"])
        ops3 = [["=", "+"]] * num

        arr = []
        for p in zip(arr1, arr2, arr3):
            arr.append(p[0])
            arr.append(p[1])
            arr.append(p[2])

        ops = []
        for p in zip(ops1, ops2, ops3):
            ops.append(p[0])
            ops.append(p[1])
            ops.append(p[2])

        content = to_content(arr, ops,skip={1})
        content = add_sep(content, gap=3, page_capacity=self.pageCapacity)
        return content


class FuncL5(object):
    """ 解方程: abc是正整数
    f(x) = ax+b
    g(x) = ax-b
    f(x)g(x) = c
    """
    pageCapacity = 15

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        abc = np.array(gen_arr(m=num, n=3, lb=1, ub=self.ub, dtype='int'))
        a, b, c = abc[:, 0].reshape(-1, 1), abc[:, 1].reshape(-1, 1), abc[:, 2].reshape(-1, 1)
        arr1 = np.hstack(([["f(x)"]] * num, a, b))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num

        arr2 = np.hstack(([["g(x)"]] * num, a, b))
        arr2 = add_chars(arr2, ["", "x"])
        ops2 = [["=", "-"]] * num

        arr3 = np.hstack(([["f(x)g(x)"]] * num, c))
        ops3 = [["="]] * num

        arr = []
        for p in zip(arr1, arr2, arr3):
            arr.append(p[0])
            arr.append(p[1])
            arr.append(p[2])

        ops = []
        for p in zip(ops1, ops2, ops3):
            ops.append(p[0])
            ops.append(p[1])
            ops.append(p[2])

        content = to_content(arr, ops)
        content = add_sep(content, gap=3, page_capacity=self.pageCapacity)
        return content


class FuncL6(object):
    """ 解决二元一次方程: abcd是整数
    f(x,y)=ax+by+c
    g(x,y)=dx+dy+f
    f(x,y)=g(x,y)=0
    """
    pageCapacity = 15

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr1 = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x,y)"]] * num, arr1))
        arr1 = add_chars(arr1, ["", "x", "y"])
        ops1 = [["=", "+", "+"]] * num

        arr2 = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["g(x,y)"]] * num, arr2))
        arr2 = add_chars(arr2, ["", "x", "y"])
        ops2 = [["=", "+", "+"]] * num

        arr3 = [["f(x,y)", "g(x,y)", "0"]] * num
        ops3 = [["=", "="]] * num

        arr = []
        for p in zip(arr1, arr2, arr3):
            arr.append(p[0])
            arr.append(p[1])
            arr.append(p[2])

        ops = []
        for p in zip(ops1, ops2, ops3):
            ops.append(p[0])
            ops.append(p[1])
            ops.append(p[2])

        content = to_content(arr, ops, skip={1})
        content = add_sep(content, gap=3, page_capacity=self.pageCapacity)
        return content


class FuncL7(object):
    """ 解方程: abc是整数
    f(x) = ax+b
    f(f(x)) = c
    """
    pageCapacity = 14

    def __init__(self):
        self.ub = 20

    def generate(self, num):

        arr1 = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x)"]] * num, arr1))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num

        arr2 = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["f(f(x))"]] * num, arr2))
        ops2 = [["="]] * num

        arr = []
        for p in zip(arr1, arr2):
            arr.append(p[0])
            arr.append(p[1])

        ops = []
        for p in zip(ops1, ops2):
            ops.append(p[0])
            ops.append(p[1])

        content = to_content(arr, ops, skip={1})
        content = add_sep(content, gap=2, page_capacity=self.pageCapacity)
        return content

