"""
-*- coding: utf-8 -*-
File    : classwork2.py
Version : 0.1
Author  : usrpi
Date    :2020/8/28
"""
# 封装http
import requests
class HttpRequest:
    def http_request(self, url, data, method, cookie = None):
        if method == 'get':
            res = requests.get(url, data, cookies = None)
        else:
            res = requests.post(url, data, cookies = None)
        return res
if __name__ == '__main__':
    url = 'http://192.168.10.133:8080/index.php?m=user&c=public&a=login'
    data = {'username': 'test01', 'password': '123456'}
    res = HttpRequest().http_request(url, data, 'post')
    print(res.status_code)




