# -*- coding: utf-8 -*-
__author__ = 'ghost'

import unittest
from LkQueue import LinkQueue

class TestLinkQueue(unittest.TestCase):

    def setUp(self):
        self.l = LinkQueue()


    def tearDown(self):
        print 'test has been done'


    def test_append(self):

        self.l.append(111)
        self.assertEquals(1, self.l.get_length())

        self.l.append(222)
        self.assertEquals(111, self.l.front.data)
        self.assertEquals(222, self.l.rear.data)

    def test_shift(self):

        self.assertRaises(ValueError, self.l.shift)

        self.l.append(111)
        self.assertEquals(111, self.l.shift())

        self.assertRaises(ValueError, self.l.shift)

        self.l.append(111)
        self.l.append(222)
        self.l.append(333)
        self.assertEquals(111, self.l.shift())
        self.assertEquals(222, self.l.shift())
        self.assertEquals(333, self.l.shift())

        self.assertEquals(0, self.l.get_length())

if __name__ == '__main__':
    unittest.main()