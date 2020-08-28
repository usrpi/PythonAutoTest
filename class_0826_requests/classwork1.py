"""
-*- coding: utf-8 -*-
File    : classwork1.py
Version : 0.1
Author  : usrpi
Date    :2020/8/28
"""
# post 请求海盗商城登录

import requests
url = 'http://192.168.10.133:8080/index.php?m=user&c=public&a=login'
data  = {'username':'test01', 'password':'123456'}
res = requests.post(url, data)
print('响应头是：', res.headers)
print('状态码是：', res.status_code)
print('cookies是：', res.cookies)
print('响应正文是：', res.json)
# print(res.text)
