# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:10:24 2013

@author: admin
"""

#!/usr/bin/env python                                                           
import operator

def factorial(n):
    if n < 0:
        raise ValueError("Factorial can't be calculated for negative numbers.")
    if type(n) is float or type(n) is complex:
        raise TypeError("Factorial doesn't use Gamma function.")
    if n == 0:
        return 1
    return reduce(operator.mul, range(1, n + 1))

if __name__ == '__main__':
    n = input('Enter the positive number: ')
    print '{0}! = {1}'.format(n, factorial(int(n)))