# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 23:05:25 2014

@author: Pyltsin
"""
import win32com.client
import os
from  PyQt4 import QtCore, QtGui
import shutil

def printToWord(lst):
    wordapp = win32com.client.Dispatch("Word.Application")
    wordapp.Visible = 1
    worddoc = wordapp.Documents.Add()
    worddoc.PageSetup.Orientation = 1
    worddoc.PageSetup.BookFoldPrinting = 1
    worddoc.ActiveWindow.Selection.Font.Size = 12
    worddoc.ActiveWindow.Selection.Font.Name="Times New Roman"
#    worddoc.ActiveWindow.Selection.BoldRun()

    for item in lst:
#        print type(item)
#        print QtCore.QString(u'a') 
        if type(item)==QtGui.QLabel:
            pict=item.pixmap()
            print pict
            temp=os.environ['TEMP']
            path=temp+'\\temp_con1.jpg'           
            pict.save(path)
            worddoc.ActiveWindow.Selection.InlineShapes.AddPicture(path)
            os.remove(path)
            worddoc.ActiveWindow.Selection.TypeParagraph()
            worddoc.ActiveWindow.Selection.TypeParagraph()

            
        elif type(item)==QtCore.QString or type(item)==type(u'a'):
#            print 'tut1'
            worddoc.ActiveWindow.Selection.Font.Size = 12

            worddoc.ActiveWindow.Selection.BoldRun()
            
            worddoc.ActiveWindow.Selection.TypeText(unicode(item))
            worddoc.ActiveWindow.Selection.TypeParagraph()
            worddoc.ActiveWindow.Selection.BoldRun()
        elif type(item)==QtGui.QComboBox:
#            print 'tut2'

            worddoc.ActiveWindow.Selection.Font.Size = 12
            txt=unicode(item.currentText())
            worddoc.ActiveWindow.Selection.TypeText(txt)
            worddoc.ActiveWindow.Selection.TypeParagraph()
            
        elif type(item)==QtGui.QTableWidget:
#            print 'tut3'

            worddoc.ActiveWindow.Selection.Font.Size = 8

            worddoc.ActiveWindow.Selection.TypeParagraph()
            
            columnCount=item.columnCount()
            rowCount=item.rowCount()
            location = worddoc.ActiveWindow.Selection.Range
            table = location.Tables.Add (location, rowCount+1, columnCount+1)
            table.ApplyStyleHeadingRows = 1
            table.AutoFormat(16)
            #ставим заголовки горизонтальный
            for i in range(columnCount):

                if item.horizontalHeaderItem(i)!=None:
                    table.Cell(1,i+2).Range.InsertAfter(unicode(item.horizontalHeaderItem(i).text()))
                else:
                    table.Cell(1,i+2).Range.InsertAfter(unicode(str(i+1)))
                    
#            ставим заголовки вертикальный                
            for i in range(rowCount):
                if item.verticalHeaderItem(i)!=None:

                    table.Cell(i+2,1).Range.InsertAfter(unicode(item.verticalHeaderItem(i).text()))
                else:
                    table.Cell(i+2,1).Range.InsertAfter(unicode(str(i+1)))
            
            #пишем остальное
            
            for i in range(1, rowCount+1):
                for j in range(1, columnCount+1):
                    print i, j
                    if item.cellWidget(i-1,j-1)==None:
                        table.Cell(i+1,j+1).Range.InsertAfter(unicode(item.item(i-1,j-1).text()))
                    else:
                        widget=item.cellWidget(i-1,j-1)
                        txt=widget.currentText()
                        table.Cell(i+1,j+1).Range.InsertAfter(unicode(txt))

            for i in range(rowCount+3):
                worddoc.ActiveWindow.Selection.MoveDown()
#            worddoc.ActiveWindow.Selection.MoveDown(rowCount+1)
            worddoc.ActiveWindow.Selection.TypeParagraph()

            worddoc.ActiveWindow.Selection.TypeParagraph()
            
    del wordapp
            
            
    #        worddoc.ActiveWindow.Selection.BoldRun()
    #        worddoc.ActiveWindow.Selection.TypeText(u"Сечение: "+unicode(lab))
    #        worddoc.ActiveWindow.Selection.TypeParagraph()
        
        
#    for i in sys.path:
#        if 'SortamentPicture' in os.listdir(i):
#            home=i
#            break
#    dir_pict=str(home+'\\'+basa.pict(lab))
#    worddoc.ActiveWindow.Selection.InlineShapes.AddPicture(dir_pict)
#    worddoc.ActiveWindow.Selection.TypeParagraph()
#    worddoc.ActiveWindow.Selection.TypeText(u"Исходные характеристики:")
#    worddoc.ActiveWindow.Selection.TypeParagraph()
#
#
#    location = worddoc.ActiveWindow.Selection.Range
#    table = location.Tables.Add (location, 2, len(basa.input_data(lab)))
#    table.ApplyStyleHeadingRows = 1
#    table.AutoFormat(16)
#    x=1
#    for i in basa.input_data(lab):
#        table.Cell(1,x).Range.InsertAfter(i)
#        table.Cell(2,x).Range.InsertAfter(window.inputtable.item(0, x-1).text())
#        x=x+1
#
#
#    worddoc.ActiveWindow.Selection.MoveDown()
#    worddoc.ActiveWindow.Selection.MoveDown()
#    worddoc.ActiveWindow.Selection.TypeParagraph()
#    worddoc.ActiveWindow.Selection.TypeText(u"Расчетные характеристики:")
#    worddoc.ActiveWindow.Selection.TypeParagraph()
#    worddoc.ActiveWindow.Selection.Font.Size = 10
#    location2 = worddoc.ActiveWindow.Selection.Range
#
#    output_table=window.outputtable
#    lenght_table=output_table.columnCount()
#    count_table=(lenght_table-0.5)//7+1
#
#    table = location2.Tables.Add (location2, 2*count_table, 7)
#    table.ApplyStyleHeadingRows = 1
#    table.AutoFormat(16)
#
#    for i in range(lenght_table):
#        j=(i)//7+1
#        z=(i+1)-(j-1)*7
##            print j, z
#        table.Cell((j-1)*2+1,z).Range.InsertAfter(unicode(output_table.horizontalHeaderItem(i).text()))
#        table.Cell((j-1)*2+2,z).Range.InsertAfter(unicode(output_table.item(0, i).text()))
#
#        del wordapp
