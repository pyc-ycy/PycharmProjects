# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/6 16:36 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : Fenci.py 
# @oftware: PyCharm

# 文章分词
import jieba
import jieba.analyse
import codecs


def cut_words(sentence):  # print sentence

    return " ".join(jieba.cut(sentence)).encode('utf-8')
f=codecs.open('wiki.zh.jian.text','r',encoding="utf8")
target = codecs.open("wiki.zh.jian.seg.txt", 'w',encoding="utf8")
print ('open files')
line_num=1
line = f.readline()
while line:
    print('---- processing', line_num, 'article----------------')
    line_seg = " ".join(jieba.cut(line))
    target.writelines(line_seg)
    line_num = line_num + 1
    line = f.readline()
f.close()
target.close()
exit()
while line:
    curr = []
    for oneline in line:
        #print(oneline)
        curr.append(oneline)
    after_cut = map(cut_words, curr)
    target.writelines(after_cut)
    print ('saved',line_num,'articles')
    exit()
    line = f.readline1()
f.close()
target.close()