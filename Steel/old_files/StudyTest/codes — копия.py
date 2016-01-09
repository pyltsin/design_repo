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
    def __init__(self, n=0, mx=0, my=0, w=0, qx=0, qy=0, t=0, sr=0, floc=0, lstForce=[]):
        force.n=n
        force.mx=mx
        force.my=my 
        force.w=w  
        force.qx=qx  
        force.qy=qy 
        force.t=t
        force.sr=sr  
        force.floc=floc
        force.lstForce=lstForce
              
class normes(object):
    def __init__(self, element, forces, yc, ycb=0):
        self.element=element
        self.el=self.element
        self.force=forces
        self.__yc=yc
        self.__ycb=ycb
        self.pr=self.element.profile
    def yc(self):
        if type(self.__yc)==type([""]):
            return self.__yc[0]
        else:
            return self.__yc
    def yc1(self):
        return self.__yc[0]        
    def yc2(self):
        return self.__yc[1]
    def ycb(self):
        return self.__ycb          


class snipn(normes):
    def yu(self):
        """Коэффициент надежности по материалу для Ru, принимается 1.3"""
        return 1.3
    def phi_n(self, lambda_, typ=0, typ_s=0):
        """Вычисление коэффициента продольной устойчивости по новому снипу.
        Реализованы сечения:
            - короб, труба
            - двутавр, уголки в крест, в тавр
        Входные данные:
            lambda_ - гибкость приведенная
            typ - направление плоскости (typ=1 - в плоскости стенки двутавра)
        Выходные данные: phi, тип сечения"""
        #typ = 1 - в плоскости стенки
        if typ_s==0:
            if self.pr.title()=='korob' or self.pr.title()=='ring':       
                typ_sec='a'
            if self.pr.title()=='dvut' or self.pr.title()=='ugol_tavr_st_krest' :
                typ_sec='b'
            if self.pr.title()=='dvut' and    self.pr.h()>500 and typ==1:
                typ_sec='a'
            if self.pr.title()=='ugol_tavr_st_right' or self.pr.title()=='ugol_tavr_st_up':               
                typ_sec='c'
        else:
            typ_sec=typ_s

           
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
        if lambda_!=0:
            delta=9.87*(1-a+b*lambda_)+lambda_**2
            phi_n=0.5*(delta-(delta**2-39.48*lambda_**2)**0.5)/lambda_**2
        else:
            phi_n=1
        
        if lambda_>c:
            if phi_n>7.6/lambda_**2:
                phi_n=7.6/lambda_**2
               
        if phi_n>1 or lambda_<0.4:
            phi_n=1

        if phi_n<0:
            phi_n=0

        
        return phi_n, typ_sec


            
    def phix(self):
        """Вычисление коэффициента продольной устойчивости относительно оси X по новому снипу.
        Реализованы сечения: аналогично phi_n
        Выходные данные:
            phi, typ_sec"""      
        return self.phi_n(self.element.lambdax_(), typ=1)
    def phiy(self):
        """Вычисление коэффициента продольной устойчивости относительно оси Y по новому снипу.
        Реализованы сечения: аналогично phi_n
        Выходные данные:
            phi, typ_sec"""
            
        return self.phi_n(self.element.lambday_(), typ=2)
        
    def phi(self):
        """Вычисление коэффициента продольной устойчивости по новому снипу.
        Направление выбирается автоматически
        Выходные данные: phi, тип сечения"""        
        phix=self.phix()[0]
        phiy=self.phiy()[0]
        if phix<phiy:
            return phix
        else:
            return phiy

    def phi_n_old(self, lambda_):
        """Вычисление коэффициента продольной устойчивости по старому снипу.
        Реализованы сечения: любые
        Входные данные:
            lambda_ - гибкость приведенная
        Выходные данные:
            phi"""

        ry=self.element.steel.ry()
        e=self.element.steel.e() 
        if 0<lambda_ and lambda_<=2.5:
            phi=1-(0.073-5.53*ry/e)*lambda_*lambda_**0.5
        if 2.5<lambda_ and lambda_<=4.5:
            phi=1.47-13*ry/e-(0.371-27.3*ry/e)*lambda_+(0.0275-5.53*ry/e)*lambda_**2
        if lambda_>4.5:
            phi=332/(lambda_**2*(51-lambda_))
        if lambda_==0:
            phi=1
            
        if phi<0:
            phi=0

        return phi
        
    def phix_old(self):
        """Вычисление коэффициента продольной устойчивости относительно оси X по старому снипу.
        Реализованы сечения: любые
        Выходные данные:
            phi"""
        return self.phi_n_old(self.element.lambdax_())

    def phiy_old(self):
        """Вычисление коэффициента продольной устойчивости относительно оси Y по старому снипу.
        Реализованы сечения: любые
        Выходные данные:
            phi"""

        return self.phi_n_old(self.element.lambday_())

    def phi_old(self):
        """Вычисление коэффициента продольной устойчивости по старому снипу.
        Автоматический выбор направления
        Реализованы сечения: любые
        Выходные данные:
            phi"""

        phix=self.phix_old()
        phiy=self.phiy_old() 
        if phix<phiy:
            return phix
        else:
            return phiy     
            

    def q_fic(self, n, phi):
        """Вычисление фиктивно силы закрепления по новому снипу - нет проверки
        Входные данные:
            n-продолная сила
            phi - коэффициент устойчивости
        Выходные:
            q_fic"""

        ry=self.element.steel.ry()
        e=self.element.steel.e() 
        q_fic=7.15*10**(-6)*(2330-e/ry)*n/phi
        return q_fic
    def q_fic_old(self, n, phi):
        """Вычисление фиктивно силы закрепления по старому снипу - нет проверки
        Входные данные:
            n-продолная сила
            phi - коэффициент устойчивости
        Выходные:
            q_fic"""
        return self.q_fic(n, phi)
            
            
    def local_buckl_h_n(self):
        """Расчет локальной устойчивости стенки центрально сжатых элементов по новому снип. 
        Расчет реализован для двутавров и прямоугольных коробов, сложных сечений из уголков.
        Расчет для уголков выполняется в запас без учета раскрепления планками.
        Входные данные:
        Выходные данные:
            check - коэффициент использования
            lambda_uw
            lambda_w"""
               
        if self.pr.title()=='dvut':
            lambda_=self.element.lambda_()[0]  
            if lambda_<=2:
#                print 'tut1'
                lambda_uw=1.3+0.15*lambda_**2
            else:
#                print 'tut2'
                lambda_uw=1.2+0.35*lambda_
                if lambda_uw>2.3:
#                    print 'tut3'
                    lambda_uw=2.3
        elif self.pr.title()=='korob':
            lambda_=self.el.lambday_()
            if lambda_<=1:
                lambda_uw=1.2
            else:
                lambda_uw=1.0+0.2*lambda_
                if lambda_uw>1.6:
                    lambda_uw=1.6
        elif self.pr.title()=='ugol_tavr_st_krest' or self.pr.title()=='ugol_tavr_st_right' or self.pr.title()=='ugol_tavr_st_up':
            lambda_=self.element.lambda_()[0]
            if lambda_<=0.8:
                lambda_=0.8
            if lambda_>=4:
                lambda_=4

            lambda_uw=0.4+0.07*lambda_ 

        elif self.pr.title()=='ring':
            lambda_uw=3.14/2

#        print 's', self.pr.hef(),self.pr.s()
        lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        
        check=lambda_w/lambda_uw
        return check, lambda_uw, lambda_w
     
        
    def local_buckl_b_n(self):

        """Расчет локальной устойчивости полки центрально сжатых элементов по новому снип. 
        Расчет реализован для двутавров и прямоугольных коробов, сложных сечений из уголков.
        Расчет для уголков выполняется в запас без учета раскрепления планками.
        Входные данные:
        Выходные данные:
            check - коэффициент использования
            lambda_uf
            lambda_f"""
           
        if self.pr.title()=='ugol_tavr_st_krest' or self.pr.title()=='ugol_tavr_st_right' or self.pr.title()=='ugol_tavr_st_up':
            lambda_=self.element.lambda_()[0]
            if lambda_<=0.8:
                lambda_=0.8
            if lambda_>=4:
                lambda_=4
            lambda_uf=0.4+0.07*lambda_            

        elif self.pr.title()=='dvut':
#            print 'tut1'
            lambda_=self.element.lambda_() [0]
            if lambda_<=0.8:
#                print 'tut2'
                lambda_=0.8
            if lambda_>=4:
                lambda_=4
#                print 'tut3'
#            print lambda_
            lambda_uf=0.36+0.1*lambda_
#            print lambda_uf

        elif self.pr.title()=='korob':
            lambda_=self.element.lambdax_() 

            if lambda_<=1:
                lambda_uf=1.2
            else:
                lambda_uf=1.0+0.2*lambda_
                if lambda_uf>1.6:
                    lambda_uf=1.6

        elif self.pr.title()=='ring':
            lambda_uf=3.14/2
    
        lambda_f=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5

        check=lambda_f/lambda_uf
        
        return check, lambda_uf, lambda_f
    
    def local_buckl_h_n_old(self):

        """Расчет локальной устойчивости стенки центрально сжатых элементов по старому снип. 
        Расчет реализован для двутавров и прямоугольных коробов, сложных сечений из уголков.
        Расчет для уголков выполняется в запас без учета раскрепления планками.
        Входные данные:
        Выходные данные:
            check - коэффициент использования
            lambda_uw
            lambda_w"""
            
            
        if self.pr.title()=='korob':
            lambda_=self.element.lambda_()[0]
            if lambda_<=1:
                lambda_uw=1.2
            else:
                lambda_uw=1.0+0.2*lambda_
                if lambda_uw>1.6:
                    lambda_uw=1.6

            lambda_w=self.pr.hef()/self.pr.s()*(self.element.steel.ry()/self.element.steel.e())**0.5                        

            check=lambda_w/lambda_uw

            return check, lambda_uw, lambda_w
        else:
            return self.local_buckl_h_n()




    def local_buckl_b_n_old(self):

        """Расчет локальной устойчивости полки центрально сжатых элементов по старому снип. 
        Расчет реализован для двутавров и прямоугольных коробов, сложных сечений из уголков.
        Расчет для уголков выполняется в запас без учета раскрепления планками.
        Входные данные:
        Выходные данные:
            check - коэффициент использования
            lambda_uf
            lambda_f"""

        if self.pr.title()=='korob':
            lambda_=self.element.lambda_()[0]

            if lambda_<=1:
                lambda_uf=1.2
            else:
                lambda_uf=1.0+0.2*lambda_
                if lambda_uf>1.6:
                    lambda_uf=1.6

            lambda_f=self.pr.bef()/self.pr.t()*(self.element.steel.ry()/self.element.steel.e())**0.5
    
            check=lambda_f/lambda_uf
            
            return check, lambda_uf, lambda_f
        else:

            return self.local_buckl_b_n()

    '''---------------------------------------------'''

        
    def local_buckl_h_m(self, typ1=1, typ2=1):
        '''Проверка местной устойчивости стенки в изгибаемом элементе по СП для балок 1-го класса. Расчет не выполняется - только по отношению h/t
        Входные данные - typ1 - 1 - вообще без ребер, 2 - c ребрами, которые ставятся конструктивно
        typ2 - 1 - без местной нагрузки, 2 - с местной нагрузкой.'''

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

        check=lambda_w/lambda_uw
        return check, lambda_uw, lambda_w  
    
    def local_buckl_h_m_old(self, typ1=1, typ2=1):
        '''Проверка местной устойчивости стенки в изгибаемом элементе по СНиП для балок 1-го класса. Расчет не выполняется - только по отношению h/t
        Входные данные - typ1 - 1 - вообще без ребер, 2 - c ребрами, которые ставятся конструктивно
        typ2 - 1 - без местной нагрузки, 2 - с местной нагрузкой.'''

        return self.local_buckl_h_m(typ1, typ2)  



    def local_buckl_b_m(self): 
        '''Проверка местной устойчивости полки в изгибаемом элементе по СП для балок 1-го класса.'''
        lambdaf=self.pr.bef()/self.pr.t()  /(self.element.steel.e()/self.element.steel.ry())**0.5                     
        if self.pr.title()=='dvut' or self.pr.title()=='shvel':
            lambdauf=0.5
        if self.pr.title()=='korob':
            lambdauf=1.5
        
        check=lambdaf/lambdauf
        return check, lambdauf, lambdaf

    def local_buckl_b_m_old(self):
        '''Проверка местной устойчивости полки в изгибаемом элементе по СНиП для балок 1-го класса. Расчет короба выполняется по СП,
        так как в СНиП нет указаний'''
        return self.local_buckl_b_m()     



    def cxcyn(self):
        '''расчет коэффициентов cx cy n по СП.
        Сечения - двутавр, швеллер, короб'''
        if self.pr.title()=='dvut':
            n=1.5
            cy=1.47
            if 0.25<=self.pr.afaw() and self.pr.afaw()<=0.5:
                cx=(1.12-1.19)/(0.5-0.25)*(self.pr.afaw()-0.25)+1.19
            if 0.5<=self.pr.afaw() and self.pr.afaw()<=1:
                cx=(1.07-1.12)/(1-0.5)*(self.pr.afaw()-0.5)+1.12

            if 1<=self.pr.afaw() and self.pr.afaw()<=2:

                cx=(1.04-1.07)/(2-1)*(self.pr.afaw()-1)+1.07
        elif self.pr.title()=='shvel':
            n=1
            cy=1.6
            afaw=1/self.pr.afaw()/2
            cx=1
            if 0.5<=afaw and afaw<=1:
                cx=(1.12-1.07)/(1-0.5)*(afaw-0.5)+1.07
            if 1<=afaw and afaw<=2:
                cx=(1.19-1.12)/(2-1)*(afaw-1)+1.12

        elif self.pr.title()=='korob':
            n=1.5
            if 0.25<=self.pr.afaw() and self.pr.afaw()<=0.5:
