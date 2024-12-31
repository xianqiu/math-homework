import numpy as np

from .utils import to_content, gen_arr, gen_ops


def _add_chars(arr, chars):
    """
    给二维数组 arr 中每一行逐个添加 chars 中的字符。
    例如：arr[i]是arr的第i行，假设 arr[i] = [3, 5, 2]，那么
    1、当 vars = ['x', 'y', 'z'] 时，返回 ['3x', '5y', '2z']
    2、当 vars = ['x', 'y'] 时，返回 ['3x', '5y', 2]
    3、当 vars = ['x', '', 'z'] 时，返回 ['3x', 5, '2z']
    :param arr: list, 二维数组
    :parma chars: list, 字符串列表
    :return: list
    """
    result = []
    for row in arr:
        new_row = []
        for i, value in enumerate(row):
            if i < len(chars) and chars[i] != '':
                new_row.append(f"{value}{chars[i]}")
            else:
                new_row.append(value)
        result.append(new_row)
    return result


class FormL1(object):
    """
    一元一次方程 ax+b=c, abcx是整数
    """

    def __init__(self):
        self.ub = 30

    def generate(self, num):
        axb = np.array(gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int'))
        a, x, b = axb[:, 0], axb[:, 1], axb[:, 2]
        c = a * x + b
        arr = np.array([axb[:, 0], axb[:, 2], c]).transpose()
        ops = [['x +', '=']] * num
        return to_content(arr, ops, skip={0, 2})


class FormL2(object):
    """
    一元一次方程 ax+b=c, abc是分数
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        arr = np.array(gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                               dtype='frac'))
        ops = [['x +', '=']] * num
        return to_content(arr, ops, skip={0, 2})


class FormL3(object):
    """
    一元一次方程 ax+b=c, abc是小数
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = np.array(gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                               dtype='float', dec=1))
        ops = [['x +', '=']] * num
        return to_content(arr, ops, skip={0, 2})


class FormL4(object):

    """
    二元一次方程组，abcdefxy 是整数
    ax + by = c
    dx + ey = f
    """

    def __init__(self):
        self.ub = 10

    def generate(self, num):
        abxyde = np.array(gen_arr(m=num//2, n=6, lb=-self.ub, ub=self.ub,
                      dtype='int'))
        a, b, x, y, d, e = (abxyde[:, 0], abxyde[:, 1],
                            abxyde[:, 2], abxyde[:, 3],
                            abxyde[:, 4], abxyde[:, 5])
        c = a * x + b * y
        f = d * x + e * y

        arr1 = np.column_stack((a, b, c))
        arr2 = np.column_stack((d, e, f))
        arr = []
        for p in zip(arr1, arr2):
            arr.append(p[0])
            arr.append(p[1])

        ops = [['x +', 'y =']] * num

        return to_content(arr, ops, skip={0, 2})


class FormL5(object):
    """
    二元一次方程组，abcdef 是整数
    ax + by = c
    dx + ey = f
    """

    def __init__(self):
        self.ub = 15

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='int')
        ops = [['x +', 'y =']] * num

        return to_content(arr, ops, skip={0, 2})


class FormL6(object):
    """
    二元一次方程组，abcdef 是小数
    ax + by = c
    dx + ey = f
    """

    def __init__(self):
        self.ub = 15

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                      dtype='float', dec=1)
        ops = [['x +', 'y =']] * num

        return to_content(arr, ops, skip={0, 2})


class FormL7(object):
    """
    二次展开, ab是整数
    (ax+b)(ax-b)=
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                      dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a, b))
        arr = _add_chars(arr, chars=['x'])
        ops1, ops2 = [['+']] * num, ['-'] * num
        res1, res2 = to_content(arr, ops1, cc={(0, 2)}), to_content(arr, ops2, cc={(0, 2)})
        res = []
        for p in zip(res1, res2):
            res.append(''.join(p) + ' =')

        return res


class FormL8(object):
    """
    因式分解，ab是整数
    a^2x^2-b^2=
    """
    def __init__(self):
        self.ub = 30

    def generate(self, num):
        arr = gen_arr(m=num, n=2, lb=11, ub=self.ub, dtype='int')
        arr = np.array(arr)
        arr = arr * arr
        arr = _add_chars(arr, chars=['x^2'])
        ops = [['-','=']] * num
        return to_content(arr, ops)


class FormL9(object):
    """
    二次展开, ab是整数
    (ax+b)^2=
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                      dtype='int')
        b = gen_arr(m=num, n=1, lb=0, ub=self.ub,
                    dtype='int')
        arr = np.hstack((a, b))
        arr = _add_chars(arr, chars=['x'])
        ops = gen_ops(m=num, n=1, chars={'+', '-'})
        temp = to_content(arr, ops, cc={(0,2)})
        res = [item + '^2 =' for item in temp]
        return res


class FormL10(object):
    """
    因式分解, ab是整数
    a^2x^2+2abx+b^2=
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=1, ub=self.ub,
                      dtype='int')
        b = gen_arr(m=num, n=1, lb=1, ub=self.ub,
                    dtype='int')
        a = np.array(a)
        b = np.array(b)
        ab = 2 * a * b
        a2 = a * a
        b2 = b * b
        arr = np.hstack((a2, ab, b2))
        arr = _add_chars(arr, chars=['x^2', 'x'])

        ops1 = gen_ops(m=num, n=1, chars=['+', '-'])
        ops2 = [['+', '=']] * num
        ops = np.hstack((ops1, ops2))
        return to_content(arr, ops)


class FormL11(object):
    """
    二次方程, abc是整数
    ax^2+b=c
    注意：存在没有实数解的情况，这不是BUG。
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        arr = gen_arr(m=num, n=3, lb=-self.ub, ub=self.ub,
                dtype='int')
        arr = _add_chars(arr, ['x^2'])
        ops = [['+', '=']] * num
        return to_content(arr, ops, skip={0, 2})


