# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 22:00:52 2014

@author: Pyltsin
"""

from  PyQt4 import QtCore, QtGui, uic

from basa_sort import BasaSort
from table import tables_csv

from key_press_event import copy_past



class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("gui\\sortament_list.ui", self)
        load_sort_list(self)
    def keyPressEvent(self, e):
        copy_past(e, [], [window.view], window)
        
def load_sort_list(window):

    model =  QtGui.QStandardItemModel()
    parent = model.invisibleRootItem()
    i=0
    for x in sort_list[0]:
        item = QtGui.QStandardItem(x[0])
        item.setEditable(False)
        parent.appendRow(item)
        for y in sort_list[i+1]:
            item2=QtGui.QStandardItem(y[0])
            item2.setEditable(False)

            item.appendRow(item2)
        i=i+1
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u'Список сортаментов'))
    sel_model=QtGui.QItemSelectionModel(model)
    window.list_sort.setModel(model)

    window.list_sort.setSelectionModel(sel_model)

    model_signal=window.list_sort.selectionModel()
    model_signal.currentChanged.connect(edit_table)
    return 0

def edit_table():
    a=window.list_sort.selectionModel().currentIndex()
    ind=a.data().toString()
    par_ind=a.parent().data().toString()
    if par_ind!="":
        i=0
        for x in sort_list[0]:
            if par_ind==x[0]:
                par=x
                for y in sort_list[i+1]:
                    if ind==y[0]:
                        el=y
                        break
                break
            i=i+1
        solve_load_table(el[1], window.view, par[1])
        load_picture(basa.pict4sortament(par[1]), window.pict)
def load_picture(path, frame):
    try:
        frame.setPixmap(QtGui.QPixmap(path))
    except():
        print u"Ошибка загрузки файла"

def solve_load_table(path, frame, num_sort):
#получаем весь файл
    table=tables_csv(path, 'float')
    table_data=table.get_table()
#определяем кол-во профилей в файле
    len_table=len(table_data)-1

#определяем кол-во входных данных     
    input_data=basa.input_data4sortament(num_sort)
    len_input_data=len(input_data)

#формируем заголовок
    header_horisontal=input_data

    prof_first=basa.output_data(num_sort, table_data[1][1:len_input_data+1])
    header_horisontal=list(u"№")+header_horisontal+(prof_first.output_list())
#ставим заголовок:
#    print header_horisontal

    
#запонлняем таблицу    
    output_table=[]
    for x in table_data[1:]:
        prof_item=basa.output_data(num_sort, x[1:len_input_data+1])
        #формируем строку:
        
        line=x[0:len_input_data+1]
        
#        line[0]=line[0].replace(u'II',u'П')
#        window.setWindowTitle(line[0])

#        print line[0]
        p1=abs(prof_item.output_dict()[u'A, см2']-x[-3])/x[-3]
        p2=abs(prof_item.output_dict()[u'Jx, см4']-x[-2])/x[-2] 

        p3=abs(prof_item.output_dict()[u'Jy, см4']-x[-1])/x[-1]

        if p1<0.005 and p2<0.005 and p3<0.005:
            for y in prof_item.output_list():
                if type(prof_item.output_dict()[y])==type(0.1):
                    txt="%.2f"%(prof_item.output_dict()[y])
                else:
                    txt=prof_item.output_dict()[y]

  

                line.append(txt)
        else:
            print line[0], p1, p2, p3
            print "Error", prof_item.output_dict()[u'A, см2'],prof_item.output_dict()[u'Jx, см4'],prof_item.output_dict()[u'Jy, см4']
            for y in prof_item.output_list():
                line.append("Error")   
        output_table.append(line)

    frame.setColumnCount(len(output_table[0]))
    frame.setRowCount(len(output_table))
    frame.setHorizontalHeaderLabels(header_horisontal)

    x=-1
    for i in output_table:
        x=x+1 
        y=-1
        for j in i:
            y=y+1
            item = QtGui.QTableWidgetItem(unicode(j))
            frame.setItem(x,y,item)
            frame.item(x,y).setFlags(QtCore.Qt.ItemFlags(1+2+4+8+6+12+64))
      
#    for i in range(0,0):
#        frame.setColumnWidth(i, 40)    
    
    for i in range(0,len_input_data+1):
        frame.setColumnWidth(i, 35)    
    for i in range(len_input_data+1,len(output_table[0])+1):
        frame.setColumnWidth(i, 55)    

    frame.setColumnWidth(0, 65)                            
    return 0   
    
        
if __name__=="__main__":
    import sys
    basa=BasaSort()
    sort_list=basa.list4sortament()

    app=QtGui.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())