#                print 'tut1'

                cx=(1.12-1.19)/(0.5-0.25)*(self.pr.afaw()-0.25)+1.19
                cy=(1.12-1.07)/(0.5-0.25)*(self.pr.afaw()-0.25)+1.07
                 
            if 0.5<=self.pr.afaw() and self.pr.afaw()<=1:
                cx=(1.07-1.12)/(1-0.5)*(self.pr.afaw()-0.5)+1.12
                cy=(1.19-1.12)/(1-0.5)*(self.pr.afaw()-0.5)+1.12
#                print 'tut2'
                
            if 1<=self.pr.afaw() and self.pr.afaw()<=2:
                cx=(1.04-1.07)/(2-1)*(self.pr.afaw()-1)+1.07    
                cy=(1.26-1.19)/(2-1)*(self.pr.afaw()-1)+1.19
#                print 'tut3'

        return cx, cy, n   
    def cxcyn_old(self):
        '''расчет коэффициентов cx cy n по СНиП.
        Сечения - двутавр, швеллер, короб'''

        return self.cxcyn()





        
               
    def phi_b_old(self, typ, typ1, typ2, typ3):
        '''расчет устойчивости по СНиП 
        Профиля - двутавр, швеллер, короб
        Исходные данные:
            typ - 1- балка или 2-консоль
            typ1 - 1-без закреплений, 2-два и более, 3 - один по центру
            typ2 - 1 - сосредоточенная нагрузка в центре, 2 - сосредоточенная в четверти, 3 - равномерная
            typ3 - 1 - нагрузка приложена к сжатому поясу, 2- к расстянутому'''
        return self.phi_b(typ, typ1, typ2, typ3, 0)

        
    def phi_b(self, typ, typ1, typ2, typ3, typ4=1):
        '''расчет устойчивости по СП
        Профиля - двутавр, швеллер, короб
        Исходные данные:
            typ - 1- балка или 2-консоль
            typ1 - 1-без закреплений, 2-два и более, 3 - один по центру
            typ2 - 1 - сосредоточенная нагрузка в центре, 2 - сосредоточенная в четверти, 3 - равномерная
            typ3 - 1 - нагрузка приложена к сжатому поясу, 2- к расстянутому
            typ4 - 1-расчет по СП!!!'''
        pr=self.element.profile
        el=self.element
        if  self.element.lb()!=0:

            if pr.title()=='dvut' or pr.title()=='shvel':
    
                if pr.title2()=='prokat':
#                    print 'tut1'
                    if typ4==1:
                        jt=self.pr.jt_sp()
    #                    print 'jt', jt
                    if typ4!=1:
                        jt=self.pr.jt()
    
                        
                    a=1.54*jt/pr.jy()*(el.lb()/pr.h())**2
#                    print jt, pr.jy(),el.lb(), pr.h()
    #                print 'jy', pr.jy()
                else:
    #                print 'tut1'
                    h=self.pr.h()
                    t=self.pr.t()
                    s=self.pr.s()
                    b=self.pr.b()
                    h1=h-t                
                    a1=0.5*h1
                    a=8*(el.lb()*t/(h1*b))**2*(1+a1*s**3/(b*t**3))
            
    #            print a
                if typ==1:
                    if typ4==1:
                        psi=self.psib(a,typ1,typ2,typ3)
                    else:
                        psi=self.psib_old(a,typ1,typ2,typ3)                    
                if typ==2:
                    if typ4==1:
                        psi=self.psik(a, typ2, typ3)
                    else:
                        psi=self.psik_old(a, typ2, typ3)                    
                if pr.title2()=='prokat':
                    h_t=pr.h()
                else:
                    h_t=pr.h()-pr.t()
                phi1=psi*pr.jy()/pr.jx()*((h_t)/el.lb())**2*el.steel.e()/el.steel.ry()
                if pr.title()=='dvut' or pr.title()=='shvel':
                    if pr.title()=='shvel':
                        phi1=0.7*phi1
                    if phi1<=0.85:
                        phib=phi1
                    else:
                        phib=0.68+0.21*phi1
                        if phib>1:
                            phib=1

        if pr.title()=='korob' or el.lb()==0:
            phib=1
            phi1=1
            psi=1
            a=0
        
        return phib, phi1, psi, a
        
        
    def psib(self,a, typ1, typ2, typ3):
        '''Определение psi_k по СП
            a - коэффициент
            typ1 - 1-без закреплений, 2-два и более, 3 - один по центру
            typ2 - 1 - сосредоточенная нагрузка в центре, 2 - сосредоточенная в четверти, 3 - равномерная
            typ3 - 1 - нагрузка приложена к сжатому поясу, 2- к расстянутому'''

        psi=10**(-10)
        psi1=psi
#        print a
        if a<0.1:
            a=0.1
        
        if 0.1<=a and a<=40:
            psi1=2.25+0.07*a
        elif 40<a and a<=400:
            psi1=3.6+0.04*a-3.5*10**(-5)*a**2
        

        if typ1==1:
            if 0.1<=a and a<=40:
                if typ2==1 or typ2==2:
                    if typ3==1:
                        psi=1.75+0.09*a
#                        print 'tut1'
                    else:
                        psi=5.05+0.09*a
#                        print 'tut2'

                if typ2==3:
                    if typ3==1:
                        psi=1.6+0.08*a
#                        print 'tut3'

                    else:
                        psi=3.8+0.08*a
#                        print 'tut4'

            if 40<a and a<=400:
                if typ2==1 or typ2==2:
                    if typ3==1:
                        psi=3.3+0.053*a-4.5*10**(-5)*a**2
#                        print 'tut5'

                    else:
                        psi=6.6+0.053*a-4.5*10**(-5)*a**2
#                        print 'tut6'

                if typ2==3:
                    if typ3==1:
                        psi=3.15+0.04*a-2.7*10**(-5)*a**2
#                        print 'tut7'

                    else:
                        psi=5.35+0.04*a-2.7*10**(-5)*a**2
#                        print 'tut8'

        if typ1==2:
            psi=psi1
#            print 'tut9'

        if typ1==3:
            if typ2==1:
                psi=1.75*psi1
#                print 'tut10'

            if typ2==2:
                if typ3==1:
                    psi=1.14*psi1
#                    print 'tut11'

                if typ3==2:
                    psi=1.6*psi1
#                    print 'tut12'

            if typ2==3:
                if typ3==1:
                    psi=1.14*psi1
#                    print 'tut13'

                if typ3==2:
                    psi=1.3*psi1 
#                    print 'tut14'

        return psi
    def psik(self, a, typ2, typ3):
        '''Определение psi_b по СП
            a - коэффициент
            typ2 - 1 - сосредоточенная на конце, 2 - сосредоточенная в четверти, 3 - равномерная
            typ3 - 1 - нагрузка приложена к сжатому поясу, 2- к расстянутому'''

        if a<4:
            a=4

        psi=10**(-10)
        if typ2==1 or typ2==2:
            if typ3==1:
                if 4<=a and a<=28:
                    psi=6.2+0.08*a
#                    print 'tut15'

                if 28<=a and a<=100:
                    psi=7.+0.05*a
#                    print 'tut16'

            if typ3==2:
                if 4<=a and a<=28:
                    psi=1+0.16*a
#                    print 'tut17'

                if 28<=a and a<=100:
                    psi=4+0.05*a
#                    print 'tut18'

        if typ2==3:
            if typ3==2:
                psi=1.42*a**0.5
#                print 'tut19'

        return psi

    def psib_old(self,a, typ1, typ2, typ3):
        '''Определение psi_b по СНиП
            a - коэффициент
            typ1 - 1-без закреплений, 2-два и более, 3 - один по центру
            typ2 - 1 - сосредоточенная нагрузка в центре, 2 - сосредоточенная в четверти, 3 - равномерная
            typ3 - 1 - нагрузка приложена к сжатому поясу, 2- к расстянутому'''

        return self.psib(a,typ1, typ2, typ3)
    def psik_old(self, a, typ2, typ3):
        '''Определение psi_k по СНиП
            a - коэффициент
            typ2 - 1 , 2 - сосредоточенная на конце, 3 - равномерная
            typ3 - 1 - нагрузка приложена к сжатому поясу, 2- к расстянутому'''

        return self.psik(a, typ2, typ3)




    '''---------------------------------------------'''
    def phi_e(self, typ):
        '''определение phi_e для симметричных сечений  по СНиП и СП; выполняется учет phi>=phi_e
        входные данные - typ - 1- относительно оси X, 2- Y
        выходные - phi_e, mef, nau, lambda_'''
    
        mefm=self.mef(typ)
        mef=mefm[0]
        nau=mefm[1]
        if typ==1:
            lambda_=self.el.lambdax_()
        if typ==2:
            lambda_=self.el.lambday_()  
        phi_e=self.phi_etable(mef, lambda_)
        
