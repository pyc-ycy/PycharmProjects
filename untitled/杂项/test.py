#!/usr/bin/python3.7
# -*-coding:UTF-8-*-


'''import sys
print(sys.argv)
print(sys.argv[2])
print(sys.api_version)'''

'''import os
cmd_res = os.system("dir")#只执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("----->",cmd_res)'''


class Test(object):
    def __init__(self):
        pass

    def __foo(self):
        print("这是私有方法")

    def foo(self):
        print("这是公共方法")
        print("公共方法中调用私有方法")
        self.__foo()
        print("公共方法调用私有方法结束")

    @staticmethod
    def action(num):
        if num == 1:
            print("turn right")
        elif num == 2:
            print("turn left")
        elif num == 3:
            print("go ahead")
        elif num == 4:
            print("come back")
        else:
            print("your order is missing, I can't do it")
        return 0

class Does(object):
    @staticmethod
    def t1():
        move = Test()
        op = int(input("please input a number:"))
        move.action(op)
        return 0




'''pri_pub = Test()
print("开始调用公共方法")
pri_pub.foo()
print("开始调用私有方法")
pri_pub.action(2)
pri_pub.action(4)
pri_pub.action(5)'''
c = Does()
c.t1()

