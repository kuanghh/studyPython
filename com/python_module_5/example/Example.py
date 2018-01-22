# 用来校验模块的访问限制
name = 'Jack'

_score = 85

__age = 20

__address__ = '广州'

def get_age():
    return __age


def _printDate():
    print("_printDate")

def __printDate():
    print("__printDate")

def __printDate__():
    print("__printDate__")