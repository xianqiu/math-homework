from mathw import MathWork


def _test_series(series, max_lv, **kwargs):
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
    jobs = [
        {"series": "add", "max_lv": 24},
        {"series": "mult", "max_lv": 26},
        {"series": "frac", "max_lv": 18},
        {"series": "form", "max_lv": 15},
    ]
    for job in jobs:
        _test_series(**job)


if __name__ == '__main__':
    test()
