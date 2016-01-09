# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 00:44:39 2014

@author: Pyltsin
"""
import numpy as np
import numpy.ma as ma

def e2sigma4(xmatr, ymatr, kymatr, e):
    '''e - матрица e
    проверено - тестов нет'''
    import time
    startTime=time.time()
    xmatr=xmatr
    ymatr=ymatr
    kymatr=kymatr
    
    print 'time1', (time.time()-startTime)*100000
    startTime=time.time()
   
    boolmatr=(e>xmatr)
    one=np.zeros(boolmatr.shape[1])
    
    boolmatrInvert=np.vstack((boolmatr[1:],one))
    boolmatrInvert=(boolmatrInvert==False)
#    boolmatr=(boolmatr==boolmatrInvert)
    boolmatr=(boolmatr!=boolmatrInvert)

    print 'time2', (time.time()-startTime)*100000
    startTime=time.time()
    
#    ymatr = ma.masked_array(ymatr, mask=boolmatr)  
    ymatr*=boolmatr
    ymatr=np.sum(ymatr, axis=0)

    print 'time31', (time.time()-startTime)*100000
    startTime=time.time()

    
    kymatr*=boolmatr[:-1]
    kymatr=np.sum(kymatr, axis=0)

    print 'time32', (time.time()-startTime)*100000
    startTime=time.time()
    
    xmatr*=boolmatr
    xmatr=np.sum(xmatr, axis=0)
    sigma=kymatr*(e-xmatr)+ymatr
#        print sigma
    print 'time33', (time.time()-startTime)*100000

    return sigma

n=1000000
x=np.array((1,2,3,4,5))
xone=np.ones(n)
xmatr=np.meshgrid(x,xone)
xmatr=xmatr[0].transpose()

e2sigma4(xmatr, xmatr, xmatr[:-1], xone*2)