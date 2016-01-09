# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:47:36 2013

@author: puma
"""

from table import *
from profiles2 import *

def excel_get_profiles(files, number, column):
    table=tables_csv((str(files)),'float')
    return table.get_cell(str(column), str(int(number)))

def excel_get_sigma(files, number, typ, nn=1,   n=0, m_x=0, m_y=0, w=0):
    profile=profiles_infile(files, number,typ)
    return profile.get_sigma(nn=int(nn), n=n, m_x=m_x, m_y=m_y, w=w)


def excel_get_tau( files, number, typ, nn=1, q_x=0, q_y=0, t=0, sr=0):
    profile=profiles_infile(files, number,typ)
    return profile.get_tau(nn=int(nn), q_x=q_x, q_y=q_y, t=t, sr=sr)  
    
def excel_get_sigma_e(files, number, typ, nn=1, n=0, m_x=0, m_y=0, w=0, q_x=0, q_y=0, t=0, sr=0):
    profile=profiles_infile(files, number,typ)
    return profile.get_sigma_e(nn=int(nn),n=n, m_x=m_x, m_y=m_y, w=w, q_x=q_x, q_y=q_y, t=t, sr=sr)   
    
#if __name__ == "__main__":
#    a=excel_get_sigma(files='gost8239_89.csv',number='10', typ='dvut', nn=1,   n=1000., m_x=0, m_y=0, w=0)
#    profile=profiles_infile(files='gost8239_89.csv',number='10', typ='dvut')  
#          
#    print  profile.t1(),profile.t2()