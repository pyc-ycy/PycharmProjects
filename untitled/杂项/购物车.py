#!/usr/bin/env python3.7 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/26 11:42 
# @Author : 御承扬 
# @Site :  
# @File : 购物车.py
# @Software: PyCharm
import time

a = int(input("请输入你的余额："))
print("你的余额：", a)
goods = ["1.Iphone-plus 12000", "2。bicycle 800", "3.computer 5000", "4.大英百科 140", "5.速溶咖啡 20/盒", "6.华为智能手环 120"]
pay = [12000, 800, 5000, 140, 20, 120]
cart = []
print("商品列表：")
for i in goods:
    print(i)

while True:
    b = input("请输入商品编号(如果不想购买，请输入not）：")
    if b.isdigit():
        b = int(b)
        print(goods[b - 1])
        c = input("确认是否购买此商品(yes, not or exit):")
        if c == "yes":
            if a - pay[b - 1] >= 0:
                print("购买成功！")
                print("你的余额：", a - pay[b - 1])
                a = a - pay[b - 1]
                cart.append(goods[b - 1])
            else:
                print("余额不够，请重新选择")
        elif c == "not":
            print("取消购买，请重新选择")
        elif c == "exit":
            break
        else:
            print("命令错误！")
    elif b == "not":
        break
    else:
        print("输入错误，请重新输入")

print("------您所购买的商品-------")
print("商品编号 商品名称 价格")
for j in cart:
    print("\033[32;1m%s\033[0m" % j)
print("您的余额目前剩下：\033[31;1m%s\033[0m" % a)
print("欢迎下次惠顾，祝您生活愉快！！")
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print("-------------------------")
