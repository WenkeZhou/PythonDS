# -*- coding: utf-8 -*-
__author__ = 'ghost'

import sys
sys.path.append('..')


import unittest
from src.Stack.LkStack import LinkStack

class TestLinkStack(unittest.TestCase):

    def setUp(self):
        self.s = LinkStack()

    def tearDown(self):
        print 'test has been down'

    def test_is_empty(self):
        self.assertTrue(self.s.is_empty())

    def test_push(self):

        self.s.push(111)
        self.assertEquals(1, self.s.get_length())

        self.s.push(222)
        self.assertEquals(222, self.s.get_top())

        self.s.push(333)
        self.assertEquals(333, self.s.get_top())

    def test_pop(self):
        self.assertRaises(ValueError, self.s.pop)

        self.s.push(111)
        self.assertEquals(1, self.s.get_length())

        self.assertEquals(111, self.s.pop())
        self.s.push(222)
        self.s.push(333)
        self.assertEquals(2, self.s.get_length())
        self.assertEquals(333, self.s.pop())


if __name__ == '__main__':
    unittest.main()