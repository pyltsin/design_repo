# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 22:09:55 2014

@author: Pyltsin
"""

# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print(u"Данные:", ind.data())
        print(u"row:", ind.row(), u"column:", ind.column())
        ind_parent = ind.parent()
        if ind_parent.isValid():
            print(u"Родитель:", ind_parent.data())
        else:
            print(u"Нет родителя")

        ind_child = ind.child(0, 0)
        if ind_child.isValid():
            print(u"child:", ind_child.data())
        else:
            print(u"Нет child")

        ind_sibling = ind.sibling(0, 0)
        if ind_sibling.isValid():
            print(u"sibling:", ind_sibling.data())
        else:
            print(u"Нет sibling")

    else:
        print(u"Нет текущего элемента")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u"Класс QTreeView")
window.resize(500, 400)
view = QtGui.QTreeView()

model =  QtGui.QStandardItemModel()
parent=QtGui.QStandardItem(3,4)
parent.setText(u"Родитель")
for row in range(0,3):
    for column in range(0,4):
        item=QtGui.QStandardItem("({0},{1})".format(row,column))
        parent.setChild(row, column, item)
model.appendRow(parent)

#model = QtGui.QStandardItemModel()
#parent = model.invisibleRootItem()
#for i in range(0, 4):
#    item = QtGui.QStandardItem(u"Пункт {0}-1".format(i))
#    parent.appendRow(item)
#    item = QtGui.QStandardItem(u"Пункт {0}-2".format(i))
#    parent.appendRow(item)
#    item = QtGui.QStandardItem(u"Пункт {0}-3".format(i))
#    parent.appendRow(item)
#    parent = item
view.setModel(model)

button = QtGui.QPushButton(u"Получить значения")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())


