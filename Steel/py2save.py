# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:44:25 2014

@author: Pyltsin
"""
from  PyQt4 import QtCore, QtGui

def save2file(fil, widgetList):
    '''сама запись и возврат 1 если ошибка, 0 - если все ок'''
    
    f= open(fil, 'w')
    for item in widgetList:
        if type(item)==QtGui.QComboBox:
            txt=str(item.currentIndex()).rstrip()+u'\n'
            f.write(txt)
#                print txt
        if type(item)==QtGui.QSpinBox:
            txt=str(item.value()).rstrip()+u'\n'
            f.write(txt)
#                print txt

        if type(item)==QtGui.QTableWidget:
            columnCount=item.columnCount()
            rowCount=item.rowCount()
            for i in range(columnCount):
                for j in range(rowCount):
                    if item.cellWidget(j,i)==None:
                        txt=str(item.item(j,i).text()).rstrip()+u'\n'
                        f.write(txt)
#                            print txt

                    else:
                        txt=str(item.cellWidget(j,i).currentIndex()).rstrip()+u'\n'
                        f.write(txt)
#                            print txt


#                    if self.input_table.cellWidget(j,i)==None and self.input_table.item(j, i).text()=="" :
#                        self.input_table.item(j,i).setText(u"0")


    f.close()
                
def load2form(fil, lst):
    
    f=open(fil, 'r') 

    for item in lst:
        if type(item)==QtGui.QComboBox:
            txt=int(f.readline())
            item.setCurrentIndex(txt)
        elif type(item)==QtGui.QSpinBox:
            txt=int(f.readline())
            item.setValue(txt)
        elif type(item)==QtGui.QTableWidget:
            columnCount=item.columnCount()
            rowCount=item.rowCount()

            for i in range(columnCount):
                for j in range(rowCount):
                    if item.cellWidget(j,i)==None:
                        txt=(f.readline())
        #                    print txt
                        item.setItem(j, i, QtGui.QTableWidgetItem(""))
                        item.item(j,i).setText(txt)
                    else:
                        txt=int(f.readline())
        #                    print txt
                        item.cellWidget(j,i).setCurrentIndex(txt)

    f.close()        
