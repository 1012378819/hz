# -*- coding:utf-8 -*-
# @Time : 2020/4/6 12:28
# @Author: lup
__author__ = 'pei.lu'
import requests
class DoRequest:
    def __init__(self,base_url):
        self.base_url=base_url

    def api_method(self,method,url,data=None):
        if method.upper()=='GET':
            requests.get(self.base_url+url,params=data)
        elif method.upper()=='POST':
            requests.post(self.base_url+url,data=data)  # json是请求头里content-type为json格式，data是content-type为form表单格式