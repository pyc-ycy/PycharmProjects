#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @Time : 2018/9/19 17:34
# @Author : 御承扬
# @Site :
# @File : __init__.py.py
# @Software: PyCharm
# %H=8时，对应零点时刻。

# # import time
# # print("当前时间戳：", time.time())
# # print("当前时间：", time.localtime())
# # print("time.gmtime=", time.gmtime())
# # t = (2018, 10, 28, 10, 46, 2, 6, 301, 0)
# # print("%f" % time.mktime(t))
# import time
# t = (2018, 11, 18, 24, 18, 50, 6, 308, 0)
# t = time.mktime(t)
# print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t)))
#
# struct_time = time.strptime("Nov 18 2018 ", '%b %d %Y ')
# print('return tuple:', struct_time)


import re

pt = re.compile(r'(w+)(w+)')
greeting = 'i say, hello world!'

print(pt.sub(r'l 2', greeting))


def func(m):
    return m.group(1).title() + '+m.group(2).title()'


print(pt.sub(func, greeting))
