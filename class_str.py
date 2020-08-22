s = 'hello!'

print(len(s))

print(s[1:5:1]) #步长

#请利用切片，倒叙输出S的值，输出结果为！olleh
print(s[::-1])
print(s[-1:-7:-1])

#字符长的分割   字符串.split(可以指定切割符号，切割次数)
# 返回一个列表类型的数据  列表里面的子元素都是字符串类型
# 指定切割符 被切走了
print(s.split())
print(s.split('e')) #  e 被切走了
print(s.split('l',1))  # 指定切割次数

#字符串的替换  字符串.replace(指定替换值，新值，替换次数)
new = s.replace('o', '@') # 将 o 替换成 @
print(new)

#字符串的去除指定字符 字符串.strip(指定字符)
# 1 默认去掉空格 ，
# 2 只能去掉头和尾的指定的字符
l = ' 666hel6lo!'
print(len(l))
new1 = l.strip('6')
print(len(new1))

# 字符串的拼接 + 保证+两边的变量值类型要一直
s_1 = 'python'
s_2 = '中秋节快乐！'
s_3 = 666
print(s_1+s_2)
print(s_1+s_2+str(s_3)) # 报错，s_3为整形,str转换成字符串

# 字符串格式化输出 % format
age = 18
name = '小恒星'
print('')

# 格式化输出1： format 特点{} 用这个{}来占坑
print('python12期的{}，今年{}岁!'.format(name,age))

# 格式化输出2：%  %s字符串 %d数字 %f浮点数
print('python12期的%s，今年%d岁!' %(name,age))
# %s 可以填任何类型数据
# %d 只能填数字 整形 浮点型

