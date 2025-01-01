from mathw import MathWork


if __name__ == '__main__':

    MathWork.get_series()
    exit(0)

    MathWork(
        series='func',  # 类别
        pageNum=4,  # 页数
        level=9,  # 等级
    ).go()

