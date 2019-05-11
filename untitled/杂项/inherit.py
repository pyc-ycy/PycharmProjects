# /usr/bin/python3.7
# /-*-coding:UTF-8-*-

class Electrical(object):
    def function(self):
        print("Electrical can perform specific functions after power supply")


class Location(object):
    def weizhi(self):
        print("Every electrical have its own location")


class Television(Electrical, Location):
    def function(self):
        print("Television can play TV shows and see news")

    def weizhi(self):
        print("stand at home.")


class SoundBox(Electrical, Location):
    def function(self):
        print("SoundBox can play musics")

    def weizhi(self):
        print("stand at home.")


class Computer(Electrical, Location):
    def function(self):
        print("Computer can search information online and do office works")

    def weizhi(self):
        print("can bring to everywhere")


def using(electrical):
    electrical.function()
    electrical.weizhi()


using(Computer())
using(SoundBox())
