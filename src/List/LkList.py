# -*- coding: utf-8 -*-
__author__ = 'ghost'


class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList():

    def __init__(self):
        self.L = Node(None) # 头结点
        self.L.next = None
        self.__r = self.L
        self.length = 0

    def is_empty(self):
        empty = self.length == 0 and True or False
        return empty

    def get_length(self):
        return self.length

    def create(self, elem):
        p = Node(elem)
        self.__r.next = p
        self.__r = self.__r.next
        self.length += 1

    def get_elem(self, i):

        if self.is_empty():
            raise IndexError, u'LinkList is empty'
        elif self.length < i or i <= 0:
            raise IndexError, u'out of index'
        else:
            j = 1
            p = self.L.next
            while p and j < i:
                p = p.next
                j += 1
            elem = p.data
            return elem

    def insert(self, i, elem):

        if self.is_empty() and i == 1:
            self.L.next = Node(elem)
            self.length += 1
        else:
            if 0 < i <= self.length:
                j = 1
                p = self.L
                while p and j < i:
                    p = p.next
                    j += 1
                n = Node(elem)
                n.next = p.next
                p.next = n
                self.length += 1
            else:
                raise IndexError, u'out of index'

    def delete(self, i):

        if self.is_empty():
            raise IndexError, u'out of index'
        else:
            if 0 < i <= self.length:

                j = 1
                p = self.L
                while p and j < i:
                    p = p.next
                    j += 1
                delnode = p.next
                p.next = delnode.next
                self.length -= 1
                return delnode.data
            else:
                raise IndexError, u'out of index'


if __name__ == '__main__':
    l = LinkList()
