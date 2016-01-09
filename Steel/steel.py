# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:03:38 2013

@author: puma
"""
from table import tables_csv
#from profiles2 import *

#typ - тип стали, el - элемент, dim - 0 в мм, 1 - в см.typ_steel - тип стали

class mat(object):
    def __init__(self, typ, el, dim=0, typ_steel='prokat'):
        return 0


class list_steel(mat):
    def __init__(self, code,typ_steel='prokat'):
        list_code=[u'СНиП II-23-81*', u'СП16.13330.2011']
        if code==list_code[0] and typ_steel=='prokat':
            fil='SteelData/mat_steel1987.csv'
        if code==list_code[0] and typ_steel=='list':
            fil='SteelData/mat_steel1987l.csv'
        if code==list_code[1] :
            fil='SteelData/mat_steel.csv'
        table=tables_csv(fil,'float')
        list_table=table.get_title_column()
        
        lst=[]
        for x in list_table:
            if not(x in lst):
                lst.append(x)
        self.lst=lst
    def get_list(self):
        return self.lst
        
        
class steel_general(mat):
    def __init__(self, ry, ryn, ru, run):
        #значения в МПа
        self.__ryn=ryn/9.81*100
        self.__run=run/9.81*100
        self.__ry=ry/9.81*100
        self.__ru=ru/9.81*100
        self.__rs=0.58*self.__ry
        self.__rth=0.5*self.__ru
        self.__rthf=0.5*self.__ry        
    def ryn(self):
        return self.__ryn
    def ry(self):
        return self.__ry
    def ru(self):
        return self.__ru
    def run(self):
        return self.__run
    def rs(self):
        return self.__rs
    def rth(self):
        return self.__rth
    def rthf(self):
        return self.__rthf
    def mu(self):
        return 0.3
    def e(self):
        return 2.06*10**5/9.81*100
            
class steel_snip20107n(mat):
    def __init__(self, typ, el, dim=0):
        
        if dim==0:
            t=el.t()*1
        else:
            t=el.t()*10
#        print el.t()
        table=tables_csv('SteelData/mat_steel.csv','float')
        list_table=table.get_title_column()
        i=0
        ryn=0
        run=0
        ry=0
        ru=0

        for typ_list in list_table:
            i=i+1
#            print typ_list
            if str(typ_list)==str(typ):
#                print('tut')

                t1=table.get_ij(i,1)
                t2=table.get_ij(i,2)
#                print t1, t2
                if t>=t1 and t<=t2:             
                    ryn=table.get_ij(i,3)
                    run=table.get_ij(i,4)
                    ry=table.get_ij(i,5)
                    ru=table.get_ij(i,6)
        self.__ryn=ryn/9.81*100
        self.__run=run/9.81*100
        self.__ry=ry/9.81*100
        self.__ru=ru/9.81*100
        self.__rs=0.58*self.__ry
        self.__rth=0.5*self.__ru
        self.__rthf=0.5*self.__ry
        
    def ryn(self):
        return self.__ryn
    def ry(self):
        return self.__ry
    def ru(self):
        return self.__ru
    def run(self):
        return self.__run
    def rs(self):
        return self.__rs
    def rth(self):
        return self.__rth
    def rthf(self):
        return self.__rthf
    def mu(self):
        return 0.3
    def e(self):
        return 2.06*10**5/9.81*100

class steel_snip1987(mat):
    def __init__(self, typ, el, dim=0, typ_steel='prokat'):
        
        if dim==0:
            t=el.t()*1
        else:
            t=el.t()*10
#        print el.t()
        if typ_steel=='list':
            table=tables_csv('SteelData/mat_steel1987l.csv','float')
        if typ_steel=='prokat':
            table=tables_csv('SteelData/mat_steel1987.csv','float')
        list_table=table.get_title_column()
        i=0
        ryn=0
        run=0
        ry=0
        ru=0

        for typ_list in list_table:
            i=i+1
#            print typ_list
            if str(typ_list)==str(typ):
#                print('tut')

                t1=table.get_ij(i,1)
                t2=table.get_ij(i,2)
#                print t1, t2
                if t>=t1 and t<=t2:             
                    ryn=table.get_ij(i,3)
                    run=table.get_ij(i,4)
                    ry=table.get_ij(i,5)
                    ru=table.get_ij(i,6)
        self.__ryn=ryn/9.81*100
        self.__run=run/9.81*100
        self.__ry=ry/9.81*100
        self.__ru=ru/9.81*100
        self.__rs=0.58*self.__ry
        self.__rth=0.5*self.__ru
        self.__rthf=0.5*self.__ry
        
    def ryn(self):
        return self.__ryn
    def ry(self):
        return self.__ry
    def ru(self):
        return self.__ru
    def run(self):
        return self.__run
    def rs(self):
        return self.__rs
    def rth(self):
        return self.__rth
    def rthf(self):
        return self.__rthf
    def mu(self):
        return 0.3
    def e(self):
        return 2.06*10**5/9.81*100

        
#a=dvut(h=360., b=130., t=22., s=9.5, r1=14., r2=6., a1=atan(12./100))
#s=steel_snip20107n('C245',a)
#print(s.ry())