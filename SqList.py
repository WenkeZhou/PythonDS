# -*- coding: utf-8 -*-
__author__ = 'ghost'

class SqList():

    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.maxsize = size
        self.length = 0

    def is_empty(self):
        empty = self.length == 0 and True or False
        return empty

    def is_full(self):
        full = self.length == self.maxsize and True or False
        return full

    def get_length(self):
        return self.length

    def create(self, elem):
        for i, item in enumerate(self.data):
            if self.length < self.maxsize:
                if item is None:
                    self.data[i] = elem
                    self.length += 1
                    break
            else:
                raise IndexError, u'SqList is full'

    def get_elem(self, i):
        if self.is_empty():
            raise IndexError, u'SqList is empty'
        elif self.length < i or 0 > i:
            raise IndexError, u'index out of range'
        else:
            return self.data[i-1]

    def insert(self, i, elem):
        if not self.is_full():
            if 0 < i <= self.length:
                for index in range(self.length-1, i-2, -1):
                    self.data[index+1] = self.data[index]
                self.data[i-1] = elem
                self.length += 1
            else:
                raise IndexError, u'index out of range'
        else:
            raise IndexError, u'SqList is full'

    def delete(self, i):

        if self.is_empty():
            raise IndexError, u'SqList is empty'
        elif 0 < i <= self.length:
            deelem = self.get_elem(i)
            for index in range(i, self.length):
                if index != 0:
                    self.data[index - 1] = self.data[index]
            self.data[self.length - 1] = None
            self.length -= 1
            return deelem
        else:
            raise IndexError, u'index out of range'


if __name__ == '__main__':

    s = SqList(5)
    s.create(0)
    s.create(1)
    s.create(2)

