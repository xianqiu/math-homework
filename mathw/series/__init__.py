__all__ = []

import inspect
import sys

from .add import *
from .mult import *


def clean_import(prefix):
    # __all__ only contains classes start with prefix.
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if name.lower().startswith(prefix):
            __all__.append(name)


clean_import('add')
clean_import('mult')

