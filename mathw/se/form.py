import numpy as np
from fractions import Fraction

from .utils import to_content


class FormL1(object):

    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        axb = np.random.randint(-self._ub, self._ub, (num, 3))
        c = axb[:, 0] * axb[:, 1] + axb[:, 2]
        arr = np.array([axb[:, 0], axb[:, 2], c]).transpose()
        ops = [['x +', '=']] * num
        return to_content(arr, ops, skip={0, 2})


class FormL2(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        # items = np.random.randint(0, self._ub, (3*num, 2))
        frac = gen_frac(self._ub, 3*num)
        #frac = to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[2*i], frac[2*i+1]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = [['x +', '=']] * num
        return to_content(arr, ops, cc=[(0, 0)])


class FormL3(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        axb = np.random.uniform(-self._ub, self._ub, (num, 3))
        axb = axb.round(1)
        c = axb[:, 0] * axb[:, 1] + axb[:, 2]
        c = c.round(2)
        arr = np.array([axb[:, 0], axb[:, 2], c]).transpose()
        ops = [['x +', '=']] * num
        return to_content(arr, ops, skip={0, 2})


class FormL4(object):

    def __init__(self, ub=30):
        self._ub = ub

    def generate(self, num):
        """
        ----------------
        ax + by = c
        dx + ey = f
        ----------------
        """
        def gen_two_items():
            x = np.random.randint(-self._ub, self._ub)
            y = np.random.randint(-self._ub, self._ub)
            a = np.random.randint(-self._ub, self._ub)
            b = np.random.randint(-self._ub, self._ub)
            d = np.random.randint(-self._ub, self._ub)
            e = np.random.randint(-self._ub, self._ub)
            c = a * x + b * y
            f = d * x + e * y
            return [[a, b, c], [d, e, f]]

        items = []
        row_num = num // 2
        for i in range(row_num):
            items += gen_two_items()

        return _formate_two_of_equations(items, skip={2})


def _formate_two_of_equations(items, sep_length=20, **kwargs):
    """
    输入 items = [[a,b,c], [d,e,f], [a,b,c], [d,e,f], ...],
    其中每两个数组代表一组方程，例如
    ax+by=c
    dx+ey=f
    把它们格式化成如下形式：
    ax+by=c
    dx+ey=f
    --------
    ax+by=c
    dx+ey=f
    --------
    ...
    """
    item_num = len(items)
    arr = []
    ops = []

    i = 0
    for it in items:
        i += 1
        if i <= 2:
            arr.append(it)
            ops.append(['x +', 'y ='])
        else:
            i = 0
            arr.append(['- ' * sep_length, '', ''])
            ops.append(['', ''])

    return to_content(arr, ops, **kwargs)


class FormL5(object):

    def __init__(self, ub=10):
        self._ub = ub

    def generate(self, num):
        """
        ----------------
        ax + by = c
        dx + ey = f
        a,b,c,d,e,f 是分数
        ----------------
        """
        def random_sign():
            return 1 if np.random.random() < 0.5 else -1

        def gen_fraction():
            a = np.random.randint(-self._ub, self._ub)
            b = np.random.randint(1, self._ub)
            return Fraction(a, b)

        def gen_two_items():
            x = gen_fraction()
            y = gen_fraction()
            a = gen_fraction()
            b = gen_fraction()
            d = gen_fraction()
            e = gen_fraction()
            c = a * x + b * y
            f = d * x + e * y
            return [[str(a), str(b), str(c)], [str(d), str(e), str(f)]]

        items = []
        row_num = num // 2
        for i in range(row_num):
            items += gen_two_items()

        return _formate_two_of_equations(items)