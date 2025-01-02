import numpy as np


from .utils import to_content, gen_arr, insert_placeholder, gen_ops, calculate_formula_result


class MultL1(object):
    """
    乘法 a×b，ab是一位数，非负
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=0, ub=self.ub,
                      dtype='int')
        ops = [['×', '=']] * num
        return to_content(arr, ops)


class MultL2(object):
    """
    乘法 a×b，ab是一位数，可负
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['×', '=']] * num
        return to_content(arr, ops)


class MultL3(object):
    """
    乘法填空 a×__=c, ab是1位数，非负
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        ab = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                     dtype='int'))
        a, b = ab[:, 0], ab[:, 1]
        c = a * b
        arr = np.array((a, c)).T
        ops = [['× __ =']] * num

        return to_content(arr, ops)


class MultL4(object):
    """
    乘法填空 a×__=c, ab是1位数
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        ab = np.array(gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                     dtype='int'))
        a, b = ab[:, 0], ab[:, 1]
        c = a * b
        arr = np.array((a, c)).T
        ops = [['× __ =']] * num

        return to_content(arr, ops, skip={0, 1})


class MultL5(object):
    """
    除法基础（非负） c÷a, a是1位数，非负
    注意：除数等于0的情况没有排除，这不是BUG。
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        ab = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                              dtype='int'))
        a, b = ab[:, 0], ab[:, 1]
        c = a * b
        # 把 '0 = a * 0' 修改成 'n = a * 0'
        d = [np.random.randint(0, self.ub) if a[i] ==0
             else c[i]
             for i in range(len(b))]
        arr = np.array((d, a)).T
        ops = [['÷', '=']] * num

        return to_content(arr, ops)


class MultL6(object):
    """
    除法基础（非负） c÷a, a是1位数
    注意：除数等于0的情况没有排除，这不是BUG。
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        ab = np.array(gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                              dtype='int'))
        a, b = ab[:, 0], ab[:, 1]
        c = a * b
        # 把 '0 = a * 0' 修改成 'n = a * 0'
        d = [np.random.randint(0, self.ub) if a[i] == 0
             else c[i]
             for i in range(len(b))]
        arr = np.array((d, a)).T
        ops = [['÷', '=']] * num

        return to_content(arr, ops)


class MultL7(object):
    """
    除法填空 c÷__=b 或 __÷a=b, ab是1位数，非负
    注意：除数等于0的情况没有排除，这不是BUG。
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        b = np.array(gen_arr(m=num, n=1, lb=0, ub=self.ub, dtype='int'))
        c = np.array(gen_arr(m=num, n=1, lb=0, ub=self.ub, dtype='int'))
        a = b * c
        arr1 = np.hstack((a, [["__"]] * num, c))
        ops1 = [['÷', "="]] * num
        content1 = to_content(arr1, ops1, skip={0, 2})

        arr2 = np.hstack(([["__"]] * num, b, c))
        ops2 = [['÷', "="]] * num
        content2 = to_content(arr2, ops2, skip={0, 2})

        content = content1 + content2
        np.random.shuffle(content)
        return content[0: num]


class MultL8(object):
    """
    除法填空 c÷__=b 或 __÷a=b, ab是1位数
    注意：除数等于0的情况没有排除，这不是BUG。
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        b = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        c = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        a = b * c
        arr1 = np.hstack((a, [["__"]]*num, c))
        ops1 = [['÷', "="]] * num
        content1 = to_content(arr1, ops1, skip={0, 2})

        arr2 = np.hstack(([["__"]]*num, b, c))
        ops2 = [['÷', "="]] * num
        content2 = to_content(arr2, ops2, skip={0, 2})

        content = content1 + content2
        np.random.shuffle(content)
        return content[0: num]


