from beautiful_asserts.settings.base import *  # noqa

try:
    from beautiful_asserts.settings.local import *  # noqa
except ImportError:
    pass
