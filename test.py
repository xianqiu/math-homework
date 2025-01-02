from mathw import MathWork, MathWorkMix


class TestMathWork:

    @staticmethod
    def _test_series(series, levels):
        for level in levels:
            print(f">> [TEST] class = MathWork, series = {series}, level = {level}")
            MathWork(
                series=series,  # 类别
                pageNum=10,  # 页数
                level=level  # 等级
            ).go()

    @classmethod
    def test(cls):
        series = MathWork.get_series()
        for s in series:
            levels = MathWork.get_series_levels(s)
            cls._test_series(s, levels)


class TestMathWorkMix:

    @staticmethod
    def test():
        series = MathWork.get_series()
        for se in series:
            levels = MathWork.get_series_levels(se)
            for level in levels:
                print(f">> [TEST] class = MathWorkMix, series = {se}, level = {level}")
                mm = MathWorkMix()
                mm.add_series(se, levels=[level])
                mm.go()


if __name__ == '__main__':
    TestMathWork.test()
    TestMathWorkMix.test()
