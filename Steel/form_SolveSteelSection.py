# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 22:22:00 2014

@author: Pyltsin
"""

from  PyQt4 import QtCore, QtGui, uic

from steel import list_steel
import win32com.client
import os
from basa_sort import BasaSort
from key_press_event import copy_past
from py2word import printToWord
import sys
from py2save import save2file, load2form

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("gui/solve_steel_sectionv2.ui", self)
        self.basa=BasaSort()
        #загружаем код и связываем его изменение
        self.loadCode()
        self.boxCode.currentIndexChanged.connect(self.changeCode)

        #загружаем элементы и связываем его изменение

        self.loadElement()
        self.boxElement.currentIndexChanged.connect(self.changeElement)

        #загружаем тип расчета и связываем его изменение

        self.loadTypeSolve()
        self.boxTypeSolve.currentIndexChanged.connect(self.changeTypeSolve)
        
        #загружаем тип сечения и связываем его изменение

        self.loadTypeSection()
        self.boxTypeSection.currentIndexChanged.connect(self.changeTypeSection)

        #загружаем тип расчета и связываем его изменение

        self.loadFormSection()
        self.boxFormSection.currentIndexChanged.connect(self.changeFormSection)


        #загружаем сортаменты и связываем его изменение

        self.loadSortament()
        self.boxSortament.currentIndexChanged.connect(self.changeSortament)

        #загружаем элементы и связываем его изменение

        self.loadNumberSection()
        self.boxNumberSection.currentIndexChanged.connect(self.changeNumberSection)

        #загружаем сталь и связываем его изменение

        self.loadSteel()
        self.boxSteel.currentIndexChanged.connect(self.changeSteel)
        
        #загружаем таблицу и связываем его изменение

        self.loadTableInput()
        self.tableInput.currentItemChanged.connect(self.changeTableInput)
        #загружаем таблицу усилий и связываем его изменение
        self.loadTableLoad()
        self.tableLoad.currentItemChanged.connect(self.changeTableLoad)
        self.tableLoad.itemChanged.connect(self.changeTableLoad)

        #загружаем рисунок
        self.loadPicture()
        
        #на всякий случай сбрасываем выходные данные
        self.changeInputData()
        
        #связываем счетчик с дейтсвиями
        self.boxCountLoad.valueChanged.connect(self.changeCountTableLoad)
        self.boxCountLoad.setValue(1)
        
        self.changeCountTableLoad()

        self.buttonSolve.clicked.connect(self.solve)
        
 # ставим тип сечения -фермаЖ
        self.boxElement.setCurrentIndex(0)
        self.loadTableInput()

#Сохранение/открытие файлов
#выбор рабочей папки
        self.buttonFolder.clicked.connect(self.show_dia_folder)

#направляем на открытие:
        self.listFiles.itemDoubleClicked.connect(self.loadFiles)
        
#устанавливаем начальный путь
        self.load_list_files('c:\\') 
        self.textFolder.clear()
        self.textFolder.insert('c:\\')
    
#Сохраняем файл
        self.buttonSave.clicked.connect(self.toSave)     

#в ворд
        self.buttonWord.clicked.connect(self.toWord)     

    def solve(self):
        """Расчет сам: выход в два списка - один в таблицу решения, один в общий вывод"""
        #собираем все данные
        code=self.boxCode.currentText()
        element=self.boxElement.currentText()
        typeSolve=self.boxTypeSolve.currentText()
        typeSection=self.boxTypeSection.currentText() 
        formSection=self.boxFormSection.currentText() 
        sortament=self.boxSortament.currentText() 
        numberSection=self.boxNumberSection.currentText() 
        steel=self.boxSteel.currentText() 
        addData=self.basa.add_data_sostav(formSection)
        

        if addData!=[]:         
            lenAddData=len(addData[0])
        else:
            lenAddData=0

#        print formSection
#        print addData


        #простые данные собрали, теперь собираем данные из таблиц и обрабатываем, если что - экстеншин

        class errorData():pass 
        class errorSteel():pass 
            
        try:
            #сначала собираем данные для addData
            lstAddData=[]

            if lenAddData>0:
                for i in range(lenAddData):
                    
                    text=self.tableInput.item(i,0).text()
                    if "," in text:
                        text=text.replace(',','.')
                    text=float(text)
                    self.tableInput.item(i,0).setText(str(text))

                    if text>=addData[1][0] and  text<=addData[1][1]:
                        lstAddData.append(text)
                    else:
                        raise(errorData)
            
            #собираем остальные данные
            inputData=self.basa.lstInputDataPP(code, element)
            lenInputData=len(inputData)
            lstInputData=[]
            for i in range(lenInputData):
                j=i+lenAddData
                #сначала widget
#                print self.tableInput.cellWidget(j,0)
                if self.tableInput.cellWidget(j,0)!=None:
                    wid=self.tableInput.cellWidget(j,0)
                    lstInputData.append(wid.currentIndex()+1)
                else:
#                    print j, i, lenAddData
                    #потом остальное
                    text=self.tableInput.item(j,0).text()
                    if "," in text:
                        text=text.replace(',','.')
                    text=float(text)
                    self.tableInput.item(j,0).setText(str(text))

#                    print text
                    if text>=inputData[i][1][0] and  text<=inputData[i][1][1]:
                        lstInputData.append(text)
                    else:
                        raise(errorData)
            
#            print lstInputData, lstAddData

#            '''собираем нагрузки'''
            lstForce=[]
            countColumnLoad=self.tableLoad.columnCount()            
            countRowLoad=self.tableLoad.rowCount() 
            for i in range(countRowLoad):
                lstRow=[]
                for j in range(countColumnLoad):
                    if self.tableLoad.item(i,j)==None or self.tableLoad.item(i,j).text()=='':
                        self.tableLoad.setItem(i, j, QtGui.QTableWidgetItem(""))
                        self.tableLoad.item(i,j).setText('0')
                    text=self.tableLoad.item(i,j).text()
                    if "," in text:
                        text=text.replace(',','.')
                    text=float(text)
                    self.tableLoad.item(i,j).setText(str(text))

                    lstRow.append(text)
                lstForce.append(lstRow)                    
                    
#            lstIn=code, element, typeSolve,typeSection,formSection,sortament,numberSection,steel,lstAddData, lstInputData, lstForce
#            print lstIn
            out=self.basa.solvePP(code, element, typeSolve,typeSection,formSection,sortament,numberSection,steel,lstAddData, lstInputData, lstForce)
#            print out
            
            if out==0:
                raise errorSteel
            #заполняем таблицу усилий
            self.tabOutputData.setEnabled(True)
            numColumn=len(out[1][0])
            numRow=len(out[1])-1
            self.tableOutLoad.setColumnCount(numColumn)
            self.tableOutLoad.setRowCount(numRow)
#            print out[1]
            self.tableOutLoad.setHorizontalHeaderLabels(out[1][0])
            
            for i in range(numRow):
                for j in range(numColumn):
                    if type(out[1][i+1][j])==type(1.0) or type(out[1][i+1][j])==type(1):
                        txt="%.2f"%(out[1][i+1][j])
                    else:
                        txt=out[1][i+1][j]
#                    print i, j
                    self.tableOutLoad.setItem(i, j, QtGui.QTableWidgetItem(""))
                    self.tableOutLoad.item(i,j).setText(txt)
                    self.tableOutLoad.item(i,j).setFlags(QtCore.Qt.ItemFlags(1+2+4+8+6+12+64))


        #заполняем таблицу K исп
            self.tabGeneralOutputData.setEnabled(True)
            self.tabWidget.setCurrentIndex(3)
            
            numRow=len(out[2])
            verticalHeader=[]
            for i in out[2]:
                verticalHeader.append(i[0])
#            print verticalHeader
            self.tableOutK.setRowCount(numRow)
            self.tableOutK.setColumnCount(1)
            self.tableOutK.setVerticalHeaderLabels(verticalHeader)
            self.tableOutK.setHorizontalHeaderLabels([''])
            
#            print out[2]
            j=-1
            for i in out[2]:
                j+=1                
#                print i
                if type(i[1])==type(1.0):
                    txt="%.2f"%(i[1])

                elif type(i[1])==type(1):
                    txt="%.0f"%(i[1])

                else:
                    txt=i[1]
#                    print i, j
                self.tableOutK.setItem(j, 0, QtGui.QTableWidgetItem(""))
                self.tableOutK.item(j,0).setText(txt)
                self.tableOutK.item(j,0).setFlags(QtCore.Qt.ItemFlags(1+2+4+8+6+12+64))
            
            #Ставим - проходит/не проходит сечение
            if out[0][0]>1:
                self.labelComment.setText(u'Требования норм НЕ обеспечены')
                self.labelComment.setStyleSheet("background: red")
            else:
                self.labelComment.setText(u'Требования норм обеспечены')
                self.labelComment.setStyleSheet("background: green")
                
            #заполняем последнюю таблицу
            numRow=len(out[3])
            verticalHeader=[]
            for i in out[3]:
                verticalHeader.append(i[1])
#            print verticalHeader
            self.tableOutGeneral.setRowCount(numRow)
            self.tableOutGeneral.setColumnCount(1)
            self.tableOutGeneral.setVerticalHeaderLabels(verticalHeader)
            self.tableOutGeneral.setHorizontalHeaderLabels([''])
            
#            print out[2]
            j=-1
            for i in out[3]:
                j+=1                
#                print i
                if type(i[0])==type(1.0):
                    txt="%.2f"%(i[0])

                elif type(i[0])==type(1):
                    txt="%.0f"%(i[0])

                else:
                    txt=i[0]
#                    print i, j
                self.tableOutGeneral.setItem(j, 0, QtGui.QTableWidgetItem(""))
                self.tableOutGeneral.item(j,0).setText(txt)
                self.tableOutGeneral.item(j,0).setFlags(QtCore.Qt.ItemFlags(1+2+4+8+6+12+64))
                
                
            
        except errorData:
            self.labelComment.setText(u'Выход за границы допустимых значений')
            self.labelComment.setStyleSheet("background: yellow")
        except ValueError:
            self.labelComment.setText(u'Недопустимые исходные данные')
            self.labelComment.setStyleSheet("background: yellow")
        except errorSteel:
            self.labelComment.setText(u'Не найдены значения стали для профиля')
            self.labelComment.setStyleSheet("background: yellow")
        else:
            self.buttonWord.setEnabled(True)
            self.buttonSave.setEnabled(True)

            

        

    def keyPressEvent(self, e):
        """обеспечивает возможность копирования, вставить"""
        copy_past(e, [window.tableInput, window.tableLoad], [window.tableOutLoad, window.tableOutK, window.tableOutGeneral], window)

        
    def loadComboBox(self, widget, lst):
        '''load ComboBox'''
        widget.clear()
        widget.addItems(lst)
        
    def changeInputData(self):
        '''Делать, когда изменились данные'''
        self.tabOutputData.setEnabled(False)
        self.tableOutLoad.clear()
        self.tabGeneralOutputData.setEnabled(False)
        self.labelComment.setText(u'Исходные данные изменились')
        self.labelComment.setStyleSheet("background: white")

        self.buttonWord.setEnabled(False)
        self.buttonSave.setEnabled(False)

    
    def loadCode(self):
        '''загружаем и ставим список норм'''
        lst=self.basa.list_code()
        self.loadComboBox(self.boxCode, lst)

    def changeCode(self):
        '''Делаем когда изменились нормы,
        1. Меняем список стали
        2. Делаем стандартные действия'''
        self.loadSteel()
        self.changeInputData()


    def loadElement(self):
        '''загружаем и ставим список элементов'''
        tempLst=self.basa.output_list_elements()
        lst=[]
        for i in tempLst:
            lst.append(i[0])
#        print lst
        self.loadComboBox(self.boxElement, lst)

    def changeElement(self):
        '''делаем когда изменился тип элемента:
        1. меняем список форму сечения
        2. меняем таблицу входных данных
        3. меняем таблицу усилий
        4. делаем стандартные дейтсивя'''
        
        self.loadFormSection()
        self.loadTableInput()
        self.loadTableLoad()
        self.changeInputData()

    def loadTypeSolve(self):
        '''загружаем и ставим список расчетов - подбор и проверка'''
#        lst=[u'Проверка', u'Подбор']
        lst=[u'Проверка']

        self.loadComboBox(self.boxTypeSolve, lst)

    def changeTypeSolve(self):
        '''делаем когда изменился тип расчета:
        1. если подбор - заблокировать выбор номера сечения
        2. делаем стандартные дейтсивя'''
        flag=self.boxTypeSolve.currentIndex()
        if flag==0:
            self.boxNumberSection.setEnabled(True)
            self.loadNumberSection()
        elif flag==1:
            self.boxNumberSection.setEnabled(False)
            self.boxNumberSection.clear()
        self.changeInputData()

    def loadTypeSection(self):
        '''загружаем и ставим тип сечения'''
        lst=[u'Прокат']
        self.loadComboBox(self.boxTypeSection, lst)


    def changeTypeSection(self):
        'Пока ничего не делаем'
        pass

    def loadFormSection(self):
        '''загружаем и ставим форму сечения'''

        element=self.boxElement.currentText()
        lst=self.basa.output_list_section(element)
        self.loadComboBox(self.boxFormSection, lst)

    def changeFormSection(self):
        '''делаем когда изменился тип расчета:
        1. загрузить список сортаментов
        2. меняем рисунок
        3. делаем стандартные дейтсивя'''
        self.loadSortament()        
        self.loadPicture()        
        self.changeInputData()
        self.loadTableInput()
        


    def loadSortament(self):
        '''загружаем и ставим список сортаментов'''
        formSection=self.boxFormSection.currentText()
        lstSortament=self.basa.output_list_sortament(formSection)
        self.loadComboBox(self.boxSortament, lstSortament)


    def changeSortament(self):
        '''делаем когда изменился тип расчета:
        1. загрузить список сортаментов
        2. делаем стандартные дейтсивя'''
        self.loadNumberSection()
        self.changeInputData()

    def loadNumberSection(self):
        '''загружаем и ставим список профилей, если элемент активен'''
        if self.boxNumberSection.isEnabled():
            formSection=self.boxFormSection.currentText()
            sortament=self.boxSortament.currentText()
            lstNumberSection=self.basa.output_list_sect_num(sortament, formSection)
            self.loadComboBox(self.boxNumberSection, lstNumberSection)

    def changeNumberSection(self):
        '''делаем когда изменился номер профиоя:
        1. делаем стандартные дейтсивя'''
        self.changeInputData()
    
        
        
    def loadSteel(self):
        '''загружаем и ставим список стали'''
        code=self.boxCode.currentText()
        lstSteel=list_steel(code=code,typ_steel='prokat').get_list()
#        print lstSteel
        self.loadComboBox(self.boxSteel, lstSteel)

    def changeSteel(self):
        '''делаем когда изменилась сталь:
        1. делаем стандартные дейтсивя'''
        self.changeInputData()

    def loadTableInput(self):
        
        '''загружаем данные в таблицу'''
        self.tableInput.clear()
        code=self.boxCode.currentText()
        element=self.boxElement.currentText()
        lst=self.basa.lstInputDataPP(code, element)
        formSection=self.boxFormSection.currentText()
        
        addDataForm=self.basa.add_data_sostav(formSection)
#        print lst
#        ln=len(lst)
        
        if addDataForm!=[]:
            name=addDataForm[0][:]
        else:
            name=[]
        i=len(name)-1
            
        for num in lst:
            i+=1
            if type(num[1][0])==type(0.10) or type(num[1][0])==type(1):
                self.tableInput.setItem(i, 0, QtGui.QTableWidgetItem(""))
            else:
#                print num[1]
                userWidget=QtGui.QComboBox()
                self.loadComboBox(userWidget, num[1])
                self.tableInput.setCellWidget(i,0,userWidget)
                
            name.append(num[0])

        self.tableInput.setRowCount(len(name))
            
        self.tableInput.setVerticalHeaderLabels(name)
            

    
    def changeTableInput(self):
        '''делаем когда изменилась таблица:
        1. делаем стандартные дейтсивя'''
        self.changeInputData()

    def loadTableLoad(self):
        '''загружаем таблицу усилий '''

        self.tableLoad.clear()
        code=self.boxCode.currentText()
        element=self.boxElement.currentText()
        lst=self.basa.lstLoadDataPP(code, element)
        self.tableLoad.setColumnCount(len(lst))
        self.tableLoad.setHorizontalHeaderLabels(lst)

    def changeTableLoad(self):
        '''делаем когда изменилась таблица:
        1. делаем стандартные дейтсивя'''
        self.changeInputData()


    def loadPicture(self):
        '''загружаем рисунок'''
        lab=self.boxFormSection.currentText()
        if lab!="":
#            print lab
            pict=self.basa.pict(lab)
            self.labelPicture.setPixmap(QtGui.QPixmap(pict))    

    def changeCountTableLoad(self):
        '''изменяем кол-во строк при изенении счетчика'''
        i=self.boxCountLoad.value()
        self.tableLoad.setRowCount(i)
        self.changeInputData()


    def show_dia_folder(self):
        """отправляет список файлов, которые можно открыть в окно"""
        folder_name = QtGui.QFileDialog.getExistingDirectory(self, 'Open Folfer', self.textFolder.text())
        if folder_name!='':
            self.textFolder.clear()
            self.textFolder.insert(folder_name)
            self.load_list_files(folder_name)
       
    def load_list_files(self, folder_name):
        if folder_name!='':        
            raw_list_files=os.listdir(folder_name)
            list_files=[]
            for x in raw_list_files:
                if x[-5:]=='.con2':
                    list_files.append(unicode(x))
                
                
            self.listFiles.clear()
            self.listFiles.addItems(list_files)


    def loadFiles(self):
        folder=self.textFolder.text()
        fil_name=self.listFiles.currentItem().text()
        fil=folder+str(u"\\")+fil_name

#        try:
        lst=[self.boxCode, self.boxElement, self.boxTypeSolve, self.boxTypeSection,self.boxFormSection, self.boxSortament, 
             self.boxNumberSection, self.boxSteel,self.tableInput,self.boxCountLoad, self.tableLoad, self.tableOutLoad, self.tableOutK, self.tableOutGeneral]        
        load2form(fil, lst)
        self.changeInputData()
#        except:
#            self.labelComment.clear()
#            self.labelComment.setText(u'Ошибка чтения')
#            self.labelComment.setStyleSheet("background: yellow")
        self.textName.setText(fil_name[:-5])
            
    def toSave(self):
        lst=[self.boxCode, self.boxElement, self.boxTypeSolve, self.boxTypeSection,self.boxFormSection, self.boxSortament, 
             self.boxNumberSection, self.boxSteel,self.tableInput,self.boxCountLoad, self.tableLoad, self.tableOutLoad, self.tableOutK, self.tableOutGeneral]        

        '''сохраняем данные в файл, в указанную папку, имя==название 1-го элемента,
        если такой файл уже есть - спрашиваем про перезапись, после записи обновляем список файлов'''
        #1 - получаем путь и имя файла
        folder=self.textFolder.text()
        if self.textName.text()!='':
            
            fil_name=unicode(self.textName.text()).rstrip()+'.con2'
        else:
            fil_name=u'1.con2'
            self.textName.setText('1')
            
        if folder[-2:]==":\\":
            fil=folder+fil_name
        else:
            fil=folder+str("\\")+fil_name
        #спрашиваем про перезапись файлов
        raw_list_files=os.listdir(folder)
#        print fil_name
#        print raw_list_files
        
        if fil_name in raw_list_files:
#            print 'tut'
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'Перезапись файла')
            msgBox.setText(u'Файл существует, перезаписать?')
            msgBox.addButton(QtGui.QPushButton(u'Да'), QtGui.QMessageBox.YesRole)
            msgBox.addButton(QtGui.QPushButton(u'Нет'), QtGui.QMessageBox.NoRole)
            ret = msgBox.exec_()
            if ret==0:
                try:
                    save2file(fil, lst)
                except(IOError):
                    self.labelComment.clear()
                    self.labelComment.insert(u'Ошибка записи, файл возможно создан с ошибкой')
                    self.labelComment.setStyleSheet("background: yellow")
                    

        else:
            try:
                save2file(fil, lst)
            except(IOError):
                self.labelComment.clear()
                self.labelComment.insert(u'Ошибка записи, файл возможно создан с ошибкой')
                self.labelComment.setStyleSheet("background: yellow")
        
        #обновляем список файлов
        self.load_list_files(folder)
            
    def toWord(self):
        '''импорт в ворд'''
        if self.boxCountLoad.value()<100 and self.boxElement.currentIndex()!=2:
            lst=['Расчет сечения',self.boxCode, self.boxElement, self.boxTypeSolve, self.boxTypeSection,self.boxFormSection, self.boxSortament, 
                 self.boxNumberSection, self.boxSteel,self.tableInput, self.tableLoad, self.tableOutLoad, self.tableOutK, self.tableOutGeneral]  
        elif self.boxCountLoad.value()<100 and self.boxElement.currentIndex()!=2:
            lst=['Расчет сечения',self.boxCode, self.boxElement, self.boxTypeSolve, self.boxTypeSection,self.boxFormSection, self.boxSortament, 
                 self.boxNumberSection, self.boxSteel,self.tableInput, self.tableLoad, self.tableOutK, self.tableOutGeneral]  
        else:
            lst=['Расчет сечения',self.boxCode, self.boxElement, self.boxTypeSolve, self.boxTypeSection,self.boxFormSection, self.boxSortament, 
                 self.boxNumberSection, self.boxSteel,self.tableInput,  self.tableOutK, self.tableOutGeneral]  
            

#        lst=[u'Расчет сечения',self.boxCode, self.boxElement, self.boxTypeSolve, self.boxTypeSection,self.boxFormSection, self.boxSortament, 
#             self.boxNumberSection, self.boxSteel, self.labelPicture, self.tableInput, self.tableLoad, self.tableOutLoad, self.tableOutK, self.tableOutGeneral]            
#    
        printToWord(lst)
    
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())
