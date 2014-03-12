# -*- coding: utf-8 -*-
__author__ = 'ghost'


class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkQueue():

    def __init__(self):
        self.front = Node()
        self.rear = Node()
        self.length = 0

    def get_length(self):
        return self.length

    def is_empty(self):
        empty = self.length == 0 and True or False
        return empty

    def append(self, elem):
        p = Node(elem)
        if self.is_empty():
            self.front = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p
        self.length += 1

    def shift(self):
        if self.is_empty():
            raise ValueError, u'LinkQueue is empty'
        else:
            del_elem = self.front.data
            self.front = self.front.next
            self.length -= 1
            return del_elem

if __name__ == '__main__':
    l = LinkQueue()

