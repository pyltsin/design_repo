# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:52:37 2013

@author: puma
"""
#добавить устойчивость для короба
import unittest

from codes import *
from profiles2 import *
from table import *
pi=3.14159265358979



from steel import *


class test_snipn(unittest.TestCase):
    def test_snipn(self):
#только двутавр
#    def snipn1(self):
        #том 
#        print(1)



        pr1=dvut(h=520, b=200, t=20, s=8, r1=0, r2=0, a1=0)

        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=7000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1) 


#phi_b
#        print sol.phi_etable(10.,2.)
        self.assertLess(abs(sol.phi_etable(10.,2.)-0.125)/0.125,0.001) 
        self.assertLess(abs(sol.phi_etable(18.5,2.)-0.073)/0.073,0.001)
#nau
#        print sol.nau(10.,1)
        self.assertLess(abs(sol.nau(10.,1)-1.3783)/1.3783,0.001)  
        self.assertLess(abs(sol.nau(4,1)-1.456)/1.456,0.001) 
        print 21       
    def test_snipn2(self):

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=600, ly=600, lb=000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=150*1000/9.81*100)        
        sol=snipn(el,forc,1)
        #phi_e, mef, nau, lambda_
        r=sol.phi_e(1)     
#        print 'phi_e',   r[0]
#        print 'mef', r[1]
#        print 'nau', r[2]
#        print 'lambda_', r[3]
#        print 'phi', sol.phiy()
        self.assertLess(abs(r[0]-0.443)/0.443,0.001)   
        self.assertLess(abs(r[1]-2.193)/2.193,0.001)   
        self.assertLess(abs(r[2]-1.654)/1.654,0.001)
#        self.assertLess(abs(sol.phiy()-0.792)/0.792,0.001)

        pr1=dvut(h=40, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=600, ly=600, lb=000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, my=150*1000/9.81*100)        
        sol=snipn(el,forc,1)
        r=sol.phi_e(2)  

#        print 'phi_e',   r[0]
#        print 'mef', r[1]
#        print 'nau', r[2]


        self.assertLess(abs(r[0]-0.08658)/0.08658,0.001)   
        self.assertLess(abs(r[1]-10.592)/10.592,0.001)   
        self.assertLess(abs(r[2]-1.)/1.,0.001)

        print 25
    def test_snipn3(self):
        pr1=dvut(h=40, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=600, ly=600, lb=000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, my=150*1000/9.81*100)        
        sol=snipn(el,forc,1) 
        
     
        self.assertLess(abs(sol.a_c(1)-0.7)/0.7,0.001)
        self.assertLess(abs(sol.a_c(4)-0.85)/0.85,0.001)  

#        print 'phi_n', sol.phi_n(lambda_=3.14, typ=2)
#        print 'phiy',sol.phiy()
#        print 'lambday_',sol.el.lambday_()
#        print 'b_c', sol.b_c()
        
        self.assertLess(abs(sol.b_c()-1.384)/1.384,0.001) 

        pr1=dvut(h=40, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=200, ly=200, lb=000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, my=150*1000/9.81*100)        
        sol=snipn(el,forc,1) 

#        print 'phi_n', sol.phi_n(lambda_=3.14, typ=2)
#        print 'phiy',sol.phiy()
#        print 'lambday_',sol.el.lambday_()
#        print 'b_c', sol.b_c()

        self.assertLess(abs(sol.b_c()-1.0)/1.0,0.001)               


        pr1=dvut(h=40, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=1000, ly=1000, lb=1000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=150*1000/9.81*100)        
        sol=snipn(el,forc,1)
        
#        print sol.c_max()
        self.assertLess(abs(sol.c_max()-0.914)/0.914,0.001) 
        self.assertLess(abs(sol.c()[0]-0.914)/0.914,0.001)    

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=1000, ly=1000, lb=1000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=150*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.c()[0]            
#        print sol.c()[1] 
#        print sol.c()[2] 
        
        self.assertLess(abs(sol.c()[0]-0.551)/0.551,0.001) 
        self.assertLess(abs(sol.c()[1]-0.783)/0.783,0.001) 
        self.assertLess(abs(sol.c()[2]-1.326)/0.914,0.001) 



        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=1000, ly=5000, lb=1000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=150*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.c()[0]            
#        print sol.c()[1] 
#        print sol.c()[2] 
        
        self.assertLess(abs(sol.c()[0]-0.977)/0.977,0.001) 
        self.assertLess(abs(sol.c()[1]-0.977)/0.977,0.001) 
        self.assertLess(abs(sol.c()[2]-1.326)/0.914,0.001) 

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=500, ly=1000, lb=500, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=150*1000/9.81*100*10)        
        sol=snipn(el,forc,1)

#        print sol.c()[0]            
#        print sol.c()[1] 
#        print sol.c()[2] 
#        
        self.assertLess(abs(sol.c()[0]-0.124172)/0.124172,0.001) 
#        self.assertLess(abs(sol.c()[1]-0.305)/0.305,0.001) 
        self.assertLess(abs(sol.c()[2]-13.264)/13.264,0.001) 


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=500, ly=1000, lb=500, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=566*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.c()[0]            
#        print sol.c()[1] 
#        print sol.c()[2] 
        
        self.assertLess(abs(sol.c()[0]-0.1952196)/0.1952196,0.001) 
        self.assertLess(abs(sol.c()[1]-0.377438)/0.377438,0.001) 
        self.assertLess(abs(sol.c()[2]-5.005)/5.005,0.001) 


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=500, ly=1000, lb=500, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=435*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.c()[0]            
#        print sol.c()[1] 
#        print sol.c()[2] 
        
        self.assertLess(abs(sol.c()[0]-0.253482)/0.253482,0.001) 
        self.assertLess(abs(sol.c()[1]-0.454079)/0.454079,0.001) 
        self.assertLess(abs(sol.c()[2]-3.84666)/3.84666,0.001) 



        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=500, ly=500, lb=500, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
        sol=snipn(el,forc,1)
        
#        print sol.phi_exy()[0]            
#        print sol.phi_exy()[1] 
#        print sol.phi_exy()[2] 
       
        self.assertLess(abs(sol.phi_exy()[0]-0.072648)/0.072648,0.001) 
        self.assertLess(abs(sol.phi_exy()[1]-0.11186)/0.11186,0.001) 
        self.assertLess(abs(sol.phi_exy()[2]-0.235839)/0.235839,0.001) 

#        print sol.phix()        
#        print sol.phiy() 
        
        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-0.5378)/0.5378,0.001)

#        print sol.local_buckl_b_ne(1)[1]
#        print sol.local_buckl_b_ne(1)[2]
        
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-0.4528)/0.4528,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[2]-0.3243)/0.3243,0.001)


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=150, ly=150, lb=150, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-0.44)/0.44,0.001)

#        print sol.local_buckl_b_ne(1)[1]
#        print sol.local_buckl_b_ne(1)[2]
        
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-0.36075)/0.36075,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[2]-0.3243)/0.3243,0.001)
        

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=50, ly=50, lb=50, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.local_buckl_b_ne(2)[1]

        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-0.44)/0.44,0.001)

#        print sol.local_buckl_b_ne(1)[1]
#        print sol.local_buckl_b_ne(1)[2]
        
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-0.36075)/0.36075,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[2]-0.3243)/0.3243,0.001)

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=435*1000/9.81*100, my=435*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.local_buckl_b_ne(2)[1]

        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-0.76)/0.76,0.001)

#        print sol.local_buckl_b_ne(1)[1]
#        print sol.local_buckl_b_ne(1)[2]
        
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-0.5946)/0.5946,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[2]-0.3243)/0.3243,0.001)


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=100*1000/9.81*100, my=100*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.local_buckl_b_ne(2)[1]

        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-0.76)/0.76,0.001)

#        print sol.local_buckl_b_ne(1)[1]
#        print sol.local_buckl_b_ne(1)[2]
        
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-0.722)/0.722,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[2]-0.3243)/0.3243,0.001)

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=1000*1000/9.81*100, my=1000*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print sol.local_buckl_b_ne(2)[1]

        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-0.76)/0.76,0.001)

#        print sol.local_buckl_b_ne(1)[1]
#        print sol.local_buckl_b_ne(1)[2]

        self.assertLess(abs(sol.local_buckl_b_ne(1)[0]-0)/0.001,0.001)        
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-0.533)/0.533,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[2]-0.3243)/0.3243,0.001)

#        print  sol.local_buckl_h_ne(2,2)[2]
        self.assertLess(abs(sol.local_buckl_h_ne(2,2)[1]-5.276)/5.276,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(2,2)[2]-0.6144)/0.6144,0.001)

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=800*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(2,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(2,2)[1]-3.11)/3.11,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(2,2)[2]-0.6144)/0.6144,0.001)


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=1*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(2,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(2,2)[1]-5.5)/5.5,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(2,2)[2]-0.6144)/0.6144,0.001)
         



        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=1*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(2,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(2,1)[1]-2.3)/2.3,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(2,1)[2]-0.6144)/0.6144,0.001)
        


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=10*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-3.26)/3.26,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)




        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=100000*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-2.3)/3.26,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)



        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=3000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=10000*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-2.02)/3.26,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)




        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=3000, ly=10000, lb=3000, lr=0, br=0, hr=0) 
        forc=force(n=10000*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)

#        print  sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-2.02)/3.26,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)




        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=1000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=10000*1000/9.81, mx=20000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)
        
    

#        print  'a', sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-1.0356)/1.0356,0.0001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)
        
        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=10000*1000/9.81, mx=1000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)
        
#        print "new"    
        
#        print  'a', sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-2.86594568222)/2.86594568222,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=1000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=10000*1000/9.81, mx=10000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)
        
#        print "new"    
        
#        print  'a', sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-1.91050549183)/1.91050549183,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)
        
        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=900, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=10000*1000/9.81, mx=10000*1000/9.81*100, my=10*1000/9.81*100, qx=10*1000/9.81*100)        
        sol=snipn(el,forc,1)
        
#        print "new"    
        
#        print  'a', sol.local_buckl_h_ne(1,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[1]-1.80069709022)/1.80069709022,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2)[2]-0.6144)/0.6144,0.001)



        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)



        self.assertLess(abs(sol.local_buckl_h_m2()[3]-2.36479)/2.36479,0.001)
        self.assertLess(abs(sol.local_buckl_h_m2()[4]-0.23)/0.23,0.001)

#        print sol.local_buckl_h_m2()[0]
        self.assertLess(abs(sol.local_buckl_h_m2()[1]-9978455)/9978455,0.001)

        self.assertLess(abs(sol.local_buckl_h_m2()[0]-0.5107)/0.5107,0.001)
        self.assertLess(abs(sol.local_buckl_h_m2()[2]-3.311)/3.311,0.001)

        self.assertLess(abs(sol.local_buckl_b_m2(1)[1]-0.31189)/0.31189,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2(2)[1]-0.36866)/0.36866,0.001)
#        print sol.local_buckl_b_m2(2)[2]
        self.assertLess(abs(sol.local_buckl_b_m2(2)[2]-0.388)/0.388,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2(2)[0]-1)/0.0001,0.001)
        
        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_m2()[4]-0.0)/0.001,0.001)


        pr1=dvut(h=40, b=40, t=2, s=5, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_m2()[4]
        self.assertLess(abs(sol.local_buckl_h_m2()[4]-0.2389)/0.2389,0.001)
        print 29
    def test_snipn4(self):
#        print "new"         
        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_n()

        self.assertEqual(test[0],0) 
#        print 'tutu',(test[1])
        self.assertLess(abs(test[1]-0.5879)/0.5879,0.0001)        
        self.assertLess(abs(test[2]-0.333615248)/0.333615248,0.0001)     

        self.assertLess(abs(sol.local_buckl_b_n_old()[1]-0.5879)/0.5879,0.0001)        
        self.assertLess(abs(sol.local_buckl_b_n_old()[2]-0.333615248)/0.333615248,0.0001)   


        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=700000, ly=700000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_n()

        self.assertEqual(test[0],0) 
#        print 'tutu',(test[1])
        self.assertLess(abs(test[1]-0.76)/0.76,0.0001)        
        self.assertLess(abs(test[2]-0.333615248)/0.333615248,0.0001)     

        self.assertLess(abs(sol.local_buckl_b_n_old()[1]-0.76)/0.76,0.0001)        
        self.assertLess(abs(sol.local_buckl_b_n_old()[2]-0.333615248)/0.333615248,0.0001)


        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=70, ly=70, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_n()

        self.assertEqual(test[0],0) 
#        print 'tutu',(test[1])
        self.assertLess(abs(test[1]-0.44)/0.44,0.0001)        
        self.assertLess(abs(test[2]-0.333615248)/0.333615248,0.0001)     

        self.assertLess(abs(sol.local_buckl_b_n_old()[1]-0.44)/0.44,0.0001)        
        self.assertLess(abs(sol.local_buckl_b_n_old()[2]-0.333615248)/0.333615248,0.0001)
        


        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=100*1000/9.81)        
        sol=snipn(el,forc,1)

#!!!дополнительные тесты по местной устойчивости
        
        self.assertLess(abs(sol.local_buckl_h_m_old(1,1)[1]-3.2)/3.2,0.001)
        self.assertLess(abs(sol.local_buckl_h_m_old(1,2)[1]-2.2)/2.2,0.001)

        self.assertLess(abs(sol.local_buckl_h_m_old(2,1)[1]-3.5)/3.2,0.001)
        self.assertLess(abs(sol.local_buckl_h_m_old(2,2)[1]-2.5)/2.2,0.001)




        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)



        self.assertLess(abs(sol.local_buckl_h_m2_old()[3]-2.36479)/2.36479,0.001)

        self.assertLess(abs(sol.local_buckl_h_m2_old()[4]-0.2374)/0.2374,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_m2_old()[4]-0.0)/0.001,0.001)


        pr1=dvut(h=40, b=40, t=2, s=5, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_m2_old()[4]
        self.assertLess(abs(sol.local_buckl_h_m2_old()[4]-0.24)/0.24,0.001)        
        
#        print "tutu" 
        
        pr1=dvut(h=100, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_m2_old()[4]
        self.assertLess(abs(sol.local_buckl_h_m2_old()[4]-0)/0.0001,0.001)     
        


        pr=dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_m_old()

        self.assertEqual(test[0],0) 
#        print('lalal0,',test[2])
        self.assertLess(abs(test[1]-0.5)/0.5,0.0001)        
        self.assertLess(abs(test[2]-0.4572)/0.4572,0.0001)  


        pr1=dvut(h=20, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_m2_old()[4]
        self.assertLess(abs(sol.local_buckl_b_m2_old()[0]-0)/0.0001,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2_old()[1]-0.3)/0.3,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2_old()[2]-0.17736)/0.17736,0.001)        
        

        pr1=dvut(h=2000, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_m2_old()[4]
        self.assertLess(abs(sol.local_buckl_b_m2_old()[0]-0)/0.0001,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2_old()[1]-0.5)/0.5,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2_old()[2]-0.17736)/0.17736,0.001) 


        pr1=dvut(h=200, b=20, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_m2_old()[4]
        self.assertLess(abs(sol.local_buckl_b_m2_old()[0]-0)/0.0001,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2_old()[1]-0.4249)/0.4249,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2_old()[2]-0.17736)/0.17736,0.001) 




        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_n()

        self.assertEqual(test[0],0) 
#        print 'tutu',(test[1])
        self.assertLess(abs(test[1]-0.5879)/0.5879,0.0001)        
        self.assertLess(abs(test[2]-0.333615248)/0.333615248,0.0001)     

        self.assertLess(abs(sol.local_buckl_b_ne_old()[1]-0.5879)/0.5879,0.0001)        
        self.assertLess(abs(sol.local_buckl_b_ne_old()[2]-0.333615248)/0.333615248,0.0001)


        
        
#!!! Расчет после дополнения балок
#!!!не понятно как считать по таблице 23 примечание - по 8.5.18 или 8.5.9
#!!! и как считать по формуле 86 предельную гибкость        
#!!! исправить и разделить двутавр прокатной и сварной - в частностти в вычислении фи балочное
#!!! коэффициент эта, и везде где используется аф/ав, устойчивость стенок и полок.
#!!1 расчет всех tau -  уточнить  , h_ef, b_ef       
         
        print 22   

    def test_snipn5(self):
        print 26
        
        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=1000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=0*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-0.0)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-3.8)/3.8,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)



        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=1000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-0.0)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-3.0165)/3.0165,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=1000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=0*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-1.958)/1.958,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)

        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=100, ly=050, lb=50, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=0*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-1.307)/1.307,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)




        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=300, ly=05, lb=5, lr=0, br=0, hr=0) 
        forc=force(n=2000*1000/9.81, mx=20*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-1.363)/1.363,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=1200, ly=05, lb=5, lr=0, br=0, hr=0) 
        forc=force(n=2000*1000/9.81, mx=20*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-2.1096)/2.1096,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5000, ly=05, lb=5, lr=0, br=0, hr=0) 
        forc=force(n=2000*1000/9.81, mx=400*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-0)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-3.1)/3.1,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5000, ly=05, lb=5, lr=0, br=0, hr=0) 
        forc=force(n=2000*1000/9.81, mx=50*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-0)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-2.4207)/2.4207,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


#        print 'new'
        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=100, ly=0500, lb=500, lr=0, br=0, hr=0) 
        forc=force(n=2000*1000/9.81, mx=50*1000/9.81*100, my=0*1000/9.81*100, qx=0*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-1.4735)/1.4735,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


#        print 'new'

        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5, ly=01000, lb=1000, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=20*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[1]-2.089)/2.089,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,2)[2]-2.365)/2.365,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5000, ly=05, lb=5, lr=0, br=0, hr=0) 
        forc=force(n=2000*1000/9.81, mx=50*1000/9.81*100, my=0*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.local_buckl_h_ne_old(1,2)[1]
#        print sol.local_buckl_h_ne_old(1,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,1)[0]-1)/0.001,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,1)[1]-2.3)/2.3,0.001)
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,1)[2]-2.365)/2.365,0.001)
        
#        print "new" 
        

        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=9900, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=25*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

#        print  'a', sol.local_buckl_h_ne(1,2,1)[1]

        
        self.assertLess(abs(sol.local_buckl_h_ne(1,2,1)[1]-2.90386259244)/2.90386259244,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2,1)[2]-2.36479)/2.36479,0.001)



        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=9900, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

                
   
        
#        print  'a', sol.local_buckl_h_ne(1,2,2)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2,2)[1]-3.20642896047)/3.20642896047,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2,2)[2]-2.36479)/2.36479,0.001)

#        print  'a', sol.local_buckl_h_ne(1,2,1)[1]
        self.assertLess(abs(sol.local_buckl_h_ne(1,2,1)[1]-2.72529559491)/2.72529559491,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne(1,2,1)[2]-2.36479)/2.36479,0.001)

#        print 'new'
#        print  'a', sol.local_buckl_b_ne(1,2)[2]

        self.assertLess(abs(sol.local_buckl_b_ne(1,2)[1]-0.426216939673)/0.426216939673,0.000001)
        self.assertLess(abs(sol.local_buckl_b_ne(1,2)[2]-0.38822)/0.38822,0.001)


#        print 'new'
#        print  'a', sol.local_buckl_b_ne(1,1)[1]

        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[0]-1)/0.00001,0.001)  
        
        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[1]-0.388090912529)/0.388090912529,0.000001)
        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[2]-0.38822)/0.38822,0.001)        


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=9900, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=20*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[0]-0)/0.00001,0.001)  


#        print  'a', sol.local_buckl_b_ne(1,1)[1]        
        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[1]-0.734033908525)/0.734033908525,0.000001)
        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[2]-0.38822)/0.38822,0.001) 


#        print 'h_ne_ut'
        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=300, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=100*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_ne_ut(2,2)[0]-0)/0.00001,0.001)  


#        print  'a', sol.local_buckl_h_ne_ut(2,2)[2]        
        self.assertLess(abs(sol.local_buckl_h_ne_ut(2,2,2)[1]-5.5)/5.5,0.000001)
        self.assertLess(abs(sol.local_buckl_h_ne_ut(2,2,2)[2]-2.36479)/2.36479,0.001)

        self.assertLess(abs(sol.local_buckl_h_ne_ut(2,1,2)[1]-2.3)/2.3,0.000001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=300, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2)[0]-0)/0.00001,0.001)  


#        print  'a', sol.local_buckl_h_ne_ut(1,2,2)[1]        
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[1]-4.2088)/5.5,0.00001)
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[2]-2.36479)/2.36479,0.001)



        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2)[0]-0)/0.00001,0.001)  


#        print  'a', sol.local_buckl_h_ne_ut(1,2,2)[1]        
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[1]-4.2088)/5.5,0.00001)
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[2]-2.36479)/2.36479,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=200*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2)[0]-0)/0.00001,0.001)  


#        print  'a', sol.local_buckl_h_ne_ut(1,2,2)[1]        
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[1]-4.75405181941)/5.5,0.00001)
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[2]-2.36479)/2.36479,0.001)


        pr1=dvut(h=40, b=40, t=2, s=0.6, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr1)
        el=elements(s, pr1, lx=5000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=400*1000/9.81*100, my=000*1000/9.81*100, qx=50*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2)[0]-0)/0.00001,0.001)  


#        print  'a', sol.local_buckl_h_ne_ut(1,2,2)[1]        
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[1]-3.89192819168)/3.89192819168,0.00001)
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,2,2)[2]-2.36479)/2.36479,0.001)

    def test_snipn_prokat(self):
        print 27
        
        pr1=profiles_infile(files='gost8239_89.csv',number='50', typ='dvut')        
        s=steel_snip20107n('C345',pr1, 1)
        el=elements(s, pr1, lx=5000, ly=300, lb=700, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
#        print pr1.afaw()
#        print s.ry()
#        print sol.local_buckl_h_ne_ut(1,2,2)[2]
#        print sol.local_buckl_b_ne(1,1)[2]

        self.assertLess(abs(sol.local_buckl_h_ne(1,2,2)[2]-1.694)/1.694,0.001)
        self.assertLess(abs(sol.local_buckl_b_ne(1,1)[2]-0.1685)/0.1685,0.001)        
        
        
        self.assertLess(abs(sol.local_buckl_h_m2()[4]-0.190475694648)/0.190475694648,0.001)  

#        print sol.phi_b(1,1,1,1)
        self.assertLess(abs(sol.phi_b(1,1,1,1)-0.274798557732)/0.274798557732,0.001)  


    def test_snipn_korob(self):
        print 28






        el=elements(s, pr1, lx=300, ly=200, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)

#        print         sol.local_buckl_h_m2()[0]

        self.assertLess(abs(sol.local_buckl_h_m2()[0]-0.0828460969188)/0.0001,0.001)
        self.assertLess(abs(sol.local_buckl_h_m2()[2]-1.278)/1.278,0.001)
        self.assertLess(abs(sol.local_buckl_h_m2()[3]-0.36785)/0.36785,0.001)

        self.assertLess(abs(sol.local_buckl_b_m2()[0]-0)/0.0001,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2()[1]-1.005)/1.005,0.001)
        self.assertLess(abs(sol.local_buckl_b_m2()[2]-0.6306)/0.6306,0.001)
        




        pr1=truba_pryam(h=8,b=6,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=10, ly=10, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.cxcyn()[1]

        self.assertLess(abs(sol.phi_b(1,1,1,1)-1.)/1.,0.0001)
        
        pr1=truba_pryam(h=12,b=8,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print pr1.afaw()
#        print sol.nau(m=0.4, typ=1)
        self.assertLess(abs(sol.nau(m=0.4, typ=1)-1.50282)/1.50282,0.0001) 
#        print sol.nau(m=7.991, typ=1)
        self.assertLess(abs(sol.nau(m=7.991, typ=1)-1.22407)/1.22407,0.0001) 
        
        
        pr1=truba_pryam(h=12,b=8,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=1000, ly=1000, lb=1000, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        self.assertLess(abs(sol.nau(m=7.991, typ=1)-1.22407)/1.22407,0.0001) 
        self.assertLess(abs(sol.nau(m=0.2, typ=1)-1.22407)/1.22407,0.0001)



        pr1=truba_pryam(h=20,b=20,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=1000, ly=1000, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.nau(m=4.287, typ=1)
        self.assertLess(abs(sol.nau(m=4.287, typ=1)-1.25319148936)/1.2532,0.0001) 
        self.assertLess(abs(sol.nau(m=17.15, typ=1)-1.253191489362)/1.2532,0.0001)


        pr1=truba_pryam(h=20,b=20,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.nau(m=4.027, typ=1)
        self.assertLess(abs(sol.nau(m=4.027, typ=1)-1.3465)/1.3465,0.0001) 
        self.assertLess(abs(sol.nau(m=16.109, typ=1)-1.259)/1.259,0.0001)
        

        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.nau(m=10.6, typ=1)
        self.assertLess(abs(sol.nau(m=4.024, typ=1)-1.41878)/1.41878,0.0001) 
        self.assertLess(abs(sol.nau(m=10.60, typ=1)-1.345587)/1.345587,0.0001)
        


#В ДРУГУЮ СТОРОНУ

        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print pr1.afaw()
#        print sol.nau(m=0.4, typ=2)
        self.assertLess(abs(sol.nau(m=0.4, typ=2)-1.50282)/1.50282,0.0001) 
#        print sol.nau(m=7.991, typ=1)
        self.assertLess(abs(sol.nau(m=7.991, typ=2)-1.22407)/1.22407,0.0001) 
        
        
        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=1000, ly=1000, lb=1000, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        self.assertLess(abs(sol.nau(m=7.991, typ=2)-1.22407)/1.22407,0.0001) 
        self.assertLess(abs(sol.nau(m=0.2, typ=2)-1.22407)/1.22407,0.0001)



        pr1=truba_pryam(h=20,b=20,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=1000, ly=1000, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.nau(m=4.287, typ=1)
        self.assertLess(abs(sol.nau(m=4.287, typ=2)-1.25319148936)/1.2532,0.0001) 
        self.assertLess(abs(sol.nau(m=17.15, typ=2)-1.253191489362)/1.2532,0.0001)


        pr1=truba_pryam(h=20,b=20,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.nau(m=4.027, typ=1)
        self.assertLess(abs(sol.nau(m=4.027, typ=2)-1.3465)/1.3465,0.0001) 
        self.assertLess(abs(sol.nau(m=16.109, typ=2)-1.259)/1.259,0.0001)
        

        pr1=truba_pryam(h=12,b=8,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.nau(m=10.6, typ=1)
        self.assertLess(abs(sol.nau(m=4.024, typ=2)-1.41878)/1.41878,0.0001) 
        self.assertLess(abs(sol.nau(m=10.60, typ=2)-1.345587)/1.345587,0.0001)


        pr1=truba_pryam(h=12,b=8,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        
        
#        print         sol.local_buckl_b_ne(2)
        self.assertLess(abs(sol.local_buckl_b_ne(1)[1]-1.1464)/1.1464,0.0001)       
        self.assertLess(abs(sol.local_buckl_b_ne(2)[1]-1.1106)/1.1106,0.0001)    


        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        
#        print sol.el.lambda_()
#        print sol.local_buckl_h_ne_old(1,0)[1]
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,0)[1]-1.40956234295)/1.40956234295,0.0001)    


        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=0.5*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        
#        print sol.el.lambda_()
#        print sol.local_buckl_h_ne_old(1,0)[1]
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,0)[1]-1.3478)/1.3478,0.0001)    



        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=1000, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=0.5*1000/9.81*100, my=0.500*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        
#        print sol.el.lambda_()
#        print 'otvet', sol.local_buckl_h_ne_old(1,0)[1]
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,0)[1]-2.658)/2.658,0.0001) 
        self.assertLess(abs(sol.local_buckl_h_ne(1,0)[1]-2.658)/2.658,0.0001) 

        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=1000, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=0.5*1000/9.81*100, my=0.500*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)        
        self.assertLess(abs(sol.local_buckl_h_ne(2,0)[1]-2.658)/2.658,0.0001) 

        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=300, ly=100, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=0.5*1000/9.81*100, my=0.500*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        
#        print sol.el.lambda_()
#        print 'otvet', sol.local_buckl_h_ne_old(1,0)[1]
        self.assertLess(abs(sol.local_buckl_h_ne_old(1,0)[1]-1.925101)/1.925101,0.0001) 

# просто констатация данных без проверок
        self.assertLess(abs(sol.local_buckl_h_ne(1,0)[1]-1.925101)/1.925101,0.0001)          


#        print 'sled'
#        print sol.local_buckl_h_ne_ut(1,0,0)[1]
        self.assertLess(abs(sol.local_buckl_h_ne_ut(1,0,0)[1]-2.39080)/2.39080,0.0001) 


        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=300, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=0.5*1000/9.81*100, my=0.500*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print 'sled'
        self.assertLess(abs(sol.local_buckl_h_ne(2,0)[1]-1.925101)/1.925101,0.0001)          

#        print sol.local_buckl_h_ne_ut(2,0,0)[1]
        self.assertLess(abs(sol.local_buckl_h_ne_ut(2,0,0)[1]-2.39080)/2.39080,0.0001) 

#    def test_snipn_korob(self):
#        print 29        
#
        pr1=truba_pryam(h=12,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        s=steel_snip20107n('C345',pr1, 1)
        el=elements(s, pr1, lx=100, ly=300, lb=100, lr=0, br=0, hr=0) 
        forc=force(n=20*1000/9.81, mx=0.5*1000/9.81*100, my=0.500*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print 'sled'
        self.assertLess(abs(sol.local_buckl_h_ne(2,0)[1]-1.925101)/1.925101,0.0001)          










        
if __name__ == "__main__":
    unittest.main()
    
    #        self.assertNotEqual(self.seq, range(10))
#    assertEqual(a, b) 	a == b 	 
#assertNotEqual(a, b) 	a != b 	 
#assertTrue(x) 	bool(x) is True 	 
#assertFalse(x) 	bool(x) is False 	 
#assertIs(a, b) 	a is b 	2.7
#assertIsNot(a, b) 	a is not b 	2.7
#assertIsNone(x) 	x is None 	2.7
#assertIsNotNone(x) 	x is not None 	2.7
#assertIn(a, b) 	a in b 	2.7
#assertNotIn(a, b) 	a not in b 	2.7
#assertIsInstance(a, b) 	isinstance(a, b) 	2.7
#assertNotIsInstance(a, b) 	not isinstance(a, b) 	2.77
#assertAlmostEqual(a, b) 	round(a-b, 7) == 0 	 
#assertNotAlmostEqual(a, b) 	round(a-b, 7) != 0 	 
#assertGreater(a, b) 	a > b 	2.7
#assertGreaterEqual(a, b) 	a >= b 	2.7
#assertLess(a, b) 	a < b 	2.7
#assertLessEqual(a, b) 	a <= b 	2.7
#assertRegexpMatches(s, re) 	regex.search(s) 	2.7
#assertNotRegexpMatches(s, re) 	not regex.search(s) 	2.7
#assertItemsEqual(a, b) 	sorted(a) == sorted(b) and works with unhashable objs 	2.7
#assertDictContainsSubset(a, b) 	all the key/value pairs in a exist in b 	2.7
