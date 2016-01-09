# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 18:05:38 2014

@author: admin
"""

import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
table = QtGui.QTableWidget(5,5)
combobox = QtGui.QComboBox()
combobox.addItem("Combobox item1")
combobox.addItem("Combobox item12")
combobox.addItem("Combobox item13")
print range(5)
print range(4,7)
table.setCellWidget(1,0, combobox)
table.show()
app.exec_()