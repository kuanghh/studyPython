# 继承与多态

class Animal(object):

    def run(self):
        print('animal run')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()

dog.run()  # 输出 animal run
cat.run()  # 输出 animal run

# 可以覆盖父类的方法
class Rabbit(Animal):
    def run(self):
        print('rabbit run')


rabbit = Rabbit()
rabbit.run()  # 输出 rabbit run


# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：







