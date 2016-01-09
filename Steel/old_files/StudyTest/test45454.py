# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 18:11:06 2014

@author: admin
"""

import os
for key in os.environ.keys():
    print "{0:>25} : {1}".format(key, os.environ[key])