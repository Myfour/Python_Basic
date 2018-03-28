# 单元测试
import unittest


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 为了编写单元测试，我们需要引入Python自带的unittest模块
# ........................


class TestDict(unittest.TestCase):
    pass