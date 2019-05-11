#!/usr/bin/env python3.7 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/8 9:14 
# @Author : 御承扬 
# @Site :  
# @File : __init__.py.py 
# @Software: PyCharm


class Demo(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print("name: %s" % self.name)


stu = Demo("楼月明")
stu()
print(callable(Demo("楼月明")))
print(callable(None))
print(callable(stu))
print(callable(max))
print(callable(abs(1)))
