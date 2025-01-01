from mathw import MathWork


def _test_series(series, levels, **kwargs):
    for level in levels:
        print(f">> TEST: series = {series}, level = {level}")
        MathWork(
            series=series,  # 类别
            pageNum=10,  # 页数
            level=level,  # 等级
            **kwargs
        ).go()
        print(f">> OK.\n")


def test_all_series():
    series = MathWork.get_series()
    for s in series:
        levels = MathWork.get_series_levels(s)
        _test_series(s, levels)


if __name__ == '__main__':
    test_all_series()
