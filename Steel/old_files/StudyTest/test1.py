# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 22:08:51 2014

@author: Pyltsin
"""

from PyQt4 import QtGui
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print(u"Данные:", ind.data())
        print(u"row:", ind.row(), u"column:", ind.column())
    else:
        print(u"Нет текущего элемента")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u"Класс QTableView")
window.resize(500, 200)
view = QtGui.QTableView()

model = QtGui.QStandardItemModel(4, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
view.setModel(model)

button = QtGui.QPushButton(u"Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

