# 使用枚举类

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

# value属性则是自动赋给成员的int常量，默认从1开始计数。


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique  # 装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问这些枚举类型可以有若干种方法：

print(Weekday.Tue)      # 输出 Weekday.Tue
print(Weekday['Tue'])   # 输出 Weekday.Tue
print(Weekday.Tue.value)  # 输出 2
print(Weekday(2))       # 输出 Weekday.Tue
