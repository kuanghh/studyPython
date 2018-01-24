# 使用 @property
from types import MethodType


class Student(object):
    pass


student = Student()


# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# student.score = 99999  # 这样显然是不符合逻辑的
# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

def set_score(self, score):
    if not isinstance(score, int):
        raise ValueError('score must be an integer!')
    if score < 0 or score > 100:
        raise ValueError('score must between 0 ~ 100!')
    self._score = score


def get_score(self):
    return self._score


Student.set_score = set_score
Student.get_score = get_score
student.set_score(99)
print(student.get_score())  # 输出 99


# -----------------------------------------------------------
# 但像上面这样略显复杂
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class HighStudent(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score


# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：


hstudent = HighStudent()
hstudent.score = 60
print(hstudent.score)  # 输出 60

hstudent2 = HighStudent()
# hstudent.score = 9999  # 报错
