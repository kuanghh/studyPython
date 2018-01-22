# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 举个栗子，返回一个 计算数列每个元素平方并返回计算后的数列的 函数

def getMySquareList(l):
    def mySquare():
        return [x * x for x in l]
    return mySquare


# 在这里并不会马上计算出所有元素的平方
nl = list(range(10))
f = getMySquareList(nl)
# 当真正调用返回的函数时，才开始计算，能起到一个懒加载的效果
print(f())  # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
nl.append(10)
print(f())  # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 解决办法如下
def getMySquareList2(l):
    nl = l.copy()   # 这里可以防止返回函数引用后续会发生变化的变量
    def mySquare2():
        return [x * x for x in nl]
    return mySquare2


nl2 = list(range(10))
g = getMySquareList2(nl2)
print(g())   # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
nl2.append(10)
print(g())   # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# -----------------------------------------------------------------------------------------------------------
# 闭包

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 举个列子

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())  # 输出9
print(f2())  # 输出9
print(f3())  # 输出9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def newCount():
    def k(j):
        def cal():
            return j * j
        return cal
    fs = []
    for x in range(1, 4):
        fs.append(k(x))
    return fs


f4, f5, f6 = newCount()
print(f4())  # 输出1
print(f5())  # 输出4
print(f6())  # 输出9
# 缺点是代码较长，可利用lambda函数缩短代码。





