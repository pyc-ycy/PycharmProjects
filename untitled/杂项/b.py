#!/usr/bin/env python3.7 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/26 14:43 
# @Author : 御承扬 
# @Site :  斐波那契数列
# @File : b.py 
# @Software: PyCharm

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration();
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b

        return a


for n in Fib():
    print('%d\t' % n)
print("-----------")
fib = Fib()
print(fib[3])