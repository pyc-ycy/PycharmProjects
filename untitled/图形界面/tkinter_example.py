# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/13 19:29 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : tkinter_example.py 
# @oftware: PyCharm

import tkinter


def turn_propety(event):  # 自定义回调函数
    event.widget["activeforeground"] = "red"  # 鼠标左键按下时，标题显示红色
    event.widget["text"] = "OK"  # 鼠标指针接触按钮时，标题变为OK


MainFrom = tkinter.Tk()  # 建立窗体实例
MainFrom.geometry("400x300")  # 设置窗体物理大小（长x高）
MainFrom.title("Python图形界面测试实例")  # 设置窗体标题
MainFrom.iconbitmap("D:\\users\\lenovo\\PycharmProjects\\untitled\\图形界面\\bitmap3.ico")  # 设置图标属性
MainFrom['background'] = 'LightSlateGray'  # 设置窗体背景颜色为亮石板石灰色
btn1 = tkinter.Button(MainFrom, text='退出', fg='black')  # 创建按钮
btn1.pack(side="top")  # pack()方法将btn1放置到窗体上顶部
btn1.bind("<Enter>", turn_propety)
btn2 = tkinter.Button(MainFrom, text="2", fg="black")
btn3 = tkinter.Button(MainFrom, text="3", fg="black")
btn4 = tkinter.Button(MainFrom, text="Cancel", fg="black")
btn2.pack(side="left")  # 将按钮放置在窗体的左部
btn3.pack(side="right")  # 将按钮放置在窗体的右部
btn4.pack(side="bottom")  # 将按钮放置在窗体的底部
MainFrom.mainloop()  # 启动窗体运行，并等待接收各种事件信息
