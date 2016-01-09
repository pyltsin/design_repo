# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:24:40 2013

@author: admin
"""

from table import *

def excel_get_profiles(files, number, column):
    table=tables_csv((str(files)),'float')
    return table.get_cell(str(column), str(int(number)))