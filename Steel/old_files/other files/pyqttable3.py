# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:59:27 2013

@author: admin
"""

# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    ind = listView.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("Индекс строки:", ind.row())
    else:
        print("Нет текущего элемента")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)
listView = QtGui.QListView()
L = []
for i in range(1, 11):
    L.append("Пункт {0}".format(i))
model = QtGui.QStringListModel(L)
model.insertRows(1, 1)
ind = model.index(1)
model.setData(ind, "Новый элемент")
model.sort(0, order=QtCore.Qt.DescendingOrder)
listView.setModel(model)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(listView)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())
