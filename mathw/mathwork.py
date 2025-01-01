import datetime
from pathlib import Path

from .formatter import Formatter
from .se import *


class MathWork(object):

    _config = {
        'pageNum': 20,  # 生成的页数
        'pageCapacity': 10, # 每页行数
        'outputName': 'math-work.pdf',
        'showHeaderInfo': True,
    }

    def __init__(self, series, level, **kwargs):
        self._se = series.capitalize()
        self._lv = level
        # load math series class
        self._Math = globals()[f"{self._se}L{self._lv}"]
        # update self._config['pageCapacity'] value
        # if a math series class has defined pageCapacity
        self._init_page_capacity()

        for k, v in self._config.items():
            # 要放在 setattr 之前
            if k in kwargs:
                self._config[k] = kwargs[k]
            setattr(self, k, self._config[k])

    def _init_page_capacity(self):
        # update self._config['pageCapacity'] value
        # if a math series class has defined pageCapacity
        page_capacity = getattr(self._Math, "pageCapacity", None)
        if page_capacity is not None:
            self._config['pageCapacity'] = page_capacity

    def _gen_header_info(self):
        info = ''
        if self.showHeaderInfo is True:
            t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            info = 'Series = {}, Level = {}.   Generated at {}'.\
                format(self._se, self._lv, t)
        return info

    def _print_congrats(self):
        congrats = [">> [Math Exercises Generated]",
                    f"   |-- series = {self._se}",
                    f"   |-- level = {self._lv}",
                    f"   |-- pages = {self.pageNum}",
                    f"   |-- filename = '{self.outputName}'",
                    f"   |-- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
        print('\n'.join(congrats))

    def go(self):
        self._config['headerInfo'] = self._gen_header_info()
        content = self._Math().generate(self.pageNum * self.pageCapacity)
        fmt = Formatter(content, **self._config)
        fmt.save()
        self._print_congrats()

    @staticmethod
    def get_series():
        exclude = ['utils']
        # 获取.se子模块所在的目录路径
        se_module_dir = Path(__file__).parent / 'se'
        return  [name.stem for name in se_module_dir.iterdir()
                      if '__' not in name.stem and name.stem not in exclude]

    def get_series_levels(self, name):
        pass


