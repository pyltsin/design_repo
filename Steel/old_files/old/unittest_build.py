# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:52:37 2013

@author: puma
"""
#добавить устойчивость для короба
import unittest

from profiles2 import *
from table import *
pi=3.14159265358979



from steel import *

class Test_mat(unittest.TestCase):
    def test_mat_steel(self):
        el=dvut(h=400., b=130., t=11., s=9.5, r1=14., r2=6., a1=atan(12./100))
        s=steel_snip20107n('C245',el)
        self.assertLess(abs(s.ry()-2446.5)/2446.5,0.00002)          
        self.assertLess(abs(s.ryn()-2497.45)/2497.45,0.00002)
        self.assertLess(abs(s.ru()-3669.72)/3669.72,0.00002)          
        self.assertLess(abs(s.run()-3771.66)/3771.66,0.00002) 
        self.assertLess(abs(s.rs()-1418.97)/1418.97,0.00002) 
        self.assertLess(abs(s.rth()-1834.86)/1834.86,0.00002)
        self.assertLess(abs(s.rthf()-1223.25)/1223.25,0.00002) 
        self.assertLess(abs(s.mu()-0.3)/0.3,0.00002) 
        self.assertLess(abs(s.e()-2.0999*10**6)/(2.0999*10**6),0.00002)  
        print 18       
from snipn import *

class test_snipn(unittest.TestCase):
    def test_elements(self):    
        pr=dvut(h=600, b=190, t=17.8, s=12., r1=20., r2=08., a1=atan(12./100))
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=1000, ly=2000, lb=3000, lr=10, br=1, hr=2) 
        
        self.assertEqual(el.lx(),1000)
        self.assertEqual(el.ly(),2000)
        self.assertEqual(el.lb(),3000)
        self.assertEqual(el.lr(),10)
        self.assertEqual(el.br(),1)
        self.assertEqual(el.hr(),2)
#        print el.profile.ix()

        self.assertLess(abs(el.lambdax()-4.23170259)/4.23170259,0.00002) 
        self.assertLess(abs(el.lambday()-56.4765)/56.4765,0.00002) 
#        print (el.lambdax_())
        self.assertLess(abs(el.lambdax_()-0.14454)/0.14454,0.001) 
        self.assertLess(abs(el.lambday_()-1.9291)/1.9291,0.001)
        print 19       
    def test_force(self):
        forc=force(n=10, mx=20, my=30, w=40, qx=50, qy=60, t=70, sr=80, floc=90)
        self.assertEqual(forc.n,10)
        self.assertEqual(forc.mx,20)
        self.assertEqual(forc.my,30)
        self.assertEqual(forc.w,40)
        self.assertEqual(forc.qx,50)
        self.assertEqual(forc.qy,60)
        self.assertEqual(forc.t,70)
        self.assertEqual(forc.sr,80)
        self.assertEqual(forc.floc,90)  
        print 20               
    def test_snipn(self):
#только двутавр
#    def snipn1(self):
        #том 
#        print(1)
        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_h_n()
#        print el.lambdax_()
#        print el.lambday_()
        
        self.assertEqual(test[0],0) 
#        print(test[2])
        self.assertLess(abs(test[1]-1.997905)/1.997905,0.0001)        
        self.assertLess(abs(test[2]-1.44116298)/1.44116298,0.0001)   

        el2=elements(s, pr, lx=210000, ly=7000, lb=3000, lr=10, br=1, hr=2)  
        sol2=snipn(el2,forc,1)      
#        print el2.lambdax_()
#        print el2.lambday_()
        test=sol2.local_buckl_h_n()
        self.assertLess(abs(test[1]-2.3)/2.3,0.0001)        


        el2=elements(s, pr, lx=7000, ly=5000, lb=3000, lr=10, br=1, hr=2)  
        sol2=snipn(el2,forc,1)      
#        print el2.lambdax_()
#        print el2.lambday_()
        test=sol2.local_buckl_h_n()
#        print test[1]
        self.assertLess(abs(test[1]-1.6975)/1.6975,0.0001) 

        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_n()

        self.assertEqual(test[0],0) 
#        print(test[2])
        self.assertLess(abs(test[1]-0.5879)/0.5879,0.0001)        
        self.assertLess(abs(test[2]-0.333615248)/0.333615248,0.0001)        
        

        pr=dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C345',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
        test=sol.local_buckl_b_m()

        self.assertEqual(test[0],0) 
#        print('lalal0,',test[2])
        self.assertLess(abs(test[1]-0.5)/0.5,0.0001)        
        self.assertLess(abs(test[2]-0.4572)/0.4572,0.0001)        

        test=sol.local_buckl_h_m()

        self.assertEqual(test[0],1) 
#        print(test[2])
        self.assertLess(abs(test[1]-3.2)/3.2,0.0001)        
        self.assertLess(abs(test[2]-5.173)/5.173,0.0001)   

        pr=dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr)
        el=elements(s, pr, lx=7000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.phiy()-0.781)/0.781,0.0001)  
        self.assertLess(abs(sol.phi()-0.781)/0.781,0.0001)
   
        self.assertLess(abs(sol.phix()-0.919)/0.919,0.0001)                  

        pr1=dvut(h=520, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=35000, ly=7000, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.phi()-0.28394)/0.28394,0.0001)


        pr1=dvut(h=520, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=7000, ly=700, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
#        print el.lambda_()[0]
#        print sol.phi()
        self.assertLess(abs(sol.phi()-0.9654)/0.9654,0.0001)

        self.assertLess(abs(sol.cxcyn()[1]-1.47)/1.47,0.0001)      
        self.assertLess(abs(sol.cxcyn()[2]-1.5)/1.5,0.0001)   

        self.assertLess(abs(sol.cxcyn()[0]-1.0444)/1.0444,0.0001) 

        pr1=dvut(h=520, b=400, t=10, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=7000, ly=700, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)
#        print pr1.afaw()
#        print sol.cxcyn()[0]
        self.assertLess(abs(sol.cxcyn()[0]-1.08111)/1.08111,0.0001) 


        pr1=dvut(h=520, b=400, t=5, s=9, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=7000, ly=700, lb=3000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)  
#        print sol.cxcyn()[0]
        self.assertLess(abs(sol.cxcyn()[0]-1.138)/1.138,0.0001) 

        pr1=dvut(h=520, b=200, t=20, s=8, r1=0, r2=0, a1=0)

        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=7000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1) 
#тип: 1 - балка, 2 -консиль
#тип 1: 1- без закреплений, 2 - два и более, 3 - один по центру
#тип 2: 1-сосредоточенная, 2 - сосредоточенная в четверти, 3 - равномерная
#тип 3: 1- сжатый, 2 - расстянутый
        self.assertLess(abs(sol.psib(0.319,1,1,1)-1.7787)/1.7787,0.0001) 
        self.assertLess(abs(sol.psib(0.319,1,1,2)-5.0787)/5.0787,0.0001)
        self.assertLess(abs(sol.psib(0.319,1,2,1)-1.7787)/1.7787,0.0001)         
        self.assertLess(abs(sol.psib(0.319,1,2,2)-5.0787)/5.0787,0.0001) 
        self.assertLess(abs(sol.psib(0.319,1,3,1)-1.62552)/1.62552,0.0001)         
        self.assertLess(abs(sol.psib(0.319,1,3,2)-3.8255)/3.8255,0.0001)
        self.assertLess(abs(sol.psib(0.319,2,1,1)-2.27233)/2.27233,0.0001)
        self.assertLess(abs(sol.psib(0.319,3,1,1)-3.9765775)/3.9765775,0.0001)
        self.assertLess(abs(sol.psib(0.319,3,2,1)-2.590456)/2.590456,0.0001)
        self.assertLess(abs(sol.psib(0.319,3,2,2)-3.635728)/3.635728,0.0001)
        self.assertLess(abs(sol.psib(0.319,3,3,1)-2.590456)/2.590456,0.0001)
        self.assertLess(abs(sol.psib(0.319,3,3,2)-2.95403)/2.95403,0.0001)
        
        
        self.assertLess(abs(sol.psib(300,1,1,1)-15.15)/15.15,0.0001) 
        self.assertLess(abs(sol.psib(300,1,1,2)-18.45)/18.45,0.0001)
        self.assertLess(abs(sol.psib(300,1,2,1)-15.15)/15.15,0.0001)         
        self.assertLess(abs(sol.psib(300,1,2,2)-18.45)/18.45,0.0001) 
        self.assertLess(abs(sol.psib(300,1,3,1)-12.72)/12.72,0.0001)         
        self.assertLess(abs(sol.psib(300,1,3,2)-14.92)/14.92,0.0001) 
        self.assertLess(abs(sol.psib(300,2,1,1)-12.45)/12.45,0.0001)
        self.assertLess(abs(sol.psib(300,3,1,1)-21.7875)/21.7875,0.0001)
        self.assertLess(abs(sol.psib(300,3,2,1)-14.193)/14.193,0.0001)
        self.assertLess(abs(sol.psib(300,3,2,2)-19.92)/19.92,0.0001)
        self.assertLess(abs(sol.psib(300,3,3,1)-14.193)/14.193,0.0001)
        self.assertLess(abs(sol.psib(300,3,3,2)-16.185)/16.185,0.0001)


#тип 2: 4 - на конце консоли, 3 - равномерная
#тип 3: 1- сжатый, 2 - расстянутый

        self.assertLess(abs(sol.psik(10,4,1)-7)/7,0.0001) 
        self.assertLess(abs(sol.psik(10,4,2)-2.6)/2.6,0.0001) 
        self.assertLess(abs(sol.psik(10,3,2)-4.4904343)/4.4904343,0.0001) 
        self.assertLess(abs(sol.psik(50,4,1)-9.5)/9.5,0.0001) 
        self.assertLess(abs(sol.psik(50,4,2)-6.5)/6.5,0.0001) 
 
#        print (pr1.jy()/pr1.jx())
#        print sol.phi_b(2,1,4,1)
        self.assertLess(abs(sol.phi_b(1,1,1,1)-0.583120178122)/0.583120178122,0.0001)   
        
        self.assertLess(abs(sol.phi_b(2,1,4,1)-0.94089102707)/0.94089102707,0.001) 


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
        pr1=dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=3500, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,1)-1.25574)/1.25574,0.001)  
#
#        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4,1)-1.344)/1.344,0.001) 


        pr1=dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=3500, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)


        self.assertLess(abs(sol.nau(10.,1)-1.20208)/1.20208,0.001)  
#
#        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4,1)-1.2474)/1.2474,0.001)      

        pr1=dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=70000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,1)-1.20208)/1.20208,0.001)  
#
#        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4,1)-1.20208)/1.20208,0.001)  


        pr1=dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=70000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,1)-1.25208)/1.25208,0.001)  
#
#        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4,1)-1.25208)/1.25208,0.001)  


        pr1=dvut(h=520, b=400, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=70000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,1)-1.3)/1.3,0.001)  
#
#        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4,1)-1.3)/1.3,0.001)

#nau 2
        pr1=dvut(h=520, b=200, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=3500, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-0.91366)/0.91366,0.001) 
        
        


        pr1=dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=3500, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1)/1,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-0.88773)/0.88773,0.001) 


        pr1=dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=3500, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)


        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-0.932848)/0.932848,0.001)      

        pr1=dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=70000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-0.932848)/0.932848,0.001)  


        pr1=dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=70000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-0.88773)/0.88773,0.001)  


        pr1=dvut(h=520, b=350, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=70000, ly=700, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-0.94807)/0.94807,0.001)          


        pr1=dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=700, ly=700000, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-1)/1,0.001)  


        pr1=dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1, lx=700, ly=700000, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-1)/1,0.001)  


        pr1=dvut(h=520, b=350, t=20, s=8, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C245',pr1)
        el=elements(s, pr1,lx=700, ly=700000, lb=8000, lr=10, br=1, hr=2) 
        forc=force()        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.nau(10.,2)-1.)/1.,0.001)  
#
#        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4,2)-1)/1,0.001)           

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

        self.assertLess(abs(sol.phix()-0.946)/0.946,0.001) 
        self.assertLess(abs(sol.phiy()-0.8579)/0.8579,0.001)
        
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

        pr1=dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s=steel_snip20107n('C255',pr1)
        el=elements(s, pr1, lx=10000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=500*1000/9.81*100, my=500*1000/9.81*100, qx=100*1000/9.81)        
        sol=snipn(el,forc,1)

#!!!дополнительные тесты по местной устойчивости
        
        self.assertLess(abs(sol.local_buckl_h_m(1,1)[1]-3.2)/3.2,0.001)
        self.assertLess(abs(sol.local_buckl_h_m(1,2)[1]-2.2)/2.2,0.001)

        self.assertLess(abs(sol.local_buckl_h_m(2,1)[1]-3.5)/3.2,0.001)
        self.assertLess(abs(sol.local_buckl_h_m(2,2)[1]-2.5)/2.2,0.001)


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


        s=steel_snip20107n('C345',pr1, 1)
        el=elements(s, pr1, lx=5000, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
        
        self.assertLess(abs(sol.local_buckl_h_n()[0]-0)/0.0001,0.001)        
        self.assertLess(abs(sol.local_buckl_h_n()[1]-1.6)/1.6,0.001)    

#        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_h_n()[2]-0.6306)/0.6306,0.001) 

        s=steel_snip20107n('C345',pr1, 1)
        el=elements(s, pr1, lx=50, ly=3, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_n()[0]-0)/0.0001,0.001)        
        self.assertLess(abs(sol.local_buckl_h_n()[1]-1.2)/1.2,0.001)    

#        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_h_n()[2]-0.6306)/0.6306,0.001)


        el=elements(s, pr1, lx=200, ly=3, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_h_n()[0]-0)/0.0001,0.001)        
        self.assertLess(abs(sol.local_buckl_h_n()[1]-1.364)/1.364,0.001)    

#        print sol.local_buckl_h_n()[1]     
        self.assertLess(abs(sol.local_buckl_h_n()[2]-0.6306)/0.6306,0.001)


        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)

        s=steel_snip20107n('C345',pr1, 1)
        el=elements(s, pr1, lx=300, ly=5000, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)
        
        self.assertLess(abs(sol.local_buckl_b_n()[0]-0)/0.0001,0.001)        
        self.assertLess(abs(sol.local_buckl_b_n()[1]-1.6)/1.6,0.001)    

#        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_b_n()[2]-0.6306)/0.6306,0.001) 

        s=steel_snip20107n('C345',pr1, 1)
        el=elements(s, pr1, lx=3, ly=50, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_b_n()[0]-0)/0.0001,0.001)        
        self.assertLess(abs(sol.local_buckl_b_n()[1]-1.2)/1.2,0.001)    

#        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_b_n()[2]-0.6306)/0.6306,0.001)


        el=elements(s, pr1, lx=3, ly=200, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=100*1000/9.81*100, my=000*1000/9.81*100, qx=500*1000/9.81)        
        sol=snipn(el,forc,1)

        self.assertLess(abs(sol.local_buckl_b_n()[0]-0)/0.0001,0.001)

        self.assertLess(abs(sol.local_buckl_b_n()[1]-1.364)/1.364,0.001)    

#        print sol.local_buckl_h_n()[1]     
        self.assertLess(abs(sol.local_buckl_b_n()[2]-0.6306)/0.6306,0.001)
        

        self.assertLess(abs(sol.local_buckl_b_m()[0]-0)/0.0001,0.001)
        self.assertLess(abs(sol.local_buckl_b_m()[1]-1.5)/1.5,0.001)
        self.assertLess(abs(sol.local_buckl_b_m()[2]-0.6306)/0.6306,0.001)


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
        

        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=300, ly=300, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
        self.assertLess(abs(sol.phi()-0.541)/0.541,0.001)
#        print sol.phi()           


        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=1000, ly=1000, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.phi()    
        self.assertLess(abs(sol.phi()-0.04863)/0.04863,0.001)

        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=100, ly=100, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.phi()    
        self.assertLess(abs(sol.phi()-0.95)/0.95,0.001)
        

        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=10, ly=10, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.phi()    
        self.assertLess(abs(sol.phi()-1)/1,0.001)

        pr1=truba_pryam(h=8,b=12,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=10, ly=10, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.cxcyn()[1]
        self.assertLess(abs(sol.cxcyn()[0]-1.08176)/1.08176,0.0001)        
        self.assertLess(abs(sol.cxcyn()[1]-1.1735)/1.1735,0.0001)  
        self.assertLess(abs(sol.cxcyn()[2]-1.5)/1.5,0.0001)  

        pr1=truba_pryam(h=8,b=24,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=10, ly=10, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.cxcyn()[1]
        self.assertLess(abs(sol.cxcyn()[0]-1.0471)/1.0471,0.0001)        
        self.assertLess(abs(sol.cxcyn()[1]-1.2435)/1.2435,0.0001)  
        self.assertLess(abs(sol.cxcyn()[2]-1.5)/1.5,0.0001)


        pr1=truba_pryam(h=8,b=6,t=0.6, s=0.6, r2=1.2, r1=0.6)
        el=elements(s, pr1, lx=10, ly=10, lb=300, lr=0, br=0, hr=0) 
        forc=force(n=200*1000/9.81, mx=1*1000/9.81*100, my=000*1000/9.81*100, qx=00*1000/9.81)        
        sol=snipn(el,forc,1)
#        print sol.cxcyn()[1]
        self.assertLess(abs(sol.cxcyn()[0]-1.1365)/1.1365,0.0001)        
        self.assertLess(abs(sol.cxcyn()[1]-1.108235)/1.108235,0.0001)  
        self.assertLess(abs(sol.cxcyn()[2]-1.5)/1.5,0.0001)

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









    def test_steel_snip1987(self):
        print 33     
        el=dvut(h=400., b=130., t=11., s=9.5, r1=14., r2=6., a1=atan(12./100))
        s=steel_snip1987('C245',el)
        self.assertLess(abs(s.ry()-2446.5)/2446.5,0.00002)          
        self.assertLess(abs(s.ryn()-2497.45)/2497.45,0.00002)
        self.assertLess(abs(s.ru()-3669.72)/3669.72,0.00002)          
        self.assertLess(abs(s.run()-3771.66)/3771.66,0.00002) 
        self.assertLess(abs(s.rs()-1418.97)/1418.97,0.00002) 
        self.assertLess(abs(s.rth()-1834.86)/1834.86,0.00002)
        self.assertLess(abs(s.rthf()-1223.25)/1223.25,0.00002) 
        self.assertLess(abs(s.mu()-0.3)/0.3,0.00002) 
        self.assertLess(abs(s.e()-2.0999*10**6)/(2.0999*10**6),0.00002)  

        s=steel_snip1987('C345',el)
#        print s.ry()
        self.assertLess(abs(s.ry()-315/9.81*100)/2446.5,0.00002)          
        self.assertLess(abs(s.ryn()-325/9.81*100)/2497.45,0.00002)
        self.assertLess(abs(s.ru()-460/9.81*100)/3669.72,0.00002)          
        self.assertLess(abs(s.run()-470/9.81*100)/3771.66,0.00002) 

        self.assertLess(abs(s.mu()-0.3)/0.3,0.00002) 
        self.assertLess(abs(s.e()-2.0999*10**6)/(2.0999*10**6),0.00002)

        el=dvut(h=400., b=130., t=61., s=9.5, r1=14., r2=6., a1=atan(12./100))
        s=steel_snip1987('C345',el, typ_steel='list')
#        print s.ry()
        self.assertLess(abs(s.ry()-270/9.81*100)/2446.5,0.00002)          
        self.assertLess(abs(s.ryn()-275/9.81*100)/2497.45,0.00002)
        self.assertLess(abs(s.ru()-430/9.81*100)/3669.72,0.00002)          
        self.assertLess(abs(s.run()-440/9.81*100)/3771.66,0.00002) 

        self.assertLess(abs(s.mu()-0.3)/0.3,0.00002) 
        self.assertLess(abs(s.e()-2.0999*10**6)/(2.0999*10**6),0.00002)
        
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
