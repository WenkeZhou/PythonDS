# -*- coding: utf-8 -*-
__author__ = 'ghost'

import sys
sys.path.append('..')


import unittest
from src.Queue.SqQueue import SqQueue

class TestSqQueue(unittest.TestCase):

    def setUp(self):
        self.s = SqQueue(5)

    def tearDown(self):
        print 'test has been done'

    def test_get_length(self):
        self.s.append(111)
        self.assertEquals(1, self.s.get_length())
        self.s.append(222)
        self.assertEquals(2, self.s.get_length())
        self.assertEquals(self.s.length, self.s.get_length())

    def test_empty(self):
        self.assertTrue(self.s.is_empty())

    def test_full(self):
        pass

    def test_append(self):
        self.s.append(111)
        self.assertEquals(0, self.s.front)
        self.assertEquals(1, self.s.rear)
        self.assertEquals(1, self.s.length)
        self.s.append(222)
        self.s.append(333)
        self.s.append(444)
        self.assertEquals(4, self.s.get_length())
        self.s.append(555)
        self.assertRaises(ValueError, self.s.append, 666)
        print self.s.data

    def test_shift(self):
        self.assertRaises(ValueError, self.s.shift)
        self.s.append(111)
        self.s.append(222)
        self.assertEquals(111, self.s.shift())
        self.assertEquals(1, self.s.get_length())

        self.s.append(333)
        self.s.append(444)
        self.s.append(555)
        self.s.append(666)

        self.assertEquals(222, self.s.shift())
        self.assertEquals(333, self.s.shift())
        self.assertEquals(444, self.s.shift())
        self.assertEquals(555, self.s.shift())
        self.assertEquals(666, self.s.shift())


if __name__ == '__main__':
    unittest.main()