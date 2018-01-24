# 获取对象信息

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型

# 可以使用type
print(type(123))  # 输出 <class 'int'>
print(type(None))  # 输出 <class 'NoneType'>
print(type('str'))  # 输出  <class 'str'>

# 如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))  # <class 'builtin_function_or_method'>

# type 返回的是 对应的Class类型

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types

def fn():
    pass


print(type(fn) == types.FunctionType)  # True

# ----------------------------------------------------------------------------------------
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
print(isinstance(fn, types.FunctionType))  # True

# !!!!!!!!! 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# ----------------------------------------------------------------------------------------
# 使用dir
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

class A:
    def __init__(self, name, score, age, address):
        self.name = name
        self._score = score
        self.__age = age
        self.__address__ = address


a = A('Mike', 90, 23, '广东省')
print(dir(a))
# 输出以下一堆东西
# ['_A__age', '__address__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_score', 'name']


print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__']

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

print(hasattr(a, 'name'))  # 输出 True
setattr(a, 'name', 'Tom')
print(getattr(a, 'name'))  # 输出 Tom

