#!/usr/bin/env python3.7 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/8 16:28 
# @Author : 御承扬 
# @Site :  
# @File : __init__.py.py 
# @Software: PyCharm


a = [1, 2, 3, 4, 9, 12, 20]
a = set(a)
b = set([2, 6, 4, 1, 8, 225])
c = set([1, 2, 4])
'''print(a.intersection(b))
print(a, type(a))
print(a.union(b))
print(b.difference(a))
print(a.difference(b))
print(c.issubset(a))
print(b.issuperset(c))
print(b.issuperset(a))
print(b.symmetric_difference(c))
print(set([0]).isdisjoint(a))'''
print(a & b)
print(a | b)
print(a - b)
print(a ^ b)
print(a.discard(100))