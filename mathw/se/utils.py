import re
import numbers
import random

import numpy as np


def gen_arr(m, n, lb, ub, dtype, **kwargs):
    """
    随机生成 m 行 n 列的二维列表, 其中每个元素大于等于 lb 且 小于等于 ub
    :param m: int, 行数
    :param n: int, 列数
    :param lb: int or float, 下界
    :param ub: int or float, 上界
    :param dtype: str, 数据类型, 'int': 整数, 'float': 小数, 'frac': 分数
    :return: list
    """
    if dtype == 'int':
        return _gen_arr_int(m, n, lb, ub)
    elif dtype == 'frac':
        return _gen_arr_frac(m, n, lb, ub)
    elif dtype == 'float':
        return _gen_arr_float(m, n, lb, ub, **kwargs)
    else:
        vals = {'int', 'frac', 'float'}
        raise ValueError(f"Wrong [dtype]! Possible values in {str(vals)}")

def _gen_arr_int(m, n, lb, ub):
    """
    随机生成 m 行 n 列的二维列表。
    满足如下条件：每个元素是整数，它的值大于等于 lb 且小于等于 ub.
    :param m: int, 行数
    :param n: int, 列数
    :param lb: int, 下界
    :param ub: int, 上界
    :return: list
    """
    return [[random.randint(lb, ub) for _ in range(n)] for _ in range(m)]


def _gen_arr_float(m, n, lb, ub, dec=2):
    """
    随机生成 m 行 n 列的二维列表。
    满足如下条件：
    1、每个元素是 float；
    2、它的值大于等于 lb 且小于等于 ub；
    3、四舍五入，保留小数点后 dec 位；
    :param m: int, 行数
    :param n: int, 列数
    :param lb: int or float, 下界
    :param ub: int or float, 上界
    :param dec: int, 保留的小数点位数
    :return: list
    """
    return [[round(random.uniform(lb, ub), dec)
             for _ in range(n)] for _ in range(m)]


def _gen_arr_frac(m, n, lb, ub):
    """
    随机生成 m 行 n 列的二维列表。
    满足如下条件：
    1、每个元素是分数形式的字符串 'a/b', 其中 a 代表分子，b代表分母（可以为0）；
    2、分子大于等于lb且小于等于ub；
    3、分母大于等于0且小于等于lb；
    :param m: int, 行数
    :param n: int, 列数
    :param lb: int, 下界
    :param ub: int, 上界
    :return: list
    """
    return [[f"{random.randint(lb, ub)}/{random.randint(0, ub)}"
             for _ in range(n)] for _ in range(m)]


def gen_ops(m, n, chars, distinct=True, has_eq=False):
    """ 随机生成 m 行 n 列的二维列表，其中的元素来自 chars.
    :param m: int，行
    :param n: int，列
    :param chars: set, 字符集合, 例如 chars = {'+', '-', '×', '÷'}
    :param distinct: bool, 如果为Ture，则每一行不得出现重复的符号（此时 n <= len(chars))
    :param has_eq: bool, 如果为Ture，则添加一个等号列，即 [['='], ['='], ...]
    """
    if distinct:
        if n > len(chars):
            raise ValueError('Parameter sizes [chars] and [n] do not match!')
        # 从字符集合中选择 n 个不同的符号
        chars_list = list(chars)
        ops = [random.sample(chars_list, n) for _ in range(m)]
    else:
        ops = [[random.choice(list(chars))
                 for _ in range(n)] for _ in range(m)]
    if has_eq:
        eq = '='
        ops = np.hstack((ops, [[eq]] * m))

    return ops


