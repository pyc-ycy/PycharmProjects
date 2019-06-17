#!/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/17 13:42 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : testPyQt.py 
# @oftware: PyCharm

import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle("Hello,pyqt5")
widget.show()
sys.exit(app.exec_())