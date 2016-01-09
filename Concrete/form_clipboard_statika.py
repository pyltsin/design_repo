# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import win32clipboard
import sys

from PyQt4 import QtGui, QtCore, uic

from key_press_event import copy_past

__author__ = 'Pyltsin'


# noinspection PyCallByClass,PyArgumentList
class MainWindow(QtGui.QMainWindow):
    """init mainWindow"""

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.cp = Clipboard()
        uic.loadUi('gui/main_form_clipboard.ui', self)
        self.connect_function()
        self.init_prop()

    def keyPressEvent(self, e):
        copy_past(e, [self.table], [self.table], self)

    def connect_function(self):
        """connect"""
        self.buttonLoad.clicked.connect(self.load_from_cb)
        self.buttonUnload.clicked.connect(self.unload_to_cb)
        self.boxCountTable.valueChanged.connect(self.index_changed)
        self.menuLoad.triggered.connect(self.load_from_cb)
        self.menuUnload.triggered.connect(self.unload_to_cb)
        self.menuExit.triggered.connect(self.exit_program)
        self.menuAbout.triggered.connect(self.about)
        self.menuQt.triggered.connect(self.about_qt)

    # noinspection PyTypeChecker
    def about_qt(self):
        QtGui.QMessageBox.aboutQt(self)

    # noinspection PyTypeChecker
    def about(self):
        QtGui.QMessageBox.about(self, QtCore.QString(u"О программе"),
                                QtCore.QString(u"""
Программа создана для работы с ПК Статика.
Порядок работы:
1. Вырезать или скопировать из таблицы Статики, содержащей не менее 2 строк и состоящей только из чисел.
2. Нажать 'Загрузить'
3. Исправить усилия
4. Нажать 'Выгрузить'
5. Вставить таблицу в позицию Статики

При работе с таблицей в программе поддерживаются сочетания Ctrl+C, Ctrl+V

(c)kapmik pma88@list.ru
2015
Программа бесплатная. Распространяется AsIs.
Автор не несет ответственности за результат и процесс использования программы."""))

    @staticmethod
    def exit_program():
        sys.exit()

    def load_table(self):
        """load data in table and label"""

        # load in label1
        self.label1.setText(self.cp.get_name_table())
        # load in table
        ny = self.cp.get_count_row()
        nx = self.cp.get_count_column()
        self.table.setColumnCount(nx)
        self.change_count_table_load(ny, self.table)

        names_row_table = self.cp.get_names_row_table()
        self.table.clear()
        self.table.setHorizontalHeaderLabels(names_row_table)

        cells_table = self.cp.get_cells_table()
        self.set_text_in_table(cells_table, self.table)
        # enable boxCount
        self.boxCountTable.setEnabled(True)
        # set boxCount
        self.boxCountTable.setValue(ny)
        # enable Unload
        self.buttonUnload.setEnabled(True)
        # enable table
        self.table.setEnabled(True)
        # enable menu
        self.menuUnload.setEnabled(True)

    @staticmethod
    def set_text_in_table(lst, widget):
        lnx = widget.columnCount()
        lny = widget.rowCount()
        for i in range(lnx):
            for j in range(lny):
                widget.setItem(j, i, QtGui.QTableWidgetItem(""))
                txt = lst[j][i]
                widget.item(j, i).setText(QtCore.QString(str(txt)))
                #                widget.item(j,i).setFlags(QtCore.Qt.ItemFlags(1+2+4+8+6+12+64))

    @staticmethod
    def change_count_table_load(i, widget):
        """изменяем кол-во строк при изенении счетчика"""
        widget.setRowCount(i)
        for j in range(widget.rowCount()):
            for k in range(widget.columnCount()):
                if widget.item(j, k) is None:
                    widget.setItem(j, k, QtGui.QTableWidgetItem('0'))

    # noinspection PyTypeChecker,PyTypeChecker
    def load_from_cb(self):
        """load data from clipboard to table"""
        try:
            self.cp.raw_clipboard()
        except ClipboardException:
            # noinspection PyCallByClass
            QtGui.QMessageBox.information(self, QtCore.QString(u"Ошибка"), QtCore.QString(u"Ошибка работы с буфером"))

        if self.cp.is_mb_aec() and self.cp.is_table():
            self.load_table()
        else:
            # noinspection PyCallByClass
            QtGui.QMessageBox.information(self, QtCore.QString(u"Ошибка"),
                                          QtCore.QString(u"Буфер не содержит таблицу Статики с 2 строками"))

    # noinspection PyTypeChecker
    def unload_to_cb(self):
        """load data from table to clipboard"""
        # create txt for clipboard
        try:
            txt = ""

            txt += unicode(self.cp.get_name_table())

            lst_header = self.cp.get_names_row_table()
            for i in xrange(self.table.columnCount()):
                txt += "\n  "
                for j in xrange(self.table.rowCount()):
                    if j == 0:
                        txt += unicode(lst_header[i]) + u"="
                    text_from_table = self.table.item(j, i).text()
                    if "," in text_from_table:
                        text_from_table = text_from_table.replace(",", ".")

                    if not is_number(str(text_from_table.toUtf8())):
                        raise TypeError
                    self.table.item(j, i).setText(QtCore.QString(text_from_table))
                    if j != self.table.rowCount() - 1:
                        txt += unicode(text_from_table) + u","
                    else:
                        txt += unicode(text_from_table)
            txt += u"\r\n"
            txt = unicode(txt)
            self.cp.set_in_clipboard(txt)

            self.init_prop()
        except TypeError:
            QtGui.QMessageBox.information(self, QtCore.QString(u"Ошибка"),
                                          QtCore.QString(
                                              u"В таблице присутсвует не число. Поддерживается только работа с числами")
                                          )

        except ClipboardException:
            QtGui.QMessageBox.information(self, QtCore.QString(u"Ошибка"),
                                          QtCore.QString(u"Запись в буфер не выполнена"))

    def index_changed(self):
        self.change_count_table_load(self.boxCountTable.value(), self.table)

    def init_prop(self):
        self.buttonUnload.setEnabled(False)
        self.boxCountTable.setEnabled(False)
        self.table.setEnabled(False)
        self.menuUnload.setEnabled(False)
        self.menuLoad.setEnabled(True)

        self.buttonLoad.setEnabled(True)


