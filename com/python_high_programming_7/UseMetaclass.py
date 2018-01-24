# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：


# 先定义一个函数
def fn(self, name='world'):
    print('Hello %s' % name)


# 创建hello class
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()  # 输出 Hello world

# 要创建一个class对象，type()函数依次传入3个参数：
# 1,class的名称；
# 2,继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3,class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# -----------------------------------

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

# metaclass，直译为元类，简单的解释就是：
#
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
#
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
#
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
#
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。




