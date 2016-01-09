# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 19:48:12 2014

@author: Pyltsin
"""

import numpy as np
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
print X
print Y
print Z