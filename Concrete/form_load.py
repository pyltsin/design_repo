# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import io

from PyQt4 import QtGui, QtCore, uic
import scipy.spatial as sp
import numpy as np
import matplotlibwidget
from scipy.sparse.csgraph import _validation

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



from key_press_event import copy_past

import importlib
importlib.import_module('mpl_toolkits').__path__

__author__ = 'Pyltsin'


class MainWindow(QtGui.QMainWindow):
    """init mainWindow"""

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi('gui/main_form_load.ui', self)
        self.connect_function()
        self.init_prop()
        self.clear()

    def keyPressEvent(self, e):
        copy_past(e, [self.tableIn], [self.tableOut, self.tableIn], self)
        self.change_color_table()

    def enabled_clear(self):
        self.tableOut.setEnabled(True)

        self.buttonDraw.setEnabled(True)
        self.buttonCopy.setEnabled(True)
        self.boxCountDraw1.setEnabled(True)
        self.boxCountDraw2.setEnabled(True)
        self.boxCountDraw3.setEnabled(True)

    def clear(self):
        self.tableOut.setEnabled(False)

        self.buttonDraw.setEnabled(False)
        self.buttonCopy.setEnabled(False)
        self.mpl.setEnabled(False)
        self.boxCountDraw1.setEnabled(False)
        self.boxCountDraw2.setEnabled(False)
        self.boxCountDraw3.setEnabled(False)

    # noinspection PyAttributeOutsideInit
    def connect_function(self):
        """connect"""
        self.tableIn.clicked.connect(self.clear)
        lst_column_solve = [self.boxCount1, self.boxCount2, self.boxCount3, self.boxCount4, self.boxCount5,
                            self.boxCount6]

        lst_column_draw = [self.boxCountDraw1, self.boxCountDraw2, self.boxCountDraw3]

        self.buttonSolve.clicked.connect(self.solve)
        self.buttonCopy.clicked.connect(self.copy)
        self.buttonDraw.clicked.connect(self.draw)

        self.menuSolve.triggered.connect(self.solve)
        self.menuExit.triggered.connect(self.exit_program)
        self.menuAbout.triggered.connect(self.about)
        self.menuQt.triggered.connect(self.about_qt)

        self.boxCountRow.valueChanged.connect(self.table_count_row)
        self.boxCountColumn.valueChanged.connect(self.table_count_column)

        self.boxCountSolveColumn.valueChanged.connect(self.change_column)

        for box in lst_column_solve:
            box.valueChanged.connect(self.clear)
            box.valueChanged.connect(self.change_color_table)
        self.lstColumnSolve = lst_column_solve

        for box in lst_column_draw:
            box.valueChanged.connect(self.clear_draw)
        self.lstColumnDraw = lst_column_draw

    def change_color_table(self):
        for i in range(self.tableIn.rowCount()):
            for j in range(self.tableIn.columnCount()):
                self.tableIn.item(i, j).setBackgroundColor(QtGui.QColor(255, 255, 255))

        for box in self.lstColumnSolve:
            if box.isEnabled():
                number_column = box.value() - 1
                for i in range(self.tableIn.rowCount()):
                    self.tableIn.item(i, number_column).setBackgroundColor(QtGui.QColor(200, 200, 255))

    def clear_draw(self):
        self.buttonCopy.setEnabled(False)
        self.mpl.setEnabled(False)

    def table_count_row(self):
        self.change_count_row_any_table(self.boxCountRow.value(), self.tableIn)

    def change_count_row_any_table(self, i, widget):
        """изменяем кол-во строк при изенении счетчика"""
        widget.setRowCount(i)
        for j in range(widget.rowCount()):
            for k in range(widget.columnCount()):
                if widget.item(j, k) is None:
                    widget.setItem(j, k, QtGui.QTableWidgetItem('0'))
        self.change_color_table()

    def change_count_column_any_table(self, i, widget):
        """изменяем кол-во колонн при изенении счетчика"""
        widget.setColumnCount(i)
        for j in range(widget.columnCount()):
            for k in range(widget.rowCount()):
                if widget.item(k, j) is None:
                    widget.setItem(k, j, QtGui.QTableWidgetItem('0'))
        self.change_color_table()

    def table_count_column(self):
        max_value = self.boxCountColumn.value()
        self.boxCountSolveColumn.setMaximum(max_value if max_value <= 6 else 6)
        for box in self.lstColumnSolve:
            box.setMaximum(max_value)

        for box in self.lstColumnDraw:
            box.setMaximum(max_value)
        self.change_count_column_any_table(self.boxCountColumn.value(), self.tableIn)

        if self.boxCountRow.value() < max_value + 1:
            self.change_count_row_any_table(max_value + 1, self.tableIn)

        self.boxCountRow.setMinimum(max_value + 1)

    def change_column(self):
        value = self.boxCountSolveColumn.value()
        for i in range(6):
            self.lstColumnSolve[i].setEnabled(i < value)

    def init_prop(self):
        self.boxCountRow.setValue(4)
        self.boxCountColumn.setValue(2)

        self.table_count_column()
        self.table_count_row()

        self.boxCountSolveColumn.setValue(3)
        self.change_column()

        for i, box in enumerate(self.lstColumnSolve):
            box.setValue(i + 1)

        for i, box in enumerate(self.lstColumnDraw):
            box.setValue(i + 1)

    def rearrange_array(self, array):
        lst = []
        for box in self.lstColumnSolve:
            if box.isEnabled():
                value = box.value() - 1
                lst.append(array[:, value])
        return np.vstack(lst)

    # noinspection PyArgumentList,PyArgumentList,PyTypeChecker,PyCallByClass,PyAttributeOutsideInit
    def solve(self):
        try:
            array = self.get_array_from_table(self.tableIn)
            array_hull = np.transpose(self.rearrange_array(array))
            self.hull = sp.ConvexHull(array_hull, qhull_options='QJ Pp')
            lst_out = []
            for i in self.hull.vertices:
                lst_temp = [1 + i] + list(array[i])
                lst_out.append(lst_temp)
            array_out = np.array(lst_out)
            self.input_table_in(array_out, self.tableOut)
            self.enabled_clear()
            self.arrayOut = array_out
            self.array = array
        except TypeError:
            QtGui.QMessageBox.information(self, QtCore.QString(u"Ошибка"),
                                          QtCore.QString(u"Таблица содержит недопустимые исходные данные"))
        except sp.qhull.QhullError:
            QtGui.QMessageBox.information(self, QtCore.QString(u"Ошибка"),
                                          QtCore.QString(u"Ошибка алгоритма вычисления QHull"))

    @staticmethod
    def input_table_in(array, widget):
        lx, ly = np.shape(array)

        widget.setRowCount(lx)

        widget.setColumnCount(ly)

        name = [str(x + 1) for x in range(ly)]
        # noinspection PyTypeChecker
        name = [u"№"] + name

        widget.setHorizontalHeaderLabels(name)
        for x in xrange(lx):
            for y in xrange(ly):
                widget.setItem(x, y, QtGui.QTableWidgetItem(""))
                text = str(array[x][y])
                widget.item(x, y).setText(QtCore.QString(text))
                widget.item(x, y).setFlags(QtCore.Qt.ItemFlags(1 + 2 + 4 + 8 + 6 + 12 + 64))

    @staticmethod
    def get_array_from_table(widget):
        lst = []
        for j in xrange(widget.rowCount()):

            lst_temp = []
            for i in xrange(widget.columnCount()):

                text = widget.item(j, i).text()
                if "," in text:
                    text = text.replace(",", ".")
                if not is_number(str(text.toUtf8())):
                    raise TypeError
                else:
                    lst_temp.append(float(text))
            lst.append(lst_temp)

        return np.array(lst)

    # noinspection PyArgumentList,PyCallByClass
    def copy(self):
        buf = io.BytesIO()
        fig = self.mpl.figure
        fig.savefig(buf)
        # noinspection PyTypeChecker
        QtGui.QApplication.clipboard().setImage(QtGui.QImage.fromData(buf.getvalue()))
        buf.close()

    def draw(self):
        array_out = self.arrayOut
        array = self.array
        lst = []
        lst_out = []
        for box in self.lstColumnDraw:
            value = box.value() - 1
            lst.append(array[:, value])
            lst_out.append(array_out[:, value + 1])
        point_in = np.transpose(np.vstack(lst))
        fig = self.mpl.figure
        ax = fig.gca(projection='3d')
        ax.clear()
        ax.plot(point_in[:, 0], point_in[:, 1], point_in[:, 2], 'o')
        # рисуем по 3 точкам ))
        for number_point in self.hull.simplices:
            ax.plot(point_in[number_point, 0], point_in[number_point, 1], point_in[number_point, 2], c='r', marker='o')
        ax.set_xlabel(self.lstColumnDraw[0].value())
        ax.set_ylabel(self.lstColumnDraw[1].value())
        ax.set_zlabel(self.lstColumnDraw[2].value())
        self.mpl.draw()
        self.mpl.setEnabled(True)
        self.buttonCopy.setEnabled(True)

    # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
    def about_qt(self):
        QtGui.QMessageBox.aboutQt(self)

    # noinspection PyTypeChecker,PyArgumentList,PyArgumentList,PyCallByClass
    def about(self):
        QtGui.QMessageBox.about(self, QtCore.QString(u"О программе"),
                                QtCore.QString(u"""
Программа создана для построения выпуклой поверхности.

При работе с таблицей в программе поддерживаются сочетания Ctrl+C, Ctrl+V

(c)kapmik pma88@list.ru
2015
Программа бесплатная. Распространяется AsIs.
Автор не несет ответственности за результат и процесс использования программы."""))

    @staticmethod
    def exit_program():
        sys.exit()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
