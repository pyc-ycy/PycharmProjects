# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/17 21:09 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : CallMain.py 
# @oftware: PyCharm

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from 图形界面.test import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())