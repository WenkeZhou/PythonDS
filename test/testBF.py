# -*- coding: utf-8 -*-
__author__ = 'ghost'

import sys
sys.path.append('..')


import unittest
from src.String.BF import brute_force

class testBF(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        print 'test has been down'

    def tear_brute_force(self):

        s = 'hello python'

        t = 'h'
        self.assertEquals(0, brute_force(s, t))

if __name__ == '__main__':

    unittest.main()

