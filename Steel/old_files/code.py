# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:57:52 2013

@author: puma
"""
#местная устойчивость по п.8.5.3.
from table import tables_csv
#from profiles2 import *

#from steel import *



           
class elements(object):
    def __init__(self, steel, profile, mux=0, muy=0, mub=0, lfact=0, br=0, hr=0):
        self.steel=steel
        self.profile=profile
        self.__lx=float(lfact)*float(mux)
        self.__ly=float(lfact)*float(muy)
        self.__lb=float(lfact)*float(mub)
        self.__lfact=float(lfact)
        self.__br=float(br)
        self.__hr=float(hr)
        self.__lambdax=self.__lx/self.profile.ix()
        self.__lambday=self.__ly/self.profile.iy() 
#        print self.steel.ry()
#        print self.steel.e()        
        self.__lambdax_=self.__lambdax*(self.steel.ry()/self.steel.e())**0.5
        self.__lambday_=self.__lambday*(self.steel.ry()/self.steel.e())**0.5

    def lx(self):
        return self.__lx
    def ly(self):
        return self.__ly
    def lb(self):
        return self.__lb
    def lfact(self):
        return self.__lfact
    def br(self):
        return self.__br
    def hr(self):
        return self.__hr
    def lambdax(self):
        return self.__lambdax        
    def lambday(self):
        return self.__lambday
    def lambdax_(self):
        return self.__lambdax_       
    def lambday_(self):
        return self.__lambday_
    def lambda_(self):
        if self.lambdax_()>self.lambday_():
            lambda_=self.lambdax_()
            typ=1
        else:
            lambda_=self.lambday_()
            typ=0
        return lambda_, typ
class force(object):
    def __init__(self, n=0, mx=0, my=0, w=0, qx=0, qy=0, t=0, sr=0, floc=0):
        force.n=n
        force.mx=mx
        force.my=my 
        force.w=w  
        force.qx=qx  
        force.qy=qy 
        force.t=t
        force.sr=sr  
        force.floc=floc     
              
class normes(object):
    def __init__(self, element, forces, yc):
        self.element=element
        self.el=self.element
        self.force=forces
        self.__yc=yc
        self.pr=self.element.profile
    def yc(self):
        return self.__yc


class snipn(normes):
    def yu(self):
        return 1.3
    def phi_n(self, lambda_, typ=0):
        #typ = 1 - в плоскости стенки
        if self.pr.title()=='korob' or self.pr.title()=='truba':       
            typ_sec='a'
        if self.pr.title()=='dvut' or self.pr.title()=='ugol_tavr_st_krest' or self.pr.title()=='shvel_korob' or self.pr.title()=='shvel_dvut':
            typ_sec='b'
        if self.pr.title()=='dvut' and    self.pr.h()>500 and typ==1:
            typ_sec='a'
        if self.pr.title()=='ugol_tavr_st_right' or self.pr.title()=='ugol_tavr_st_up':               
            typ_sec='c'

           
        if typ_sec=='a':
            a=0.03
            b=0.06 
            c=3.8
#            print self.pr.h()
        if typ_sec=='b':
            a=0.04
            b=0.09
            c=4.4
        if typ_sec=='c':
            a=0.04
            b=0.14 
            c=5.8
#        print a, b
        delta=9.87*(1-a+b*lambda_)+lambda_**2
        phi_n=0.5*(delta-(delta**2-39.48*lambda_**2)**0.5)/lambda_**2
        
        if lambda_>c:
            if phi_n>7.6/lambda_**2:
                phi_n=7.6/lambda_**2
               
        if phi_n>1 or lambda_<0.4:
            phi_n=1
        
        return phi_n, typ_sec

#нет тестов 

    def phi_n_old(self, lambda_, typ=0):
        ry=self.element.steel.ry()
        e=self.element.steel.e() 
        if 0<lambda_ and lambda_<=2.5:
            phi=1-(0.073-5.53*ry/e)*lambda_*lambda_**0.5
        if 2.5<lambda_ and lambda_<=4.5:
            phi=1.47-13*ry/e-(0.371-27.3*ry/e)*lambda_+(0.0275-5.53*ry/e)*lambda_**2
        if lambda_>4.5:
            phi=332/(lambda_**2*(51-lambda_))
        return phi
            
    def phix(self):
        return self.phi_n(self.element.lambdax_(), typ=1)
    def phiy(self):
        return self.phi_n(self.element.lambday_(), typ=0)
        
    def phi(self):
        phix=self.phix()[0]
        phiy=self.phiy()[0]
        if phix<phiy:
            return phix
        else:
            return phiy

#нет тестов 
    def phix_old(self):
        return self.phi_n_old(self.element.lambdax_(), typ=1)
    def phiy_old(self):
        return self.phi_n_old(self.element.lambday_(), typ=0)

    def phi_old(self):
        phix=self.phix()
        phiy=self.phiy() 
        if phix<phiy:
            return phix
        else:
            return phiy     
            

    def q_fic(self, n, phi):
        ry=self.element.steel.ry()
        e=self.element.steel.e() 
        q_fic=7.15*10**(-6)*(2330-e/ry)*n/phi
        return q_fic
    def q_fic_old(self, n, phi):
        return self.q_fic(n, phi)
            














            
    def local_buckl_h_n(self, typ=3):

        if typ==3:
            lambda_=self.element.lambda_()[0]  
#        print lambda_
        if typ==1:
            lambda_=self.el.lambdax_()
        if typ==2:
            lambda_=self.el.lambday_()
                
        if self.pr.title()=='dvut':
            if lambda_<=2:
                lambda_uw=1.3+0.15*lambda_**2
            else:
                lambda_uw=1.2+0.35*lambda_
                if lambda_uw>2.3:
                    lambda_uw=2.3
        if self.pr.title()=='korob':
            if lambda_<=1:
                lambda_uw=1.2
            else:
                lambda_uw=1.0+0.2*lambda_
                if lambda_uw>1.6:
                    lambda_uw=1.6
        lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
        if lambda_uw>=lambda_w:
            check=0
        else:
            check=1
        return check, lambda_uw, lambda_w
     
        
    def local_buckl_b_n(self):
        lambda_=self.element.lambda_() [0]  
#        print 'lambda_', lambda_    
        if self.pr.title()=='dvut':

            if lambda_<=0.8:
                lambda_=0.8
            if lambda_>=4:
                lambda_=4
            lambda_uf=0.36+0.1*lambda_
        if self.pr.title()=='korob':
            if lambda_<=1:
                lambda_uf=1.2
            else:
                lambda_uf=1.0+0.2*lambda_
                if lambda_uf>1.6:
                    lambda_uf=1.6
    
        lambda_f=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5
#        print(('bef',self.pr.bef()),('t',self.pr.t()),('ry',self.element.steel.ry()),('e',self.element.steel.e()) )        
#        print 'lambda_uf', lambda_uf

        if lambda_uf>=lambda_f:
            check=0
        else:
            check=1
        return check, lambda_uf, lambda_f

    def local_buckl_b_n_old(self):

        lambda_=self.element.lambda_() [0]  
            
        if self.pr.title()=='dvut':

            if lambda_<=0.8:
                lambda_=0.8
            if lambda_>=4:
                lambda_=4
            lambda_uf=0.36+0.1*lambda_

    
        lambda_f=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5
#        print(('bef',self.pr.bef()),('t',self.pr.t()),('ry',self.element.steel.ry()),('e',self.element.steel.e()) )        
#        print lambda_f, lambda_uf
        if lambda_uf>=lambda_f and  self.pr.title()=='dvut':
            check=0
        else:
            check=1
        return check, lambda_uf, lambda_f

        
    def local_buckl_h_m(self, typ1=1, typ2=1):

#без ребер "простая" проверка
# typ1 =1 - без ребер
#typ2 - 
# 1 - без местной нагрузки
# 2 - с местной нагрузкой

        if typ1==1:
            if typ2==1:        
                lambda_uw=3.2
            if typ2==2:
                lambda_uw=2.2
        if typ1==2:
            if typ2==1:        
                lambda_uw=3.5
            if typ2==2:
                lambda_uw=2.5
        lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
        if lambda_uw>=lambda_w:
            check=0
        else:
            check=1
        return check, lambda_uw, lambda_w     
    
    def local_buckl_h_m_old(self, typ1, typ2):

        return self.local_buckl_h_m(typ1, typ2)  
        
    def local_buckl_h_m2(self, typ=1):
#        typ=2 - для старого снипа


        hef=self.pr.hef()
        t=self.pr.s()
        ry=self.element.steel.ry()
        rs=self.element.steel.rs()
        m=self.force.mx
#        print 'rs', rs
        lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
                #получаем a
        
        tau=self.force.qx/(self.pr.s()*(self.pr.hw()))
        if self.pr.title()=='dvut':
            tau_t=tau/rs
        if self.pr.title()=='korob':
            tau_t=tau/rs/2            
        yc=self.yc()
        
        if lambda_w>5.5 or tau_t>0.9 or (typ==2 and self.pr.afaw()<0.25):
            a=0
        else:
            if lambda_w<2.2:
                lambda_wt=2.2
            else:
                lambda_wt=lambda_w
            a_table=tables_csv('a18.csv', 'float_all')
            a=a_table.get_interpolate(lambda_wt, tau_t)
            
            if typ==2:
                a=0.24-0.15*(tau_t)**2-8.5*10**(-3)*(lambda_wt-2.2)**2
                
#            print 'lambda_wt', lambda_wt
#            print 'tau_t', tau_t
#            print 'lambda_w', lambda_w 
#            print 'self.pr.afaw ', self.pr.afaw ()
#            print 'a ', a
#       
        if      self.pr.title()=='dvut':
            af=self.pr.afaw ()
        if      self.pr.title()=='korob':
            af=self.pr.afaw ()*2            
        r=1

        mult1=ry*yc*hef**2*t*(r*af+0)
        mult2=ry*yc*hef**2*t*(0+a)
        mult=mult1+mult2
        k=self.force.mx/mult
        if a==0:
            k=2
        if k>1:
            lambda_uw=0
        else:
            lambda_uw=lambda_w/(k)**0.5
            if lambda_uw>5.5:
                lambda_uw=5.5
            if lambda_uw<2.2:
                lambda_uwt=2.2
            else:
                lambda_uwt=lambda_uw
            t_d=hef/lambda_uw*(self.element.steel.ry()/self.element.steel.e())**0.5                
            tau_d=self.force.qx/(t_d*(self.pr.hw()))
            if self.pr.title()=='dvut':
                tau_td=tau_d/rs
            if self.pr.title()=='korob':
                tau_td=tau_d/rs/2          
            a_d=a_table.get_interpolate(lambda_uwt, tau_td)
            mult2_d=ry*yc*hef**2*t*(0+a_d)
            if m>mult2_d+mult1:
                lambda_uw=0
            
        
        
#        print 'tau_t', tau_t
#        
#        print 'mult1', mult1
#        print 'mult2', mult2
#        print 'lambda_uw', lambda_uw
        return k, mult, lambda_uw, lambda_w, a

    def local_buckl_h_m2_old(self):

        return self.local_buckl_h_m2(2)  

        
    def local_buckl_b_m2(self, typ1=1): 

        #typ1=1 ламбда_ув=ламбда_в - в запас расчета.
        lambdaf=self.pr.bef()/self.pr.t()  /(self.element.steel.e()/self.element.steel.ry())**0.5                     

        if typ1==1:
            lambda_uw=self.local_buckl_h_m2()[3]
        if typ1==2:
            lambda_uw=self.local_buckl_h_m2()[2]    
        
        if lambda_uw<=5.5 and lambda_uw>0:
            if lambda_uw<2.2:
                lambda_uw=2.2
                
            if self.pr.title()=='dvut' or self.pr.title()=='shvel':
                lambdauf=0.17+0.06*lambda_uw
            if self.pr.title()=='korob':
                lambdauf=0.675+0.15*lambda_uw
        else:
            lambdauf=0
            
        if lambdauf>=lambdaf:
            check=0
        else:
            check=1
        return check, lambdauf, lambdaf    

    def local_buckl_b_m2_old(self):

        lambdaf=self.pr.bef()/self.pr.t() /(self.element.steel.e()/self.element.steel.ry())**0.5                     

        lambdauf=0.11*self.pr.hef()/self.pr.s()/(self.element.steel.e()/self.element.steel.ry())**0.5                     

        if lambdauf>0.5:
            lambdauf=0.5

        if self.pr.hef()/self.pr.s()<=2.7*(self.element.steel.e()/self.element.steel.ry())**0.5:
            lambdauf=0.3          
                     
#        print 'lambdauf', lambdauf
#        print 'lambdaf', lambdaf
        
        if lambdauf>=lambdaf:
            check=0
        else:
            check=1
        return check, lambdauf, lambdaf 
        
    def local_buckl_b_m(self): 

        lambdaf=self.pr.bef()/self.pr.t()  /(self.element.steel.e()/self.element.steel.ry())**0.5                     
        if self.pr.title()=='dvut' or self.pr.title()=='shvel':
            lambdauf=0.5
        if self.pr.title()=='korob':
            lambdauf=1.5
        if lambdauf>=lambdaf:
            check=0
        else:
            check=1
        return check, lambdauf, lambdaf

    def local_buckl_b_m_old(self):
        
        lambdaf=self.pr.bef()/self.pr.t()  /(self.element.steel.e()/self.element.steel.ry())**0.5                     
        if self.pr.title()=='dvut' or self.pr.title()=='shvel':
            lambdauf=0.5
        if lambdauf>=lambdaf:
            check=0
        else:
            check=1
        return check, lambdauf, lambdaf        

        
     
#нет тестов на все элементы        
   


#нет тестов     

        
    def cxcyn(self):
        if self.pr.title()=='truba':
            n=1.5
            cx=1.26
            cy=1.26
        if self.pr.title()=='dvut':
            n=1.5
            cy=1.47
            if 0.25<=self.pr.afaw() and self.pr.afaw()<=0.5:
                cx=(1.12-1.19)/(0.5-0.25)*(self.pr.afaw()-0.25)+1.19
            if 0.5<=self.pr.afaw() and self.pr.afaw()<=1:
                cx=(1.07-1.12)/(1-0.5)*(self.pr.afaw()-0.5)+1.12
            if 1<=self.pr.afaw() and self.pr.afaw()<=2:
                cx=(1.04-1.07)/(2-1)*(self.pr.afaw()-1)+1.07
        if self.pr.title()=='shvel':
            n=1
            cy=1.6
            afaw=1/self.pr.afaw()/2
            if 0.5<=afaw and afaw<=1:
                cx=(1.12-1.07)/(1-0.5)*(afaw-0.5)+1.07
            if 1<=afaw and afaw<=2:
                cx=(1.19-1.12)/(2-1)*(afaw-1)+1.12

        if self.pr.title()=='korob':
            n=1.5
            if 0.25<=self.pr.afaw() and self.pr.afaw()<=0.5:
                cx=(1.12-1.19)/(0.5-0.25)*(self.pr.afaw()-0.25)+1.19
                cy=(1.12-1.07)/(0.5-0.25)*(self.pr.afaw()-0.25)+1.07
                 
            if 0.5<=self.pr.afaw() and self.pr.afaw()<=1:
                cx=(1.07-1.12)/(1-0.5)*(self.pr.afaw()-0.5)+1.12
                cy=(1.19-1.12)/(1-0.5)*(self.pr.afaw()-0.5)+1.12
                
            if 1<=self.pr.afaw() and self.pr.afaw()<=2:
                cx=(1.04-1.07)/(2-1)*(self.pr.afaw()-1)+1.07    
                cy=(1.26-1.19)/(2-1)*(self.pr.afaw()-1)+1.19
        return cx, cy, n   
    def cxcyn_old(self):
        return self.cxcyn()
               
#тип: 1 - балка, 2 -консиль
#тип 1: 1- без закреплений, 2 - два и более, 3 - один по центру
#тип 2: 1-сосредоточенная, 2 - сосредоточенная в четверти, 3 - равномерная
#тип 3: 1- сжатый, 2 - расстянутый
# тип 4=1 - новый снип иначе старый 
#полная проверка на старый снип не проводилась   

#нет тестов    
    def phi_b_old(self, typ, typ1, typ2, typ3):
        return self.phi_b(self, typ, typ1, typ2, typ3, typ4=0, typ_norm='old')

#    def phi_b(self, typ, typ1, typ2, typ3, typ4=1):
##        print 'typ4'
#        return self.phi_ballnorm(self, typ, typ1, typ2, typ3, typ4=typ4, typ_norm='new') 
        
    def phi_b(self, typ, typ1, typ2, typ3, typ4=1, typ_norm='new'):
        pr=self.element.profile
        el=self.element
        if pr.title()=='dvut' or pr.title()=='shvel':
            if pr.title2()=='prokat':
                if typ4==1:
                    jt=self.pr.jt_sp()
#                    print 'jt', jt
                if typ4<>1 and pr.title()=='dvut':
                    jt=self.pr.jt()

                if typ_norm=='old':
                    jt=self.pr.jt()                    
                    
                a=1.54*jt/pr.jy()*(el.lb()/pr.h())**2
#                print 'jy', pr.jy()
            else:
                h=self.pr.h()
                t=self.pr.t()
                s=self.pr.s()
                b=self.pr.b()
                h1=h-t                
                a1=0.5*h1
                a=8*(el.lb()*t/(h1*b))**2*(1+a1*s**3/(b*t**3))
#            print a
            if typ==1:
                if typ_norm=='new':
                    psi=self.psib(a,typ1,typ2,typ3)
                else:
                    psi=self.psib_old(a,typ1,typ2,typ3)                    
            if typ==2:
                if typ_norm=='new':                
                    psi=self.psik(a, typ2, typ3)
                else:
                    psi=self.psik_old(a, typ2, typ3)                    
            if pr.title2()=='prokat':
                h_t=pr.h()
            else:
                h_t=pr.h()-pr.t()
            phi1=psi*pr.jy()/pr.jx()*((h_t)/el.lb())**2*el.steel.e()/el.steel.ry()
#            print psi,pr.jy()/pr.jx(), ((pr.h()-pr.t1())/el.lb())**2, el.steel.e()/el.steel.ry()
            if pr.title()=='dvut':
                if phi1<=0.85:
                    phib=phi1
                else:
                    phib=0.68+0.21*phi1
                    if phib>1:
                        phib=1
            if pr.title()=='shvel':
                phib=0.7*phi1
                if phib>1:
                    phib=1  
        if pr.title()=='korob':
            phib=1
        
        return phib
        
        
    def psib(self,a, typ1, typ2, typ3):

        psi=10**(10)
        if 0.1<=a and a<=40:
            psi1=2.25+0.07*a
        if 40<a and a<=400:
            psi1=3.6+0.04*a-3.5*10**(-5)*a**2
        

        if typ1==1:
            if 0.1<=a and a<=40:
                if typ2==1 or typ2==2:
                    if typ3==1:
                        psi=1.75+0.09*a
                    else:
                        psi=5.05+0.09*a
                if typ2==3:
                    if typ3==1:
                        psi=1.6+0.08*a
                    else:
                        psi=3.8+0.08*a
            if 40<a and a<=400:
                if typ2==1 or typ2==2:
                    if typ3==1:
                        psi=3.3+0.053*a-4.5*10**(-5)*a**2
                    else:
                        psi=6.6+0.053*a-4.5*10**(-5)*a**2
                if typ2==3:
                    if typ3==1:
                        psi=3.15+0.04*a-2.7*10**(-5)*a**2
                    else:
                        psi=5.35+0.04*a-2.7*10**(-5)*a**2
        if typ1==2:
            psi=psi1
        if typ1==3:
            if typ2==1:
                psi=1.75*psi1
            if typ2==2:
                if typ3==1:
                    psi=1.14*psi1
                if typ3==2:
                    psi=1.6*psi1
            if typ2==3:
                if typ3==1:
                    psi=1.14*psi1
                if typ3==2:
                    psi=1.3*psi1  
        return psi
    def psik(self, a, typ2, typ3):
        psi=10**(10)
        if typ2==4:
            if typ3==1:
                if 4<=a and a<=28:
                    psi=6.2+0.08*a
                if 28<=a and a<=100:
                    psi=7.+0.05*a
            if typ3==2:
                if 4<=a and a<=28:
                    psi=1+0.16*a
                if 28<=a and a<=100:
                    psi=4+0.05*a
        if typ2==3:
            if typ3==2:
                psi=1.42*a**0.5
        return psi

#нет тестов 
    def psib_old(self,a, typ1, typ2, typ3):
        return self.psib(a,typ1, typ2, typ3)
    def psik_old(self, a, typ2, typ3):
        return self.psik_old(a, typ2, typ3)


    def phi_e(self, typ):
#только для симметричных профилей   
        mefm=self.mef(typ)
        mef=mefm[0]
        nau=mefm[1]
        if typ==1:
            lambda_=self.el.lambdax_()
        if typ==2:
            lambda_=self.el.lambday_()  
        phi_e=self.phi_etable(mef, lambda_)
        phi=self.phi_n(lambda_,typ-1)
        if phi<phi_e:
            phi_e=phi
        return phi_e, mef, nau, lambda_
        
    def phi_etable(self, mef, lambda_):
        mef=float(mef)
        lambda_=float(lambda_)
        if mef<0.1:
            mef=0.1
        if mef>20:
            mef=20
        if lambda_<0.5:
            lambda_=0.5
        if lambda_<14:
            
            table=tables_csv('table_phi_n.csv', 'float_all')
            phi=table.get_interpolate(mef, lambda_)
        if lambda_>14:
            phi=1/10.**10
        phi=phi/1000.
        
        return phi
        
    def mef(self, typ):
        if typ==1:
            e=self.force.mx/self.force.n
            m=self.pr.a()/self.pr.wx()*e
        if typ==2:
            e=self.force.my/self.force.n
            m=self.pr.a()/self.pr.wy()*e
        nau=self.nau(m, typ)
        mef=nau*m
        return mef, nau
                
    def nau(self, m, typ):
        #typ -1 -в главной плоскости, typ2  - в другой
        n=10**10
        n1=n
        if self.pr.title()=='dvut' or self.pr.title()=='korob':
            if typ==1:            
                if 0<=self.el.lambdax_() and self.el.lambdax_()<=5:      
                    if 0.1<=m and m<=5:
                        n025=(1.45-0.05*m)-0.01*(5-m)*self.el.lambdax_()
                        n05=(1.75-0.1*m)-0.02*(5-m)*self.el.lambdax_()
                        n1=(1.9-0.1*m)-0.02*(6-m)*self.el.lambdax_()
                    if 5<m and m<=20: 
                        n025=1.2
                        n05=1.25
                        n1=1.4-0.02*self.el.lambdax_()
                if self.el.lambdax_()>5:
                    n025=1.2
                    n05=1.25
                    n1=1.3
                afaw=self.pr.afaw ()
#                print 'afaw - ', afaw
#                print 'n025', n025
#                print 'n05 ', n05
#                print 'n1', n1
#                print 'lambdax', self.el.lambdax_()
                
                if 0.25<=afaw and afaw<=0.5:
                    n=(n05-n025)/(0.5-0.25)*(afaw-0.25)+n025
                if 0.5<=afaw and afaw<=1:
                    n=(n1-n05)/(1-0.5)*(afaw-0.5)+n05
                if afaw>1:   
                    n=n1

            if typ==2:
                if m<0.1:
                    m=0.1
#                print 'm', m
#                print 'lambday_', self.el.lambday_()
                if self.pr.title()=='dvut':                
                    if 0<=self.el.lambday_() and self.el.lambday_()<=5:      
                        if 0.1<=m and m<=5:
                            n025=(0.75+0.05*m)+0.01*(5-m)*self.el.lambday_()
                            n05=(0.5+0.1*m)+0.02*(5-m)*self.el.lambday_()
                            n1=(0.25+0.15*m)+0.03*(5-m)*self.el.lambday_()
                        if 5<m and m<=20: 
                            n025=1.0
                            n05=1.0
                            n1=1.0
                    if self.el.lambday_()>5:
                        n025=1.0
                        n05=1.0
                        n1=1.0
                if self.pr.title()=='korob':
                    if 0<=self.el.lambday_() and self.el.lambday_()<=5:      
                        if 0.1<=m and m<=5:
                            n025=(1.45-0.05*m)-0.01*(5-m)*self.el.lambday_()
                            n05=(1.75-0.1*m)-0.02*(5-m)*self.el.lambday_()
                            n1=(1.9-0.1*m)-0.02*(6-m)*self.el.lambday_()
                        if 5<m and m<=20: 
                            n025=1.2
                            n05=1.25
                            n1=1.4-0.02*self.el.lambday_()
                    if self.el.lambday_()>5:
                        n025=1.2
                        n05=1.25
                        n1=1.3
                            
                            
#                print 'afaw - ', self.el.profile.s()*(self.el.profile.h()-2*self.el.profile.t())/(2*self.el.profile.t()*self.el.profile.b())
#                print 'n025', n025
#                print 'n05 ', n05
#                print 'n1', n1
#                print 'lambdax', self.el.lambday_()
                
                
                if self.pr.title()=='korob':                                         
                    afaw=self.pr.h()/(self.pr.b()-2*self.pr.s())/2
                if self.pr.title()=='dvut':  
                    afaw=1/(2*self.pr.afaw())                    
                if 0.25<=afaw and afaw<=0.5:
#                    print n05
                    n=(n05-n025)/(0.5-0.25)*(afaw-0.25)+n025
                if 0.5<afaw and afaw<=1:
                    n=(n1-n05)/(1-0.5)*(afaw-0.5)+n05
                if afaw>1:   
                    n=n1   
        return n
        

            
    def c(self):
            
        e=self.force.mx/self.force.n
        mx=self.pr.a()/self.pr.wx()*e
        
        if self.pr.title()=='dvut':
            c_max=self.c_max()
        if self.pr.title()=='korob':
            c_max=1
       
            
        if mx<=5:
            c=self.b_c()/(1+self.a_c(mx)*mx)
            if c>1:
                c=1            
        if mx>=10:
            c=1/(1+mx*self.phiy()/self.phi_b(typ=1, typ1=2, typ2=3, typ3=1))
        if 5<mx and mx<10:
            c5=self.b_c()/(1+self.a_c(5)*5)
            if c5>1:
                c5=1
            c10=1/(1+10*self.phiy()/self.phi_b(typ=1, typ1=2, typ2=3, typ3=1))
            c=c5*(2-0.2*mx)+c10*(0.2*mx-1)
#            print 'c5', c5, 'c10', c10
        if self.el.lambday_()>3.14 and c>c_max:
            c=c_max
        if c>1:
            c=1
#        print c
        return c, c_max, mx
                
            
            
    def a_c(self, mx):
        if mx<=1:
            a_c=0.7
        if 1<mx and mx<=5:
            a_c=0.65+0.05*mx
        return a_c
    def b_c(self):
#        print self.el.lambday_()
        if self.el.lambday_()<=3.14:
            b_c=1
        if self.el.lambday_()>3.14:
            b_c=(self.phi_n(lambda_=3.14, typ=0)/self.phiy())**0.5
        return b_c

                
    def c_max(self):
        w=0.25
#        print w
        a=0.
#        b=0.
        h=self.pr.h()-self.pr.t()
        p=(self.pr.jx()+self.pr.jy())/(self.pr.a()*h**2)+a**2
#        print 'p',p
#        print 'self.el.lambday_()',self.el.lambday()        
        jt=self.pr.jt()/1.3
#        print 'jt', jt
        mu=8*w+0.156*jt*self.el.lambday()**2/(self.pr.a()*h**2)
#        print 'mu', mu
        ex=self.force.mx/self.force.n
#        print 'ex', ex
#        bb=1
#        print 'bb', bb
        delta=4*p/mu
#        print 'delta', delta
        cmax=2./(1.+delta+((1-delta)**2+16/mu*(a-ex/h)**2)**0.5)
#        print cmax
        return cmax
            
    def phi_exy(self):
        c=self.c()[0]
        phi_ey=self.phi_e(typ=2)[0]
#        print 'c', c
#        print 'phi_ey', phi_ey
        phi_exy=phi_ey*(0.6*c**(1./3)+0.4*c**(1./4))
        return phi_exy, phi_ey, c
            
     
    #typ - 1 в главной плоскости, 2- в другой
    def local_buckl_h_ne_old(self, typ, typ1):
     
        #тайп - направление момента
        #тайп1 - учет ребер
        ex=self.force.mx/self.force.n
        ey=self.force.my/self.force.n
        mx=self.pr.a()/self.pr.wx()*ex
        my=self.pr.a()/self.pr.wy()*ey
        lambdax_=self.el.lambdax_()
        lambday_=self.el.lambday_()
        lambda_=self.el.lambda_() [0] 
#        print  self.element.steel.ry()     
        if typ==1:
            
            lambda1_=lambdax_
            m=mx
            if self.c()[0]*self.phiy()<=self.phi_e(1)[0]:
                if lambdax_>lambday_:
                    lambda1_=lambday_
        if typ==2:
            lambda1_=lambday_
            m=my
#        print m
        if self.pr.title()=='dvut':
            lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
        if  self.pr.title()=='korob':
            if typ==1:
                lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
            if typ==2:
                lambda_w=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
        
        if self.pr.title()=='dvut':
            if lambda_<2:
                lambda_uw0=1.3+0.15*lambda_**2
            else:
                lambda_uw0=1.2+0.35*lambda_
                if lambda_uw0>2.3:
                    lambda_uw0=2.3

        if self.pr.title()=='korob':
            if lambda_<1:
                lambda_uw0=1.2
            else:
                lambda_uw0=1.0+0.2*lambda_
                if lambda_uw0>1.6:
                    lambda_uw0=1.6
        
        if lambda1_<2:
            lambda_uw1=1.3+0.15*lambda1_**2
        else:
            lambda_uw1=1.2+0.35*lambda1_
            if lambda_uw1>3.1:
                lambda_uw1=3.1
        
#        print 'lambda_uw1', lambda_uw1
#        print 'lambda_uw0', lambda_uw0
#        print 'm', m
        
        if m==0:
            lambda_uw=lambda_uw0
        if m>1:
#            print 'tyt'
            lambda_uw=lambda_uw1
        if m>0 and m<=1:
            lambda_uw=(lambda_uw1-lambda_uw0)/(1)*(m)+lambda_uw0
#            print 'lambda_uw', lambda_uw
        
#
#        if mx<s>0:
#            print 'self.c()[0]*self.phiy()', self.c()[0]*self.phiy()
#            print 'self.phi_e(1)[0]', self.phi_e(1)[0]
#            print 'lambda1_', lambda1_
#            print 'lambda_', lambda_
#            print 'm', m
#            print 'lambda_uw', lambda_uw1
#            print 'lambda_uw0', lambda_uw0
        if (typ==1 and (mx<0 or mx>0) and self.c()[0]*self.phiy()<=self.phi_e(1)[0]):
#            print 'tyt'
#                print 'self.c()[0]', self.c()[0]
#                print 'self.phiy()', self.phiy()
#                print 'self.phi_e(1)[0]', self.phi_e(1)[0]    
   
            ry=self.el.steel.ry()

            e=self.el.steel.e()
            sigma=self.force.n/self.pr.a()+self.force.mx/self.pr.jx()*(self.pr.h()/2-self.pr.t1()-self.pr.t2())
            sigma1=self.force.n/self.pr.a()-self.force.mx/self.pr.jx()*(self.pr.h()/2-self.pr.t1()-self.pr.t2())
            a=(sigma-sigma1)/sigma
            
            if self.pr.title()=='dvut':
                tau=self.force.qx/(self.pr.s()*(self.pr.hw()))
            if self.pr.title()=='korob':
                tau=self.force.qx/(self.pr.s()*(self.pr.hw()))/2
                
            lambda_uw05=lambda_uw
            
            beta=1.4*(2*a-1)*tau/sigma
           
            if a>0.5:
                lambda_uw1=4.35*((2*a-1)*e/(2-a+(a**2+4*beta**2)**0.5)/sigma)**0.5*(ry/e)**0.5
#            print 'tut', lambda_uw1  
#            print 'a', a
#            print 'tau', tau
#            print 'beta', beta

            if lambda_uw1>3.8:
                lambda_uw1=3.8
                
#            print 'tyt'
#            print a
#            print lambda_uw1
#            print lambda_uw05
#            
            if a<=0.5:
                lambda_uw=lambda_uw05
            if a>=1:
                lambda_uw=lambda_uw1
            if a>0.5 and a<1:

                lambda_uw=(lambda_uw1-lambda_uw05)/(1-0.5)*(a-0.5)+lambda_uw05
        
        if typ1==1 and lambda_uw>2.3:
            lambda_uw=2.3
              
        if lambda_uw>=lambda_w:
            check=0
        else:
            check=1
                
        return check, lambda_uw, lambda_w          
                        
        
        
    
    def local_buckl_h_ne(self, typ, typ1, typ2=1, typ3=0):
    #typ - направление момента
    #typ1- учет 2.3 
    #typ2=1 - в запас расчета
    #typ3=0 - по п.9.4.3., если 1 или 2 просто достает значения
    #без ребер "простая" проверка
        ex=self.force.mx/self.force.n
        ey=self.force.my/self.force.n
        mx=self.pr.a()/self.pr.wx()*ex
        my=self.pr.a()/self.pr.wy()*ey
        lambdax_=self.el.lambdax_()
        lambday_=self.el.lambday_()
#        print mx
        def lambda_uw11(typ):
            if lambda_<2:
                lambda_uw110=1.3+0.15*lambda_**2
            if lambda_>=2:
                lambda_uw110=1.2+0.35*lambda_
                if lambda_uw110>3.1:
                    lambda_uw110=3.1
            lambda_uw0=self.local_buckl_h_n(typ)[1]
            if typ2==1:
                lambda_uw20=self.local_buckl_h_m2()[3]
            else:
                lambda_uw20=self.local_buckl_h_m2()[2]                
#            print mx, 'mx'
            if 1<=mx and mx<=10:
                lambda_uw=lambda_uw110
            if 0<mx and mx<1:
#                print 'lambda_uw110', lambda_uw110
#                print 'lambda_uw0', lambda_uw0
                lambda_uw=(lambda_uw110-lambda_uw0)/(1.-0.)*(mx-0.)+lambda_uw0
            if 10<mx and mx<=20:
#                print 'lambda_uw110', lambda_uw110
#                print 'lambda_uw20', lambda_uw20
#                print 'mx', mx                
                if lambda_uw20==0:
                    lambda_uw=0
                else:
                    lambda_uw=(lambda_uw20-lambda_uw110)/(20.-10.)*(mx-10.)+lambda_uw110
                    
            if mx>20:
                lambda_uw=lambda_uw20
#            print lambda_uw, "tut"
            return lambda_uw
#        print self.c()[0], self.phiy(), self.phi_e(1)[0]



        if (self.pr.title()=='korob' and typ3<>2) or (self.pr.title()=='dvut' and typ==1 and self.c()[0]*self.phiy()>self.phi_e(1)[0]) or typ3==1:
#            print 'tut1'
#            if typ==1 or typ3==1:
            if typ==1:
                lambda_=lambdax_
                lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        

            if typ==2:
                lambda_=lambday_    
                lambda_w=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
                
            if self.pr.title()=='korob':
                typ_uw11=typ
            if self.pr.title()=='dvut'or typ3==1:
                typ_uw11=3
#            print 'lambda_', lambda_
            lambda_uw=lambda_uw11(typ_uw11)
#            print lambda_uw, "tut2"
        if (self.pr.title()=='dvut' and (typ==2 or (typ==1 and self.c()[0]*self.phiy()<=self.phi_e(1)[0]))) or typ3==2:
            lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        

            if typ==1 and self.pr.title()=='korob':
                lambda_=lambdax_
                lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        

            if typ==2 and self.pr.title()=='korob':
                lambda_=lambday_    
                lambda_w=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
            
            if self.pr.title()=='dvut':
                lambda_=lambdax_

#            print 'tyt 1'
            if typ==2 and typ3<>1 and typ3<>2:
            
#                print self.pr.a(), self.el.steel.ry(), self.yc(), self.force.n
                lambda_uw1=2*(self.pr.a()*self.el.steel.ry()*self.yc()/self.force.n)**0.5
                if lambda_uw1>5.5:
                    lambda_uw1=5.5
                lambda_uw0=self.local_buckl_h_n()[1]
#                print my
                if my>=1:
                    lambda_uw=lambda_uw1
                else:
                    lambda_uw=(lambda_uw1-lambda_uw0)/(1-0)*(my-0)+lambda_uw0
#                    print 'tyt 1', 'lambda_uw1', lambda_uw1, 'lambda_uw0', lambda_uw0
#                print lambda_uw
            if (typ==1 and self.c()[0]*self.phiy()<=self.phi_e(1)[0]) or typ3==2:
#                print 'self.c()[0]', self.c()[0]
#                print 'self.phiy()', self.phiy()
#                print 'self.phi_e(1)[0]', self.phi_e(1)[0]    
                
                ry=self.el.steel.ry()
                yc=self.yc()
                
                if typ==1:
                    sigma1=self.force.n/self.pr.a()+self.force.mx/self.pr.jx()*(self.pr.h()/2-self.pr.t1()-self.pr.t2())
                    sigma2=self.force.n/self.pr.a()-self.force.mx/self.pr.jx()*(self.pr.h()/2-self.pr.t1()-self.pr.t2())
                    tau=self.force.qx/(self.pr.s()*(self.pr.hw()))
                if typ==2:
                    sigma1=self.force.n/self.pr.a()+self.force.my/self.pr.jy()*(self.pr.b()/2-self.pr.t1()-self.pr.t2())
                    sigma2=self.force.n/self.pr.a()-self.force.my/self.pr.jy()*(self.pr.b()/2-self.pr.t1()-self.pr.t2())
                    tau=self.force.qx/(self.pr.s()*(self.pr.bw()))
                if  self.pr.title()=='korob':
                    tau=tau/2
                    
                a=(sigma1-sigma2)/sigma1

#                print 'a',a
#                print 'tau', tau     
                
                def lambda_uw22(ar):
#                    print ar
                    c_cr_table=tables_csv('c_cr.csv', 'float_all')
                    c_cr=c_cr_table.get_interpolate(ar, 2)
                    
#                    print c_cr
                    b=0.15*c_cr*tau/sigma1
                    lambda_uw=1.42*(c_cr*ry*yc/(sigma1*(2-ar+(ar**2+4*b**2)**0.5)))**0.5
                    if lambda_uw>0.7+2.4*ar:
                        lambda_uw=0.7+2.4*ar
                    return lambda_uw, c_cr
                
                lambda_uw12=lambda_uw22(a)[0]
              
                lambda_uw1=lambda_uw22(1)[0]                 

                lambda_uw05=self.local_buckl_h_n()[1]
                

                lambda_uwt05=lambda_uw11(3)
#                print lambda_uwt05,'lambda_uwt05'
#                print 'lambda_uw05', lambda_uw05 
                if lambda_uw05>lambda_uwt05:
                    lambda_uw05=lambda_uwt05
                    
#                print 'lambda_uw12', lambda_uw12
               
#                print 'lambda_uw1', lambda_uw1  
#                print 'a', a
                                
                if 1<=a and a<=2:
                    lambda_uw=lambda_uw12
                if 0.5<a and a<1:
                    lambda_uw=(lambda_uw1-lambda_uw05)/(1-0.5)*(a-0.5)+lambda_uw05
                if a<0.5:
                    lambda_uw=lambda_uw05

#        print lambda_uw  
        if typ1==1 and typ3==0 and lambda_uw>2.3:
            lambda_uw=2.3
              
        if lambda_uw>=lambda_w:
            check=0
        else:
            check=1
                
        return check, lambda_uw, lambda_w   

    def local_buckl_h_ne_ut(self, typ, typ1, typ2=1):
    #typ - направление момента
    #typ1- учет 2.3 
    #typ2=1 - в запас расчета
    #без ребер "простая" проверка
        if (typ==1 and self.pr.title()=='dvut') or self.pr.title()=='korob':
            if self.c()[0]*self.phiy()>self.phi_e(1)[0] or self.pr.title()=='korob':
#                print self.force.n
#                print self.phi_e(typ=1)
                k=self.force.n/(self.phi_e(typ=typ)[0]*self.element.steel.ry()*self.yc()*self.element.profile.a())
                lambda_uw1=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2, typ3=1)[1]    
                lambda_uw2=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2, typ3=2)[1]
                lambda_w=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2, typ3=2)[2]
#                print 'lambda_uw1', lambda_uw1
#                print 'lambda_uw2', lambda_uw2
#                print 'lambda_w', lambda_w
#                print 'k', k
                
                if 0.8<=k and k<=1:
                    lambda_uw=lambda_uw1+5*(lambda_uw2-lambda_uw1)*(1-k)
                if k<0.8:
                    lambda_uw=lambda_uw2
            else:
                lambda_uw=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2, typ3=1)[1]    
                lambda_w=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2, typ3=1)[2]
        if typ==2 and self.pr.title()=='dvut':
            lambda_uw=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2)[1]    
            lambda_w=self.local_buckl_h_ne(typ=typ,typ1=0,typ2=typ2)[2]  
            
        if typ1==1:
            lambda_uw=2.3
              
        if lambda_uw>=lambda_w:
            check=0
        else:
            check=1
                
        return check, lambda_uw, lambda_w  
                
    def local_buckl_b_ne_old(self):
        return self.local_buckl_b_n_old() 
            
    def local_buckl_b_ne(self, typ, typ2=1): 
#typ2=1 - в запас расчета

        ex=self.force.mx/self.force.n
        ey=self.force.mx/self.force.n
        mx=self.pr.a()/self.pr.wx()*ex
        my=self.pr.a()/self.pr.wy()*ey
#        print 'mx', mx
#        print 'my', my
#
#        print 'self.el.lambdax_()', self.el.lambdax_()
#        print 'self.el.lambday_()', self.el.lambday_()
        
        lambdax_=self.el.lambdax_()
        if lambdax_<=0.8:
            lambdax_=0.8
        if lambdax_>4:
            lambdax_=4
            
        lambday_=self.el.lambday_() 

        if lambday_<=0.8:
            lambday_=0.8
        if lambday_>4:
            lambday_=4
            
        lambda_ufc=self.local_buckl_b_n()[1]
        if self.pr.title()=='korob' or (self.pr.title()=='dvut' and typ==1):
            if typ==1:
                m=mx
                lambda_=lambdax_
                lambda_f=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5                        

            if typ==2:
                m=my
                lambda_=lambday_ 
                lambda_f=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
            
            #нет тестов вот тут
            if self.pr.title()=='dvut':            
                if self.c()[0]*self.phiy()<=self.phi_e(1)[0] or self.force.n/(self.pr.a()*self.phi_e(1)[0]*self.element.steel.ry()*self.yc())<0.8:
                    lambda_uf20=self.local_buckl_b_m()[1]
                else:
                    if typ2==1:
                        lambda_uf20=self.local_buckl_b_m2(1)[1]
                    else:
                        lambda_uf20=self.local_buckl_b_m2(2)[1]                    
            if self.pr.title()=='korob':
                if  self.phi()<=self.phi_e(1)[0] or self.force.n/(self.pr.a()*self.phi_e(1)[0]*self.element.steel.ry()*self.yc())<0.8:
                    lambda_uf20=self.local_buckl_b_m()[1]
                else:
                    if typ2==1:
                        lambda_uf20=self.local_buckl_b_m2(1)[1]
                    else:
                        lambda_uf20=self.local_buckl_b_m2(2)[1]  
                        
            
            if self.pr.title()=='korob':
                lambda_uf1=lambda_ufc-0.01*(5.3+1.3*lambda_)*m
                lambda_uf5=lambda_ufc-0.01*(5.3+1.3*lambda_)*5
            if self.pr.title()=='dvut':
                lambda_uf1=lambda_ufc-0.01*(1.5+0.7*lambda_)*m
                lambda_uf5=lambda_ufc-0.01*(1.5+0.7*lambda_)*5
            if 0<=mx and mx<=5:
                lambda_uf=lambda_uf1
            if 5<=mx and mx<=20:
#                print 'lambda_uf20', lambda_uf20
#                print 'lambda_uf5', lambda_uf5
#                print 'lambda_ufc', lambda_ufc                
                lambda_uf=(lambda_uf20-lambda_uf5)/(20-5)*(mx-5)+lambda_uf5
                if lambda_uf20==0:
                    lambda_uf=0
                    
        if self.pr.title()=='dvut' and typ==2:
            lambda_uf=0.36+0.1*lambday_
            lambda_f=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
            
        if lambda_uf>=lambda_f:
            check=0
        else:
            check=1
            
        return check, lambda_uf, lambda_f
        
class simple_ferma(snipn):
    def add_data(self):
        lst=[u'yc', u'lx, м', u'ly, м']
        return  lst   
    def output_data(self):
        lst=[]
        #Исходные данные:
        yu=self.yu()
        commentyu=u'п.4'
        
        a=self.pr.a()
        commenta=u'A, см2'
        
        ix=self.pr.ix()
        commentix=u'ix, см'

        iy=self.pr.iy()
        commentiy=u'iy, см'

        lambdax=self.element.lambdax()
        commentlx=u'lambdax'
        
        lambday=self.element.lambdax()
        commently=u'lambday'

        ry=self.element.steel.ry()
        commentry=u'Ry, кг/см2'        
        lst=[[yu, commentyu],
             [ry, commentry],
             [a, commenta],
             [ix, commentix],
             [iy, commentiy],
             [lambdax, commentlx],
             [lambday, commently]]
        return lst
        
    def output_data_snip_old_global(self):
        lst=[]        
        #Расчет на расстяжение
        n1=self.pr.a()*self.element.steel.ry()*self.yc()
        comment1=u'N=An*Ry*yc (п.5.1. (5))'         

        n2=self.pr.a()*self.element.steel.ru()*self.yc()/self.yu()
        comment2=u'N=A*Ru*yc/yu (п.5.2. (6))'         

        if n1<n2:
            nmin=n1
        else:
            nmin=n2
        commentnmin='min(п.5.1,п.5.2)'
        #сжатие:
        phix_old=self.phix_old()
        commentpx=u'phix (п.5.3.)'

        phiy_old=self.phiy_old()
        commentpy=u'phiy (п.5.3.)'

        n3=self.nminus_old
        comment3=u'N=An*Ry*yc*phi (п.5.3. (7))'

        lst=[[n3, comment3],
             [nmin,commentnmin],
             [phix_old, commentpx],
             [phix_old, commentpy],
             [n1, comment1],
             [n2, comment2]]
             
        if self.element.lx()!=self.element.lfact() :
            q_ficmaxx=self.q_fic_old(n3,phix_old)
            commentqx=u'п.5.8. (23)'
            lst.append(list(q_ficmaxx, commentqx))
        if self.element.ly()!=self.element.lfact() :
            q_ficmaxy=self.q_fic_old(n3,phiy_old)
            commentqy=u'п.5.8. (23)'
            lst.append(list(q_ficmaxy, commentqy))
            
        if self.pr.title0()=='sostav':
            if self.pr.title()=='ugol_tavr_st_up' or self.pr.title()=='ugol_tavr_st_right':
                ix=self.pr.pr1.ix()
                ixplus=80*ix
                ixminus=40*ix
                
                lst.append(list(ixplus,u'Шаг планкок (+) (п.5.7.), см'))
                lst.append(list(ixminus,u'Шаг планкок (-) (п.5.7.), см'))

            if self.pr.title()=='ugol_tavr_st_krest':
                iy0=self.pr.pr1.iy0()
                ixplus=80*iy0
                ixminus=40*iy0
                
                lst.append(list(ixplus,u'Шаг планкок (+) (п.5.7.), см'))
                lst.append(list(ixminus,u'Шаг планкок (-) (п.5.7.), см'))
        return lst

    def output_data_snip_n_global(self):
        lst=[]        
        #Расчет на расстяжение
        n1=self.pr.a()*self.element.steel.ry()*self.yc()
        comment1=u'N=An*Ry*yc (п.7.1.1 (5))'         

        n2=self.pr.a()*self.element.steel.ru()*self.yc()/self.yu()
        comment2=u'N=A*Ru*yc/yu (п.7.1.1 )'         

        if n1<n2:
            nmin=n1
        else:
            nmin=n2
        commentnmin='min(п.7.1.1)'
        #сжатие:
        
        phix, typx=self.phix()
        commentpx=u'phix (п.7.1.3)'
        comment_typx=u'Тип сечения Х'
        
        phiy, typy=self.phiy()
        commentpy=u'phiy (п.7.1.3)'
        comment_typy=u'Тип сечения Y'

        n3=self.nminus
        comment3=u'N=An*Ry*yc*phi (п.п.7.1.3 (7))'

        lst=[[n3, comment3],
             [nmin,commentnmin],
             [phix, commentpx],
             [phix, commentpy],
             [typx, comment_typx],
             [typy, comment_typy],
             [n1, comment1],
             [n2, comment2]]
             
        if self.element.lx()!=self.element.lfact() :
            q_ficmaxx=self.q_fic(n3,phix)
            commentqx=u'п.7.2.7 (18)'
            lst.append(list(q_ficmaxx, commentqx))
        if self.element.ly()!=self.element.lfact() :
            q_ficmaxy=self.q_ficd(n3,phiy)
            commentqy=u'п.7.2.7 (18)'
            lst.append(list(q_ficmaxy, commentqy))
            
        if self.pr.title0()=='sostav':
            if self.pr.title()=='ugol_tavr_st_up' or self.pr.title()=='ugol_tavr_st_right':
                ix=self.pr.pr1.ix()
                ixplus=80*ix
                ixminus=40*ix
                
                lst.append(list(ixplus,u'Шаг планкок (+) (п.7.2.6), см'))
                lst.append(list(ixminus,u'Шаг планкок (-) (п.7.2.6), см'))

            if self.pr.title()=='ugol_tavr_st_krest':
                iy0=self.pr.pr1.iy0()
                ixplus=80*iy0
                ixminus=40*iy0
                
                lst.append(list(ixplus,u'Шаг планкок (+) (п.7.2.6), см'))
                lst.append(list(ixminus,u'Шаг планкок (-) (п.7.2.6), см'))
        return lst
                

                
    def output_data_snip_old_local(self):
        return 0
    def output_data_snip_n_local(self):
        return 0

    def nminus(self):
        n=self.pr.a()*self.element.steel.ry()*self.yc()*self.phi()
        return n

    def nplus(self):
        return self.nplus_old
        
    def nminus_old(self):
        n=self.pr.a()*self.element.steel.ry()*self.yc()*self.phi_old()
        return n
        
    def nplus_old(self):
        n1=self.pr.a()*self.element.steel.ry()*self.yc()

        n2=self.pr.a()*self.element.steel.ru()*self.yc()/self.yu()

        if n1<n2:
            nmin=n1
        else:
            nmin=n2
        return nmin                            
        
#        def el_ferm_simple(self):
##нет тестов
#            n=self.force.n
#            phi_nx=self.phix()
#            phi_ny=self.phiy()
#            if n>=0:
#                messege_general="Центральное расстяжение"
#                if self.elem.steel.ryn<=440:
#                    n_ultx=self.pr.a()*self.elem.steel.ry()*self.yc()
#                else:
#                    n_ultx=self.pr.a()*self.elem.steel.ru()*self.yc() /self.elem.steel.yu()                  
#                n_ulty=n_ultx
#                phi_nx=1
#                phi_ny=1
#            if n<0:
#                messege_general="Центральное сжатие"
#                n_ultx=self.pr.a()*self.elem.steel.ry()*self.yc()*phi_nx
#                n_ultx=self.pr.a()*self.elem.steel.ry()*self.yc()*phi_nx
#            
#            local_buckl_h_n=self.local_buckl_h_n()
#            local_buckl_b_n=self.local_buckl_b_n()            
#            
#            kx_general=n/n_ultx
#            ky_general=n/n_ulty            
#            if kx_general<1 and  ky_general<1 and local_buckl_h_n[0]==0 and local_buckl_b_n[0]==0:
#                check=0
#            else:
#                check=1               
#            
#            return check, messege_general, kx_general, ky_general, n, n_ultx, n_ulty, phi_nx, phi_ny,  local_buckl_h_n[0], local_buckl_h_n[1], local_buckl_h_n[2],  local_buckl_b_n[0], local_buckl_b_n[1], local_buckl_b_n[2]
#            
#        def el_beam_simple(self, clas):
#            mx=self.force.mx
#            my=self.force.my
#            qx=self.force.qx
#            qy=self.force.qy
#            w=self.force.w            
#            if clas==1:
#                return 0
#            if clas==2:
#                return 0
#            return 0
#        def el_column_simple(self):
#            return 0
#        def el_beam_cran(self):
#            return 0
#        def el_ferm_sostav(self):
#            return 0