#        print lambda_, typ
        phi=self.phi_n(lambda_,typ)[0]
#        print 'phi', phi,phi_e
        if phi<phi_e:
            phi_e=phi
#            print 'point 1'
        return phi_e, mef, nau, lambda_

    def phi_e_old(self, typ):
        mefm=self.mef_old(typ)
        mef=mefm[0]
        nau=mefm[1]
        if typ==1:
            lambda_=self.el.lambdax_()
        if typ==2:
            lambda_=self.el.lambday_()  
        phi_e=self.phi_etable_old(mef, lambda_)
        
        phi=self.phi_n_old(lambda_)
#        print 'phi', phi,phi_e

        if phi<phi_e:
            phi_e=phi
#            print 'point 2'
        return phi_e, mef, nau, lambda_

        
    def phi_etable(self, mef, lambda_):
        '''определение phi_e по табличным данным;
        входные данные - mef, lambda_
        выходные - phi'''
        
        mef=float(mef)
        lambda_=float(lambda_)
        if mef<0.1:
            mef=0.1
        if mef>20:
            mef=20
        if lambda_<0.5:
            lambda_=0.5
        if lambda_<14:
            
            table=tables_csv('SolveSteelData\\table_phi_n.csv', 'float_all')
            phi=table.get_interpolate(mef, lambda_)
        if lambda_>14:
            phi=1/10.**10
        phi=phi/1000.
        
        return phi

    def phi_etable_old(self, mef, lambda_):
        return self.phi_etable(mef, lambda_)
        
    def mef(self, typ):
        '''определение mef для симметричных сечений  по СНиП и СП
        входные данные - typ - 1- относительно оси X, 2- Y
        выходные -  mef, nau'''

        if typ==1:
            e=self.force.mx/self.force.n
            m=self.pr.a()/self.pr.wx()*e
        if typ==2:
            e=self.force.my/self.force.n
            m=self.pr.a()/self.pr.wy()*e
        nau=self.nau(m, typ)
        mef=nau*m
        return mef, nau

    def mef_old(self, typ):
        return self. mef(typ)  
              
    def nau(self, m, typ):
        '''определение nau для симметричных сечений  по СНиП и СП
        входные данные - typ - 1- относительно оси X, 2- Y
        m вводится в рамки - 0,1 - 20 
        выходные -  nau'''
        n=10**10
        n1=n
        if m<0.1:
            m=0.1
        elif m>20:
            m=20
        if self.pr.title()=='dvut' or self.pr.title()=='korob':
            if typ==1:            
                if 0<=self.el.lambdax_() and self.el.lambdax_()<=5:      
                    if 0.1<=m and m<=5:
#                        print 'point 1'
                        n025=(1.45-0.05*m)-0.01*(5-m)*self.el.lambdax_()
                        n05=(1.75-0.1*m)-0.02*(5-m)*self.el.lambdax_()
                        n1=(1.9-0.1*m)-0.02*(6-m)*self.el.lambdax_()
                    elif 5<m and m<=20: 
#                        print 'point 2'

                        n025=1.2
                        n05=1.25
                        n1=1.4-0.02*self.el.lambdax_()
                elif self.el.lambdax_()>5:
#                    print 'point 3'

                    n025=1.2
                    n05=1.25
                    n1=1.3
                afaw=self.pr.afaw ()
#                print 'afaw', afaw
#                print 'afaw - ', afaw
#                print 'n025', n025
#                print 'n05 ', n05
#                print 'n1', n1
#                print 'lambdax', self.el.lambdax_()
                if afaw<0.25:
                    afaw=0.25

                if 0.25<=afaw and afaw<=0.5:
#                    print 'point 4'

                    n=(n05-n025)/(0.5-0.25)*(afaw-0.25)+n025
                if 0.5<=afaw and afaw<=1:
#                    print 'point 5'

                    n=(n1-n05)/(1-0.5)*(afaw-0.5)+n05
                if afaw>1:   
                    n=n1
#                    print 'point 6'


            if typ==2:
#                print 'm', m
#                print 'lambday_', self.el.lambday_()
                if self.pr.title()=='dvut':                
                    if 0<=self.el.lambday_() and self.el.lambday_()<=5:      
                        if 0.1<=m and m<=5:
#                            print 'point 7'

                            n025=(0.75+0.05*m)+0.01*(5-m)*self.el.lambday_()
                            n05=(0.5+0.1*m)+0.02*(5-m)*self.el.lambday_()
                            n1=(0.25+0.15*m)+0.03*(5-m)*self.el.lambday_()
                        if 5<m and m<=20:
#                            print 'point 8'

                            n025=1.0
                            n05=1.0
                            n1=1.0
                    if self.el.lambday_()>5:
#                        print 'point 9'

                        n025=1.0
                        n05=1.0
                        n1=1.0
                if self.pr.title()=='korob':
                    if 0<=self.el.lambday_() and self.el.lambday_()<=5:      
                        if 0.1<=m and m<=5:
#                            print 'point 10'

                            n025=(1.45-0.05*m)-0.01*(5-m)*self.el.lambday_()
                            n05=(1.75-0.1*m)-0.02*(5-m)*self.el.lambday_()
                            n1=(1.9-0.1*m)-0.02*(6-m)*self.el.lambday_()
                        if 5<m and m<=20:
#                            print 'point 11'

                            n025=1.2
                            n05=1.25
                            n1=1.4-0.02*self.el.lambday_()
                    if self.el.lambday_()>5:
#                        print 'point 12'

                        n025=1.2
                        n05=1.25
                        n1=1.3
                            
                            
#                print 'afaw - ', self.el.profile.s()*(self.el.profile.h()-2*self.el.profile.t())/(2*self.el.profile.t()*self.el.profile.b())
#                print 'n025', n025
#                print 'n05 ', n05
#                print 'n1', n1
#                print 'lambdax', self.el.lambday_()
                
                
                if self.pr.title()=='korob':
#                    print 'point 13'
                                         
                    afaw=self.pr.h()/(self.pr.b()-2*self.pr.s())/2.
                elif self.pr.title()=='dvut':  
                    afaw=1/(2.*self.pr.afaw())  
#                    print 'point 14'
                if afaw<0.25:
                    afaw=0.25

                if 0.25<=afaw and afaw<=0.5:
#                    print n05
#                    print 'point 15'

                    n=(n05-n025)/(0.5-0.25)*(afaw-0.25)+n025
                elif 0.5<afaw and afaw<=1:
#                    print 'point 16'

                    n=(n1-n05)/(1-0.5)*(afaw-0.5)+n05
                elif afaw>1:
#                    print 'point 17'

                    n=n1   
        return n
    
    def nau_old(self, m, typ):
        return self.nau(m, typ)

            
    def c_old(self):
        """Определение коэффициента c по СНиП (формула 56)
        возвращает с, с_max, mx"""
        
        e=self.force.mx/self.force.n
        mx=self.pr.a()/self.pr.wx()*e
        
        if self.pr.title()=='dvut':
            c_max=self.c_max_old()
        if self.pr.title()=='korob':
            c_max=1
       
            
        if mx<=5:
            c=self.b_c_old()/(1+self.a_c_old(mx)*mx)
#            print 'c 1'
#            if c>1:
#                c=1            
        if mx>=10:
            c=1/(1+mx*self.phiy_old()/self.phi_b_old(typ=1, typ1=2, typ2=3, typ3=1)[0])
#            print self.phiy_old(), 'phi_y'
#            print 'c 2'
        if 5<mx and mx<10:
#            print 'c 3'
            c5=self.b_c_old()/(1+self.a_c_old(5)*5)
#            if c5>1:
#                c5=1
            c10=1/(1+10*self.phiy_old()/self.phi_b_old(typ=1, typ1=2, typ2=3, typ3=1)[0])
            c=c5*(2-0.2*mx)+c10*(0.2*mx-1)
#            print 'c5', c5, 'c10', c10
#        print 'c', c
        if self.el.lambday_()>3.14 and c>c_max:
            c=c_max
#        if c>1:
#            c=1
#        print c
        return c, c_max, mx
                
    def c(self):
        """Определение коэффициента c по СП (формула 111)
        возвращает с, с_max, mx
        Для mx<5 проверяется доп. условие C<1 (проверки нет - сложно поймать)"""
        
        e=self.force.mx/self.force.n
        mx=self.pr.a()/self.pr.wx()*e
        
        if self.pr.title()=='dvut':
            c_max=self.c_max()
        if self.pr.title()=='korob':
            c_max=1
       
            
        if mx<=5:
            c=self.b_c()/(1+self.a_c(mx)*mx)
#            print 'c 1'

            if c>1:
                c=1            
        if mx>=10:
            c=1/(1+mx*self.phiy()[0]/self.phi_b(typ=1, typ1=2, typ2=3, typ3=1)[0])
#            print 'c 2'

        if 5<mx and mx<10:
#            print 'c 3'

            c5=self.b_c()/(1+self.a_c(5)*5)
            if c5>1:
                c5=1
            c10=1/(1+10*self.phiy()[0]/self.phi_b(typ=1, typ1=2, typ2=3, typ3=1)[0])
            c=c5*(2-0.2*mx)+c10*(0.2*mx-1)
#            print 'c5', c5, 'c10', c10
        if self.el.lambday_()>3.14 and c>c_max:
            c=c_max
#        if c>1:
#            c=1
#        print c
        return c, c_max, mx

            
            
    def a_c_old(self, mx):
        """Определение a_c по СНиП"""
        if self.pr.title()=='korob':
            if mx<=1:
                a_c=0.6
            elif 1<mx and mx<=5:
                a_c=0.55+0.05*mx

        elif self.pr.title()=='dvut':
            if mx<=1:
#                print 'a_c 1'
                a_c=0.7
            elif 1<mx and mx<=5:
                a_c=0.65+0.05*mx
#                print 'a_c 2'
        return a_c
        
    def a_c(self, mx):
        """Определение a_c по СП"""
        if self.pr.title()=='dvut':
            if mx<=1:
                a_c=0.7
#                print 'a 1'
            elif 1<mx and mx<=5:
                a_c=0.65+0.05*mx
#                print 'a 2'
        return a_c
        
    def b_c(self):
        """Определение b_c по СП"""

#        print self.el.lambday_()
        if self.el.lambday_()<=3.14:
#            print 'b_c 1'
            b_c=1
        if self.el.lambday_()>3.14:
#            print 'b_c 2'
            b_c=(self.phi_n(lambda_=3.14, typ=0)[0]/self.phiy()[0])**0.5
#            print self.phi_n(lambda_=3.14, typ=0)[0], self.phiy()[0]
        return b_c

    def b_c_old(self):
        """Определение b_c по СНиП"""
        if self.el.lambday_()<=3.14:
#            print 'b_c 1'
            b_c=1
        if self.el.lambday_()>3.14:
#            print 'b_c 2'
            b_c=(self.phi_n_old(lambda_=3.14)/self.phiy_old())**0.5
        return b_c
                
    def c_max_old(self):
        """определение по СНиП"""
        e=self.force.mx/self.force.n
        h=self.pr.h()-self.pr.t()
        jt=self.pr.jt()
        mu=2.+0.156*jt/(self.pr.a()*h**2)*self.el.lambday()**2
        p=(self.pr.jx()+self.pr.jy())/(self.pr.a()*h**2)
        delta=4.*p/mu
        c_max=2./(1.+delta+((1.-delta)**2+16./mu*(e/h)**2)**0.5)
