# 读文件
# 使用open(fileName,'r'，encoding = 'gbk')
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('test_demo.txt', 'r', encoding='utf8', errors='ignore')
print(f.read())
# 使用完后，务必关闭流
f.close()

# read()方法可以一次读取文件的全部内容，Python把内容读到内存

# 如果