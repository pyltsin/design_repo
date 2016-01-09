# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 13:48:34 2014

@author: admin
"""
import unittest

from profiles2 import *
from table import *
pi=3.14159265358979



from steel import *

from codes import *            

pr1=truba_pryam(h=10, b=6, t=0.6, r1=0.6, r2=1.2)
s=steel_snip1987('C235',pr1, dim=1)
el=elements(s, pr1, mux=0.7, muy=1,mub=1, lfact=300) 
forc=force()        
sol=snipn(el,forc,1)

