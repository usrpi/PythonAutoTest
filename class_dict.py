"""
字典
Version: 0.1
Author: usrpi
date: 2020-08-22
"""
# 字典  dict 符号{} 大括号 无序的
#1 可以存在空字典a=[]
#2 字典里面数据存储方式：key:value
#3 字典里面value可以包含任何类型的数据
#4 字典里面的元素 根据逗号来进行分隔
a = {'class':'python',
     'student':119,
     'teacher':'girl',
     'age':20,
     'score':[99,88.8,100,5]}

# 字典取值：字典[key]
print(a['score'])

# 删除 pop(key) 指明删除的值的key
res = a.pop('teacher')
print(res)

# 新增 a[新key]=value  字典里不存在的key
a['name']='阿珂'

# 修改 a[已经存在的key]=新value  字典里面已存在的key
a['age'] = 22