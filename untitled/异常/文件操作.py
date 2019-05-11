#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/1 11:39
# @Author : 御承扬
# @mail: 2923616405@qq.com
# @Site : E:\users\lenovo\PycharmProjects\untitled
# @File : 文件操作.py
# @Software: PyCharm

path = './demo.txt'
with open(path,'w') as f:
    f_name = open(path,'w')
    print('write length:',f_name.write("云深不知处，天子笑谈中"))

# str_list = ["风雨前尘\n","傲视苍穹\n","轻抚陈情亦从容\n"]
# print("write length:",f_name.writelines(str_list))
# f_name = open(path,'r')
# print("read result:",f_name.read())
# f_name = open(path,'r')
# print('readline result:',f_name.readlines())
'''f = open("demo", 'wb')  # 文件句柄
# f.write("末尾增加内容")
f.write("\n粤若稽古，"
        "\n圣人之在天地间也，"
        "\n为众生之先。"
        "\n观阴阳之开阖以命物，"
        "\n知存亡之门户，"
        "\n筹策万类之终始，"
        "\n达人心之理，见变化之朕焉，"
        "\n而守司其门户。"
        "\n故圣人之在天下也，"
        "\n自古至今，其道一也。"
        "\n变化无穷，各有所归。"
        "\n或阴或阳，或柔或刚，"
        "\n或开或闭，或弛或张。\n".encode())
# f.seek(20)
f.write("heloowood".encode())
# f.write('\n')
# f.write("------------------")
# f.write("hello\n")
# f.write("wert\n")
# import sys,time
# for i in range(50):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.5)

# print(f.tell())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.tell())  # 打印已读内容字符个数
# f.seek(17)  # 回到文件第17个字符后非换行符开始
# print(f.readline())
# print(f.encoding)  # 打印字符集名称
# print(f.fileno())  # 打印正在使用的电脑文件处理接口序号
# print(f.flush())   # 刷新
# print(f.seekable())  # 回到前文
# print(f.isatty())
# print(f.buffer)
# count = 0
# for line in f:
#     if count == 9:
#         print("-------------")
#         count += 1
#         continue
#     print(line.strip())
#     count += 1
# low loop
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print("-------------")
#         continue
#     print(line.strip())
# a = f.readline()
# b = f.readlines()
# f.write("I like reading, because I can learn a lot by reading\n")
# f.write("zaisuz")
# a = f.read()
# print(a)
# print(b)
f.close()
'''