__all__ = ['MathWork']

import datetime
from .se import *
from .formatter import Formatter


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
        # 调整页面的行数
        self._refine_page_capacity()
        # 要放在 setattr 之前
        for k, v in self._config.items():
            if k in kwargs:
                self._config[k] = kwargs[k]
            setattr(self, k, self._config[k])

    def _gen_header_info(self):
        info = ''
        if self.showHeaderInfo is True:
            t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            info = 'Series = {}, Level = {}.   Generated at {}'.\
                format(self._se, self._lv, t)
        return info

    def go(self):
        mathLL = globals()['{}L{}'.format(self._se, self._lv)]
        items = mathLL().generate(self.pageNum * self.pageCapacity)
        self._config['headerInfo'] = self._gen_header_info()
        Formatter(items, **self._config).save()
        congrats = ['好好学习，天天向上。',
                    '>> Series = {}'.format(self._se),
                    '>> Level = {}'.format(self._lv),
                    '>> 页数 = {}'.format(self.pageNum),
                    '不要放弃。']
        print('\n'.join(congrats))

    def _refine_page_capacity(self):
        config = {
            'Frac': [
                {
                    'levels': {8, 9, 17, 18},
                    'pageCapacity': 12
                },
            ],
            'Form': [
                {
                    'levels': {8, 9},
                    'pageCapacity': self._config['pageCapacity']
                                    + self._config['pageCapacity'] // 2 - 1
                },
            ]
        }
        if self._se not in config.keys():
            return
        for item in config[self._se]:
            if self._lv in item['levels']:
                self._config['pageCapacity'] = item['pageCapacity']
                break