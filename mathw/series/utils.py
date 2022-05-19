

def to_result(arr, ops, wrap=True, skip=None, cc=None):
    """
    把公式格式化成字符串
    :param arr: 二维数组，每一行代表公式的数字，例如 [a, b]
    :param ops: 二维数组，每一行代表公式的操作，例如 [+, =]
    :param wrap: 自动加括号，例如 a + (-b)
    :param skip: 不加括号的列(set)
    :param cc: tuple list,
        e.g. [(left-index, right-index), (l, r), ...]
        用来指定括号位置，例如
            [(-3) + 6] * [4 + (-5)],
            对应的列表为 ['(-3)', '+', '6', '*', '4', '+', '(-5)']
        式子中的中括号[]，用cc表示就是 cc = [(0, 2), (4, 6)]
    :return: str list，例如 ['a1 + b1 = ', 'a2 + b2 = ']
    """
    if skip is None:
        skip = {}
    res = []
    for row, op in zip(arr, ops):
        comb = []
        for i in range(len(row)):
            # 字符，比如 placeholder
            if isinstance(row[i], str):
                comb.append(row[i])
            # 给负数加括号
            elif wrap and row[i] < 0 and i not in skip:
                comb.append('(' + str(int(row[i])) + ')')
            # 数字转成字符
            else:
                comb.append(str(int(row[i])))
            # 符号
            if i < len(op):
                comb.append(op[i])
        # 加括号
        if cc:
            for lr in cc:
                comb[lr[0]] = '(' + comb[lr[0]]
                comb[lr[1]] += ')'
        res.append(' '.join(comb))
    return res


def insert_placeholder(arr, col, x='__'):
    """
    给数组新增一列，用占位符表示。
    :param arr: numpy 数组
    :param col: 列下标
    :param x: 占位符
    """
    arr = list(arr)
    res = []
    for row in arr:
        row = list(row)
        res.append(row[: col] + [x] + row[col:])
    return res

