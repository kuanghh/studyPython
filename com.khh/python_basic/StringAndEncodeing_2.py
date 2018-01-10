# 字符串与编码

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：

print("包含中文的str")

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

print(ord('A'))

print(chr(65))

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：

print('ABC'.encode('ascii'))  # 输出 b'ABC'

print('中文'.encode('utf-8'))  # 输出 b'\xe4\xb8\xad\xe6\x96\x87'

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

print(b'ABC'.decode('ascii'))  # 输出 ABC

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 输出 中文

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：

print(len(b'ABC'))  # 输出 3

print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 输出 6

print(len('中文'.encode('utf-8')))  # 输出 6

# ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

# 格式化 采用的格式化方式和C语言是一致的，用%实现

print("hello,%s" % 'world')  # 输出 hello,world

print('Hi, %s, you have $%d.' % ('Michael', 1000000))  # 输出 Hi, Michael, you have $1000000.

# 常见的占位符有：
# 占位符	    替换内容
#   %d	      整数
#   %f	     浮点数
#   %s	     字符串
#   %x	   十六进制整数


# 格式化还有另外一种方法  format
# 使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……

print('Hello, {0}, 成绩提升了 {1:.2f}%，总分 {2: .2f}'.format('tom', 17.65, 150.673))  # 输出 Hello, tom, 成绩提升了 17.65%，总分 150.67
#  {1:.2f}的意思是 ： 第二个位置，并且需要一个浮点数，而且会保留两位数字
