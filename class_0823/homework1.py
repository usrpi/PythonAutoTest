"""
homework
Version: 0.1
Author: usrpi
date: 2020-08-23
"""
# 例如：passwd={'admin':'123321','user1':'123456'}
# 1、设计一个登录程序，不同的用户名和对应密码存在一个字典里面，输入正确的用户和密码去登录
# 2、首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
# 3、当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入
# 4、如果密码输入错误超过三次，中断程序运行
# 5、当输入密码错误时，提示还有几次机会
# 5、用户名和密码都输入成功的时候，提示登录成功
passwd={'admin':'123321','user1':'123456'}
count = 3
while True:
    name = input('请输入用户名：')
    if name in passwd.keys():
        while count > 0:
            pwd = input('请输入密码：')
            if pwd == passwd[name]:
                print('登录成功')
                break
            else:
                print('密码输入错误请重新输入')
                count -= 1
                print('你还有%d次机会' % count)
        break
    elif name not in passwd.keys() or name =='':
            print('请输入正确的用户名')
















