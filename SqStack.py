# -*- coding: utf-8 -*-
__author__ = 'ghost'

class SqStack():

    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.maxsize = size
        self.top = 1

    def get_length(self):
        return self.top - 1

    def is_empty(self):
        empty = self.top == 1 and True or False
        return empty

    def is_full(self):
        full = self.maxsize < self.top and True or False
        return full

    def get_top(self):
        if self.is_empty():
            raise ValueError, u'SqStack is empty'
        return self.data[self.top - 2]

    def push(self, elem):
        if self.is_full():
            raise ValueError, u'SqStack is full'
        else:
            self.data[self.top - 1] = elem
            self.top += 1

    def pop(self):
        if self.is_empty():
            raise ValueError, u'SqStack is empty'
        popdata = self.data[self.top - 2]
        self.data[self.top - 2] = None
        self.top -= 1
        return popdata

if __name__ == '__main__':
    s = SqStack(5)




