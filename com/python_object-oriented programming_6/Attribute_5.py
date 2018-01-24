# 实例属性 和 类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：


class Student(object):
    score = 10    # 类的属性

    def __init__(self, name):
        self.name = name        # name是实例的属性


# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
s1 = Student("Mike")
s2 = Student("Tom")

print(s1.score)  # 输出10
print(s2.score)  # 输出10

s1.score = 20    # 重新给s1赋值了一个实例属性score把类属性的score屏蔽掉了
print(s1.score)  # 输出20
print(s2.score)  # 输出10
# 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

print(Student.score)  # 输出10
Student.score = 20
print(s2.score)  # 输出20

# 类属性属于类所有，所有实例共享一个属性;


