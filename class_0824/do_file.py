"""
文件操作
Version: 0.1
Author: usrpi
date: 2020-08-24
"""

# file txt xml html
file = open('python11.txt','r+', encoding='utf-8')
# mode 打开这个文件的模式
# r  w  a
# r+ w+  a+
res = file.read() # 进行完一次读取操作后 光标就到文末
file.write('卡卡666')
print(res)

#1 file文件open之后默认是r 只读模式 如果你要是写入内容 报错
#2 r+ 可读可写 先写的话 从头开始覆盖写 读光标之后的内容 读写跟着光标走
#3 如果要写入中文，要指定编码格式
#4 w 只写 硬要去读 就会报错
#5 w+ 可读可写 不管是w 还是w+ 如果文件存在 就直接清空 再重写
# 如果文件不存在 则新建一个文件 然后写
#6 a 追加 a+ 推荐