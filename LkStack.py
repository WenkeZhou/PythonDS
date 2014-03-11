# -*- coding: utf-8 -*-
__author__ = 'ghost'

class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkStack():

    def __init__(self):
        self.top = Node(None) # 头结点
        self.count = 0

    def is_empty(self):
        empty = self.count == 0 and True or False
        return empty

    def get_length(self):
        return self.count

    def get_top(self):

        topelem = self.top.data
        return topelem

    def push(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.count += 1

    def pop(self):

        if self.is_empty():
            raise ValueError, u'LinkStack is empty'
        topelem = self.top.data
        self.top = self.top.next
        self.count -= 1
        return topelem