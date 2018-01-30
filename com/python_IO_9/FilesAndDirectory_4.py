# 操作文件和目录

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
import os

# 查看当前目录的绝对路径
print(os.path.abspath('.'))  # D:\PycharmProjects\studyPython\com\python_IO_9

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
newDirPath = os.path.join(os.path.abspath('.'), 'newdir')
print(newDirPath)  # D:\PycharmProjects\studyPython\com\python_IO_9\newdir

# 创建一个目录
os.mkdir(newDirPath)

# 删除一个目录
os.rmdir(newDirPath)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

print(os.path.split(newDirPath))  # 输出 ('D:\\PycharmProjects\\studyPython\\com\\python_IO_9', 'newdir')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/abc/demo.txt'))  # 输出 ('/abc/demo', '.txt')

# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')


