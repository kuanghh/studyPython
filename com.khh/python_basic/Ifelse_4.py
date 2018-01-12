# 条件判断

age = 20
if age >= 20:
    print('your age is ', age)
    print('audit')

# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。


age = 3
if age >= 18:
    print('your age is ', age)
    print('audit')
else:
    print('your age is ', age)
    print('child')

age = 8
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# if判断条件还可以简写，比如写
x = ''
if x:
    print('True')
else:
    print('False')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。


s = input('your birth: ')
birth = int(s)   # 因为 input输入的是string，所以如果要将birth转换成int，需要用到 int()函数
if birth < 2000:
    print('00前')
else:
    print("00后")
