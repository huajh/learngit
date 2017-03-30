#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Time60(object):

    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'

        self.hr = hr
        self.min = min

    def __str__(self):
        'Time60 - string representation'

        return '%d:%d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        'Time60 - ovrloading the addtion operator'

        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        'Time60 - overloading in-place addition'

        self.hr += other.hr
        self.min += other.min
        return self


if __name__ == '__main__':

    mon = Time60(10, 30)
    tue = Time60(11, 15)
    print(type(mon + tue))
    print(mon + tue)
