# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 18:55:48 2014

@author: Pyltsin
"""

from  PyQt4 import QtCore, QtGui, uic
from math import sin, cos, sqrt, tan
import win32com.client
import os
import sys
import rcMaterial
from key_press_event import copy_past

import matplotlib
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.mlab import griddata

import rcSolves

import numpy as np
from scipy.spatial import ConvexHull


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):

        self.listSection = [u'Прямоугольник', u'Двутавр', u'Круг']
        self.listSectionRein = [[u'Угловое', u'По периметру', u'Равное сверху/снизу', u'Сверху и снизу', u'Свободное'],
                                [u'Сверху/снизу', u'Свободное'], [u'По кругу', u'Свободное']]
        self.listSectionProp = [[u'h, см', u'b, см'],
                                [u'b1, см', u'b2, см', u'b3, см', u'h1, см', u'h2, см', u'h3, см'], [u'd, см']]
        self.listSectionReinPropCheck = [
            [[u'a, см', u'd, мм'],
             [u'n1', u'n2', u'a, см', u'd, мм'],
             [u'n1', u'a, см', u'd, мм'],
             [u'n1', u'n2', u'a1, см', u'a2, см', u'd1, мм', u'd2, мм']
             ],
            [[u'n1', u'n2', u'a1, см', u'a2, см', u'd1, мм', u'd2, мм']
             ],
            [[u'n1', u'a, см', u'd, мм']]
        ]

        self.listSectionReinPropFind = [
            [[u'a, см'],
             [u'a, см'],
             [u'a, см'],
             [u'a1, см', 'a2, см']
             ],
            [[u'a1, см', 'a2, см']
             ],
            [[u'a, см']]
        ]

        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("gui/solve_concrete_section.ui", self)

        #        связывеам нормы с материалами - ппока только отечественные нормы
        self.boxCode.currentIndexChanged.connect(self.changeCode)
        self.changeCode()

        self.boxTypeSection.currentIndexChanged.connect(self.changeTypeSection)
        self.changeTypeSection()

        self.boxTypeSolve.currentIndexChanged.connect(self.changeTypeSolve)
        self.changeTypeSolve()

        #       связываем галочки прочность и трещиностойкость
        self.checkBoxPS1.clicked.connect(self.changeCheckBoxSolve)
        self.checkBoxPS2.clicked.connect(self.changeCheckBoxSolve)
        self.checkBoxD.clicked.connect(self.changeCheckBoxSolve)
        self.changeCheckBoxSolve()


        # загружаем формы

        self.boxFormConc.currentIndexChanged.connect(self.changeForm)
        self.loadComboBox(self.boxFormConc, self.listSection)

        self.boxFormRein.currentIndexChanged.connect(self.changeRein)
        self.changeRein()

        # рисуем формы если могем
        self.buttonDraw.clicked.connect(self.drawForm)
        # связываем кнопку по умолчанию 1 пс
        self.buttonPS1.clicked.connect(self.PS1Reset)
        self.PS1Reset()
        # связываем счетчик с дейтсвиями
        self.boxCountLoadPS1.valueChanged.connect(self.changeCountTableLoadPS1)
        self.boxCountLoadPS1.setValue(1)

        self.boxCountLoadPS2.valueChanged.connect(self.changeCountTableLoadPS2)
        self.boxCountLoadPS2.setValue(1)

        self.changeCountTableLoadPS1()
        self.changeCountTableLoadPS2()

        # связываем изменения с функцией изменения
        self.tableFormConc.itemChanged.connect(self.changed)
        self.tableFormConc.itemChanged.connect(self.changed)
        self.tableFormRein.itemChanged.connect(self.changed)
        self.boxCodeConc.currentIndexChanged.connect(self.changed)
        self.boxCodeRein.currentIndexChanged.connect(self.changed)

        self.spinBoxPhi.valueChanged.connect(self.changed)

        self.doubleBoxYbi.valueChanged.connect(self.changed)
        self.doubleBoxYsi.valueChanged.connect(self.changed)
        self.boxNx.valueChanged.connect(self.changed)
        self.boxNy.valueChanged.connect(self.changed)

        self.tableLoadPS1.itemChanged.connect(self.changed)
        self.tableLoadPS2.itemChanged.connect(self.changed)

        # связываем изменение в пункте расчета
        self.boxPS1ShortChar.currentIndexChanged.connect(self.changed)
        self.boxPS1Short.currentIndexChanged.connect(self.changed)
        self.boxPS1ShortDia.currentIndexChanged.connect(self.changed)
        self.boxPS1ShortRt.currentIndexChanged.connect(self.changed)

        self.boxPS1LongChar.currentIndexChanged.connect(self.changed)
        self.boxPS1Long.currentIndexChanged.connect(self.changed)
        self.boxPS1LongDia.currentIndexChanged.connect(self.changed)
        self.boxPS1LongRt.currentIndexChanged.connect(self.changed)

        self.doubleBoxTol.valueChanged.connect(self.changed)
        self.boxNum.valueChanged.connect(self.changed)
        self.boxStatOpr.currentIndexChanged.connect(self.changed)

        self.doubleBoxLx.valueChanged.connect(self.changed)
        self.doubleBoxLy.valueChanged.connect(self.changed)
        self.doubleBoxL.valueChanged.connect(self.changed)


        # кнопка расчета
        self.buttonSolve.clicked.connect(self.solve)

        # показать графики
        self.buttonGrafConcreteShort.clicked.connect(self.grafConcreteShort)
        self.buttonGrafConcreteLong.clicked.connect(self.grafConcreteLong)
        self.buttonGrafReinShort.clicked.connect(self.grafReinShort)
        self.buttonGrafReinLong.clicked.connect(self.grafReinLong)

        # временная
        self.pushButton_2.clicked.connect(self.reset)
        # графики
        self.buttonPlotPS1Short.clicked.connect(self.diaShortPlot)
        self.buttonPlotPS1Long.clicked.connect(self.diaLongPlot)

    def diaShortPlot(self):
        # определяем что печатать - то что выделено
        table = self.tableResPS1Short
        flagBox = self.comboBoxShort
        canPlot = self.mplResPS1Short

        self.diaPlot(table, flagBox, canPlot)

    def diaLongPlot(self):
        # определяем что печатать - то что выделено
        table = self.tableResPS1Long
        flagBox = self.comboBoxLong
        canPlot = self.mplResPS1Long

        self.diaPlot(table, flagBox, canPlot)

    def diaPlot(self, table, flagBox, canPlot):
        flag = flagBox.currentIndex()
        curRow = table.currentRow()
        if curRow == -1:
            curRow = 0

        e0 = float(table.item(curRow, 5).text())
        rx = float(table.item(curRow, 6).text())
        ry = float(table.item(curRow, 7).text())

        slv = SolveWindow(self)

        bol = slv.loadFormMatSimple()
        if bol == False:
            return False

        if flag == 0:
            z = slv.solve.e0rxry2e(e0, rx, ry)
        if flag == 1:
            e = slv.solve.e0rxry2e(e0, rx, ry)
            z = slv.solve.e2sigma4(e)

        matrX = []
        matrY = []
        matrZ = []
        for i in range(len(slv.solve.elemMatrC[0])):
            if i == 0:
                b = abs(slv.solve.elemMatrC[0][i + 1] - slv.solve.elemMatrC[0][i])
                h = slv.solve.elemMatrC[3][i] / b
            elif i == len(slv.solve.elemMatrC[0]) - 1:
                b = abs(slv.solve.elemMatrC[0][i] - slv.solve.elemMatrC[0][i - 1])
                h = slv.solve.elemMatrC[3][i] / b
            else:
                b1 = abs(slv.solve.elemMatrC[0][i + 1] - slv.solve.elemMatrC[0][i])
                b2 = abs(slv.solve.elemMatrC[0][i] - slv.solve.elemMatrC[0][i - 1])
                b = min([b1, b2])
                h = slv.solve.elemMatrC[3][i] / b
            x = slv.solve.elemMatrC[0][i]
            y = slv.solve.elemMatrC[1][i]

            matrX.append(x - b / 2. * 0.8)
            matrX.append(x - b / 2. * 0.8)
            matrX.append(x + b / 2. * 0.8)
            matrX.append(x + b / 2. * 0.8)

            matrY.append(y - h / 2. * 0.8)
            matrY.append(y + h / 2. * 0.8)
            matrY.append(y - h / 2. * 0.8)
            matrY.append(y + h / 2. * 0.8)

            matrZ.append(z[i])
            matrZ.append(z[i])
            matrZ.append(z[i])
            matrZ.append(z[i])

        matrX = np.asarray(matrX, order='F')
        matrY = np.asarray(matrY, order='F')

        matrZ = np.array(matrZ)
        print matrX, matrY
        # мешим секцию
        fig = canPlot.figure
        ax = fig.gca(projection='3d')
        ax.clear()
        surf = ax.plot_trisurf(matrX, matrY, matrZ, cmap=cm.terrain, linewidth=0.1)
        canPlot.draw()

    def reset(self):
        self.labelComment.setText(u'Данные cброшены')
        self.labelComment.setStyleSheet("background: green")

    def grafConcreteShort(self):
        '''график бетона'''
        slv = SolveWindow(self)
        item = slv.initMatSimple()[0][0]
        self.plotMatSimpleWindow(item)

    def grafConcreteLong(self):
        '''график бетона'''
        slv = SolveWindow(self)

        item = slv.initMatSimple()[1][0]
        self.plotMatSimpleWindow(item)

    def grafReinShort(self):
        '''график арматуры'''
        slv = SolveWindow(self)

        item = slv.initMatSimple()[0][1]
        self.plotMatSimpleWindow(item)

    def grafReinLong(self):
        '''график арматуры'''
        slv = SolveWindow(self)

        item = slv.initMatSimple()[1][1]
        self.plotMatSimpleWindow(item)

    def plotMatSimpleWindow(self, mat):
        '''пишем материал в новом окне'''
        lst = []
        #        print mat.x
        #        print mat.y
        for i in range(len(mat.x)):
            if 1 > abs(mat.x[i]):
                lst.append([mat.x[i], mat.y[i]])
        array = np.array(lst)

        fig = self.mplGrafMat.figure
        ax = fig.add_subplot(111)
        ax.clear()

        ax.plot(array[:, 0], array[:, 1])
        self.mplGrafMat.draw()

    def solve(self):
        slv = SolveWindow(self)
        bol = slv.critSolve()
        if bol == False:
            return False

        bol = slv.loadFormMatSimple()
        if bol == False:
            return False

        if self.checkBoxPS1.isChecked() == True:

            bol = slv.DSolve()
            if bol == False:
                return False

            bol = slv.solvePS1()

            if bol == False:
                return False

            self.tabResPS1.setEnabled(True)

        if self.checkBoxPS2.isChecked() == True:
            bol = slv.solvePS2()

    def keyPressEvent(self, e):
        """обеспечивает возможность копирования, вставить"""
        copy_past(e, [window.tableLoadPS1, window.tableLoadPS2], [], window)

    def changeCountTableLoadPS1(self):
        self.changeCountTableLoad(self.boxCountLoadPS1.value(), self.tableLoadPS1)

    def changeCountTableLoadPS2(self):
        self.changeCountTableLoad(self.boxCountLoadPS2.value(), self.tableLoadPS2)

    def changeCountTableLoad(self, i, widget):
        '''изменяем кол-во строк при изенении счетчика'''
        widget.setRowCount(i)
        for j in range(widget.rowCount()):
            for k in range(widget.columnCount()):
                if widget.item(j, k) == None:
                    widget.setItem(j, k, QtGui.QTableWidgetItem('0'))

    def PS1Reset(self):
        '''сбрасываем на умолчание'''
        self.boxPS1ShortChar.setCurrentIndex(0)
        self.boxPS1ShortDia.setCurrentIndex(0)
        self.boxPS1ShortRt.setCurrentIndex(0)
        self.boxPS1Short.setCurrentIndex(0)

        self.boxPS1LongChar.setCurrentIndex(0)
        self.boxPS1LongDia.setCurrentIndex(0)
        self.boxPS1LongRt.setCurrentIndex(0)
        self.boxPS1Long.setCurrentIndex(1)

        self.doubleBoxTol.setValue(0.001)
        self.boxNum.setValue(100)

    def drawForm(self):
        '''v1 получаем список и рисуем картинку'''
        slv = SolveWindow(self)
        lst = slv.getLstFormSimple()

        if lst != 'Error':
            fig = self.mplForm.figure
            ax = fig.add_subplot(111)
            ax.clear()
            for i in lst:
                if i[0] == 'Rectangle':
                    rect = mpatches.Rectangle((i[1][0][0], i[1][0][1]), i[1][1][0] - i[1][0][0],
                                              i[1][1][1] - i[1][0][1])

                    ax.add_patch(rect)

                elif i[0] == 'Circle':
                    circle = mpatches.Circle((i[1][0], i[1][1]), radius=i[1][2] / 2., color=[0., 1, 0])

                    ax.add_patch(circle)
                elif i[0] == 'SolidCircle':
                    circle = mpatches.Circle((i[1][0], i[1][1]), radius=i[1][2] / 2., color=[1, 0.0, 0.0])

                    ax.add_patch(circle)

            ax.relim()
            ax.autoscale_view(tight=True, scalex=True, scaley=True)
            self.mplForm.draw()
            # получаем границы
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()
            #            print xlim
            if xlim[1] - xlim[0] > ylim[1] - ylim[0]:
                ylim0 = (ylim[0] + ylim[1]) / 2. - (xlim[1] - xlim[0]) / 2.
                ylim1 = (ylim[0] + ylim[1]) / 2. + (xlim[1] - xlim[0]) / 2.
                ax.set_ylim(ylim0, ylim1)
            else:
                xlim0 = (xlim[0] + xlim[1]) / 2. - (ylim[1] - ylim[0]) / 2.
                xlim1 = (xlim[0] + xlim[1]) / 2. + (ylim[1] - ylim[0]) / 2.
                ax.set_xlim(xlim0, xlim1)
            self.mplForm.draw()

        else:
            self.error('Data')

    def error(self, sign):
        self.labelComment.setText(u'Error:' + str(sign))
        self.labelComment.setStyleSheet("background: red")

    def changed(self):
        '''Ловиться только изменения общих данных, и стандартное сечение'''
        self.labelComment.setText(u'Данные изменились')
        self.labelComment.setStyleSheet("background: yellow")

        #        self.tabDShort.setEnabled(False)
        #        self.tabDLong.setEnabled(False)
        #
        #
        #        self.tabCrShort.setEnabled(False)
        self.tabCr1PS.setEnabled(False)

        self.tabCrNorm.setEnabled(False)

        self.tabResPS1.setEnabled(False)

    #        print 'Error:', sign

    def changeForm(self):
        '''v1 загружаем данные для ввода 
        и заодно способ ввода арматуры'''
        self.changed()
        index = self.boxFormConc.currentIndex()
        self.loadComboBox(self.boxFormRein, self.listSectionRein[index])

        self.loadTable(self.tableFormConc, self.listSectionProp[index], [''])

    def changeRein(self):
        '''v1 загружаем форму для ввода'''
        indFormConc = self.boxFormConc.currentIndex()
        indFormRein = self.boxFormRein.currentIndex()
        lstFreeRein = [u'x, см', u'y, см', u'd, мм']
        lstD = []
        for i in range(30):
            lstD.append(str(i + 1))

        if self.boxTypeSolve.currentIndex() == 0:  # только проверка
            if indFormRein == len(self.listSectionRein[indFormConc]) - 1:
                self.loadTable(self.tableFormRein, lstD, lstFreeRein)  # грузим свободну арматуру
            else:
                self.loadTable(self.tableFormRein, self.listSectionReinPropCheck[indFormConc][indFormRein],
                               [''])  # грузим список

    def changeCheckBoxSolve(self):
        '''v1 работает при изменении что и как считаем'''
        #        первый случай - нет галок вообще
        if self.checkBoxPS1.isChecked() == False and self.checkBoxPS2.isChecked() == False:
            self.checkBoxPS1.setChecked(True)
            self.checkBoxD.setChecked(False)
            self.changeCheckBoxSolve()
        #   если расчет прочности галка стоит:
        if self.checkBoxPS1.isChecked() == True:
            self.checkBoxD.setEnabled(True)
        else:
            self.checkBoxD.setEnabled(False)
            self.checkBoxD.setChecked(False)

        self.changeSolvePS1(self.checkBoxPS1.isChecked())
        self.changeSolvePS2(self.checkBoxPS2.isChecked())
        self.changeSolveD(self.checkBoxD.isChecked())

    def changeSolvePS1(self, bol):
        '''v1 переключаем при расчете по 1 ps:
        1. сбрасываем решения
        2. Замораживаем и скрываем усилия
        3. Замораживаем блок настроек'''

        self.changed()

        self.tabLoad.setEnabled(bol)
        #        self.tabLoad.setVisible(bol)
        self.boxPS1.setEnabled(bol)

    def changeSolvePS2(self, bol):
        '''v1 переключаем при расчете по 2 ps
                1. сбрасываем решения
        2. Замораживаем и скрываем усилия
        3. Замораживаем блок настроек'''

        self.changed()

        self.tabNLoad.setEnabled(bol)
        #        self.tabNLoad.setVisible(bol)

        self.boxPS2.setEnabled(bol)

    def changeSolveD(self, bol):
        '''v1 переключаем при расчете по D
        1. сбрасываем решения
        2. Замораживаем блок настроек'''

        self.changed()

        self.boxPSD.setEnabled(bol)

    def changeTypeSolve(self):
        '''v1 работает при изменении типа расчета'''
        self.changed()

        pass

    def changeTypeSection(self):
        '''v1 работает при изменении типа сечения'''
        self.changed()

        pass

    def changeCode(self):
        self.changed()
        '''v1 работает при изменении и загрузки норм.
        1. загружаем типы материалов'''
        if self.boxCode.currentIndex() == 0:
            self.code = 52
        elif self.boxCode.currentIndex() == 1:
            self.code = 63
        tempRein = rcMaterial.Reinforced()
        tempConc = rcMaterial.Concrete()

        if self.code == 52:
            lstRein = tempRein.listSP52()
            lstConc = tempConc.listSP52()
        elif self.code == 63:
            lstRein = tempRein.listSP63()
            lstConc = tempConc.listSP63()

        self.loadComboBox(self.boxCodeConc, lstConc)
        self.loadComboBox(self.boxCodeRein, lstRein)

    def loadComboBox(self, widget, lst):
        '''v1 load ComboBox'''
        widget.clear()
        widget.addItems(lst)

    def loadTable(self, widget, lstVertical, lstGorisont):
        widget.clear()
        indexV = len(lstVertical)
        indexG = len(lstGorisont)
        widget.setRowCount(indexV)
        widget.setColumnCount(indexG)
        widget.setHorizontalHeaderLabels(lstGorisont)
        widget.setVerticalHeaderLabels(lstVertical)
        for i in range(indexV):
            for j in range(indexG):
                widget.setItem(i, j, QtGui.QTableWidgetItem('0'))


class SolveWindow(object):
    def __init__(self, window):
        self.wnd = window

    def getLstMatSimple(self):
        '''возвращаем готовый для rcSolve список материалов, благо их всего 2 штуки'''
        #        определяем нориы
        code = self.wnd.code
        con = rcMaterial.Concrete()
        con.norme = code
        con.approxSP = False

        con.phi = float(self.wnd.spinBoxPhi.value())
        con.b = self.wnd.boxCodeConc.currentText()
        con.yb = self.wnd.doubleBoxYbi.value()
        con.initProperties()
        #        print con.eb2
        rein = rcMaterial.Reinforced()

        rein.norme = code
        rein.approxSP = False
        rein.typ = 'A'
        rein.setA(self.wnd.boxCodeRein.currentText())
        rein.ysi = self.wnd.doubleBoxYsi.value()
        rein.initProperties()

        lst = [con, rein]
        return lst

    def getLstFormSimple(self):
        '''берем таблицы, проверяем, меняем и возвращаем готовый список готовый и для rcSolve
                lst=[['Rectangle',[[-1,-1],[1,1]],[100,100],1,1,[0,0,0]],
                 ['Circle',[1,0,-1],[1,1],1,2,[0,0,0]],
                 ['Circle',[1,0,1],[1,1],1,2,[0,0,0]]]
                 lstXY - [1,2,3] 1- x, 2-y, 3-d 
                lstN - список количества мешов [100]
                mat - добавка mat
                sign - коэффициент для площади
                e0rxry - добавка для e0rxr
                '''
        lst = []
        indFormConc = self.wnd.boxFormConc.currentIndex()
        indFormRein = self.wnd.boxFormRein.currentIndex()

        tC = self.wnd.tableFormConc
        tR = self.wnd.tableFormRein

        def getItemTable(widget, sign):
            row = widget.rowCount()
            column = widget.columnCount()
            try:
                lst = []
                for i in range(row):
                    lstRow = []
                    for j in range(column):
                        text = widget.item(i, j).text()
                        if "," in text:
                            text = text.replace(',', '.')
                        text = int(text)
                        if sign == '+':
                            if text >= 0:
                                widget.item(i, j).setText(str(text))
                            else:
                                return 'Error'
                        else:
                            widget.item(i, j).setText(str(text))

                        lstRow.append(text)
                    lst.append(lstRow)
                return lst
            except:
                return 'Error'

        lstConc = getItemTable(tC, '+')
        lstRein = getItemTable(tR, '+')
        if lstRein == "Error" or lstConc == "Error":
            return 'Error'
        #        print lstRein, 'lstRein'
        nx = int(self.wnd.boxNx.value())
        ny = int(self.wnd.boxNy.value())
        if indFormConc == 0:
            y1 = lstConc[0][0]
            x1 = lstConc[1][0]

            if x1 == 0 or y1 == 0:
                return 'Error'

            lst1 = ['Rectangle', [[0, 0], [x1, y1]], [nx, ny], 0, 1, [0, 0, 0]]
            lst.append(lst1)
        elif indFormConc == 1:
            x11 = 0
            y11 = 0
            x12 = lstConc[0][0]
            y12 = lstConc[3][0]

            x21 = x12 / 2. - lstConc[1][0] / 2.
            x22 = x21 + lstConc[1][0]
            y21 = y12
            y22 = y21 + lstConc[4][0]

            x31 = x12 / 2. - lstConc[2][0] / 2.
            x32 = x31 + lstConc[2][0]
            y31 = y22
            y32 = y31 + lstConc[5][0]

            if lstConc[0][0] == 0 or lstConc[3][0] == 0:
                return 'Error'
            lst1 = ['Rectangle', [[x11, y11], [x12, y12]], [nx, ny], 0, 1, [0, 0, 0]]
            lst2 = ['Rectangle', [[x21, y21], [x22, y22]], [nx, ny], 0, 1, [0, 0, 0]]
            lst3 = ['Rectangle', [[x31, y31], [x32, y32]], [nx, ny], 0, 1, [0, 0, 0]]
            lst.append(lst1)
            lst.append(lst2)
            lst.append(lst3)

        elif indFormConc == 2:
            dd = lstConc[0][0] / 1.
            if dd == 0:
                return "Error"
            lst1 = ['SolidCircle', [dd / 2., dd / 2., dd], [nx, ny], 0, 1, [0, 0, 0]]
            lst.append(lst1)

        lstD = []

        if indFormConc == 0 and indFormRein == 0:
            a = lstRein[0][0] * 1.
            d = lstRein[1][0] / 10.

            if d == 0:
                return "Error"
            lstD = [[a, a, d], [x1 - a, a, d], [x1 - a, y1 - a, d], [a, y1 - a, d]]
        elif indFormConc == 0 and indFormRein == 1:
            n1 = lstRein[0][0]
            n2 = lstRein[1][0]
            a = lstRein[2][0] * 1.
            d = lstRein[3][0] / 10.
            if d == 0:
                return "Error"

            lstD = [[a, a, d], [x1 - a, a, d], [x1 - a, y1 - a, d], [a, y1 - a, d]]
            for i in range(n1):
                lstTemp = [(x1 - 2 * a) * 1. / (n1 + 1) * (1 + i) + a, a, d]
                lstTemp1 = [(x1 - 2 * a) * 1. / (n1 + 1) * (1 + i) + a, y1 - a, d]
                lstD.append(lstTemp)
                lstD.append(lstTemp1)

            for i in range(n2):
                lstTemp = [a, (y1 - 2 * a) * 1. / (n2 + 1) * (1 + i) + a, d]
                lstTemp1 = [x1 - a, (y1 - 2 * a) * 1. / (n2 + 1) * (1 + i) + a, d]
                lstD.append(lstTemp)
                lstD.append(lstTemp1)


        elif indFormConc == 0 and indFormRein == 2:
            n1 = lstRein[0][0]
            a = lstRein[1][0] * 1.
            d = lstRein[2][0] / 10.
            if d == 0 or n1 == 0:
                return "Error"

            if n1 != 1:
                for i in range(n1):
                    lstTemp = [(x1 - 2 * a) * 1. / (n1 - 1) * (i) + a, a, d]
                    lstTemp1 = [(x1 - 2 * a) * 1. / (n1 - 1) * (i) + a, y1 - a, d]
                    lstD.append(lstTemp)
                    lstD.append(lstTemp1)
            else:
                lstTemp = [x1 / 2., a, d]
                lstTemp1 = [x1 / 2., y1 - a, d]
                lstD.append(lstTemp)
                lstD.append(lstTemp1)


        elif (indFormConc == 0 and indFormRein == 3) or (indFormConc == 1 and indFormRein == 0):
            n1 = lstRein[0][0]
            n2 = lstRein[1][0]
            a1 = lstRein[2][0] * 1.
            a2 = lstRein[3][0] * 1.
            d1 = lstRein[4][0] / 10.
            d2 = lstRein[5][0] / 10.
            if (d1 == 0 or n1 == 0) and (n2 == 0 or d2 == 0):
                return "Error"

            if indFormConc == 0:
                x01 = 0
                x02 = 0
                xb1 = x1
                xb2 = x1
                h = y1
            else:
                x01 = 0
                x02 = x31
                xb1 = x12
                xb2 = x32
                h = y32

            if n1 != 1:
                for i in range(n1):
                    lstTemp = [(xb1 - x01 - 2 * a1) * 1. / (n1 - 1) * (i) + a1 + x01, a1, d1]
                    lstD.append(lstTemp)
            else:
                lstTemp = [(xb1 - x01) / 2. + x01, a1, d1]
                lstD.append(lstTemp)

            if n2 != 1:
                for i in range(n2):
                    lstTemp = [(xb2 - x02 - 2 * a2) * 1. / (n2 - 1) * (i) + a2 + x02, h - a2, d2]
                    lstD.append(lstTemp)
            else:
                lstTemp = [(xb2 - x02) / 2. + x02, h - a2, d2]
                lstD.append(lstTemp)

        elif (indFormConc == 2 and indFormRein == 0):
            n = lstRein[0][0]
            a = lstRein[1][0] * 1.
            d = lstRein[2][0] / 10.
            if d == 0 and n == 0:
                return "Error"

            for i in range(n):
                x = (dd / 2. - a) * sin(3.1814 * 2 / n * i) + dd / 2.
                y = (dd / 2. - a) * cos(3.1814 * 2 / n * i) + dd / 2.
                lstTemp = [x, y, d]
                lstD.append(lstTemp)
        else:
            for i in lstRein:
                lstD.append([i[0], i[1], i[2] / 10.])

        for i in lstD:
            lst.append(['Circle', i, [1, 1], 1, 1, [0, 0, 0]])

        return lst

    def initMatSimple(self):
        '''инициализация материалов и их загрузка'''
        #        загружаем материалы
        lstMatShort = self.getLstMatSimple()
        lstMatLong = self.getLstMatSimple()
        #       берем данные для кратковр.
        '''Отдача функции расчета sigma по e или v по e
        typDia - тип диаграммы для бетонна, 
        typPS - тип предельного состояния, 
        typTime - long или short для бетона, 
        typR - для бетона, если 1 - просто режется все -, если 2 - после последнего значения - до 0, другое - продлеваем до max, 
        typRT - для бетона, если 1 - просто режется все +, если 2 - после последнего значения - до 0, другое - продлеваем до max'''
        typPSShort = self.wnd.boxPS1ShortChar.currentIndex() + 1
        typTimeShort = self.wnd.boxPS1Short.currentIndex()
        if typTimeShort == 0:
            typTimeShort = 'short'
        else:
            typTimeShort = 'long'
        typDiaShort = 3 - self.wnd.boxPS1ShortDia.currentIndex()
        typRTShort = self.wnd.boxPS1ShortRt.currentIndex() + 1
        lstMatShort[0].functDia(typDia=typDiaShort, typPS=typPSShort, typTime=typTimeShort, typR=3, typRT=typRTShort)
        lstMatShort[1].functDia(typPS=typPSShort)


        #       берем данные для длит нагрузки.
        typPSLong = self.wnd.boxPS1LongChar.currentIndex() + 1
        typTimeLong = self.wnd.boxPS1Long.currentIndex()
        if typTimeLong == 0:
            typTimeLong = 'short'
        else:
            typTimeLong = 'long'
        typDiaLong = 3 - self.wnd.boxPS1LongDia.currentIndex()
        typRTLong = self.wnd.boxPS1LongRt.currentIndex() + 1

        lstMatLong[0].functDia(typDia=typDiaLong, typPS=typPSLong, typTime=typTimeLong, typR=3, typRT=typRTLong)
        lstMatLong[1].functDia(typPS=typPSLong)

        return [lstMatShort, lstMatLong]

    def solvePS1(self):
        '''расчет 1 п.с.'''
        #        загружаем усилия в lstN
        lstNShort = self.getTableLoadlstItem(self.wnd.tableLoadPS1DShort, [0, 1, 2])
        lstNLong = self.getTableLoadlstItem(self.wnd.tableLoadPS1DLong, [0, 1, 2])

        #        print lstNShort

        lstNS = []
        for i in lstNShort:
            lstNS.append([i[0] * 1000., i[1] * 1000. * 100, i[2] * 1000. * 100])

        lstNL = []
        for i in lstNLong:
            lstNL.append([i[0] * 1000., i[1] * 1000. * 100, i[2] * 1000. * 100])

        lstNShort = lstNS
        lstNS = None

        #        print lstNShort


        lstNLong = lstNL
        lstNL = None

        crit = self.wnd.doubleBoxTol.value()
        nn = self.wnd.boxNum.value()

        outShort = []
        outLong = []

        if lstNShort == None:
            lstNShort = []

        if lstNLong == None:
            lstNLong = []
        # считае
        self.loadFormMatSimple()
        for i in lstNShort:
            #            print 'i, nn, crit', i,nn, crit
            outShort.append(self.solve.findKult9(i, nn, crit))

        self.loadFormMatSimple(typ='long')
        for i in lstNLong:
            outLong.append(self.solve.findKult9(i, nn, crit))
            # проверяем на ошибки

        for i in outShort:
            if type(i) == type('error'):
                self.error(i)
                return False

        for i in outLong:
            if type(i) == type('error'):
                self.error(i)
                return False
                # пишем все это
            #        print 'outS',outShort
            #        print 'outL',outLong

        self.loadTableRes(self.wnd.tableResPS1Short, outShort)
        self.loadTableRes(self.wnd.tableResPS1Long, outLong)

    def loadTableRes(self, table, lst):
        title = [u'N, т', u'Mx, т*м', u'My, т*м', u'k', u'n', u'e0', u'1/rx', u'1/ry', u'Nu, т', u'Mxu, т*м', u'Myu'
            , u'D11', u'D12', u'D13', u'D22', u'D23', u'D33', u'muMx', u'muMy', u'muN']
        title2 = [u'ke', u'eult', u'e(+)', u'e(-)']

        # определяем максимум
        mx = 0
        for i in lst:
            if 20 + len(i[-1]) * 4 > mx:
                mx = 20 + len(i[-1]) * 4
        n = (mx - 20) / 4

        titleSum = title + title2 * n

        lny = len(lst)
        table.setRowCount(lny)

        lnx = mx
        table.setColumnCount(lnx)

        table.setHorizontalHeaderLabels(titleSum)

        lstNorm = []
        for j in lst:
            item = [j[0][0] / 1000., j[0][1] / 1000. / 100., j[0][2] / 1000. / 100.
                , j[1], j[2]
                , j[3][0], j[3][1], j[3][2]
                , j[4][0] / 1000., j[4][1] / 1000. / 100., j[4][2] / 1000. / 100.
                , j[5][0], j[5][1], j[5][2], j[5][3], j[5][4], j[5][5]
                , j[6][0], j[6][1], j[6][2]]

            for i in j[-1]:
                item += i
            lstNorm.append(item)

        #        print lstNorm

        for i in range(lnx):
            for j in range(lny):
                table.setItem(j, i, QtGui.QTableWidgetItem(""))
                txt = lstNorm[j][i]
                #                print txt
                if abs(txt) > 100:
                    txt = "%.0f" % txt
                elif abs(txt) > 10:
                    txt = "%.2f" % txt
                else:
                    txt = "%.4f" % txt
                table.item(j, i).setText(txt)
                table.item(j, i).setFlags(QtCore.Qt.ItemFlags(1 + 2 + 4 + 8 + 6 + 12 + 64))

    def solvePS2(self):
        '''расчет 2 п.с.'''

    def loadFormMatSimple(self, typ='short'):
        '''загрузка формы и материалов'''

        #    sol.loadForm(lstForm)
        #
        #    conc=rcMaterial.Concrete()
        #    conc.norme=52
        #    conc.b=25
        #    conc.initProperties()
        #    conc.functDia(typDia=3, typPS=1,typTime='short', typR=3, typRT=1)
        #    rein=rcMaterial.Reinforced()
        #    rein.norme=52
        #    rein.typ='A'
        #    rein.a=400
        #    rein.initProperties()
        #    rein.functDia(typPS=1)
        #    lstMat=[conc, rein]
        #
        #    sol.loadMat(lstMat)
        #
        #    sol.formGen()


        lstForm = self.getLstFormSimple()

        if typ == 'short':
            lstMat = self.initMatSimple()[0]
        else:
            lstMat = self.initMatSimple()[1]

        if type(lstForm) != type('Error') and type(lstMat) != type('Error'):
            #            print u'load'
            solve = rcSolves.Solves()
            solve.loadForm(lstForm)
            #            print lstForm
            solve.loadMat(lstMat)
            #            print lstMat
            solve.formGen()
            self.solve = solve
            return True
        else:
            self.error('Data')
            return False

    def DSolve(self):
        '''расчет критических значений'''
        lstShort = self.getTableLoadlstItem(self.wnd.tableLoadPS1Short, [0, 1, 2, 3, 4, 5])
        lstLong = self.getTableLoadlstItem(self.wnd.tableLoadPS1Long, [0, 1, 2, 3, 4, 5])

        if lstShort == [] or lstLong == []:
            self.error(u'Введите усилия')
            return False
        if self.wnd.checkBoxD.isChecked() == True:
            l = self.wnd.doubleBoxL.value()
            lx = self.wnd.doubleBoxLx.value()
            ly = self.wnd.doubleBoxLy.value()
            typStat = self.wnd.boxStatOpr.currentIndex()
            typD = True
            if typStat == 0:
                typStat = False
            else:
                typStat = True
        else:
            l = 0
            lx = 0
            ly = 0
            typStat = False
            typD = False
        #        решаем задачу D
        lstDShort = self.solve.nuD(lstShort, typStat, lx, ly, l, typD)
        lstDLong = self.solve.nuD(lstLong, typStat, lx, ly, l, typD)
        #        self.wnd.tabDShort.setEnabled(True)
        #        self.wnd.tabDLong.setEnabled(True)
        if lstDShort[-1] == False or lstDLong[-1] == False:
            self.error(u'Увеличить сечение: N>Ncr')
            self.loadTableMatPlot(self.wnd.tableLoadPS1DShort, self.wnd.mplCrDShort, lstDShort[0],
                                  range(len(lstDShort[0])), [], lstShort, range(len(lstDShort[0][0])), False)

            self.loadTableMatPlot(self.wnd.tableLoadPS1DLong, self.wnd.mplCrDLong, lstDLong[0], range(len(lstDLong[0])),
                                  [], lstLong, range(len(lstDLong[0][0])), False)
            return False


        # загружаем данные, если все нормально
        self.loadTableMatPlot(self.wnd.tableLoadPS1DShort, self.wnd.mplCrDShort, lstDShort[0], range(len(lstDShort[0])),
                              [], lstShort, range(len(lstDShort[0][0])))

        self.loadTableMatPlot(self.wnd.tableLoadPS1DLong, self.wnd.mplCrDLong, lstDLong[0], range(len(lstDLong[0])), [],
                              lstLong, range(len(lstDLong[0][0])))

        return True

    def critSolve(self):
        '''считаем критические точки'''
        res1, res2 = True, True
        if self.wnd.tabLoad.isEnabled() == True:
            res1 = self.critSolvePS1()
        if self.wnd.tabNLoad.isEnabled() == True:
            res2 = self.critSolvePS2()
        if res1 == True and res2 == True:
            return True
        else:
            False

    def critSolvePS1(self):
        matrix = self.getTableLoad(self.wnd.tableLoadPS1)
        if matrix[1] == False:
            return False
        #        print matrix[0]
        hull = self.hull(matrix[0])
        #        print hull
        mtr = np.array(matrix[0])
        self.wnd.tabCr1PS.setEnabled(True)
        #        self.wnd.tabCrLong.setEnabled(True)

        self.loadTableMatPlot(self.wnd.tableLoadPS1Short, self.wnd.mplCrShort, hull[0], hull[1], hull[2], mtr,
                              [0, 1, 2, 3, 4, 5])
        self.loadTableMatPlot(self.wnd.tableLoadPS1Long, self.wnd.mplCrLong, hull[0], hull[1], hull[2], mtr,
                              [3, 4, 5, 3, 4, 5])

        return True

    def critSolvePS2(self):
        matrix = self.getTableLoad(self.wnd.tableLoadPS2)
        if matrix[1] == False:
            return False
        #        print matrix[0]
        hull = self.hull(matrix[0])
        #        print hull
        mtr = np.array(matrix[0])
        self.wnd.tabCrNorm.setEnabled(True)
        self.loadTableMatPlot(self.wnd.tableLoadPS2Norm, self.wnd.mplCrNorm, hull[0], hull[1], hull[2], mtr,
                              [0, 1, 2, 3, 4, 5])

        return True

    def loadTableMatPlot(self, table, matPlot, s, cur, reb, l, order, boolPlot=True):
        '''загружаеам данные и рисуем картинку
        1 - тблаица
        2 - матплот
        3 - список с каким работаем
        4 - номера из списка
        5- ребра
        6 - общий список
        7 - порядок
        '''
        #        загружаем данные в таблице и блокируем для изменения
        lny = len(cur)
        table.setRowCount(lny)
        for i in range(len(order)):
            for j in range(lny):
                table.setItem(j, i, QtGui.QTableWidgetItem(""))
                txt = (s[cur[j]][order[i]])
                if type(txt) == type(0.1) or type(txt) == np.float64:
                    txt = "%.2f" % txt
                else:
                    txt = str(txt)
                table.item(j, i).setText(txt)
                table.item(j, i).setFlags(QtCore.Qt.ItemFlags(1 + 2 + 4 + 8 + 6 + 12 + 64))

                # рисуем по 3 первым точкам точки))
        if boolPlot == True:
            fig = matPlot.figure
            ax = fig.gca(projection='3d')
            ax.clear()
            l = np.array(l)
            ax.plot(l[:, order[1]], l[:, order[2]], l[:, order[0]], 'o')
            # рисуем по 3 точкам ))
            if type(reb) != bool:
                for i in cur:
                    #                print s[i][0],s[i][1],s[i][2]
                    ax.plot([s[i][order[1]]], [s[i][order[2]]], [s[i][order[0]]], c='r', marker='o')
            ax.set_xlabel('Mx')
            ax.set_ylabel('My')
            ax.set_zlabel('N')
            matPlot.draw()

    def hull(self, mtr):
        '''hull
        1. убрать дубли
        3. убрать лишние размерности
        2. подготовить данные для qHull - копланарность?'''
        #        lst2=mtr
        lst1 = [mtr[0]]
        for i in mtr[1:]:
            flag = False
            for j in lst1:
                if i == j:
                    flag = True
                    break
            if flag == False:
                lst1.append(i)
            #
            #        lst2=[lst1[0]]
            #        for i in lst1[1:]:
            #            for j in lst2:
            #                kk=[]
            #                for k in range(6):
            #                    if j[k]!=0:
            #                        kk.append(i[k]/j[k])
            #                flagK=True
            #                for k in kk[1:]:
            #                    if kk[0]!=k:
            #                        flagK=False
            #                        break
            #                if flagK==True and kk[0]>1:
            #                    lst2.remove(j)
            #            lst2.append(i)

        lst2 = lst1
        lst3 = []
        for i in lst2:
            if i != [0., 0., 0., 0., 0., 0.]:
                lst3.append(i)

        lst = np.array(lst3)

        if len(lst) < 10:
            return lst, range(len(lst)), False
        else:

            matr = np.array(lst3)
            matr = np.transpose(matr)

            zero = np.zeros(len(matr[0]))

            flagMatr = False
            for i in range(len(matr)):
                if list(zero * i) != list(matr[i]):
                    if flagMatr == False:
                        matrSel = matr[i]
                        flagMatr = True
                    else:
                        matrSel = np.vstack((matrSel, matr[i]))

            matrSel = np.transpose(matrSel)

            #            hull=ConvexHull(matrSel)

            hull = ConvexHull(matrSel, qhull_options='QJ')
            return lst, hull.vertices, hull.simplices

    def getTableLoadlstItem(self, widget, lstItem):
        lst = []
        nxMax = widget.rowCount()
        nyMax = widget.columnCount()
        for i in range(nxMax):
            lstRow = []
            for j in range(nyMax):
                if j in lstItem:
                    text = widget.item(i, j).text()
                    text = float(text)
                    lstRow.append(text)
            lst.append(lstRow)
        mtr = lst
        return mtr

    def getTableLoad(self, widget):
        try:
            lst = []
            nxMax = widget.rowCount()
            nyMax = widget.columnCount()
            for i in range(nxMax):
                lstRow = []
                for j in range(nyMax):
                    text = widget.item(i, j).text()
                    if "," in text:
                        text = text.replace(',', '.')
                    if text == '':
                        text = '0'
                    text = float(text)
                    widget.item(i, j).setText(str(text))
                    lstRow.append(text)
                lst.append(lstRow)
            mtr = lst
            #            bol=self.checkTableLoad(mtr)
            bol = True
            if bol == True:
                return mtr, True
            else:
                self.error('Data')
                return mtr, False
        except:
            self.error('Data')
            return False, False

    def checkTableLoad(self, mtr):
        for i in mtr:
            k1, k2, k3 = 0, 0, 0
            if i[0] != 0:
                k1 = i[3] / i[0]
            else:
                if i[3] != 0:
                    k1 = 10
            if i[1] != 0:
                k2 = i[4] / i[1]
            else:
                if i[4] != 0:
                    k2 = 10

            if i[2] != 0:
                k3 = i[5] / i[2]
            else:
                if i[5] != 0:
                    k3 = 10

            if (k1 < 0 or k1 > 1) or (k2 < 0 or k2 > 1) or (k3 < 0 or k3 > 1):
                return False
        return True

    def error(self, txt):
        self.wnd.error(txt)
        return False


class Error():
    pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
