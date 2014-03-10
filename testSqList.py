# -*- coding: utf-8 -*-
__author__ = 'ghost'

import unittest
from SqList import SqList

class TestSqList(unittest.TestCase):

    def setUp(self):
        self.s = SqList(5)

    def tearDown(self):
        print 'test is done'
        self.s.data = None

    def test_create(self):

        self.s.create(1)
        self.assertEquals(1, self.s.data[0])
        self.s.create(2)
        self.assertEquals(2, self.s.data[1])
        self.s.create(3)
        self.assertEquals(3, self.s.data[2])
        self.s.create(4)
        self.assertEquals(4, self.s.data[3])
        self.s.create(5)
        self.assertEquals(5, self.s.data[4])
        self.assertRaises(IndexError, self.s.create, 6)


    def test_get_elem(self):
        self.s.create(1)
        self.s.create(2)
        self.s.create(3)
        self.assertEquals(1, self.s.get_elem(1))
        self.assertEquals(2, self.s.get_elem(2))
        self.assertEquals(3, self.s.get_elem(3))
        self.assertRaises(IndexError, self.s.get_elem, 4)

    def test_insert(self):
        self.s.create(1)
        self.s.create(2)
        self.s.create(3)
        # 测试插入
        self.s.insert(2, 22)
        self.assertEquals(self.s.get_elem(2), 22)
        # 测试插入超过长度
        self.assertRaises(IndexError, self.s.insert, 5, 55)

        self.s.insert(4, 44)
        self.assertEquals(self.s.get_elem(4), 44)
        # 测试满了
        self.assertRaises(IndexError, self.s.insert, 1, 43)

    def test_delete(self):
        # 空线性表
        self.assertRaises(IndexError, self.s.delete, 2)
        # 一个元素的时候
        self.s.create(1)
        self.s.delete(1)
        self.assertEquals(True, self.s.is_empty())

        self.s.create(1)
        self.s.create(2)
        self.s.create(3)
        self.assertRaises(IndexError, self.s.delete, 4)
        self.assertEquals(3, self.s.delete(3))
        self.assertEquals(2, self.s.get_length())


if __name__ == '__main__':
    unittest.main()



