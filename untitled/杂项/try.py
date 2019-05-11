#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/1/29 9:28
# @Author : 御承扬
# @mail: 2923616405@qq.com
# @Site : E:\users\lenovo\PycharmProjects\untitled
# @File : try.py
# @Software: PyCharm

f = open("demo.txt", 'wb')  # 文件句柄
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
