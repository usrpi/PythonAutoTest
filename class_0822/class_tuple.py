"""
元组
Version: 0.1
Author: usrpi
date: 2020-08-22
"""
# 元组 tuple 符号()
a = (1, 0.02, 'hello', [1,2,3], True)
#1 可以存在空元组a=[]  如果元组里面只有一个元素，要加逗号
#2 元组里面可以包含任何类型
#3 元组里面的元素 根据都好来进行分隔
#4 元组里面的元素 也是有索引索引值从0开始
#5 获取元组里面的单个值：元组[索引值]
#6 元组的切片 同字符串的操作 元组名[索引头:索引尾:步长]
#7 元组不支持任何修改（增删改）
print(a[0:6:2])
print(1,) #如果元组里面只有一个元素，要加逗号,没有都好，数据类型是整形