#        print e, 'e'
#        print h, 'h'
#        print jt, 'jt'
#        print mu, 'mu'
#        print p, 'p'
#        print delta, 'delta'        
#        print c_max, 'c_max'
        return c_max

    def c_max(self):
        """определение по СП"""
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
        cmax=2./(1.+delta+((1-delta)**2+16./mu*(a-ex/h)**2)**0.5)
#        print cmax
        return cmax

            
    def phi_exy_old(self):
        '''определение по снип. БЕЗ УЧЕТА требования mefy<mx и lambdax>lambday;
        выходные данные:
        phi_exy
        phi_ey
        c'''
        c=self.c_old()[0]
        phi_ey=self.phi_e_old(typ=2)[0]
#        print 'c', c
#        print 'phi_ey', phi_ey
        phi_exy=phi_ey*(0.6*c**(1./3)+0.4*c**(1./4))
        return phi_exy, phi_ey, c

    def phi_exy(self):
        '''определение по сп. БЕЗ УЧЕТА требования mefy<mx и lambdax>lambday;
        выходные данные:
        phi_exy
        phi_ey
        c'''
        c=self.c()[0]
        phi_ey=self.phi_e(typ=2)[0]
#        print 'c', c
#        print 'phi_ey', phi_ey
        phi_exy=phi_ey*(0.6*c**(1./3)+0.4*c**(1./4))
        return phi_exy, phi_ey, c


        '''_____________________________________________'''

        
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



        if (self.pr.title()=='korob' and typ3!=2) or (self.pr.title()=='dvut' and typ==1 and self.c()[0]*self.phiy()>self.phi_e(1)[0]) or typ3==1:
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
            if typ==2 and typ3!=1 and typ3!=2:
            
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
        
class ferma(snipn):
    """Класс для расчета элементов ферм по СНиП и СП """
    def add_data(self):
        """Дополнительные данные для расчета"""

        lst=[[u'yc1(+) [0.1; 1.]',[0.1,1.]]
        , [u'yc2(-) [0.1; 1.]',[0.1,1.]]
        ,[u'l, см [0.; 3000.]', [0., 3000.]]
        ,[u'mu_x [0.; 4.]',[0.,4.]]
        ,[u'mu_y [0.; 4.]',[0.,4.]]]
        return  lst   
    def output_data_all_snip_old(self):
        dat=self.output_data()
        dat_glob=self.output_data_snip_old_global()
        dat_local=self.output_data_snip_old_local()
        lst=dat_glob+dat+dat_local
        return lst

    def output_data_all_snip_n(self):
        dat=self.output_data()
        dat_glob=self.output_data_snip_n_global()
        dat_local=self.output_data_snip_n_local()
        lst=dat_glob+dat+dat_local
        return lst

        
    def output_data(self):
        """Выходные данные сечения"""
        lst=[]
        #Исходные данные:
        yu=self.yu()
        commentyu=u'yu, п.4'
        
        p=self.pr.p()
        commentp=u'P, кг/м3'


        a=self.pr.a()
        commenta=u'A, см2'
        
        ix=self.pr.ix()
        commentix=u'ix, см'

        iy=self.pr.iy()
        commentiy=u'iy, см'

        lambdax=self.element.lambdax()
        commentlx=u'lambda_x'
        
        lambday=self.element.lambday()
        commently=u'lambda_y'

        ry=self.element.steel.ry()
        commentry=u'Ry, кг/см2'        
        lst=[[yu, commentyu],
             [p, commentp],
             [ry, commentry],
             [a, commenta],
             [ix, commentix],
             [iy, commentiy],
             [lambdax, commentlx],
             [lambday, commently]]
        return lst
        
    def output_data_snip_old_global(self):
        """Выходные основные расчетные данные по СНиП"""
        
        lst=[]        
        #Расчет на расстяжение
#        print self.pr.a(),self.element.steel.ry(),self.yc1()
        n1=self.pr.a()*self.element.steel.ry()*self.yc1()/1000.
        comment1=u'N=An*Ry*yc (п.5.1.(5)), т'         

        n2=self.pr.a()*self.element.steel.ru()*self.yc1()/self.yu()/1000.
        comment2=u'N=A*Ru*yc/yu (п.5.2.(6)), т'         

        if n1<n2:
            nmin=n1
        else:
            nmin=n2
        commentnmin=u'N(+)min(п.5.1,п.5.2), т'
        #сжатие:
        phix_old=self.phix_old()
        commentpx=u'phix (п.5.3.)'

        phiy_old=self.phiy_old()
        commentpy=u'phiy (п.5.3.)'

        n3=self.nminus_old()
        comment3=u'N=An*Ry*yc*phi (п.5.3.(7)), т'
#        print self.output_data_snip_old_local()
        if float(self.output_data_snip_old_local()[0][0])>float(self.output_data_snip_old_local()[3][0]):
            fact_local=self.output_data_snip_old_local()[0]
        else:
            fact_local=self.output_data_snip_old_local()[3]
            
        lst=[[n3, comment3],
             [nmin,commentnmin],
            fact_local,
             [phix_old, commentpx],
             [phiy_old, commentpy],
             [n1, comment1],
             [n2, comment2]]

        if self.element.lx()!=0:
            nelx=3.14**2*self.element.steel.e()*self.pr.jx()/self.element.lx()**2/1000.
        else:
            nelx=0

        if self.element.ly()!=0:
            nely=3.14**2*self.element.steel.e()*self.pr.jy()/self.element.ly()**2/1000.
        else:
            nely=0

        lst.append([nelx, u'N_eilerx, т'])
        lst.append([nely, u'N_eilery, т'])


        commentqx=u'Q_ficmaxx (п.5.8.(23)), кг'
        commentqy=u'Q_ficmaxy (п.5.8.(23)), кг'

             
        if self.element.lx()<self.element.lfact() :
            q_ficmaxx=self.q_fic_old(n3*1000.,phix_old)
            lst.append([q_ficmaxx, commentqx])
        else:
            lst.append(['-', commentqx])
            
        if self.element.ly()<self.element.lfact() :
            q_ficmaxy=self.q_fic_old(n3*1000.,phiy_old)
            lst.append([q_ficmaxy, commentqy])
        else:
            lst.append(['-', commentqy])
            
    
        if self.pr.title()=='ugol_tavr_st_up' or self.pr.title()=='ugol_tavr_st_right':
            ix=self.pr.pr1.iy()
            ixplus=80*ix
            ixminus=40*ix
            
            lst.append([ixplus,u'Шаг планок (+)(п.5.7.), см'])
            lst.append([ixminus,u'Шаг планок (-)(п.5.7.), см'])
            

        elif self.pr.title()=='ugol_tavr_st_krest':
            iy0=self.pr.pr1.iy0()
            ixplus=80*iy0
            ixminus=40*iy0
            
            lst.append([ixplus,u'Шаг планок (+)(п.5.7.), см'])
            lst.append([ixminus,u'Шаг планок (-)(п.5.7.), см'])
        else:
            lst.append(['-',u'Шаг планок (+)(п.5.7.), см'])
            lst.append(['-',u'Шаг планок (-)(п.5.7.), см'])
                
        return lst

    def output_data_snip_n_global(self):
        """Выходные основные расчетные данные по СП"""

        lst=[]        
        #Расчет на расстяжение
        n1=self.pr.a()*self.element.steel.ry()*self.yc()/1000.
        comment1=u'N=An*Ry*yc (п.7.1.1(5)), т'         

        n2=self.pr.a()*self.element.steel.ru()*self.yc()/self.yu()/1000.
        comment2=u'N=A*Ru*yc/yu (п.7.1.1), т'         

        if n1<n2:
            nmin=n1
        else:
            nmin=n2
        commentnmin=u'N(+)min(п.7.1.1), т'
        #сжатие:
        
        phix, typx=self.phix()
        commentpx=u'phix (п.7.1.3)'
        comment_typx=u'Тип сечения Х'
        
        phiy, typy=self.phiy()
        commentpy=u'phiy (п.7.1.3)'
        comment_typy=u'Тип сечения Y'

        n3=self.nminus()
        comment3=u'N=An*Ry*yc*phi (п.7.1.3 (7)), т'

        if float(self.output_data_snip_n_local()[0][0])>float(self.output_data_snip_n_local()[3][0]):
            fact_local=self.output_data_snip_n_local()[0]
        else:
            fact_local=self.output_data_snip_n_local()[3]


        lst=[[n3, comment3],
             [nmin,commentnmin],
            fact_local,
             [phix, commentpx],
             [phiy, commentpy],
             [typx, comment_typx],
             [typy, comment_typy],
             [n1, comment1],
             [n2, comment2]]
            
        if self.element.lx()!=0:
            nelx=3.14**2*self.element.steel.e()*self.pr.jx()/self.element.lx()**2/1000.
        else:
            nelx=0

        if self.element.ly()!=0:
            nely=3.14**2*self.element.steel.e()*self.pr.jy()/self.element.ly()**2/1000.
        else:
            nely=0

        lst.append([nelx, u'N_eilerx, т'])
        lst.append([nely, u'N_eilery, т'])

        commentqx=u'Q_ficmaxx (п.7.2.7(18)), кг'
        commentqy=u'Q_ficmaxy (п.7.2.7(18)), кг'
             
        if self.element.lx()<self.element.lfact() :
            q_ficmaxx=self.q_fic(n3*1000,phix)
            lst.append([q_ficmaxx, commentqx])
        else:
            lst.append(["-", commentqx])

        if self.element.ly()<self.element.lfact() :
            q_ficmaxy=self.q_fic(n3*1000,phiy)
            lst.append([q_ficmaxy, commentqy])
        else:
            lst.append(["-", commentqy])
            
        if self.pr.title()=='ugol_tavr_st_up' or self.pr.title()=='ugol_tavr_st_right':
            ix=self.pr.pr1.iy()
            ixplus=80*ix
            ixminus=40*ix
            
            lst.append([ixplus,u'Шаг планок (+) (п.7.2.6), см'])
            lst.append([ixminus,u'Шаг планок (-) (п.7.2.6), см'])
            
        elif self.pr.title()=='ugol_tavr_st_krest':
            iy0=self.pr.pr1.iy0()
            ixplus=80*iy0
            ixminus=40*iy0
            
            lst.append([ixplus,u'Шаг планок (+) (п.7.2.6), см'])
            lst.append([ixminus,u'Шаг планок (-) (п.7.2.6), см'])
        else:
            lst.append(['-',u'Шаг планок (+) (п.7.2.6), см'])
            lst.append(['-',u'Шаг планок (-) (п.7.2.6), см'])

        return lst
                

                
    def output_data_snip_old_local(self):
        """Выходные расчетные данные по местной потери устойчивости по СНиП"""
        lst=[] 
        check_w, lambda_uw, lambda_w=self.local_buckl_h_n_old()
        check_f, lambda_uf, lambda_f=self.local_buckl_b_n_old()
        lst=[[check_w,u'К.исп. мест. уст. стенки'],
             [lambda_uw, u'lambda_uw (п.7.14., п.7.23.)'],
             [lambda_w, 'lambda_w'],
             [check_f, u'К.исп. мест. уст. полки'],
             [lambda_uf, u'lambda_uf (п.7.14., п.7.23.)'],
             [lambda_f, 'lambda_f']]        
        return lst
    def output_data_snip_n_local(self):
        """Выходные расчетные данные по местной потери устойчивости по СП"""
        lst=[] 
        check_w, lambda_uw, lambda_w=self.local_buckl_h_n()
        check_f, lambda_uf, lambda_f=self.local_buckl_b_n()
        lst=[[check_w,u'К.исп. мест. уст. стенки'],
             [lambda_uw, u'lambda_uw (п.7.3.2., п.7.3.8-9)'],
             [lambda_w, 'lambda_w'],
             [check_f, u'К.исп. мест. уст. полки'],
             [lambda_uf, u'lambda_uf (п.7.3.2., п.7.3.8-9)'],
             [lambda_f, 'lambda_f']]        
        return lst


    def nminus(self):
        """максимальная несущая способность (сжатие) по СП в Т"""
        n=self.pr.a()*self.element.steel.ry()*self.yc2()*self.phi()/1000
        return n

    def nplus(self):
        """максимальная несущая способность (расстяжение) по СП  в Т"""

        return self.nplus_old()
        
    def nminus_old(self):
        """максимальная несущая способность (сжатие) по СНиПП  в Т"""

        n=self.pr.a()*self.element.steel.ry()*self.yc2()*self.phi_old()/1000
        return n
        
    def nplus_old(self):
        """максимальная несущая способность (расстяжение) по СНиП  в Т"""

        n1=self.pr.a()*self.element.steel.ry()*self.yc1()/1000

        n2=self.pr.a()*self.element.steel.ru()*self.yc1()/self.yu()/1000

        if n1<n2:
            nmin=n1
        else:
            nmin=n2
        return nmin                            



        