def to_content(arr, ops,
               wrap=True, skip=None, cc=None):
    """
    把公式格式化成字符串
    :param arr: 二维数组，每一行代表公式的数字，例如 [a, b]
    :param ops: 二维数组，每一行代表公式的操作，例如 [+, =]
    :param wrap: 自动加括号，例如 a + (-b)。注意：第一个数不加括号。
    :param skip: 不加括号的集合，例如 skip = {0, 1} 代表 row 中的第 0 和第 1 个元素不加括号。
    返回一个列表, 例如 ['a', '+', '(-b/c)', '-', 'd', '=']
    :param cc: tuple list, e.g. [(left-index, right-index), (l, r), ...]
        例如：row = ['(-3)', '+', '6', '*', '4', '+', '(-5)']，
        它代表 (-3) + 6 * 4 + (-5),
        如果要表示 [(-3) + 6] * [4 + (-5)], 则需要添加两对括号，
        那么 cc = [(0, 2), (4, 6)].
    :return: str list，例如 ['a1 + b1 = ', 'a2 + b2 = ']
    """
    res = []
    for item, op in zip(arr, ops):
        # 自动给负数加括号
        if wrap:
            item = _auto_wrap(item, skip)
        # 把 item 和 op 拼接起来
        row = _make_row(item, op)
        # 手动加括号
        if cc:
            row = _add_cc(row, cc)

        row = [str(it) for it in row] # 确保每个元素是 str
        res.append(' '.join(row))

    return res


def _is_fraction(s):
    """
    验证输入的字符串是否数字
    test_cases = [
    "-1/2",     # True
    "2/3",      # True
    "-123/4",   # True
    "5/0",      # True (允许分母为0)
    "-12/0",    # True (允许分母为0)
    "abc",      # False
    "1/0.5",    # False (不符合分数格式)
    "1/2/3",    # False (不符合分数格式)
    "1/",       # False
    "/2",       # False
    ]
    """
    # 正则表达式模式
    pattern = r'^[+-]?\d+/\d+$'
    # 判断是否匹配
    return bool(re.match(pattern, s))


def _auto_wrap(item, skip=None):
    """ 给负数加括号
    item 是数据列表，例如 [a, '-b/c', d], 注意：其中的元素可以是占位符号 '__'
    skip 代表不加括号的集合，例如 skip = {0, 1} 代表 row 中的第 0 和第 1 个元素不加括号。
    返回一个列表, 例如 ['a', '(-b/c)', 'd']。 注意：item 中第0个元素不加括号。
    """
    if skip is None:
        skip = {0}
    res = []
    for i in range(len(item)):
        # 分数
        is_wrap = False
        if i not in skip:
            if isinstance(item[i], str) and _is_fraction(item[i]):
                # r < 0 则加括号
                if item[i][0] == '-':
                    is_wrap = True
            elif isinstance(item[i], str) and item[i][0] == '-':
                is_wrap = True
            elif isinstance(item[i], numbers.Number):
                if item[i] < 0:
                    is_wrap = True

        if is_wrap:
            res.append('(' + str(item[i]) + ')')
        else:
            res.append(item[i])
    return res

def _make_row(item, op):
    """ 把 item 和 op 拼接成一个列表
    :param item: 表示数据，例如 [8, 3]
    :param item: 表示操作符, 例如 ['+', '=']
    :return: list，例如 item = [8, 3], op = ['+', '=']，
        返回 [8, '+', 3, '=']，代表 8 + 3 =
    注意：item 的元素个数要么和 op 的元素个数相同，要么前者比后者多一个。
    """
    m = len(item)
    n = len(op)
    if m < n or m - n > 1:
        raise ValueError("[item] length and [op] length do not match!")
    row = [p for pair in zip(item, op) for p in pair]
    if m == n + 1:
        row.append(item[-1])
    return row


def _add_cc(row, cc):
    """
    给指定的列添加左括号和右括号。
    :param cc: tuple list, e.g. [(left-index, right-index), (l, r), ...]
    :return: list
    例如：row = ['(-3)', '+', '6', '*', '4', '+', '(-5)']，
    它代表 (-3) + 6 * 4 + (-5),
    如果要表示 [(-3) + 6] * [4 + (-5)], 则需要添加两对括号，
    那么 cc = [(0, 2), (4, 6)].
    """
    for lr in cc:
        row[lr[0]] = '(' + str(row[lr[0]])
        row[lr[1]] = str(row[lr[1]]) + ')'
    return row


