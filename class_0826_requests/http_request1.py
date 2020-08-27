"""
http_request 封装
Version: 0.1
Author: usrpi
date: 2020-08-27
"""
# python 来完成HTTP请求 get post
# requests 第三方库

import requests
class HttpRequest:
    # 利用request封装 get 和 post请求

    def http_request(self,url, data, method, cookie = None):
        # url:请求的地址 http：//xxx:port
        # param:传递的参数 非必填参数
        # method:请求方式 支持get post
        # cookie：请求的时候传递的cookie值
        if method == 'get':
            res = requests.get(url, data, cookies=None)  # 响应结果的消息实体
        else:
            res = requests.post(url, data, cookies = None) # 响应结果的消息实体
        # print('响应正文2：', res.json) # dict json  # 推荐使用json 方便取值
        # print('响应头：', res.headers)
        return res # 返回一个消息实体
if __name__ == '__main__':
    url = 'http://192.168.10.131:8080/api193/Login'
    data = {'username': 'liufeng', 'password': '123456'}
    res = HttpRequest().http_request(url,data,'post')
    print('登录结果是：', res.text)