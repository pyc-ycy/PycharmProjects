# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/5/9 8:21 
# Author : 御承扬
# e-mail:2923616405@qq.com
# site:  
# File : apriori_code_test.py 
# @oftware: PyCharm

from apriori_my import Apriori
from pandas import read_csv


# dataset = [
#     ['bread', 'milk'],
#     ['bread', 'diaper', 'beer', 'egg'],
#     ['milk', 'diaper', 'beer', 'cola'],
#     ['bread', 'milk', 'diaper', 'beer'],
#     ['bread', 'milk', 'diaper', 'cola'],
# ]

d = read_csv("./data.csv")
train_data = d.values
dataset = []
for k in train_data:
    for j in k:
        dataset.append(j)

minsup = minconf = 0.2

ap = Apriori(dataset, minsup, minconf)

ap.run()
ap.print_frequent_itemset()
ap.print_rule()