class MultL9(object):
    """
    乘法加减 a×b+c×d 或 a×b-c×d, abcd是1位数
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = np.hstack(([['×']]*num,
                         gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['×', '=']]*num))

        return to_content(arr, ops)


class MultL10(object):
    """
    乘法填空 a×__+c×d=e 或 a×b-__×d=e, abcd是1位数
    """

    def __init__(self):
        self.ub = 9

    def _gen1(self, num):
        # a×__+c×d=e
        a = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        b = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        c = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        d = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        e = a * b + c * d
        arr = np.hstack((a, [["__"]]*num, c, d, e))
        ops = [['×', '+', '×', '=']] * num
        return to_content(arr, ops, skip={0, 4})

    def _gen2(self, num):
        # a×b - __×d = e
        a = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        b = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        c = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        d = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        e = a * b - c * d
        arr = np.hstack((a, b, [["__"]]*num, d, e))
        ops = [['×', '-', '×', '=']] * num
        return to_content(arr, ops, skip={0, 4})

    def generate(self, num):
        half = num // 2 + 1
        res = self._gen1(half) + self._gen2(half)
        np.random.shuffle(res)
        return res[0: num]


class MultL11(object):
    """
    四则运算 a×b+c÷d 或 a×b-c÷d, abd是一位数
    注意：除数等于0的情况没有排除，这不是BUG。
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = np.array(gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='int'))
        a, b, e, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        c = d * e
        # 把 '0 = d * 0' 修改成 'n = d * 0'
        c = [np.random.randint(0, self.ub) if d[i] == 0
             else c[i]
             for i in range(len(d))]
        arr = np.array([a, b, c, d]).T
        ops = np.hstack(([['×']]*num,
                         gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['÷', '=']]*num))
        return to_content(arr, ops)


class MultL12(object):
    """
    四则填空 a×__+c÷d=e 或 a×b-c÷__=e 或 a×b+__÷d=e, abd是一位数。
    注意：除数等于0的情况没有排除，这不是BUG。
    """
    def __init__(self):
        self.ub = 9

    def _gen1(self, num):
        # a×__+c÷d=e
        arr = np.array(gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                               dtype='int'))
        a, b, f, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        c = d * f
        # 把 '0 = d * 0' 修改成 'n = d * 0'
        c = [np.random.randint(0, self.ub) if d[i] == 0
             else c[i]
             for i in range(len(d))]
        e = a * b + f
        arr = np.array([a, c, d, e]).T
        ops = [['× __ +', '÷', '=']] * num

        return to_content(arr, ops, skip={0, 3})

    def _gen2(self, num):
        # a×b-c÷__=e
        arr = np.array(gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                               dtype='int'))
        a, b, f, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        c = f * d
        e = a * b - f
        arr = np.array([a, b, c, e]).T
        ops = [['×', '-', '÷ __ =']] * num
        return to_content(arr, ops, skip={0, 3})

    def _gen3(self, num):
        # a×b+__÷d=e
        arr = np.array(gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                               dtype='int'))
        a, b, f, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        e = a * b + f
        arr = np.array([a, b, d, e]).T
        ops = [['×', '+ __ ÷', '=']] * num
        return to_content(arr, ops, skip={0, 3})

    def generate(self, num):
        k = num // 3 + 1
        res = self._gen1(k) + self._gen2(k) + self._gen3(k)
        np.random.shuffle(res)
        return res[0: num]


class MultL13(object):
    """
    乘法加减 a×(b+c) 或 a×(b-c), abc是1位数, c非负
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        ab = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                     dtype='int')
        c = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                     dtype='int')
        arr = np.hstack((ab, c))
        ops = np.hstack(([['×']]*num,
                         gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['=']]*num))

        return to_content(arr, ops, skip={0, 1}, cc={(2, 4)})


class MultL14(object):
    """
    四则填空 (a+__)×c=d 或 (a-__)×c=d, acd是一位数。
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = np.array(gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                               dtype='int'))
        a, b, c = arr[:, 0], arr[:, 1], arr[:, 2]
        d = (a + b) * c
        ops = np.hstack((gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['×', '=']]*num))
        arr = np.array([a, c, d]).T
        arr = insert_placeholder(arr.tolist(), 1)
        return to_content(arr, ops, skip={0, 3}, cc=[(0, 2)])


class MultL15(object):
    """
    四则运算 (a+b)×(c+d)
    abcd是一位数。
    """

    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = np.hstack((gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['×']] * num,
                         gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['=']] * num))

        return to_content(arr, ops, skip={0, 2}, cc=[(0, 2), (4, 6)])


class MultL16(object):
    """
    四则填空 (a+__)×(c+d)=e, abcd是一位数。
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = np.array(gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='int'))
        a, b, c, d = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        e = (a + b) * (c + d)
        arr = np.array([a, c, d, e]).T
        arr = insert_placeholder(arr.tolist(), 1)

        ops = np.hstack((gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['×']] * num,
                         gen_ops(m=num, n=1, chars={'+', '-'}),
                         [['=']] * num))

        return to_content(arr, ops, skip={0, 2, 4}, cc=[(0, 2), (4, 6)])


class MultL17(object):
    """
    连乘 a×b×c，abc是1位数
    """
    def __init__(self):
        self.ub = 9

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['×', '×', '=']] * num
        return to_content(arr, ops)


class MultL18(object):
    """
    连乘填空 a×__×c=d 或 a×b×__=d
    abc是1位数
    """

    def __init__(self):
        self.ub = 9

    def _gen1(self, num):
        # a×__×c=d
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['× __ ×', '=']] * num
        return to_content(arr, ops, skip={0, 2})

    def _gen2(self, num):
        # a×b×__=d
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['×', '× __ =']] * num
        return to_content(arr, ops, skip={0, 2})

    def generate(self, num):
        half = num // 2 + 1
        res = self._gen1(half) + self._gen2(half)
        np.random.shuffle(res)
        return res[0: num]


class MultL19(object):
    """
    乘法 a×b，ab是两位数
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['×', '=']] * num
        return to_content(arr, ops)