class beam(snipn):
    """Класс для расчета элементов балок по СНиП и СП в упругой области"""
    def add_data(self):
        """Дополнительные данные для расчета"""

        lst=[[u'yc [0.1; 1]',[0.1,1.]]
        , [u'ycb [0.1; 0.95]',[0.1,0.95]]
        ,[u'lfact, см [0.; 3000.]', [0., 3000.]]
        ,[u'mu_b [0.; 1.]',[0.,1.]]
        ,[u'Тип:',[u'Балка']]
        ,[u'Кол-во закр.:',[u'Нет',u'2 и больше',u'одно по центру']]
        ,[u'Тип нагрузки:',[u'Соср. в сер. ',u'Соср. в четвер.',u'Равномер.']]
        ,[u'Нагрузка приложена к поясу:',[u'сжатому',u'расстянутому']]

        ]
#        lst=[[u'yc [0.1; 1]',[0.1,1.]]
#        , [u'ycb [0.1; 0.95]',[0.1,0.95]]
#        ,[u'lfact, см [0.; 3000.]', [0., 3000.]]
#        ,[u'mu_b [0.; 1.]',[0.,1.]]
#        ,[u'Тип:',[u'Балка']]
#
##        ,[u'Тип:',[u'Балка',u'Консоль']]
#        ,[u'Кол-во закр. (только для балки; для консоли - закр. нет):',[u'Нет',u'2 и больше',u'одно по центру']]
#        ,[u'Тип нагрузки:',[u'Соср. в сер. (для консоли - на конце)',u'Соср. в четвер. (для консоли - на конце)',u'Равномер.']]
#        ,[u'Нагрузка приложена к поясу:',[u'сжатому',u'расстянутому']]
#
#        ]



        return  lst   
    def output_data_all_snip_old(self,typ,typ1,typ2,typ3):
        dat=self.output_data()
        dat_glob=self.output_data_snip_old_global(typ,typ1,typ2,typ3)
        dat_local=self.output_data_snip_old_local()
        lst=dat_glob+dat+dat_local
        return lst

    def output_data_all_snip_n(self,typ,typ1,typ2,typ3):

        dat=self.output_data()
        dat_glob=self.output_data_snip_n_global(typ,typ1,typ2,typ3)
        dat_local=self.output_data_snip_n_local()
        lst=dat_glob+dat+dat_local
        return lst

        
    def output_data(self):
        """Выходные данные сечения"""
        lst=[]
        #Исходные данные:
        p=self.pr.p()
        commentp=u'P, кг/м3'
        
        a=self.pr.a()
        commenta=u'A, см2'
        
        jx=self.pr.jx()
        commentjx=u'Jx, см4'

        jy=self.pr.jy()
        commentjy=u'Jy, см4'

        wx=self.pr.wx()
        commentwx=u'Wx, см3'

        wy=self.pr.wy()
        commentwy=u'Wy, см3'


        s2x=self.pr.s2x()
        comments2x=u'S2x, см3'

        s2y=self.pr.s2y()
        comments2y=u'S2y, см3'
        
        ry=self.element.steel.ry()
        commentry=u'Ry, кг/см2'        
        lst=[
             [p, commentp],
             [ry, commentry],
             [a, commenta],
             [jx, commentjx],
             [jy, commentjy],
             [wx, commentwx],
             [wy, commentwy],

             [s2x, comments2x],
             [s2y, comments2y]]
        return lst
        
    def output_data_snip_old_global(self,typ,typ1,typ2,typ3):
        """Выходные основные расчетные данные по СНиП"""

        if float(self.output_data_snip_old_local()[0][0])>float(self.output_data_snip_old_local()[3][0]):
            fact_local=self.output_data_snip_old_local()[0]
        else:
            fact_local=self.output_data_snip_old_local()[3]

#        print fact_local, self.output_data_snip_old_local()[0], self.output_data_snip_old_local()[3]
        lst=[]        
        
        mx_ult=self.mx_old()
        commentmx=u'Mx=Wx*Ry*yc (п.5.12.(28)), т*м'         

        my_ult=self.my_old()
        commentmy=u'My=Wy*Ry*yc (п.5.12.(28)), т*м'         

        
        phi_b=self.phi_b_old(typ,typ1,typ2,typ3) 
        
        mxb=self.mxb_old(typ,typ1,typ2,typ3)
        commentmxb=u'Mxb=Wy*Ry*ycb*phi (п.5.15.(34)), т*м'         
        
        cxcy=self.cxcyn_old()
        
        
        qx_ult=self.qx_old()
        qy_ult=self.qy_old()

        lst=[[mx_ult, commentmx],
             [my_ult, commentmy],
             [mxb, commentmxb],
             fact_local,
             [phi_b[0], u'phi_b (прил. 7)'],
             [phi_b[1], u'phi_1 (прил. 7)'],
             [phi_b[2], u'psi (прил. 7)'],
             [phi_b[3], u'a (прил. 7)'],
             [cxcy[0],u'cx (табл. 66)'],

             [cxcy[1],u'cy (табл. 66)'],
             [qx_ult,u'Qxult (п.5.12.(29)), т'],
             [qy_ult,u'Qyult (п.5.12.(29)), т']]



        
        commentq=u'Q_fic (п.5.8., 5.16.), кг'

        if  self.pr.title()!='korob':     
             
            if self.element.lb()<self.element.lfact() and self.element.lb()!=0:
                n3=(self.pr.b()*self.pr.t()+0.25*(self.pr.h()-2*self.pr.t())*self.pr.s())*self.element.steel.ry()
                lambda_=self.element.lb()/(self.pr.b()/12.**0.5)*(self.element.steel.ry()/self.element.steel.e())**0.5            
                phi=self.phi_n_old(lambda_)
                q_fic=self.q_fic_old(n3,phi)
                lst.append([q_fic, commentq])
            else:
                lst.append(['-', commentq])
            
            
    
        return lst

    def output_data_snip_n_global(self,typ,typ1,typ2,typ3):
        """Выходные основные расчетные данные по СП"""        


        if float(self.output_data_snip_n_local()[0][0])>float(self.output_data_snip_n_local()[3][0]):
            fact_local=self.output_data_snip_n_local()[0]
        else:
            fact_local=self.output_data_snip_n_local()[3]


        lst=[]        
        
        mx_ult=self.mx()
        commentmx=u'Mx=Wx*Ry*yc (п.8.21.), т*м'         

        my_ult=self.my()
        commentmy=u'My=Wy*Ry*yc (п.8.21.), т*м'         

        
        phi_b=self.phi_b(typ,typ1,typ2,typ3) 
        
        mxb=self.mxb(typ,typ1,typ2,typ3)
        commentmxb=u'Mxb=Wy*Ry*ycb*phi (п.8.4.1.), т*м'         
        
        cxcy=self.cxcyn()
        
        
        qx_ult=self.qx()
        qy_ult=self.qy()

        lst=[[mx_ult, commentmx],
             [my_ult, commentmy],
             [mxb, commentmxb],
             fact_local,
             [phi_b[0], u'phi_b (прил. Ж)'],
             [phi_b[1], u'phi_1 (прил. Ж)'],
             [phi_b[2], u'psi (прил. Ж)'],
             [phi_b[3], u'a (прил. Ж)'],
             [cxcy[0],u'cx (табл. Е.1.)'],

             [cxcy[1],u'cy (табл. Е.1.)'],
             [qx_ult,u'Qxult (п.8.21.), т'],
             [qy_ult,u'Qyult (п.8.21.), т']]


        
        commentq=u'Q_fic (п.5.8., 5.16.), кг'

        if  self.pr.title()!='korob':     
            if self.element.lb()<self.element.lfact() and self.element.lb()!=0:
                n3=(self.pr.b()*self.pr.t()+0.25*(self.pr.h()-2*self.pr.t())*self.pr.s())*self.element.steel.ry()
                lambda_=self.element.lb()/(self.pr.b()/12.**0.5)*(self.element.steel.ry()/self.element.steel.e())**0.5            
                phi=self.phi_n(lambda_, typ=0, typ_s='b')[0]
                q_fic=self.q_fic(n3,phi)
                lst.append([q_fic, commentq])
            else:
                lst.append(['-', commentq])

            
            
    
        return lst

                
    def output_data_snip_old_local(self):
        """Выходные расчетные данные по местной потери устойчивости по СНиП"""
        lst=[] 
        check_w, lambda_uw, lambda_w=self.local_buckl_h_m_old(typ1=1, typ2=1)
        check_f, lambda_uf, lambda_f=self.local_buckl_b_m_old()
        lst=[[check_w,u'К.исп. мест. уст. стенки (без подв. нагрузки)'],
             [lambda_uw, u'lambda_uw (п.7.10., п.7.3.)'],
             [lambda_w, 'lambda_w'],
             [check_f, u'К.исп. мест. уст. полки (для пр. трубы - по СП)'],
             [lambda_uf, u'lambda_uf (п.7.24.)'],
             [lambda_f, 'lambda_f']]        
        return lst
        
    def output_data_snip_n_local(self):
        """Выходные расчетные данные по местной потери устойчивости по СП"""
        lst=[] 
        check_w, lambda_uw, lambda_w=self.local_buckl_h_m(typ1=1, typ2=1)
        check_f, lambda_uf, lambda_f=self.local_buckl_b_m()
        lst=[[check_w,u'К.исп. мест. уст. стенки'],
             [lambda_uw, u'lambda_uw (п.8.5.9.)'],
             [lambda_w, 'lambda_w'],
             [check_f, u'К.исп. мест. уст. полки'],
             [lambda_uf, u'lambda_uf (п.8.5.18.)'],
             [lambda_f, 'lambda_f']]        
        return lst      

    def mxb_old(self,typ,typ1,typ2,typ3):
        """максимальная несущая способность устойчивость (изгиб Х) по СНиП"""
        mxb=self.pr.wx()*self.element.steel.ry()*self.ycb()*self.phi_b_old(typ,typ1,typ2,typ3) [0]/100./1000.
        return mxb


    def mx_old(self):
        """максимальная несущая способность (изгиб Х) по СНиП"""
        mx=self.pr.wx()*self.element.steel.ry()*self.yc1()/100./1000.
        return mx

    def my_old(self):
        """максимальная несущая способность (изгиб Y) по СНиП"""
        my=self.pr.wy()*self.element.steel.ry()*self.yc1()/100./1000.
        return my

    def qx_old(self):
        if self.pr.title()=='dvut' or self.pr.title()=='shvel':
            qx=self.element.steel.rs()*self.yc1()*self.pr.s()*self.pr.jx()/self.pr.s2x()/1000.
