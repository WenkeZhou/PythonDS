# -*- coding: utf-8 -*-
__author__ = 'ghost'

import sys
sys.path.append('..')

import unittest
from src.List.LkList import LinkList

class TestLkList(unittest.TestCase):

    def setUp(self):
        self.l = LinkList()

    def tearDown(self):
        print 'test is done'


    def test_create(self):
        self.assertTrue(self.l.is_empty())
        self.l.create(111)
        self.assertEquals(111, self.l.L.next.data)
        self.assertEquals(1, self.l.get_length())
        self.l.create(222)
        self.assertEquals(222, self.l.L.next.next.data)
        self.assertEquals(2, self.l.get_length())

    def test_get_elem(self):

        self.assertRaises(IndexError, self.l.get_elem, 1)
        self.l.create(111)
        self.assertRaises(IndexError, self.l.get_elem, 0)

    def test_insert(self):

        self.assertRaises(IndexError, self.l.insert, 0, 11)
        self.l.insert(1, 111)
        self.assertEquals(111, self.l.L.next.data)
        self.assertEquals(111, self.l.get_elem(1))
        self.assertEquals(1, self.l.get_length())
        self.assertRaises(IndexError, self.l.insert, 2, 222)

        self.l.insert(1, 222)
        self.assertEquals(2, self.l.get_length())
        self.assertEquals(222, self.l.get_elem(1))
        self.assertEquals(111, self.l.get_elem(2))
        self.l.insert(2, 2222)
        self.assertEquals(222, self.l.get_elem(1))
        self.assertEquals(2222, self.l.get_elem(2))
        self.assertEquals(111, self.l.get_elem(3))

    def test_delete(self):
        self.assertRaises(IndexError, self.l.delete, 1)
        self.l.create(111)
        self.assertEquals(111, self.l.delete(1))
        self.assertEquals(0, self.l.get_length())


        self.l.insert(1,333)
        self.l.insert(1,222)
        self.l.insert(1,111)

        self.assertEquals(111, self.l.get_elem(1))
        self.assertEquals(222, self.l.get_elem(2))
        self.assertEquals(333, self.l.get_elem(3))

        self.assertRaises(IndexError, self.l.delete, 4)

        self.assertEquals(111, self.l.delete(1))
        self.assertEquals(2, self.l.get_length())




if __name__ == '__main__':
   unittest.main()

