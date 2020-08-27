"""
request
Version: 0.1
Author: usrpi
date: 2020-08-26
"""
# python 来完成HTTP请求 get post
# requests 第三方库

import requests

url = 'http://192.168.10.131:8080/api193/Login?username=liufeng&password=123456'
res = requests.get(url) # 返回一个消息实体
print(res)

# 响应头 响应状态码 响应报文
print("响应头：", res.headers)
print("响应状态码：", res.status_code)
print('响应正文：', res.text)

# post请求 带参数
url1= 'http://192.168.10.131:8080/api193/Login'
data ={'username':'liufeng', 'password':'123456'}
res1 = requests.post(url1, data, cookies = None) # 响应结果的消息实体
print('响应正文2：', res1.json) # dict json  # 推荐使用这种 方便取值
