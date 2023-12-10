from .core_settings import *

try:
    from .local_settings import *
except ImportError:
    from .logger_settings import *
