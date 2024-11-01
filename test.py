from mathw import MathWork


def test_series(series, max_lv, **kwargs):
    for i in range(max_lv):
        lv = i + 1
        print(f">> TEST: series = {series}, level = {lv}")
        MathWork(
            series=series,  # 类别
            pageNum=20,  # 页数
            level=lv,  # 等级
            **kwargs
        ).go()
        print(f">> OK.\n")


def test():
    test_series('add', max_lv=24)
    test_series('mult', max_lv=26)
    test_series('frac', max_lv=18)
    # test_series('form', max_lv=16, pageCapacity=14)


if __name__ == '__main__':
    test()
