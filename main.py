from mathw import MathWork


if __name__ == '__main__':

    levels = MathWork.get_series_levels("frac")
    print(levels)
    exit(0)

    MathWork(
        series='func',  # 类别
        pageNum=4,  # 页数
        level=9,  # 等级
    ).go()

