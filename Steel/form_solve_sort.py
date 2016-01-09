# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 18:15:04 2014

@author: Pyltsin
"""

from  PyQt4 import QtCore, QtGui, uic

import win32com.client
import os
from basa_sort import BasaSort
from key_press_event import copy_past
import shutil

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("gui/sort_solve.ui", self)
        basa=BasaSort()
        for text in basa.key_sortament():
            self.listWidget.addItem(text)
        self.listWidget.currentItemChanged.connect(table_head)
        self.inputtable.currentItemChanged.connect(table_clear_output)
        self.solvebutton.clicked.connect(solve)
        self.wordbutton.clicked.connect(toword)
        self.wordbutton.setEnabled(False)


    def keyPressEvent(self, e):
        copy_past(e, [window.inputtable], [window.outputtable], window)

def toword():
#    try:
    basa=BasaSort()
    lab=window.listWidget.currentItem().text()
    wordapp = win32com.client.Dispatch("Word.Application")
    wordapp.Visible = 1
    worddoc = wordapp.Documents.Add()
    worddoc.PageSetup.Orientation = 1
    worddoc.PageSetup.BookFoldPrinting = 1
    worddoc.ActiveWindow.Selection.Font.Size = 12
    worddoc.ActiveWindow.Selection.Font.Name="Times New Roman"
    worddoc.ActiveWindow.Selection.BoldRun()

    worddoc.ActiveWindow.Selection.TypeText(u"Расчет сечения")
    worddoc.ActiveWindow.Selection.TypeParagraph()
    worddoc.ActiveWindow.Selection.BoldRun()
    worddoc.ActiveWindow.Selection.TypeText(u"Сечение: "+unicode(lab))
    
    worddoc.ActiveWindow.Selection.TypeParagraph()
    
    temp=os.environ['TEMP']
    path=basa.pict(lab)
    shutil.copy2(path,temp) 
    
    dir_pict=str(temp+'\\'+basa.pict(lab)[17:])


    worddoc.ActiveWindow.Selection.InlineShapes.AddPicture(dir_pict)
    os.remove(dir_pict)


#        for i in sys.path:
#            if 'SortamentPicture' in os.listdir(i):
#                home=i
#                break
#        dir_pict=str(home+'\\'+basa.pict(lab))
#        worddoc.ActiveWindow.Selection.InlineShapes.AddPicture(dir_pict)
    worddoc.ActiveWindow.Selection.TypeParagraph()
    worddoc.ActiveWindow.Selection.TypeText(u"Исходные характеристики:")
    worddoc.ActiveWindow.Selection.TypeParagraph()


    location = worddoc.ActiveWindow.Selection.Range
    table = location.Tables.Add (location, 2, len(basa.input_data(lab)))
    table.ApplyStyleHeadingRows = 1
    table.AutoFormat(16)
    x=1
    for i in basa.input_data(lab):
        table.Cell(1,x).Range.InsertAfter(i)
        table.Cell(2,x).Range.InsertAfter(window.inputtable.item(0, x-1).text())
        x=x+1


    worddoc.ActiveWindow.Selection.MoveDown()
    worddoc.ActiveWindow.Selection.MoveDown()
    worddoc.ActiveWindow.Selection.TypeParagraph()
    worddoc.ActiveWindow.Selection.TypeText(u"Расчетные характеристики:")
    worddoc.ActiveWindow.Selection.TypeParagraph()
    worddoc.ActiveWindow.Selection.Font.Size = 10
    location2 = worddoc.ActiveWindow.Selection.Range

    output_table=window.outputtable
    lenght_table=output_table.columnCount()
    count_table=(lenght_table-0.5)//7+1

    table = location2.Tables.Add (location2, 2*count_table, 7)
    table.ApplyStyleHeadingRows = 1
    table.AutoFormat(16)

    for i in range(lenght_table):
        j=(i)//7+1
        z=(i+1)-(j-1)*7
#            print j, z
        table.Cell((j-1)*2+1,z).Range.InsertAfter(unicode(output_table.horizontalHeaderItem(i).text()))
        table.Cell((j-1)*2+2,z).Range.InsertAfter(unicode(output_table.item(0, i).text()))

    del wordapp
#    except:
#        window.messege.clear()
#        window.messege.insert(u"Ошибка экспорта")
#        del wordapp

def solve():
    window.messege.clear()
    try:
        lab=window.listWidget.currentItem().text()
        countcolumn=window.inputtable.columnCount()
        input_list=[]
        for i in range(0, countcolumn):

            if window.inputtable.item(0, i).text()=="":
                window.inputtable.item(0, i).setText("0")
            if "," in window.inputtable.item(0, i).text():
                text=window.inputtable.item(0, i).text()
                text=text.replace(',','.')
                window.inputtable.item(0, i).setText(text)

            input_list.append(float(window.inputtable.item(0, i).text().replace(',','.')))
        basa=BasaSort()
        pr=basa.output_data(lab, input_list)
        window.outputtable.setColumnCount(len(pr.output_list()))
        window.outputtable.setHorizontalHeaderLabels(pr.output_list())
        j=0
        for i in pr.output_list():
            if type(pr.output_dict()[i])==type(0.1):
                txt="%.2f"%(pr.output_dict()[i])
            else:
                txt=pr.output_dict()[i]
            window.outputtable.setItem(0,j,QtGui.QTableWidgetItem(txt))
            window.outputtable.item(0,j).setFlags(QtCore.Qt.ItemFlags(1+2+4+8+6+12+64))
            j=j+1
    except (ValueError, AttributeError, ZeroDivisionError):
        window.messege.clear()
        window.messege.insert(u"Ошибка исходных данных")
        window.wordbutton.setEnabled(False)

    else:
        window.messege.insert(u"Расчет выполнен успешно")
        window.wordbutton.setEnabled(True)



def table_clear():
    window.inputtable.clear()
    window.inputtable.setRowCount (1)
    window.outputtable.clear()
    window.outputtable.setRowCount (1)
    window.messege.clear()
    window.outputtable.setColumnCount(0)
    window.wordbutton.setEnabled(False)

def table_clear_output():
    window.messege.clear()
    window.messege.insert(u"Расчет НЕ выполнен")
    window.wordbutton.setEnabled(False)
def table_head():
    table_clear()
    lab=window.listWidget.currentItem().text()
    basa=BasaSort()
    input_data=basa.input_data(lab)
    window.inputtable.setColumnCount(len(input_data))
    window.inputtable.setHorizontalHeaderLabels(input_data)
    pict=basa.pict(lab)
    try:
        window.picture.setPixmap(QtGui.QPixmap(pict))
    except():
        window.messege.clear()
        window.messege.insert(u"Ошибка исходных данных")

    for i in range(0, window.inputtable.columnCount()):
        window.inputtable.setItem(0, i, QtGui.QTableWidgetItem(""))




if __name__=="__main__":
    import sys
    app=QtGui.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())


