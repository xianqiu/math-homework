import datetime
from pathlib import Path
import importlib.util

import numpy as np
from Cython.Compiler.Buffer import used_buffer_aux_vars

from .formatter import Formatter
from .se import *


__all__ = ['MathWork', 'MathWorkMix']


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

    def _print_info(self):
        info = [">> [Math Exercises Generated]",
                    f"   |-- series = {self._se}, level = {self._lv}",
                    f"   |-- pages = {self.pageNum}, pageCapacity = {self.pageCapacity}",
                    f"   |-- filename = '{self.outputName}'",
                    f"   |-- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
        print('\n'.join(info))

    def go(self):
        self._config['headerInfo'] = self._gen_header_info()
        content = self._Math().generate(self.pageNum * self.pageCapacity)
        fmt = Formatter(content, **self._config)
        fmt.save()
        self._print_info()

    @staticmethod
    def get_series():
        exclude = ['utils']
        # 获取.se子模块所在的目录路径
        se_module_dir = Path(__file__).parent / 'se'
        return  [name.stem for name in se_module_dir.iterdir()
                      if '__' not in name.stem and name.stem not in exclude]

    @staticmethod
    def get_series_levels(name):
        module_name = f"mathw.se.{name.lower()}"
        module = importlib.import_module(module_name)
        k = len(name) + 1
        levels = [int(item[k:]) for item in module.__dict__.keys()
                  if item.startswith(name.capitalize())]
        return levels


class MathWorkMix(object):

    _config = {
        'pageNum': 10,  # 生成的页数
        'pageCapacity': 14, # 每页最大行数
        'outputName': 'math-work.pdf',
        'showHeaderInfo': True,
    }

    def __init__(self, **kwargs):
        for k, v in self._config.items():
            # 要放在 setattr 之前
            if k in kwargs:
                self._config[k] = kwargs[k]
            setattr(self, k, self._config[k])
        self._recipe = {}

    def add_series(self, series, levels=None, levels_exclude=None):
        if not series in MathWork.get_series():
            raise ValueError(f"{series} is not a valid series.")
        if levels is None:
            self._recipe[series] = MathWork.get_series_levels(series)
        else:
            self._recipe[series] = levels
        if levels_exclude is not None:
            self._recipe[series] = [level for level in self._recipe[series]
                                    if level not in levels_exclude]
        return self

    def _gen_header_info(self):
        info = ''
        if self.showHeaderInfo is True:
            t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            series = ", ".join(list(self._recipe.keys()))
            info = f'Series = [{series}], Levels = Mixed.    Generated at {t}'
        return info

    def _print_info(self):
        print(">> [Math Exercises Generated]")
        print(f"   |-- recipe")
        for series, levels in self._recipe.items():
            print(f"      |-- series = {series}, levels = {levels}")
        print(f"   |-- pages = {self.pageNum}, pageCapacity = {self.pageCapacity}")
        print(f"   |-- filename = '{self.outputName}'")
        print(f"   |-- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def _gen_one_group_by_random(self):
        # randomly choose one series and one level
        series = np.random.choice(list(self._recipe.keys()), 1)[0]
        level = np.random.choice(list(self._recipe[series]), 1)[0]
        # generate one item from the series and level
        Math = globals()[f"{series.capitalize()}L{level}"]
        group_size = getattr(Math, "groupSize", 1)
        group =  Math().generate(group_size)
        return group[0: group_size]

    def _add_head_separator(self, content, group_size, sep_string):
        """
        判断是否需要给 content 添加分隔符sep_string。
        如果需要，则添加分隔符，并返回对应的结果。
        添加分隔符的条件如下（同时满足）：
        1. 当前的行数不是当前页面的第一行；
        2. 上一行不是分隔符；
        3. 剩余的行数 >= group_size + 1；
        """
        used_capacity = len(content) % self.pageCapacity  # 代表当前行数，从0开始计数
        remaining_capacity = self.pageCapacity - used_capacity
        last_line = content[-1] if len(content) > 0 else ""

        conditions = [
            used_capacity != 0,
            last_line != sep_string,
            remaining_capacity >= group_size + 1
        ]
        if all(conditions):
            content += [sep_string]

        return content

    def _add_group(self, content, group, sep_string):
        """
        把 group 添加到 content中，需要同时满足如下条件：
        1. 有剩余空间，即 剩余的行数 > group的行数
        2. 如果当前行不是第一行，则上一行是分隔符
        """
        used_capacity = len(content) % self.pageCapacity  # 代表当前行数，从0开始计数
        remaining_capacity = self.pageCapacity - used_capacity
        last_line = content[-1] if len(content) > 0 else ""

        conditions = [
            remaining_capacity >= len(group),
            used_capacity == 0 or last_line == sep_string
        ]

        if all(conditions):
            content += group
            result = True
        # 否则用占位符标记
        else:
            content += ["|"] * remaining_capacity
            result = False
        return content, result

    def _add_tail_seperator(self, content, group_is_add, sep_string):
        if group_is_add:
            used_capacity = len(content) % self.pageCapacity  # 代表当前行数，从0开始计数
            remaining_capacity = self.pageCapacity - used_capacity
            if remaining_capacity >= 1:
                content += [sep_string]
        return content

    def go(self):
        content_length = self.pageNum * self.pageCapacity
        content = []
        while len(content) < content_length:
            group = self._gen_one_group_by_random()
            if len(group) == 1:
                content += group
                continue
            # 当groupSize大于1时，其前后可能需要添加分隔符
            sep_string = "-" * 40
            content = self._add_head_separator(content, len(group), sep_string)
            content, result = self._add_group(content, group, sep_string)
            content = self._add_tail_seperator(content, result, sep_string)

        self._config['headerInfo'] = self._gen_header_info()
        fmt = Formatter(content, **self._config)
        fmt.save()
        self._print_info()




