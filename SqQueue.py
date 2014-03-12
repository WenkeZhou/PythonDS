# -*- coding: utf-8 -*-
__author__ = 'ghost'


class SqQueue():

    def __init__(self, size):
        self.data = [None for i in range(size+1)]
        self.maxsize = size+1
        self.front = 0
        self.rear = 0
        self.length = 0

    def get_length(self):
        length = (self.rear - self.front + self.maxsize) % self.maxsize
        return length

    def is_full(self):
        full = (self.rear + 1) % self.maxsize == self.front and True or False
        return full

    def is_empty(self):
        empty = self.front == self.rear and True or False
        return empty

    def append(self, elem):
        if self.is_full():
            raise ValueError, u'SqQueue is full'
        else:
            self.data[self.rear] = elem
            self.rear = (self.rear + 1) % self.maxsize
            self.length += 1

    def shift(self):
        if self.is_empty():
            raise ValueError, u'SqQueue is empty'
        else:
            del_elem = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            self.length -= 1
            return del_elem

if __name__ == '__main__':
    s = SqQueue(5)




