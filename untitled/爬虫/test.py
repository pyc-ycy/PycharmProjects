# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/13 8:47 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : test.py 
# @oftware: PyCharm

import sys
import os
import urllib.request
from bs4 import BeautifulSoup


file_path = "./"
response = urllib.request.urlopen("https://movie.douban.com/subject/25890017/?from=showing/")
# print response.info()
html = response.read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('img')
j=1
for i in links:
    imgsrc = i.attrs['src']
    file_suffix = os.path.splitext(imgsrc)[1]
    file_name = "test"+str(j)
    filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
    print(filename)
    urllib.request.urlretrieve(imgsrc, filename=filename)
    j=j+1
# print html
response.close()