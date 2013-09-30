# -*- coding: utf-8 -*-


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkTable():
    def __init__(self):

        self.L = Node(None) # 头结点
        self.L.next = None  
        self.__r = self.L
        self.length = 0

    def isempty(self):
        if self.length == 0:
            return True
        else:
            return False


    def getlength(self):
        return self.length

    def create(self, elem):
        p = Node(elem)
        self.__r.next = p
        self.__r = p
        self.length += 1

    def getelem(self, i):
        if 0 < i <= self.length:
            j = 1
            p = self.L.next
            while p and j < i:
                p = p.next
                j += 1
            return p.data
        else:
            print 'Out of Index!'

    def insert(self, i, elem):
        if 0 < i <= self.length:
            j = 0
            p = self.L
            while p and j < i-1:
                p = p.next
                j += 1
            q = Node(elem)
            q.next = p.next
            p.next = q
            self.length += 1
        else:
            print 'Out of Index!'

    def delete(self, i):
        if 0 < i <= self.length:
            j = 0
            p = self.L
            while p and j < i-1:
                p = p.next
                j += 1
            q = p.next
            p.next = q.next
            del q
            self.length -= 1
        else:
            print 'Out of Index!'

[111, 222, 3333, 4444]


l = LinkTable()
l.create(1111)
l.create(2222)
l.create(3333)
