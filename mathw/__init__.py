__all__ = ['MathWork']

import datetime

from .series import *
from .formatter import Formatter


class MathWork(object):

    _config = {
        'pageNum': 40,  # 生成的页数
        'pageCapacity': 10,  # 每页的题目数'
        'outputName': 'math-work.pdf',
        'showHeaderInfo': True,
    }

    def __init__(self, series, level, **kwargs):
        self._se = series
        self._lv = level
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

