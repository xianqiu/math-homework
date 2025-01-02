from mathw import MathWork, MathWorkMix


def gen_series_mix():
    mm = MathWorkMix()
    # mm.add_series('add')
    # mm.add_series('mult')
    mm.add_series('form')
    # mm.add_series('func')
    mm.go()


def gen_series():
    MathWork(
        series='form',  # 类别
        pageNum=10,  # 页数
        level=6,  # 等级
    ).go()


if __name__ == '__main__':
    # gen_series_mix()
    gen_series()