#            print self.element.steel.rs(),self.yc1(),self.pr.s(),self.pr.jx(),self.pr.s2x()
        elif self.pr.title()=='korob':
            qx=self.element.steel.rs()*self.yc1()*(self.pr.s()*2)*self.pr.jx()/self.pr.s2x()/1000.
        return qx

    def qy_old(self):
        qy=self.element.steel.rs()*self.yc1()*(self.pr.t()*2)*self.pr.jy()/self.pr.s2y()/1000.
        return qy




    def mxb(self,typ,typ1,typ2,typ3):
        """максимальная несущая способность устойчивость (изгиб Х) по СП"""
        mxb=self.pr.wx()*self.element.steel.ry()*self.ycb()*self.phi_b(typ,typ1,typ2,typ3) [0]/100./1000.
        return mxb


    def mx(self):
        """максимальная несущая способность (изгиб Х) по СП"""
        return self.mx_old()

    def my(self):
        """максимальная несущая способность (изгиб Y) по СП"""
        return self.my_old()

    def qx(self):
        return self.qx_old()

    def qy(self):
        return self.qy_old()

class FermaPP(ferma):
    '''Класс для расчета ферм. Усилия списком'''

    def __init__(self):
        pass
    
    def reinit(self, element, forces, yc, ycb=0):
        super(FermaPP, self).__init__(element, forces, yc, ycb)
    
    def addData(self):
        lst=[[u'yc1(+) [0.1; 1.]',[0.1,1.]]
        , [u'yc2(-) [0.1; 1.]',[0.1,1.]]
        ,[u'l, см [0.; 3000.]', [0., 3000.]]
        ,[u'mu_x [0.; 4.]',[0.,4.]]
        ,[u'mu_y [0.; 4.]',[0.,4.]]
        ,[u'Lambda + [1.,400.]',[1.,400.]]
        ,[u'Lambda - ',[u'180-60a',u'210-60a',u'Другое']]
        ,[u'Lambda - [1.,300.]',[1.,300.]]]
        return  lst   
        
    def lstForce(self):
        lst=[u'N, т ("-" сжатие)']
        return lst



    def outDataOld(self, lambdaP, lambdaML, lambdaM):
        '''общий вывод по старому снип. 
        Входные данные - предельные лямбда для расстяжения и сжатия
        Выходные данные:
        4 списка - 
            1 - список - 1 - самый большой коэффициент использования, 2 - расстяжение, 3 - устойчивость
            4 -гибкость растяжение, 5 - гибкость сжатие
            6 - устойчивость стенки, 7 - полки, пример: [1,1,1,1,1,5,1]
            
            2- список усилий:
                1- усилие
                2 - коэффициент использование максимальное
                3 - коэффициент использование на расстяжение
                4 - устойчивость сжатие
                если проверка НЕ выполняется - '-'
                
            3 - общие исходные данные:
                1- повтор 1 с указанием № усилия [1- коэффициент, 1 - коэффициент, 1 - номер усилия и т.д.]
                2 - +180-60alpha
                +210-60alpha - alpha max из 2 списка
                
            4 - output_data_snip_old_all'''
        
        #собрали исходные данные        
        localData=self.output_data_snip_old_local()
        globalData=self.output_data_snip_old_global()
        sectionData=self.output_data()

        lambdaxy=max(self.el.lambdax(),self.el.lambday())
        
        nPMax=self.nplus_old()
        nMMax=self.nminus_old()

        # Организуем список № 2 и заодно находим общий плохой случай и по п.
        lst2=[]
        lst2Header=[u'Усилия, т', u'КиспMax',u'Kисп+ (п.5.1,2)',u'Kисп- (п.5.3)',u'Гибкость +', u'Гибкость -']
        
        lst2.append(lst2Header)
        
        
        for i in self.force.lstForce:
            if i[0]>=0:
                kP=i[0]/nPMax
                kM=u'-'
                kG=kP
                kLambdaP=lambdaxy/lambdaP
                kLambdaM=u'-'
            else:
                kP=u'-'
                kM=abs(i[0])/nMMax
                kG=kM
                kLambdaP=u'-'
                print lambdaML, 'ML'
                if lambdaML==1 or lambdaML==2:
                    aa=kM
                    if aa<0.5:
                        aa=0.5
                    if lambdaML==1:
                        lambdaMUlt=180-60*aa
                    else:
                        lambdaMUlt=210-60*aa
                else:
                    lambdaMUlt=lambdaM
                    
                kLambdaM=lambdaxy/lambdaMUlt

            lstTemp=[i[0],kG,kP, kM, kLambdaP, kLambdaM]
            lst2.append(lstTemp)
        
        #Организуем 1 список
        lst1=[]
        
        lst17=localData[3][0]
        lst16=localData[0][0]
        
#        lst15=lambdaxy/lambdaM
#        lst14=lambdaxy/lambdaP
        
        lst13=0
        lst12=0
        lst14=0
        lst15=0
        iP=0
        iM=0
        j=0
        for i in lst2[1:]:
            j=j+1
            if i[2]!=u'-' and lst12<i[2]:
                lst12=i[2]
                iP=j
                lst14=i[4]
            if i[3]!=u'-' and lst13<i[3]:
                lst13=i[3]
                iM=j
                lst15=i[5]
        
        lst11=max(lst12,lst13,lst14,lst15,lst16,lst17)
#        print lst11, 'lst11'
#        print lst12
#        print lst13
#        print lst14
#        print lst15
#        print lst16
#        print lst17
        lst1=[lst11,lst12,lst13,lst14,lst15,lst16,lst17]

    #формируем 3 список
        lst31=[[u'Kmax', lst11],
              [u'Kmax +', lst12],
              [u'№ усил', iP],
              [u'Kmax -', lst13],
              [u'№ усил', iM],
              [u'Kгибкость +', lst14],
              [u'Kгибкость -', lst15],
              [u'Kуст.стенки', lst16],
              [u'Kуст.полки', lst17]]
        
        alpha=lst13
        if alpha<0.5:
            alpha=0.5
        elif alpha>1:
            alpha=1
            
        lst32=[[u'180-60*a', 180-60.*alpha],
               [u'210-60*a', 210-60.*alpha]]
        
        lst3=lst31+lst32
        
        lst4=globalData+localData+sectionData
        
#        print lst1
#        print lst2
#        print lst3
#        print lst4
        
        return [lst1, lst2, lst3, lst4]
        
    def outDataN(self, lambdaP, lambdaML, lambdaM):
        '''общий вывод по новому снип. 
        Входные данные - предельные лямбда для расстяжения и сжатия
        Выходные данные:
        4 списка - 
            1 - список - 1 - самый большой коэффициент использования, 2 - расстяжение, 3 - устойчивость
            4 -гибкость растяжение, 5 - гибкость сжатие
            6 - устойчивость стенки, 7 - полки, пример: [1,1,1,1,1,5,1]
            
            2- список усилий:
                1- усилие
                2 - коэффициент использование максимальное
                3 - коэффициент использование на расстяжение
                4 - устойчивость сжатие
                если проверка НЕ выполняется - '-'
                
            3 - общие исходные данные:
                1- повтор 1 с указанием № усилия [1- коэффициент, 1 - коэффициент, 1 - номер усилия и т.д.]
                2 - +180-60alpha
                +210-60alpha - alpha max из 2 списка
                
            4 - output_data_snip_old_all'''
        
        #собрали исходные данные        
        localData=self.output_data_snip_n_local()
        globalData=self.output_data_snip_n_global()
        sectionData=self.output_data()

        lambdaxy=max(self.el.lambdax(),self.el.lambday())

        
        nPMax=self.nplus()
        nMMax=self.nminus()
        print 'nPMax', nPMax
        # Организуем список № 2 и заодно находим общий плохой случай и по п.
        lst2=[]
        lst2Header=[u'Усилия, т', u'КиспMax',u'Kисп+ (п.7.1.1,2)',u'Kисп- (п.7.1.3.(7))',u'Гибкость +', u'Гибкость -']
        
        lst2.append(lst2Header)
        
        
        for i in self.force.lstForce:
            if i[0]>=0:
                kP=i[0]/nPMax
                kM=u'-'
                kG=kP
                kLambdaP=lambdaxy/lambdaP
                kLambdaM=u'-'
            else:
                kP=u'-'
                kM=abs(i[0])/nMMax
                kG=kM
                kLambdaP=u'-'
                if lambdaML==1 or lambdaML==2:
                    aa=kM
                    if aa<0.5:
                        aa=0.5
                    if lambdaML==1:
                        lambdaMUlt=180-60*aa
                    else:
                        lambdaMUlt=210-60*aa
                else:
                    lambdaMUlt=lambdaM
                    
                kLambdaM=lambdaxy/lambdaMUlt

            lstTemp=[i[0],kG,kP, kM, kLambdaP, kLambdaM]
            lst2.append(lstTemp)
        
        #Организуем 1 список
        lst1=[]
        
        lst17=localData[3][0]
        lst16=localData[0][0]
        
#        lst15=lambdaxy/lambdaM
#        lst14=lambdaxy/lambdaP
        
        lst13=0
        lst12=0
        lst14=0
        lst15=0
        iP=0
        iM=0
        j=0
        for i in lst2[1:]:
            j=j+1
            if i[2]!=u'-' and lst12<i[2]:
                lst12=i[2]
                iP=j
                lst14=i[4]
            if i[3]!=u'-' and lst13<i[3]:
                lst13=i[3]
                iM=j
                lst15=i[5]
        
        lst11=max(lst12,lst13,lst14,lst15,lst16,lst17)
        
        lst1=[lst11,lst12,lst13,lst14,lst15,lst16,lst17]

    #формируем 3 список
        lst31=[[u'Kmax', lst11],
              [u'Kmax +', lst12],
              [u'№ усил', iP],
              [u'Kmax -', lst13],
              [u'№ усил', iM],
              [u'Kгибкость +', lst14],
              [u'Kгибкость -', lst15],
              [u'Kуст.стенки', lst16],
              [u'Kуст.полки', lst17]]
        
        alpha=lst13
        if alpha<0.5:
            alpha=0.5
        elif alpha>1:
            alpha=1
            
        lst32=[[u'180-60*a', 180-60.*alpha],
               [u'210-60*a', 210-60.*alpha]]
        
        lst3=lst31+lst32
        
        lst4=globalData+localData+sectionData
        
        return [lst1, lst2, lst3, lst4]



        