class FormL12(object):
    """
    因式分解
    ax^2+bx=
    a(x+b)^2+c(x+b)=
    """

    def __init__(self):
        self.ub = 20

    def _gen1(self, num):
        # ax^2+bx=
        arr = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                dtype='int')
        arr = _add_chars(arr, ['x^2', 'x'])
        ops = gen_ops(m=num, n=1, chars=['+', '-'], has_eq=True)
        return to_content(arr, ops)

    def _gen2(self, num):
        # a(x+b)^2+c(x+b)=
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub, dtype='int')
        b = gen_arr(m=num, n=1, lb=1, ub=self.ub, dtype='int')
        c = gen_arr(m=num, n=1, lb=1, ub=self.ub, dtype='int')
        arr = np.hstack((a,b,c,b))
        arr = _add_chars(arr, ['(x', ')^2', '(x', ')'])
        ops = gen_ops(m=num, n=2, chars=['+', '-'], distinct=False)
        ops = np.array(ops)
        ops = np.hstack((ops, ops[:, 0].reshape(-1,1), [['=']]*num))
        return to_content(arr, ops)

    def generate(self, num):
        res = self._gen1(num//2 + 1) + self._gen2(num//2 + 1)
        np.random.shuffle(res)
        return res[0: num]


class FormL13(object):
    """
    二次方程, abcde是整数
    e(ax+b)^2+c=d
    注意：存在没有实数解的情况，这不是BUG。
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        ab = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                dtype='int')
        ab = _add_chars(ab, ['x'])
        ops = [['+']] * num
        ab = to_content(ab, ops, cc={(0, 2)})
        ab = [item + '^2' for item in ab]

        cd = gen_arr(m=num, n=2, lb=-self.ub, ub=self.ub,
                dtype='int')
        ops = [['=']] * num
        cd = to_content(cd, ops, skip={1})

        abcd = [' + '.join(p) for p in zip(ab, cd)]

        e = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                dtype='int')
        res = [str(p[0][0]) + p[1] for p in zip(e, abcd)]

        return res


class FormL14(object):
    """
    二次方程, bc是正整数
    x^2 @ (b+c)x + bc = 0, @ in {+,-}
    x^2 + (b-c)x - bc = 0
    """

    def __init__(self):
        self.ub = 20

    def _gen1(self, num):
        # x^2 @ (b+c)x + bc = 0, @ in {+,-}
        bc = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                              dtype='int'))
        b, c = bc[:, 0], bc[:, 1]
        d = b + c
        e = b * c

        dxe = _add_chars(np.array([d, e, [0] * num]).T, 'x')
        arr = np.hstack(([['x^2']] * num, dxe))

        ops1 = gen_ops(m=num, n=1, chars={'+', '-'})
        ops2 = [['+', '=']] * num
        ops = np.hstack((ops1, ops2))

        return to_content(arr, ops)

    def _gen2(self, num):
        # x^2 + (b-c)x - bc = 0, @ in {+,-} distinct
        bc = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                              dtype='int'))
        b, c = bc[:, 0], bc[:, 1]
        d = b - c
        # refine format
        ops1 = []
        for i in range(len(d)):
            if d[i] < 0:
                d[i] = -d[i]
                ops1.append(['-'])
            else:
                ops1.append(['+'])

        e = b * c
        dxe = _add_chars(np.array([d, e, [0] * num]).T, 'x')
        arr = np.hstack(([['x^2']] * num, dxe))

        ops2 = [['-', '=']] * num
        ops = np.hstack((ops1, ops2))

        return to_content(arr, ops)

    def generate(self, num):
        res = self._gen1(num//2 + 1) + self._gen2(num//2 + 1)
        np.random.shuffle(res)
        return res[0:num]


class FormL15X(object):
    """
    二次方程, bc是正整数
    x^2+(b-c)x-bc=0
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        bc = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                     dtype='int'))
        b, c = bc[:, 0], bc[:, 1]
        d = b - c
        e = b * c

        dxe = _add_chars(np.array([d, e, [0] * num]).T, 'x')
        arr = np.hstack(([['x^2']]*num, dxe))
        ops = [['+', '-', '=']]*num

        return to_content(arr, ops)


class FormL15(object):
    """
    二次方程, bc是正整数
    ax^2+bx+c=0
    注意：存在没有实数解的情况，这不是BUG。
    """

    def __init__(self):
        self.ub = 20

    def generate(self, num):
        a = gen_arr(m=num, n=1, lb=-self.ub, ub=self.ub,
                     dtype='int')
        bc = np.array(gen_arr(m=num, n=2, lb=0, ub=self.ub,
                     dtype='int'))
        arr = np.hstack((a, bc, [[0]]*num))
        arr = _add_chars(arr, ['x^2', 'x'])
        ops = gen_ops(m=num, n=2, chars={'+', '-'}, distinct=False, has_eq=True)

        return to_content(arr, ops)