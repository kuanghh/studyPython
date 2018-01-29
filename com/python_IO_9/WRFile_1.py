# 读文件
# 使用open(fileName,'r'，encoding = 'gbk')
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('test_read.txt', 'r', encoding='utf8', errors='ignore')
print(f.read())
# 使用完后，务必关闭流
f.close()

# read()方法可以一次读取文件的全部内容，Python把内容读到内存

# 如果打开的文件不存在,则会报出IOError

# Python引入了with语句来自动帮我们调用close()方法,并且这种方法可以达到 try...finally的效果：
with open('test_read.txt', 'r', encoding='utf8') as f1:
    print(f1.readline())  # 读取第一行数据


# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

with open('test_read.txt', 'r', encoding='utf8') as f2:
    for line in f2.readlines():
        print(line.strip())  # 把末尾的'\n'删掉


# 如果是读取处理二进制文件,那么只要修改打开方式就可以了:open('test_read.txt', 'rb', encoding='utf8', errors='ignore')


# 写文件
with open('test_write.txt', 'w', encoding='utf8') as f3:
    f3.write('hello world')


# 模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'
# 以追加（append）模式写入。

with open('test_write.txt', 'a', encoding='utf8') as f4:
    f4.write(' \n append a')


