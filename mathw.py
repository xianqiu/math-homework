import datetime

from generators import *
from formatter import Formatter


class MathWork(object):

    _config = {
        'pageNum': 40,  # 生成的页数
        'pageCapacity': 10,  # 每页的题目数'
        'outputName': 'math-work.pdf',
        'showHeaderInfo': True,
    }

    def __init__(self, level, **kwargs):
        assert isinstance(level, int) and 1 <= level <= 12, \
            'LEVEL must be in 1, 2, ..., 12.'
        self._lv = level

        for k, v in self._config.items():
            if k in kwargs:
                self._config[k] = kwargs[k]
            setattr(self, k, self._config[k])

    def gen_header_info(self):
        info = ''
        if self.showHeaderInfo is True:
            t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            info = 'Level = {}.   Generated at {}'.format(self._lv, t)
        return info

    def go(self):
        mathLL = globals()['MathL%d' % self._lv]
        items = mathLL().generate(self.pageNum * self.pageCapacity)
        self._config['headerInfo'] = self.gen_header_info()
        Formatter(items, **self._config).save()

        congrats = ['好好学习，天天向上',
                    '>> Level = {}'.format(self._lv),
                    '>> 页数 = {}'.format(self.pageNum),
                    '恭喜宝宝，又可以做题了。']
        print('\n'.join(congrats))