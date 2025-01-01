import numpy as np

from .utils import to_content, gen_arr, add_chars, add_sep, group_contents


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
        content1 = to_content(arr1, ops1, skip={1})

        n1 = gen_arr(m=num//3+1, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        n2 = gen_arr(m=num//3+1, n=1, lb=-self.ub, ub=self.ub, dtype='float', dec=1)
        n3 = gen_arr(m=num//3+1, n=1, lb=-self.ub, ub=self.ub, dtype='frac')

        n = n1 + n2 + n3
        np.random.shuffle(n)
        n = n[0: num]
        arr2 = [[f"f({val[0]})"] for val in n]
        ops2 = [["="]] * num
        content2 = to_content(arr2, ops2)

        return group_contents([content1, content2], self.pageCapacity)


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
        content1 = to_content(arr1, ops1, skip={1})

        cde = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = add_chars(cde, ["f(x)", "x"])
        ops2 = [["+", "="]] * num
        content2 = to_content(arr2, ops2)

        return group_contents([content1, content2], self.pageCapacity)


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
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["g(x)"]] * num, arr2))
        arr2 = add_chars(arr2, ["", "/x"])
        ops2 = [["=", "+"]] * num
        content2 = to_content(arr2, ops2,skip={1})

        d = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        arr3 = np.hstack((d, [["xg(x)"]] * num, [["0"]]*num))
        arr3 = add_chars(arr3, ["f(x)"])
        ops3 = [["+", "="]] * num
        content3 = to_content(arr3, ops3)

        return group_contents([content1, content2, content3], self.pageCapacity)


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
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = gen_arr(m=num, n=1, lb=0, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["g(x)", "x"]] * num, arr2))
        ops2 = [["=", "/"]] * num
        content2 = to_content(arr2, ops2,skip={1})

        cd = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub, dtype='int')
        arr3 = np.hstack(([["f(x) / g(x)"]] * num, cd))
        arr3 = add_chars(arr3, ["", "x"])
        ops3 = [["=", "+"]] * num
        content3 = to_content(arr3, ops3, skip={1})

        return group_contents([content1, content2, content3], self.pageCapacity)


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
        ab = np.array(gen_arr(m=num, n=2, lb=1, ub=self.ub, dtype='int'))
        a, b = ab[:, 0].reshape(-1, 1), ab[:, 1].reshape(-1, 1)
        arr1 = np.hstack(([["f(x)"]] * num, a, b))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = np.hstack(([["g(x)"]] * num, a, b))
        arr2 = add_chars(arr2, ["", "x"])
        ops2 = [["=", "-"]] * num
        content2 = to_content(arr2, ops2, skip={1})

        c = gen_arr(m=num, n=1, lb=0, ub=self.ub, dtype='int')
        arr3 = np.hstack(([["f(x)g(x)"]] * num, c))
        ops3 = [["="]] * num
        content3 = to_content(arr3, ops3, skip={1})

        return group_contents([content1, content2, content3], self.pageCapacity)


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
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["g(x,y)"]] * num, arr2))
        arr2 = add_chars(arr2, ["", "x", "y"])
        ops2 = [["=", "+", "+"]] * num
        content2 = to_content(arr2, ops2, skip={1})

        arr3 = [["f(x,y)", "g(x,y)", "0"]] * num
        ops3 = [["=", "="]] * num
        content3 = to_content(arr3, ops3)

        return group_contents([content1, content2, content3], self.pageCapacity)


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
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        arr2 = np.hstack(([["f(f(x))"]] * num, arr2))
        ops2 = [["="]] * num
        content2 = to_content(arr2, ops2, skip={1})

        return group_contents([content1, content2], self.pageCapacity)


class FuncL8(object):

    """ 解方程: a是分数, b是整数
    f(x) = ax+b
    f(f(x)) = f(x)
    """

    pageCapacity = 14

    def __init__(self):
        self.ub = 20

    def generate(self, num):

        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='frac')
        b = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        arr1 = np.hstack(([["f(x)"]] * num, a, b))
        arr1 = add_chars(arr1, ["", "x"])
        ops1 = [["=", "+"]] * num
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = [["f(f(x))", "f(x)"]] * num
        ops2 = [["="]] * num
        content2 = to_content(arr2, ops2)

        return group_contents([content1, content2], self.pageCapacity)


class FuncL9(object):

    """ 解方程: a,b是整数，c是小数
    f(x, y) = ax^2 + by
    g(x) = x/a
    f(g(x), g(x)) = c
    """
    pageCapacity = 15

    def __init__(self):
        self.ub = 20

    def generate(self, num):

        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        b = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        c = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='float', dec=1)

        arr1 = np.hstack(([["f(x, y)"]] * num, a, b))
        arr1 = add_chars(arr1, ["", "x^2", "y"])
        ops1 = [["=", "+"]] * num
        content1 = to_content(arr1, ops1, skip={1})

        arr2 = np.hstack(([["g(x)"]] * num, [["x"]]*num, a))
        ops2 = [["=", "/"]] * num
        content12 = to_content(arr2, ops2)

        arr3 = np.hstack(([["f(g(x), g(x))"]] * num, c))
        ops3 = [["="]] * num
        content3 = to_content(arr3, ops3, skip={1})

        return group_contents([content1, content12, content3], self.pageCapacity)

