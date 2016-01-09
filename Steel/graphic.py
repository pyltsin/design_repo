# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 15:21:31 2014

@author: admin
"""

from codes import * 
from profiles2 import * 
from steel import * 

from numpy import *
import matplotlib.pyplot as plt
 
 
lambda_ = linspace(0.1, 10, 100)
print lambda_  # 51 точка между 0 и 3

pr1=dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
s=steel_snip20107n('C345',pr1, 1)
el=elements(s, pr1, mux=5000, muy=300, lfact=700) 
forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
sol=snipn(el,forc,1)



y=[]
for i in lambda_:
    y.append(sol.phi_n_old(i))
 
    



pr2=dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
s2=steel_snip20107n('C235',pr2, 1)
el2=elements(s2, pr2, mux=5000, muy=300, lfact=700) 
forc2=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
sol2=snipn(el2,forc2,1)

y2=[]
for i in lambda_:
    y2.append(sol2.phi_n_old(i))



pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
s=steel_snip20107n('C235',pr1)
el=elements(s, pr1, mux=1, muy=1, mub=1, lfact=500) 
forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
sol=snipn(el,forc,1)







y3=[]
for i in lambda_:
    y3.append(sol.phi_n(i)[0])

print sol.phi_n(1)[1]




pr1=truba_pryam(h=500, b=400, t=20, r1=0, r2=0)
s=steel_snip20107n('C235',pr1)
el=elements(s, pr1, mux=1, muy=1, mub=1, lfact=500) 
forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
sol=snipn(el,forc,1)

y4=[]
for i in lambda_:
    y4.append(sol.phi_n(i)[0])

print sol.phi_n(1)[1]






pr1=sost_ugol_tavr_st_up(h=500, b=400, t=20, r1=0, r2=0)
s=steel_snip20107n('C235',pr1)
el=elements(s, pr1, mux=1, muy=1, mub=1, lfact=500) 
forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
sol=snipn(el,forc,1)

y5=[]
for i in lambda_:
    y5.append(sol.phi_n(i)[0])

print sol.phi_n(1)[1]






def phi_euro(lambda_, typ):
    if typ=='a0':
        alpha=0.13
    elif typ=='a':
        alpha=0.21
    elif typ=='b':
        alpha=0.34
    elif typ=='c':
        alpha=0.49
    elif typ=='d':
        alpha=0.76
        
    p=0.5*(1+alpha*(lambda_-0.2)+lambda_**2)
    
    x=1./(p+(p**2-lambda_**2)**0.5)
    
    if x>1:
        x=1
    
    return x


def phi_euro_st(lambda_, typ):
    if typ=='a0':
        alpha=0.17
    elif typ=='a':
        alpha=0.275
    elif typ=='b':
        alpha=0.34
    elif typ=='c':
        alpha=0.49
    elif typ=='d':
        alpha=0.76
        
    p=0.5*(1+alpha*(lambda_-0.4/3.14)+lambda_**2)
    
    x=1./(p+(p**2-lambda_**2)**0.5)
    
    if x>1:
        x=1
    
    return x

lambda_e=[]
for i in lambda_:
    
    lambda_e.append(i/3.14)

print lambda_e

yea0=[]
for i in lambda_e:
    yea0.append(phi_euro(i, 'a0'))


    
yea=[]
for i in lambda_e:
    yea.append(phi_euro(i, 'a'))



yeb=[]
for i in lambda_e:
    yeb.append(phi_euro(i, 'b'))


yec=[]
for i in lambda_e:
    yec.append(phi_euro(i, 'c'))


yed=[]
for i in lambda_e:
    yed.append(phi_euro(i, 'd'))



#plt.plot(lambda_, y,'--', label=u'SNiP C345')
#plt.plot(lambda_, y2,'--', label=u'SNiP C235')

plt.plot(lambda_, y4, label=u'SP a ')
plt.plot(lambda_, y3, label=u'SP b ')
plt.plot(lambda_, y5, label=u'SP c ')

plt.plot(lambda_, yea0,'-.', label=u'EC a0')
plt.plot(lambda_, yea,'-.', label=u'EC a')
plt.plot(lambda_, yeb,'-.', label=u'EC b')
plt.plot(lambda_, yec,'-.', label=u'EC c')
plt.plot(lambda_, yed,'-.', label=u'EC d')

'''построим эйлера/1,3:'''
yel=[]
for i in lambda_:
    if 7.6/i**2>1:
        yel.append(1)
    else:
        yel.append(7.6/i**2)
        

plt.plot(lambda_, yel,'-', label=u'Ncr/1.3')


yel2=[]
for i in lambda_:
    if 7.6/i**2*1.3>1:
        yel2.append(1)
    else:
        yel2.append(7.6*1.3/i**2)
        

plt.plot(lambda_, yel2,'-', label=u'Ncr')


plt.legend()
plt.show()