# -*- coding: utf-8 -*-

class SeqTable():

    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.maxsize = size
        self.length = 0

    def getlength(self):
        return self.length

    def isempty(self):
        if self.length == 0:
            return True
        else:
            return False

    def create(self, elem):
        for i, item in  enumerate(self.data):
            if item == None:
                self.data[i] = elem
                self.length += 1
                break
            else:
                if self.length == self.maxsize:
                    print 'SeqTable is full!'
                    return

    def getelem(self, i):
        if self.isempty():
            print 'SeqTable is empty!'
        elif self.length <= i or i < 0:
            print ' Out of Index' 
        else:
            return self.data[i]


    def insert(self, i, elem):
        if self.length < i or i < 0:
            print ' Out of Index'
        elif self.length == self.maxsize:
            print 'SeqTable is full!'
            return  
        else:
            for index in range(self.length, i, -1):
                self.data[index] = self.data[index-1]
            self.data[i] = elem
            self.length += 1

    def delete(self, i):
        if self.isempty():
            print 'SeqTable is empty!'
        elif self.length <= i or i < 0:
            print ' Out of Index'
            return
        else:
            self.data[i] = None
            for index in range(i, self.length, 1):
                if index == self.length - 1:
                    self.data[index] = None
                else:
                    self.data[index] = self.data[index+1]
            self.data[self.length - 1] = None
            self.length -= 1

s = SeqTable(5)
s.create(0)
s.create(1)
s.create(2)
