# -*- coding:utf-8 -*-
# @Time : 2020/4/6 19:38
# @Author: lup
__author__ = 'pei.lu'

a=[{'word':'5 u'},{'word':'3 w'}]
res=''
for i in a:
    a=i['word']
    # s=a.split(' ')
    # b=''.join(s)
    b=a.replace(' ','')
    res+=b
print(res)
