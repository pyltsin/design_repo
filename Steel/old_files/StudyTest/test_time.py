# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 16:30:37 2014

@author: admin
"""
from codes import *            

import unittest

class Test_time(unittest.TestCase):
    def testtime(self):
        lst=[]
        for i in range(1000):
            for x in range(100):
                for y in range(100):
                    a=[i,x*2,y*3]
                    lst.append(x)
        print len(lst)
        
        self.assertLess(len(lst),1000000)

if __name__ == "__main__":
    unittest.main()