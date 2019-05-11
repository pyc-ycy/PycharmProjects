#!/usr/bin/python3.7
# -*-coding:UTF-8-*-
'''
时间：二零一八年八月十五号
函数：输出九九乘法变，使用for循环
     判断是否为闰年，使用if elseif 嵌套
     判断奇偶数 ，使用简单判断语句if
     判断阿姆斯特朗数
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=" ")
    print(" ")

print("----------")
num = int(input("请输入年份："))
if num % 100 == 0:
    if num % 400 == 0:
        print("是闰年")
    else:
        print("不是闰年")
else:
    if num % 4 == 0:
        print("是闰年")
    else:
        print("不是闰年")

print("------------")
x = int(input("请输入一个整数："))
if x % 2 == 0:
    print("输入的整数为偶数：", x)
else:
    print("输入的整数为奇数：", x)

print("--------------")


def fun(y):
    if y > 1000:
        print("数据错误，程序退出！！！")
        exit()
    else:
        if 100 < y < 1000:
            y1 = y % 10
            y2 = (y % 100 - y1) // 10
            y3 = (y - (y % 100)) // 100
            print(y1)
            print(y2)
            print(y3)
            if y == y1 * y1 * y1 + y2 * y2 * y2 + y3 * y3 * y3:
                print("输入的数为阿姆斯特朗数")
            else:
                print("不是阿姆斯特朗数")
        elif 10 < y < 100:
            y1 = y % 10
            y2 = (y - y1) / 10
            print(y1)
            print(y2)
            if y == y1 * y1 + y2 * y2:
                print("输入的是阿姆斯特朗数")
            else:
                print("输入的不是阿姆斯特朗数")
        elif y < 10:
            print("输入的数是阿姆斯特朗数")


z = int(input("请输入一个数："))

if z > 1000:
    z = int(input("请重新输入一个数，数值在1~1000之间："))
    fun(z)
else:
    fun(z)

i