class BeamPP(beam):
    '''Класс для расчета балок. Усилия списком'''

    def __init__(self):
        pass
    
    def reinit(self, element, forces, yc, ycb=0):
        super(BeamPP, self).__init__(element, forces, yc, ycb)
    
    def addData(self):
        '''Дополнительные данные - вытаскиваем из обычного класса фермы - быстрее'''
        return self.add_data()
    def lstForce(self):
        lst=[u'Mx, т*м', u'My, т*м', u'Qx, т', u'Qy, т']
        return lst
        
    def outDataOld(self, typ,typ1,typ2,typ3):
        '''общий вывод по старому снип. 
        Входные данные - нет
        Выходные данные:
        4 списка - 
            1 - список - 1 - самый большой коэффициент использования, 2 - прочность 5/12, 3 - прочность 5/12, 4 - прочность -5/14, 5 - устойчивость
            6 - устойчивость стенки, 7 - полки, пример: [1,1,1,1,1,5]
            
            2- список усилий:
                1- усилие
                2 - коэффициент использование максимальное
                3 - прочность 5/12
                4 - прочность 5/12
                
                5 - прочность 5/14
                6 - устойчивость
                если проверка НЕ выполняется - '-'
                
            3 - общие исходные данные:
                1- повтор 1 с указанием № усилия [1- коэффициент, 1 - коэффициент, 1 - номер усилия и т.д.]
                
            4 - output_data_snip_old_all'''
        
        #собрали исходные данные        
        localData=self.output_data_snip_old_local()
        globalData=self.output_data_snip_old_global(typ,typ1,typ2,typ3)
        sectionData=self.output_data()
        
        mxult=self.mx_old()
        myult=self.my_old()
        qxult=self.qx_old()
        qyult=self.qy_old()
        
        mxbult=self.mxb_old(typ,typ1,typ2,typ3)
        

        # Организуем список № 2 и заодно находим общий плохой случай и по п.
        lst2=[]
        lst2Header=[u'Mx, т*м', u'My, т*м', u'Qx, т', u'Qy, т', u'КиспMax',u'Kпр (п.5.17 (38))',u'Kпр (п.5.12 (29))',u'Kпр (п.5.14 (33))',u'Kуст (п.5.15 (34))']
        
        lst2.append(lst2Header)
        
        
        for i in self.force.lstForce:
            mx, my, qx,qy=i           
            kpr38=abs(mx/mxult)+abs(my/myult)
            kpr29=abs(qx/qxult)+abs(qy/qyult)
            sx=abs(mx/mxult*self.element.steel.ry()*self.yc())+abs(my/myult*self.element.steel.ry()*self.yc())
            sy=0
            tx=qx/qxult*self.element.steel.rs()*self.yc()
            ty=qy/qyult*self.element.steel.rs()*self.yc()
            
            kpr33=(sx**2+sy**2-sx*sy+3*tx**2+3*ty**2)**0.5/(1.15*self.element.steel.ry()*self.yc())
            kust=abs(mx/mxbult)+abs(my/myult)
            
            kmax=max(kpr38,kpr29,kpr33, kust)
            lstTemp=[i[0],i[1],i[2],i[3],kmax, kpr38, kpr29, kpr33, kust]
            lst2.append(lstTemp)
        
        #Организуем 1 список
        lst1=[]
        
        lst17=localData[3][0]
        lst16=localData[0][0]
        
        lst12=0
        lst13=0
        lst14=0
        lst15=0

        i2=0
        i3=0
        i4=0
        i5=0
        
        j=0
        for i in lst2[1:]:
            j=j+1
            if i[5]!=u'-' and lst12<i[5]:
                lst12=i[5]
                i2=j
            if i[6]!=u'-' and lst13<i[6]:
                lst13=i[6]
                i3=j
            if i[7]!=u'-' and lst14<i[7]:
                lst14=i[7]
                i4=j
            if i[8]!=u'-' and lst15<i[8]:
                lst15=i[8]
                i5=j
        
        lst11=max(lst12,lst13,lst14,lst15,lst16,lst17)
#        print lst11, 'lst11'
#        print lst12
#        print lst13
#        print lst14
#        print lst15
#        print lst16
#        print lst17
        lst1=[lst11,lst12,lst13,lst14,lst15,lst16,lst17]

    #формируем 3 список
        lst3=[[u'Kmax', lst11],
              [u'Kпр (п.5.17 (38))', lst12],
              [u'№ усил', i2],
              [u'Kпр (п.5.12 (29))', lst13],
              [u'№ усил', i3],
              [u'Kпр (п.5.14 (33))', lst14],
              [u'№ усил', i4],
              [u'Kуст (п.5.15 (34))', lst15],
              [u'№ усил', i5],

              [u'Kуст.стенки', lst16],
              [u'Kуст.полки', lst17]]
        
#u'Kпр (п.5.17 (38))',u'Kпр (п.5.12 (29))',u'Kпр (п.5.14 (33))',u'Kуст (п.5.15 (34))'        
        lst4=globalData+localData+sectionData
        
#        print lst1
#        print lst2
#        print lst3
#        print lst4
#        
        return [lst1, lst2, lst3, lst4]

    def outDataN(self, typ,typ1,typ2,typ3):
        '''общий вывод по новому снип. 
        Входные данные - нет
        Выходные данные:
        4 списка - 
            1 - список - 1 - самый большой коэффициент использования, 2 - прочность 5/12, 3 - прочность 5/12, 4 - прочность -5/14, 5 - устойчивость
            6 - устойчивость стенки, 7 - полки, пример: [1,1,1,1,1,5]
            
            2- список усилий:
                1- усилие
                2 - коэффициент использование максимальное
                3 - прочность 5/12
                4 - прочность 5/12
                
                5 - прочность 5/14
                6 - устойчивость
                если проверка НЕ выполняется - '-'
                
            3 - общие исходные данные:
                1- повтор 1 с указанием № усилия [1- коэффициент, 1 - коэффициент, 1 - номер усилия и т.д.]
                
            4 - output_data_snip_old_all'''
        
        #собрали исходные данные        
        localData=self.output_data_snip_n_local()
        globalData=self.output_data_snip_n_global(typ,typ1,typ2,typ3)
        sectionData=self.output_data()
        
        mxult=self.mx()
        myult=self.my()
        qxult=self.qx()
        qyult=self.qy()
        
        mxbult=self.mxb(typ,typ1,typ2,typ3)
        

        # Организуем список № 2 и заодно находим общий плохой случай и по п.
        lst2=[]
        lst2Header=[u'Mx, т*м', u'My, т*м', u'Qx, т', u'Qy, т', u'КиспMax',u'Kпр (п.8.2.1 (43))',u'Kпр (п.8.2.1 (42))',u'Kпр (п.8.2.1 (44))',u'Kуст (п.8.4.1 (70))']
        
        lst2.append(lst2Header)
        
        
        for i in self.force.lstForce:
            mx, my, qx,qy=i           
            kpr38=abs(mx/mxult)+abs(my/myult)
            kpr29=abs(qx/qxult)+abs(qy/qyult)
            sx=abs(mx/mxult*self.element.steel.ry()*self.yc())+abs(my/myult*self.element.steel.ry()*self.yc())
            sy=0
            tx=qx/qxult*self.element.steel.rs()*self.yc()
            ty=qy/qyult*self.element.steel.rs()*self.yc()
            
            kpr33=(sx**2+sy**2-sx*sy+3*tx**2+3*ty**2)**0.5/(1.15*self.element.steel.ry()*self.yc())
            kust=abs(mx/mxbult)+abs(my/myult)
            
            kmax=max(kpr38,kpr29,kpr33, kust)
            lstTemp=[i[0],i[1],i[2],i[3],kmax, kpr38, kpr29, kpr33, kust]
            lst2.append(lstTemp)
        
        #Организуем 1 список
        lst1=[]
        
        lst17=localData[3][0]
        lst16=localData[0][0]
        
        lst12=0
        lst13=0
        lst14=0
        lst15=0

        i2=0
        i3=0
        i4=0
        i5=0
        
        j=0
        for i in lst2[1:]:
            j=j+1
            if i[5]!=u'-' and lst12<i[5]:
                lst12=i[5]
                i2=j
            if i[6]!=u'-' and lst13<i[6]:
                lst13=i[6]
                i3=j
            if i[7]!=u'-' and lst14<i[7]:
                lst14=i[7]
                i4=j
            if i[8]!=u'-' and lst15<i[8]:
                lst15=i[8]
                i5=j
        
        lst11=max(lst12,lst13,lst14,lst15,lst16,lst17)
#        print lst11, 'lst11'
#        print lst12
#        print lst13
#        print lst14
#        print lst15
#        print lst16
#        print lst17
        lst1=[lst11,lst12,lst13,lst14,lst15,lst16,lst17]

    #формируем 3 список
        lst3=[[u'Kmax', lst11],
              [u'Kпр (п.8.2.1 (43))', lst12],
              [u'№ усил', i2],
              [u'Kпр (п.8.2.1 (42))', lst13],
              [u'№ усил', i3],
              [u'Kпр (п.8.2.1 (44))', lst14],
              [u'№ усил', i4],
              [u'Kуст (п.8.4.1 (70))', lst15],
              [u'№ усил', i5],

              [u'Kуст.стенки', lst16],
              [u'Kуст.полки', lst17]]
        
#u'Kпр (п.5.17 (38))',u'Kпр (п.5.12 (29))',u'Kпр (п.5.14 (33))',u'Kуст (п.5.15 (34))'        
        lst4=globalData+localData+sectionData
        
#        print lst1
#        print lst2
#        print lst3
#        print lst4
#        
        return [lst1, lst2, lst3, lst4]

