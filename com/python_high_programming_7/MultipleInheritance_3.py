# 多重继承

# python支持多重继承

class Runnable(object):
    pass

class Flyable(object):
    pass

class Animal(object):
    pass


class Duck(Animal, Flyable, Runnable):
    pass

# 通常，主线都是单一继承下来的，例如,Duck集成自Animal，但是如果需要“混入”额外的功能，通过多重继承就可以实现
# ，比如，让Duck除了继承自Animal外，再同时继承Runnable。这种设计通常称之为MixIn。

# 所以 一般的写法应该是
# 将额外的功能写成

class RunnableMixIn(object):
    pass

class FlyableMixIn(object):
    pass

# 然后
class Bird(Animal, RunnableMixIn, FlyableMixIn):
    pass
# 这样符合规范一点

