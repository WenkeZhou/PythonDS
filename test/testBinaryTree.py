# -*- coding: utf-8 -*-
__author__ = 'ghost'

import sys
sys.path.append('..')


import unittest
from src.Tree.binaryTree import BinaryTree, Node

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        node1 = Node(1)
        node2 = Node(2, node1, None)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5, node3, node4)
        node6 = Node(6, node2, node5)
        node7 = Node(7, node6, None)
        node8 = Node(8)
        root = Node('root', node7, node8)

        self.bt = BinaryTree(root)

        print u'''
        生成的二叉树
        ------------------------
                 root
              7        8
            6
          2   5
        1    3 4

        -------------------------
        '''

    def tearDown(self):
        print 'test has been done'

    def test_preorder(self):
        self.bt.preorder(self.bt.root)
        nlist = ['root', 7, 6, 2, 1, 5, 3, 4, 8]
        self.assertEquals(nlist, self.bt.pre_list)

    def test_inorder(self):
        self.bt.inorder(self.bt.root)
        nlist = [1, 2, 6, 3, 5, 4, 7, 'root', 8]
        self.assertEquals(nlist, self.bt.in_list)

    def test_postorder(self):
        self.bt.postorder(self.bt.root)
        nlist = [1, 2, 3, 4, 5, 6, 7, 8, 'root']
        self.assertEquals(nlist, self.bt.post_list)



if __name__ == '__main__':
    unittest.main()

