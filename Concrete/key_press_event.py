# -*- coding: utf-8 -*-
"""
Created on Sat Aug 09 22:24:03 2014

@author: Pyltsin
"""
from PyQt4 import QtCore, QtGui


def copy_past(e, list_input_table, list_output_table, window):
    # noinspection PyBroadException,PyBroadException,PyBroadException,PyBroadException
    try:
        # noinspection PyArgumentList
        clip = QtGui.QApplication.clipboard()
        flag_in = None
        flag_out = None
        focus_widget = window.focusWidget()
        if type(focus_widget) == QtGui.QComboBox:
            focus_widget = focus_widget.parent().parent()
            focus_widget.setFocus()

        for x in list_input_table:
            if window.focusWidget() == x:
                table_in = x
                flag_in = 'input'
        for y in list_output_table:
            if window.focusWidget() == y:
                table_out = y
                flag_out = 'output'

        if e.modifiers() & QtCore.Qt.ControlModifier and (flag_in is not None or flag_out is not None):
            # noinspection PyUnboundLocalVariable
            if flag_in:
                selected = table_in.selectedRanges()
            else:
                selected = table_out.selectedRanges()

            if e.key() == QtCore.Qt.Key_V and (flag_in == 'input'):  # past
                print 'ok'
                first_row = selected[0].topRow()
                first_col = selected[0].leftColumn()
                #            print clip.text()
                # copied text is split by '\n' and '\t' to paste to the cells
                for r, row in enumerate(clip.text().split('\n')):
                    #                print row
                    for c, text in enumerate(row.split('\t')):
                        #                    print text
                        if text != '' and text != ' ':
                            if table_in.cellWidget(first_row + r, first_col + c) is None:
                                table_in.setItem(first_row + r, first_col + c, QtGui.QTableWidgetItem(text))
                            else:
                                widget = table_in.cellWidget(first_row + r, first_col + c)
                                count = widget.count()
                                for i in range(count):
                                    if QtCore.QString(text) == widget.itemText(i):
                                        widget.setCurrentIndex(i)

            elif e.key() == QtCore.Qt.Key_C and (flag_out == 'output'):  # copy
                s = ""
                for r in xrange(selected[0].topRow(), selected[0].bottomRow() + 1):
                    for c in xrange(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                        try:
                            if table_out.cellWidget(r, c) is None:
                                s += str(table_out.item(r, c).text()) + "\t"
                            else:
                                widget = table_out.cellWidget(r, c)
                                txt = widget.currentText()
                                s += txt + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n"  # eliminate last '\t'
                clip.setText(s)
    except:
        pass