class Clipboard:
    """Class for work with clipboard"""

    def __init__(self):
        """text for find in clipboard"""
        self.text_find = "mbAEC Software GmbH, info structure"

    def set_in_clipboard(self, txt):
        """set txt in clipboard"""
        try:
            win32clipboard.OpenClipboard(None)
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(txt)
            num = win32clipboard.RegisterClipboardFormat(self.text_find)
            win32clipboard.SetClipboardData(num, self.get_signature())
        except:
            raise ClipboardException
        finally:
            # noinspection PyBroadException
            try:
                win32clipboard.CloseClipboard()
            except:
                pass

    def get_count_column(self):
        # noinspection PyTypeChecker
        data = self.dict_cp['data'][1]
        return len(unicode(data, "cp1251").split("\n  ")[1:])

    def get_count_row(self):
        # noinspection PyTypeChecker
        data = self.dict_cp['data'][1]
        return len(unicode(data, "cp1251").split("\n  ")[1].split(','))

    def get_cells_table(self):
        """return list for table"""
        lst = []
        # noinspection PyTypeChecker
        data = self.dict_cp['data'][1]
        for line in unicode(data, "cp1251").split("\n  ")[1:]:
            line = line.replace("\\\r\n", ",")
            line = line.strip()
            if "=" in line:
                tmp = line.split("=")[1]
                lst_row = tmp.split(',')
                lst.append(lst_row)

        lst_out = []
        for i in xrange(len(lst)):
            for j in xrange(len(lst[0])):
                if i == 0:
                    lst_out_temp = []
                    temp_text = lst[i][j].encode("utf-8").strip()

                    cell = 0 if temp_text == "" else temp_text
                    lst_out_temp.append(cell)
                    lst_out.append(lst_out_temp)
                else:
                    temp_text = lst[i][j].encode("utf-8").strip()
                    cell = 0 if temp_text == "" else temp_text
                    lst_out[j].append(cell)
        return lst_out

    def get_names_row_table(self):
        """return names row"""
        lst = []
        # noinspection PyTypeChecker
        data = self.dict_cp['data'][1]
        for line in unicode(data, "cp1251").split("\n  ")[1:]:
            lst.append(line.split("=")[0])
        return lst

    def get_signature(self):
        """return signature from self.dictCP"""
        find_num = None
        dict_format = self.dict_cp["format"]
        for (formatNum, formatName) in dict_format.items():
            if self.text_find in formatName:
                find_num = formatNum
        return self.dict_cp["data"][find_num]

    def get_name_table(self):
        """return Title table"""
        # noinspection PyTypeChecker
        data = self.dict_cp['data'][1]
        return unicode(data, "cp1251").split("\n")[0]

    def is_table(self):
        """self.dictCp is table?
        (contain 2 row)"""

        # noinspection PyTypeChecker
        data = self.dict_cp['data'][1]
        # noinspection PyBroadException
        try:
            return "," in QtCore.QString(data).split(" =")[-1]
        except:
            return False

    def is_mb_aec(self):
        """contain self.dictCp keywords?"""
        dict_format = self.dict_cp["format"]
        for formatName in dict_format.values():
            if self.text_find in formatName:
                return True
        return False

    def raw_clipboard(self):
        """raw data from clipboard to self.dictCp
    out={format:[Number: Name], data:{Number: Data}"""

        try:
            formats = {val: name for name, val in vars(win32clipboard).items() if name.startswith('CF_')}

            def format_name(format_clipboard):
                if format_clipboard in formats:
                    return formats[format_clipboard]
                # noinspection PyBroadException
                try:
                    return win32clipboard.GetClipboardFormatName(format_clipboard)
                except:
                    return "unknown"

            win32clipboard.OpenClipboard(None)
            fmt = 0
            dict_format = {}
            dict_data = {}
            while True:
                fmt = win32clipboard.EnumClipboardFormats(fmt)
                if fmt == 0:
                    break
                dict_format[fmt] = format_name(fmt)

                datum = win32clipboard.GetClipboardData(fmt)
                dict_data[fmt] = datum
            # noinspection PyAttributeOutsideInit
            self.dict_cp = {'format': dict_format, 'data': dict_data}
            return self.dict_cp
        except:
            raise ClipboardException
        finally:
            # noinspection PyBroadException
            try:
                win32clipboard.CloseClipboard()
            except:
                pass


class ClipboardException(Exception):
    """ Exception work with clipboard"""
    pass


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
