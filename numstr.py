#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import operator


class NumStr(object):

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string
        __slots__ = ('fo','bar')

    def __str__(self):
        return '[%d :: %r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __lt__(	self, other):
        return operator.lt(self.__num, other.__num) and operator.lt(self.__string, other.__string)

    def __le__(self, other):
        return operator.le(self.__num, other.__num) and operator.le(self.__string, other.__string)

    def __eq__(self, other):
        return operator.eq(self.__num, other.__num) and operator.eq(self.__string, other.__string)

    def __ne__(self, other):
        return not operator.ne(self.__num, other.__num) or not operator.ne(self.__string, other.__string)

    def __gt__(self, other):
        return operator.gt(self.__num, other.__num) and operator.gt(self.__string, other.__string)

    def __ge__(self, other):
        return operator.ge(self.__num, other.__num) and operator.ge(self.__string, other.__string)


if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
