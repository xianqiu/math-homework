

def to_result(arr, ops, wrap=True, skip=None):
    """
    把公式格式化成字符串
    :param arr: 二维数组，每一行代表公式的数字，例如 [a, b]
    :param ops: 二维数组，每一行代表公式的操作，例如 [+, =]
    :param wrap: 自动加括号，例如 a + (-b)
    :param skip: 不加括号的列(set)
    :return: str list，例如 ['a1 + b1 = ', 'a2 + b2 = ']
    """
    if skip is None:
        skip = {}
    res = []
    for row, op in zip(arr, ops):
        comb = []
        for i in range(len(row)):
            if wrap and row[i] < 0 and i not in skip:
                comb.append('(' + str(int(row[i])) + ')')
            else:
                comb.append(str(int(row[i])))
            if i < len(op):
                comb.append(op[i])
        res.append(' '.join(comb))
    return res
