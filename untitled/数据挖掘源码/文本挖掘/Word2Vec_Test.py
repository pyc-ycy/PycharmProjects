# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/6 16:51 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : Word2Vec_Test.py 
# @oftware: PyCharm

import gensim
model = gensim.models.Word2Vec.load('./model/wiki.zh.text.model')
flag = 1
while flag:
    word = input("Please input the key_word:\n")
    if word in model:
        print(model['word'])
        # 词相似度
        result = model.most_similar(word)
        for e in result:
            print(e[0], e[1])
    else:
        print('单词不在字典中')

    flag = int(input("do you want to input next(yes=1,no=0):\n"))

# 计算两个单词相似度
print("水杯和水瓶的相似度为：", model.similarity('水杯', '水瓶'))

# 模型还提供了一个方法，用于寻找离群词：
print(model.doesnt_match(u"早餐 晚餐 午餐 中心".split()))
# 我们还可以根据给定的条件推断相似词，比如下面的代码中，我们找到一个跟篮球最相关，跟计算机很不相关的第一个词：
print(model.most_similar(positive=['篮球'], negative=['计算机'],topn=1))