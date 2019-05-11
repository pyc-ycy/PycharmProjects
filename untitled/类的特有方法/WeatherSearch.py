#!/usr/bin/env python3.7 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/8 10:15 
# @Author : 御承扬 
# @Site :  
# @File : WeatherSearch.py 
# @Software: PyCharm


class WeatherSearch(object):
    def __int__(self, input_daytime):
        self.input_daytime = input_daytime

    def search_visibility(self):
        visible_leave = 0
        if self.input_daytime == "daytime":
            visible_leave = 2
        elif self.input_daytime == "night":
            visible_leave = 9
        return visible_leave

    def search_temperature(self):
        temperature = 0
        if self.input_daytime == "daytime":
            temperature = 26
        elif self.input_daytime == "night":
            temperature = 16
        return temperature


class OutAdvice(WeatherSearch):
    def __init__(self, input_daytime):
        WeatherSearch.__int__(self, input_daytime)

    def search_temperature(self):
        vehicle = " "
        if self.input_daytime == "daytime":
            vehicle = "bike"
        if self.input_daytime == "night":
            vehicle = "taxi"
        return vehicle

    def out_advice(self):
        visible_leave = self.search_visibility()
        if visible_leave == 2:
            print("the weather is good ,suitable for use %s" % self.search_temperature())
        elif visible_leave == 9:
            print("the weather bad,you should use %s" % self.search_temperature())
        else:
            print("the weather is beyond my scope, I can not give you any advice")


a = input("请输入白天或黑夜（英文）")
check = OutAdvice(a)
check.out_advice()
d = OutAdvice("night")
d.out_advice()