def insert_placeholder(arr, col=-1, x='__'):
    """
    在制定的列插入一列占位符 ['__', '__', '__', ...]
    例如：arr = [[8, 3, 5], [5, 4, 2], ...], col = 1,
        当 col >= 0 时，返回 [[8, 3, '__', 5], [5, 4, '__', 2]...]
        当 col = -1 时，在 arr 的每一行的位置[0,n-1]之间随机插入一个占位符, 其中n是列数
            例如返回 [[8, '__', 3, 5], [5, 4, '__', 2]...]
    :param arr: list, 二维列表
    :param col: int, 插入的列的下标
    :param x: str, 占位符
    :return list
    """
    # 处理 col >= 0 的情况
    if col >= 0:
        for row in arr:
            row.insert(col, x)

    # 处理 col = -1 的情况
    elif col == -1:
        for row in arr:
            # 生成随机位置
            random_col = random.randint(0, len(row)-1)
            row.insert(random_col, x)

    return arr


def calculate_formula_result(formula):
    """
    输入加减乘除的算式（字符串格式），计算其结果
    例如 '3×5+18÷3' --> 21
    """
    f = formula.replace('×', '*').replace('÷', '/')
    try:
        res = int(eval(f)) # 引发 ZeroDivisionError 异常
    except ZeroDivisionError:
        # print("Error: Division by zero")
        res = 0
    return res


def add_chars(arr, chars):
    """
    给二维数组 arr 中每一行逐个添加 chars 中的字符。
    例如：arr[i]是arr的第i行，假设 arr[i] = [3, 5, 2]，那么
    1、当 vars = ['x', 'y', 'z'] 时，返回 ['3x', '5y', '2z']
    2、当 vars = ['x', 'y'] 时，返回 ['3x', '5y', 2]
    3、当 vars = ['x', '', 'z'] 时，返回 ['3x', 5, '2z']
    :param arr: list, 二维数组
    :param chars: list, 字符串列表
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


def add_sep(content, gap, page_capacity,
            separator='-', sep_num=40, truncate=True):
    """
    给内容列表按 “页” 添加分割符。每页的第一行和最后一行不添加分隔符。
    注意：添加分隔符后，每一页的行数等于content中元素的数量加上分隔符的数量。
    :param content: list of strings, e.g. [item1, item2, item3, ...]，每个item是一个字符串
    :param gap: int, 代表分隔符之间间隔的元素数量。换句话说，在每一页中，每隔gap个元素，插入一个分隔符。
    :param page_capacity: int, 每页元素数量。
    :param separator: str, 组成分隔符的单个字符
    :param sep_num: 每个分隔符中包含的字符数量。因此，插入的分隔符 sep_string = separator * sep_num。
    :param truncate: bool, True - 截断，不会改变 content 列表的长度；False - 不截断，直接返回结果，但是会增加 content 列表的长度。
    :return: list of strings
    """
    sep_string = separator * sep_num
    new_content = []
    num_elements = len(content)

    # 计算一页item的个数(page_item_num)
    # 页的元素数量(page_capacity) = 分隔符数量 (item_num / k - 1) + 元素数量 (item_num)
    page_item_num = int((page_capacity + 1) * gap / (gap + 1))

    for page_start in range(0, num_elements, page_item_num):
        page_end = min(page_start + page_item_num, num_elements)
        page_content = content[page_start:page_end]

        # Add elements in the page and separators
        page_size = len(page_content)
        for i in range(0, page_size):
            if page_size > i > 0 == i % gap:
                new_content.append(sep_string)
            new_content.append(page_content[i])

    if truncate:
        return new_content[:num_elements]
    else:
        return new_content


def group_contents(content_list):
    """
    把contents列表中的元素按“组”重新排列。排列方式如下（例子说明）
    contents = [content1, content2, content3 ...],
    content1 = [item11, item12, ...]
    content2 = [item21, item22, ...]
    content3 = [item31, item32, ...]
    注意 content1, content2, ... 列表长度相同
    返回结果如下：
    result = [item11, item21, item31, item12, item22, item32, ...]

    :param content_list: 二维列表, 例如[[str1], [str2], [str3], ...]
    :return: 一维列表
    """
    result = []
    for items in zip(*content_list):
        # Extend list by appending elements from the iterable.
        result.extend(items)
    return result