class MultL20(object):
    """
    乘法填空 a×__=c, a是两位数
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        ab = np.array(gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                     dtype='int'))
        a, b = ab[:, 0], ab[:, 1]
        c = a * b
        arr = np.array([a,c]).T
        ops = [['× __ =']] * num

        return to_content(arr, ops, skip={0, 1})


class MultL21(object):
    """
    除法 a÷b, b是2位数
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        bc = np.array(gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                              dtype='int'))
        b, c = bc[:, 0], bc[:, 1]
        a = b * c
        arr = np.array([a, b]).T
        ops = [['÷', '=']] * num
        return to_content(arr, ops)


class MultL22(object):
    """
    除法填空 a÷__=c 或 __÷b=c, bc是两位数
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        b = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        c = np.array(gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int'))
        a = b * c
        arr1 = np.hstack((a, [["__"]]*num, c))
        ops1 = [['÷', "="]] * num
        content1 = to_content(arr1, ops1, skip={0, 2})

        arr2 = np.hstack(([["__"]]*num, b, c))
        ops2 = [['÷', "="]] * num
        content2 = to_content(arr2, ops2, skip={0, 2})

        content = content1 + content2
        np.random.shuffle(content)
        return content[0: num]


class MultL23(object):
    """
    四则运算 a @ b @ c @ d = ?
    其中 @ in {+,-,×,÷}, a,b,c,d 非负
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=0, ub=self.ub,
                      dtype='int')
        ops = gen_ops(m=num, n=3, chars={'+', '-', '×', '÷'}, has_eq=True)
        for i in range(num):
            for j in range(3):
                if ops[i][j] == '÷':
                    arr[i][j] *= arr[i][j+1]
                    break
        return to_content(arr, ops)


class MultL24(object):
    """
        四则运算 a @ b @ c @ d = ?
        其中 @ in {+,-,×,÷}, a,b,c,d 可以为负
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=4, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = gen_ops(m=num, n=3, chars={'+', '-', '×', '÷'}, has_eq=True)
        for i in range(num):
            for j in range(3):
                if ops[i][j] == '÷':
                    arr[i][j] *= arr[i][j+1]
                    break
        return to_content(arr, ops)


class MultL25(object):
    """
        四则运算填空 a @ b @ c @ __ = d
        其中 @ in {+,-,×,÷}, a,b,c,d 非负，填空的位置随机
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        res = [self._gen_one_row() for _ in range(num)]
        return res

    def _gen_one_row(self):
        arr0 = gen_arr(m=1, n=4, lb=0, ub=self.ub,
                      dtype='int')[0]
        ops0 = gen_ops(1, 3, chars={'+', '-', '×', '÷'})[0]
        for i in range(3):
            if ops0[i] == '÷':
                arr0[i] *= arr0[i+1]
                break

        formula = to_content([arr0], [ops0])[0]
        val = str(calculate_formula_result(formula))
        # 随机选择 placeholder
        arr0[np.random.randint(0, 4)] = '__'
        arr0.append(val)
        ops0.append('=')
        return to_content([arr0], [ops0])[0]


class MultL26(object):

    """ 四则填空：
    a@b@?@c=d, @ in {+,-,×,÷}
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        res = [self._gen_one_row() for _ in range(num)]
        return res

    def _gen_one_row(self):
        arr0 = gen_arr(m=1, n=4, lb=-self.ub, ub=self.ub,
                       dtype='int')[0]
        ops0 = gen_ops(1, 3, chars={'+', '-', '×', '÷'})[0]
        for i in range(3):
            if ops0[i] == '÷':
                arr0[i] *= arr0[i + 1]
                break

        formula = to_content([arr0], [ops0])[0]
        val = str(calculate_formula_result(formula))
        # 随机选择 placeholder
        arr0[np.random.randint(0, 4)] = '__'
        arr0.append(val)
        ops0.append('=')
        return to_content([arr0], [ops0])[0]