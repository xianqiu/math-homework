from mathw import MathWork, MathWorkMix


def gen_series():
    MathWork(
        series='mult',  # 类别
        pageNum=10,  # 页数
        level=1,  # 等级
    ).go()


def gen_series_mix():
    mm = MathWorkMix()
    mm.add_series('add')
    mm.add_series('mult', levels_exclude=[8])
    mm.add_series('form')
    mm.add_series('func')
    mm.go()


if __name__ == '__main__':

    # gen_series()
    gen_series_mix()


