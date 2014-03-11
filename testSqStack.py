# -*- coding: utf-8 -*-
__author__ = 'ghost'

import unittest
from SqStack import SqStack

class TestSqStack(unittest.TestCase):

    def setUp(self):

        self.s = SqStack(5)

    def tearDown(self):
        print 'test has been done'

    def test_get_top(self):
        self.assertRaises(ValueError, self.s.get_top)

        self.s.data[0] = 111
        self.s.top += 1
        self.assertEquals(111, self.s.get_top())

    def test_push(self):
        self.s.push(111)
        self.assertEquals(1, self.s.get_length())
        self.assertEquals(111, self.s.get_top())
        self.s.push(222)
        self.s.push(333)
        self.s.push(444)
        self.s.push(555)
        self.assertRaises(ValueError, self.s.push, 666)

    def test_pop(self):


        self.assertRaises(ValueError, self.s.pop)

        self.s.push(111)
        self.assertEquals(111, self.s.pop())
        self.s.push(222)
        self.s.push(333)
        self.s.push(444)
        self.s.push(555)
        self.assertEquals(555, self.s.pop())
        self.assertEquals(444, self.s.pop())
        self.assertEquals(333, self.s.pop())
        self.assertEquals(222, self.s.pop())
        self.assertRaises(ValueError, self.s.pop)

if __name__ == '__main__':
    unittest.main()

