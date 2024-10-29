from .utils import to_result
import numpy as np


def _to_frac(items):
    """
    输入 items = [(分子, 分母), ...]
    把它们转换成分数形式 frac = [`分子/分母`, ...]
    """
    return ['/'.join([str(it[0]), str(it[1])]) for it in items]


class FracL1(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (2*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[2*i], frac[2*i+1]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = [
            ['+', '='] if np.random.random() < 0.5
               else ['-', '='] for i in range(num)
            ]
        return to_result(arr, ops)


class FracL2(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (3*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[3*i], frac[3*i+1], frac[3*i+2]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.35:
                ops.append(['+', '-', '='])
            elif r < 0.7:
                ops.append(['-', '+', '='])
            else:
                ops.append(['-', '-', '='])

        return to_result(arr, ops)


class FracL3(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (3*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[3*i], frac[3*i+1], frac[3*i+2]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.25:
                ops.append(['+', '- __ ='])
            elif r < 0.5:
                ops.append(['-', '+ __ ='])
            elif r < 0.75:
                ops.append(['- __ +', '='])
            else:
                ops.append(['+ __ -', '='])

        return to_result(arr, ops)


class FracL4(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (2*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[2*i], frac[2*i+1]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = [['×', '=']] * num
        return to_result(arr, ops)


class FracL5(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (2*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[2*i], frac[2*i+1]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = [['÷', '=']] * num
        return to_result(arr, ops)


class FracL6(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (3*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[3*i], frac[3*i+1], frac[3*i+2]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.35:
                ops.append(['×', '÷', '='])
            elif r < 0.7:
                ops.append(['-', '×', '='])
            else:
                ops.append(['÷', '÷', '='])

        return to_result(arr, ops)


class FracL7(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (3*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[3*i], frac[3*i+1], frac[3*i+2]])
        return arr

    def generate(self, num):
        """
        a×__÷b=c
        a×b÷__=c
        """
        arr = self._generate_frac(num)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.5:
                ops.append(['× __ ÷', '='])
            else:
                ops.append(['×', '÷ __ ='])

        return to_result(arr, ops)


class FracL8(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (4*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[4*i], frac[4*i+1], frac[4*i+2], frac[4*i+3]])
        return arr

    def generate(self, num):
        arr = self._generate_frac(num)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.25:
                ops.append(['×', '+', '÷', '='])
            elif r < 0.5:
                ops.append(['×', '-', '÷', '='])
            elif r < 0.75:
                ops.append(['÷', '+', '×', '='])
            else:
                ops.append(['÷', '-', '×', '='])

        return to_result(arr, ops)


class FracL9(object):

    def __init__(self, ub=20):
        self._ub = ub

    def _generate_frac(self, num):
        items = np.random.randint(0, self._ub, (4*num, 2))
        frac = _to_frac(items)
        arr = []
        for i in range(num):
            arr.append([frac[4*i], frac[4*i+1], frac[4*i+2], frac[4*i+3]])
        return arr

    def generate(self, num):
        """
        a×__+b÷c=d
        a×__-b÷c=d
        a×b+__÷c=d
        a×b-__÷c=d
        a×b+c÷__=d
        a×b-c÷__=d
        """
        arr = self._generate_frac(num)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.1:
                # a×__+b÷c=d
                ops.append(['× __ +', '÷', '='])
            elif r < 0.2:
                # a×__-b÷c=d
                ops.append(['× __ -', '÷', '='])
            elif r < 0.4:
                # a×b+__÷c=d
                ops.append(['×', '+ __ ÷', '='])
            elif r < 0.6:
                # a×b-__÷c=d
                ops.append(['×', '- __ ÷', '='])
            elif r < 0.8:
                # a×b+c÷__=d
                ops.append(['×', '+', '÷ __ ='])
            else:
                # a×b-c÷__=d
                ops.append(['×', '-', '÷ __ ='])

        return to_result(arr, ops)

class FracL10(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        items = np.random.uniform(0, self._ub, (num, 2))
        arr = np.round(items, 2)
        ops = [
            ['+', '='] if np.random.random() < 0.5
               else ['-', '='] for i in range(num)
            ]
        return to_result(arr, ops)


class FracL11(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        items = np.random.uniform(0, self._ub, (num, 3))
        arr = np.round(items, 2)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.25:
                ops.append(['+', '- __ ='])
            elif r < 0.5:
                ops.append(['-', '+ __ ='])
            elif r < 0.75:
                ops.append(['- __ +', '='])
            else:
                ops.append(['+ __ -', '='])
        return to_result(arr, ops)


class FracL12(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        items = np.random.uniform(0, self._ub, (num, 3))
        arr = np.round(items, 2)
        ops = []
        for i in range(num):
            r = np.random.random()
            if r < 0.25:
                # a+b+__=c
                ops.append(['+', '+ __ ='])
            elif r < 0.5:
                # a-b-__=c
                ops.append(['-', '- __ ='])
            elif r < 0.75:
                # a-__+b=c
                ops.append(['- __ +', '='])
            else:
                # a+__-b=c
                ops.append(['+ __ -', '='])
        return to_result(arr, ops)


class FracL13(object):

    def __init__(self, ub=10):
        self._ub = ub

    def generate(self, num):
        items = np.random.uniform(0, self._ub, (num, 2))
        arr = np.round(items, 1)
        ops = [['×', '=']] * num

        return to_result(arr, ops)


class FracL14(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        arr = []
        for i in range(num):
            r = np.random.random()
            if r < 0.25:
                a = np.random.uniform(0, self._ub)
                a = np.round(a, 1)
                b = np.random.randint(0, self._ub)
            elif r < 0.5:
                a = np.random.randint(0, self._ub)
                b = np.random.uniform(0, self._ub)
                b = np.round(b, 1)
            elif r < 0.75:
                a = np.random.uniform(0, self._ub)
                a = np.round(a, 1)
                b = np.random.uniform(0, self._ub)
                b = np.round(b, 1)
            else:
                a = np.random.randint(0, self._ub)
                b = np.random.randint(0, self._ub)
            arr.append((a, b))

        print(arr)

        ops = [['÷', '=']] * num

        return to_result(arr, ops)


class FracL15(object):

    def __init__(self, ub=15):
        self._ub = ub

    def generate(self, num):
        items1 = np.random.randint(0, self._ub, num)
        items2 = np.random.uniform(0, self._ub, (num, 2))
        items2 = np.round(items2, 1)

        arr = []
        ops = []
        for i in range(num):
            item = [items1[i], items2[i][0], items2[i][1]]
            arr.append(item)
            r = np.random.random()
            if r < 0.5:
                # a×b÷c=
                ops.append(['×', '÷', '='])
            else:
                # a÷b×c=
                ops.append(['÷', '×', '='])
        return to_result(arr, ops)


class FracL16(object):

    def __init__(self, ub=15):
        self._ub = ub

    def generate(self, num):
        items1 = np.random.randint(0, self._ub, num)
        items2 = np.random.uniform(0, self._ub, (num, 2))
        items2 = np.round(items2, 1)

        arr = []
        ops = []
        for i in range(num):
            item = [items1[i], items2[i][0], items2[i][1]]
            arr.append(item)
            r = np.random.random()
            if r < 0.5:
                # a×b÷?=c
                ops.append(['×', '÷ __ ='])
            else:
                # a×?÷b=c
                ops.append(['× __ ÷', '='])
        return to_result(arr, ops)


class FracL17(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        items1 = np.random.uniform(0, self._ub, (num, 2))
        items1 = np.round(items1, 1)
        items2 = np.random.randint(0, self._ub, (num,2))

        arr = []
        ops = []
        for i in range(num):
            item = [items1[i][0], items1[i][1], items2[i][0], items2[i][1]]
            arr.append(item)
            r = np.random.random()
            if r < 0.5:
                # a×b+c÷d=
                ops.append(['×', '+', '÷', '='])
            else :
                # a×b-c÷d=
                ops.append(['×', '-', '÷', '='])
        return to_result(arr, ops)


class FracL18(object):

    def __init__(self, ub=20):
        self._ub = ub

    def generate(self, num):
        items1 = np.random.uniform(0, self._ub, (num, 2))
        items1 = np.round(items1, 1)
        items2 = np.random.randint(0, self._ub, (num,2))

        arr = []
        ops = []
        for i in range(num):
            item = [items1[i][0], items1[i][1], items2[i][0], items2[i][1]]
            arr.append(item)
            r = np.random.random()
            if r < 0.1:
                # a×?+b÷c=d
                ops.append(['× __ +', '÷', '='])
            elif r < 0.2:
                # a×?-b÷c=d
                ops.append(['× __ -', '÷', '='])
            elif r < 0.4:
                # a×b+__÷c=d
                ops.append(['×', '+ __ ÷', '='])
            elif r < 0.6:
                # a×b-__÷c=d
                ops.append(['×', '- __ ÷', '='])
            elif r < 0.8:
                # a×b+c÷__=d
                ops.append(['×', '+', '÷ __ ='])
            else:
                # a×b-c÷__=d
                ops.append(['×', '-', '÷ __ ='])
        return to_result(arr, ops)