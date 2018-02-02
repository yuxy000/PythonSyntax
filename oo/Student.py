#!usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
-------------------------------
@Author:    yuxy
@Time:      2018/2/2 14:47
@File:      Student.py
@Project:   PythonSyntax
--------------------------------
"""


class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


s = Student('yuxy', 90, 'm')
print(s.get_name())
s.print_score()
print(s._Student__name)
s. set_score(99)
s.print_score()