class ColumnPP(ferma):
    '''Класс для расчета колонн. Усилия списком.
    Локальная устойчивость для внецентренного сжатия не запрограммирована,
    принимается наихудшее из центрального сжатия и изгиба'''
    
    def __init__(self):
        pass
    def addData(self):
        '''Дополнительные данные'''
        lst=[[u'yc [0.1; 1.]',[0.1,1.]]
        , [u'ycb(-) [0.1; 1.]',[0.1,1.]]
        ,[u'l, см [0.; 3000.]', [0., 3000.]]
        ,[u'mu_x [0.; 4.]',[0.,4.]]
        ,[u'mu_y [0.; 4.]',[0.,4.]]
        ,[u'mu_b [0.; 4.]',[0.,4.]]
        ,[u'Lambda + [1.,400.]',[1.,400.]]
        ,[u'Lambda - ',[u'180-60a',u'210-60a',u'Другое']]
        ,[u'Lambda - [1.,300.]',[1.,300.]]]
        return  lst   

        return lst
    
    def lstForce(self):
        lst=[u'N, т',u'Mx, т*м', u'My, т*м', u'Qx, т', u'Qy, т']
        return lst
 
    def outDataOld(self, lambdaP, lambdaML, lambdaM):
        '''общий вывод по старому снип. 
        Входные данные - предельные лямбда для расстяжения и сжатия
        Расчет:
            1. Прочность a:
                если tau<0.5*Rs, ry<5400 и выполняются проверки по локальной устойчивости по изгибу:
                    49
                иначе:
                    50
               Прочность б:
                   приведенная прочность
            2. Устойчивость:
                a) расстяжение (N>=0)
                    N=0: Mx/Mxb+My/My; Mxb для случая - закрепления сжатого пояса ---a, psi, phi1, phib 
                б) сжатие:
                    а) Центральное сжатие в плоскости наибольшей жесткости
                    в) 51 в плоскости (61 - не делаем так как есть a и б)
                    в) 51 из плоскости (61 - не делаем так как есть a и б)

                    г) Если Mx!=0: 61
                    д) Если Mx!=0: My!=0: 62
                    
        Выходные данные:
        4 списка - 
            1 - список - 1 - самый большой коэффициент использования, 2 - расстяжение, 3 - устойчивость
            4 -гибкость растяжение, 5 - гибкость сжатие
            6 - устойчивость стенки, 7 - полки, пример: [1,1,1,1,1,5,1]
            
            2- список усилий:
                1- усилие
                2 - коэффициент использование максимальное
                3 - коэффициент использование на расстяжение
                4 - устойчивость сжатие
                если проверка НЕ выполняется - '-'
                
            3 - общие исходные данные:
                1- повтор 1 с указанием № усилия [1- коэффициент, 1 - коэффициент, 1 - номер усилия и т.д.]
                2 - +180-60alpha
                +210-60alpha - alpha max из 2 списка
                
            4 - output_data_snip_old_all'''
        
        #собрали исходные данные        
        localData=self.output_data_snip_old_local()
        globalData=self.output_data_snip_old_global()
        sectionData=self.output_data()

        lambdaxy=max(self.el.lambdax(),self.el.lambday())
        
        # Организуем список № 2 и заодно находим общий плохой случай и по п.
        lst2=[]
        lst2Header=[u'N, т',u'Mx, т*м', u'My, т*м', u'Qx, т', u'Qy, т'
        , u'КиспMax'
        ,u'Kcрез (п.5.12 (29))'
        ,u'Kпр (п.5.14 (33))'

        ,u'Kпр (п.5.25 (50))'
        ,u'KустБ (п.5.15 (34))'

        ,u'a'
        ,u'psi '
        ,u'phi1'
        ,u'phib'

        ,u'Kуст=N/(Ry*yc*phix) (п.5.32 (61))'
        ,u'phix'
        
        
        ,u'KустX=Ne/(Ry*yc*phiex) (п.5.32 (61))'
        ,u'm'
        ,u'nau'
        ,u'mef'
        ,u'phiex'
        
        ,u'KустY=Ne/(Ry*yc*phiey) (п.5.32 (61))'
        ,u'm'
        ,u'nau'
        ,u'mef'
        ,u'phiey'
        
        ,u'KустY=N/(Ry*yc*phiy*c) (п.5.30 (56))'
        ,u'mx'
        ,u'c_max'
        ,u'c'
        ,u'phiy'

        ,u'KустXY=N/(Ry*yc*phiexy) (п.5.30 (56))'
        ,u'mx'
        ,u'c_max'
        ,u'c'
        ,u'my'
        ,u'nauy'
        ,u'mefy'
        ,u'phiey'
        ,u'phiexy'
        ,u'Гибкость +'
        ,u'Гибкость -']
        
        lst2.append(lst2Header)
        
        mxult=self.mx_old()
        myult=self.my_old()
        qxult=self.qx_old()
        qyult=self.qy_old()
        
        mxbult=self.mxb_old(1,2,1,1)

        nplusult=self.nplus_old()
            
        for i in self.force.lstForce:
            self.force.n,self.force.mx,self.force.my,self.force.qx,self.force.qy=i
            n,mx,my,qx,qy=i
            
            yc=self.el.yc()
            ycb=self.el.ycb()
            
            
            #прочность на срез
            k29=abs(qx/qxult)+abs(qy/qyult)

            #прочность приведенная
            sx=(abs(n/nplusult)+abs(mx/mxult)+abs(my/myult))*self.el.steel/ry()*self.el.yc()
            taux=abs(qx/qxult)*self.el.steel/rs()*self.el.yc()

            tauy=abs(qy/qyult)*self.el.steel/rs()*self.el.yc()

            k33=(sx**2+3*taux**2+3*tauy**2)**0.5/(self.el.steel/ry()*self.el.yc()*1.15)


            #прочность по N/A+M/W
            k50=abs(n/nplusult)+abs(mx/mxult)+abs(my/myult)

            #если расстяжение - проверить балочную устойчивость по 1 2  1 1            
            if n>=0:
                k34=abs(mx/mxbult)+abs(my/myult)
                phib34=self.phi_b_old(1,2,1,1)
            else:
                k34=u'-'
                phib34=[u'-',u'-',u'-',u'-']
            
            if n<0:
                pass
            
            
            lstTemp=[i[0],kG,kP, kM, kLambdaP, kLambdaM]
            lst2.append(lstTemp)
        
        #Организуем 1 список
        lst1=[]
        
        lst17=localData[3][0]
        lst16=localData[0][0]
        
#        lst15=lambdaxy/lambdaM
#        lst14=lambdaxy/lambdaP
        
        lst13=0
        lst12=0
        lst14=0
        lst15=0
        iP=0
        iM=0
        j=0
        for i in lst2[1:]:
            j=j+1
            if i[2]!=u'-' and lst12<i[2]:
                lst12=i[2]
                iP=j
                lst14=i[4]
            if i[3]!=u'-' and lst13<i[3]:
                lst13=i[3]
                iM=j
                lst15=i[5]
        
        lst11=max(lst12,lst13,lst14,lst15,lst16,lst17)
#        print lst11, 'lst11'
#        print lst12
#        print lst13
#        print lst14
#        print lst15
#        print lst16
#        print lst17
        lst1=[lst11,lst12,lst13,lst14,lst15,lst16,lst17]

    #формируем 3 список
        lst31=[[u'Kmax', lst11],
              [u'Kmax +', lst12],
              [u'№ усил', iP],
              [u'Kmax -', lst13],
              [u'№ усил', iM],
              [u'Kгибкость +', lst14],
              [u'Kгибкость -', lst15],
              [u'Kуст.стенки', lst16],
              [u'Kуст.полки', lst17]]
        
        alpha=lst13
        if alpha<0.5:
            alpha=0.5
        elif alpha>1:
            alpha=1
            
        lst32=[[u'180-60*a', 180-60.*alpha],
               [u'210-60*a', 210-60.*alpha]]
        
        lst3=lst31+lst32
        
        lst4=globalData+localData+sectionData
        
#        print lst1
#        print lst2
#        print lst3
#        print lst4
        
        return [lst1, lst2, lst3, lst4]
    def output_data_snip_old_local(self):
        """Выходные расчетные данные по местной потери устойчивости по СНиП. Тупо берем мин из балок и колонн"""
        lst=[] 
        check_wn, lambda_uwn, lambda_wn=self.local_buckl_h_n_old()
        check_fn, lambda_ufn, lambda_fn=self.local_buckl_b_n_old()
        
        check_wm, lambda_uwm, lambda_wm=self.local_buckl_h_m_old(typ1=1, typ2=1)
        check_fm, lambda_ufm, lambda_fm=self.local_buckl_b_m_old()
        
        if check_wm<check_wn:
            check_w, lambda_uw, lambda_w=check_wn, lambda_uwn, lambda_wn
        else:
             check_w, lambda_uw, lambda_w=check_wm, lambda_uwm, lambda_wm

        if check_fm<check_fn:
            check_f, lambda_uf, lambda_f=check_fn, lambda_ufn, lambda_fn
        else:
             check_f, lambda_uf, lambda_f=check_fm, lambda_ufm, lambda_fm
           
        lst=[[check_w,u'К.исп. мест. уст. стенки'],
             [lambda_uw, u'lambda_uw (п.7.14., п.7.23., п.7.10., п.7.3.)'],
             [lambda_w, 'lambda_w'],
             [check_f, u'К.исп. мест. уст. полки'],
             [lambda_uf, u'lambda_uf (п.7.14., п.7.23., п.7.24.)'],
             [lambda_f, 'lambda_f']]        
        return lst


    def output_data_snip_n_local(self):
        """Выходные расчетные данные по местной потери устойчивости по СНиП. Тупо берем мин из балок и колонн"""
        lst=[] 
        check_wn, lambda_uwn, lambda_wn=self.local_buckl_h_n()
        check_fn, lambda_ufn, lambda_fn=self.local_buckl_b_n()
        
        check_wm, lambda_uwm, lambda_wm=self.local_buckl_h_m(typ1=1, typ2=1)
        check_fm, lambda_ufm, lambda_fm=self.local_buckl_b_m()
        
        if check_wm<check_wn:
            check_w, lambda_uw, lambda_w=check_wn, lambda_uwn, lambda_wn
        else:
             check_w, lambda_uw, lambda_w=check_wm, lambda_uwm, lambda_wm

        if check_fm<check_fn:
            check_f, lambda_uf, lambda_f=check_fn, lambda_ufn, lambda_fn
        else:
             check_f, lambda_uf, lambda_f=check_fm, lambda_ufm, lambda_fm
           
        lst=[[check_w,u'К.исп. мест. уст. стенки'],
             [lambda_uw, u'lambda_uw (п.7.3.2., п.7.3.8-9, п.8.5.9.)'],
             [lambda_w, 'lambda_w'],
             [check_f, u'К.исп. мест. уст. полки'],
             [lambda_uf, u'lambda_uf (п.7.3.2., п.7.3.8-9, п.8.5.18.)'],
             [lambda_f, 'lambda_f']]        
        return lst

    def mxb_old(self,typ,typ1,typ2,typ3):
        """максимальная несущая способность устойчивость (изгиб Х) по СНиП"""
        mxb=self.pr.wx()*self.element.steel.ry()*self.ycb()*self.phi_b_old(typ,typ1,typ2,typ3) [0]/100./1000.
        return mxb


    def mx_old(self):
        """максимальная несущая способность (изгиб Х) по СНиП"""
        mx=self.pr.wx()*self.element.steel.ry()*self.yc()/100./1000.
        return mx

    def my_old(self):
        """максимальная несущая способность (изгиб Y) по СНиП"""
        my=self.pr.wy()*self.element.steel.ry()*self.yc()/100./1000.
        return my

    def qx_old(self):
        if self.pr.title()=='dvut' or self.pr.title()=='shvel':
            qx=self.element.steel.rs()*self.yc()*self.pr.s()*self.pr.jx()/self.pr.s2x()/1000.
#            print self.element.steel.rs(),self.yc1(),self.pr.s(),self.pr.jx(),self.pr.s2x()
        elif self.pr.title()=='korob':
            qx=self.element.steel.rs()*self.yc()*(self.pr.s()*2)*self.pr.jx()/self.pr.s2x()/1000.
        return qx

    def qy_old(self):
        qy=self.element.steel.rs()*self.yc()*(self.pr.t()*2)*self.pr.jy()/self.pr.s2y()/1000.
        return qy




    def mxb(self,typ,typ1,typ2,typ3):
        """максимальная несущая способность устойчивость (изгиб Х) по СП"""
        mxb=self.pr.wx()*self.element.steel.ry()*self.ycb()*self.phi_b(typ,typ1,typ2,typ3) [0]/100./1000.
        return mxb


    def mx(self):
        """максимальная несущая способность (изгиб Х) по СП"""
        return self.mx_old()

    def my(self):
        """максимальная несущая способность (изгиб Y) по СП"""
        return self.my_old()

    def qx(self):
        return self.qx_old()

    def qy(self):
        return self.qy_old()

    def nplus(self):
        """максимальная несущая способность (расстяжение) по СП  в Т"""

        return self.nplus_old()
        
        
    def nplus_old(self):
        """максимальная несущая способность (расстяжение) по СНиП  в Т"""

        n1=self.pr.a()*self.element.steel.ry()*self.yc()/1000

