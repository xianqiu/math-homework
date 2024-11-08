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

    def _print_congrats(self):
        congrats = ['== 好好学习，天天向上 ==',
                    '>> Series = {}'.format(self._se),
                    '>> Level = {}'.format(self._lv),
                    '>> 页数 = {}'.format(self.pageNum),
                    '>> Done.']
        print('\n'.join(congrats))

    def go(self):
        self._config['headerInfo'] = self._gen_header_info()
        mathLL = globals()['{}L{}'.format(self._se, self._lv)]
        content = mathLL().generate(self.pageNum * self.pageCapacity)
        content = self._refine_content(content)
        Formatter(content, **self._config).save()
        self._print_congrats()

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
                    'levels': {4, 5, 6},
                    'pageCapacity': 13
                },
                {
                    'levels': {11},
                    'pageCapacity': 12
                },
            ]
        }
        if self._se not in config.keys():
            return
        for item in config[self._se]:
            if self._lv in item['levels']:
                self._config['pageCapacity'] = item['pageCapacity']
                break

    def _separate_equations(self, content):
        """ 给方程组添加分隔符。
        """
        k = 2 # 方程组的方程数量
        sep_length = 40 # 分隔符的长度
        sep = '-' * sep_length
        # 计算一页的方程个数(eq_num)
        # 一页的行数(pageCapacity) = 分隔符行数(eq_num / k + 1) + 方程个数(eq_num)
        eq_num = (self.pageCapacity - 1) * k / (k+1)
        res = []
        for i in range(len(content)):
            j = i % eq_num
            # 每页开头添加一行分隔符
            if j == 0:
                res.append(sep)
            # 每k个方程添加一行分隔符
            if j % k == k-1:
                res.append(content[i])
                res.append(sep)
            else:
                res.append(content[i])

        return res[0: self.pageCapacity * self.pageNum]

    def _refine_content(self, content):
        if self._se == 'Form':
            if self._lv in {4, 5, 6}:
                return self._separate_equations(content)
        return content
