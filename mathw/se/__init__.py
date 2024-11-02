"""
自动导入 series. 规范如下：
1、默认导入当前文件夹下所有模块中的类；
2、这些类的的命名格式如下：
    <module_name><postfix><level>，其中 module_name 首字母大写
    例如：AddL10, MultL3,...
3、配置 _config['ignore_modules'] 可以设置不导入的模块（写文件名，不要加后缀）
"""

__all__ = []

import inspect
import os
import importlib


_config = {
    # 动态导入模块 importlib.import_module(name), 其中 name 的前缀
    'module_name_prefix': 'mathw.se.',
    # 不自动导入的模块
    'ignore_modules': {'utils'}
}


def _auto_import():
    modules = _import_modules()
    for module in modules:
        _import_classes_from_module(module)


def _import_modules():
    """
    导入当前问文件夹下的所有模块。
    :param return: list, 被导入的模块对象列表
    """
    # 获取当前文件夹路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    modules = []
    ignore_modules = _config['ignore_modules'] if _config['ignore_modules'] else {}
    # 遍历当前文件夹中的所有文件
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != os.path.basename(__file__):
            module_name = _config['module_name_prefix'] + filename[:-3]
            if module_name not in ignore_modules:
                # 动态导入模块
                module = importlib.import_module(module_name)
                # 保存模块对象
                modules.append(module)

    return modules


def _import_classes_from_module(module, postfix='L'):
    """
    给定模块对象，导入其中的“有效的类”，
    即 AddLn, MultLn, ...，其中 n 是 level
    :param module: 模块对象 add, mult ...
    :postfix: str, 后缀
    """
    module_name = module.__name__[len(_config['module_name_prefix']):].capitalize()
    prefix = module_name + postfix
    # 获取模块中的所有函数和类
    for name, obj in inspect.getmembers(module):
        # 匹配 prefix, 格式 <series_name><postfix><level>,
        # 其中 series_name首字母大写
        if name.startswith(prefix):
            # 添加类到当前命名空间
            globals()[name] = obj
            __all__.append(name)


_auto_import()