# 类和实例

# 定义一个student类
class Student(object):
    pass


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

# 创建实例：类名+()
student = Student()
print(student)  # 输出  <__main__.Student object at 0x0000004AE0C771D0>
# 可以看到，变量student指向的就是一个Student的实例，后面的0x0000004AE0C771D0是内存地址，每个object的地址都不一样，而Student本身则是一个类。

# 可以自由地给一个实例变量绑定属性，比如，给实例student绑定一个name属性
student.name = 'Tom'
print(student.name)  # 输出 Tom

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student2(object):

    def __init__(self, name, score):
            self.name = name
            self.score = score


student2 = Student2("Jack", 89)
print("name : %s ,score %s" % (student2.name, student2.score))  # 输出 name : Jack ,score 89
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：















