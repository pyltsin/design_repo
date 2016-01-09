from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import datetime


class testView(QTableView):

    def __init__(self,parent,data):
        QTableView.__init__(self,parent)
        self.setSizePolicy(QSizePolicy.MinimumExpanding,
                QSizePolicy.MinimumExpanding)

        model = testModel(data)
        self.setModel(model)
        self.setItemDelegate(testDelegate(self))
        self.setFixedWidth(600)
        self.setColumnWidth(2,300)
        self.show()

    def focusOutEvent(self, evt):
        print repr(self) + ' lost focus';

class testModel(QAbstractTableModel):

    def __init__(self,data):
        QAbstractTableModel.__init__(self)
        self.data = data

    def focusOutEvent(self, evt):
        print repr(self) + ' lost focus';

    def flags(self,index):
        return Qt.ItemFlags(QAbstractTableModel.flags(self,index)
                            |Qt.ItemIsEditable)

    def rowCount(self, index=QModelIndex()):
        return 1

    def columnCount(self,index=QModelIndex()):
        return len(self.data)

    def data(self,index,role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.data[index.column()]

    def setData(self, index, value, role=Qt.EditRole):
        self.data[index.column()] = value.toString()
        return True

class testDelegate(QItemDelegate):

    def createEditor(self,parent,option,index):
        if index.column() != 2:
            editor = QLineEdit(parent)
            return editor
        else:
            editor = PathEditor(parent)
            return editor

    def setModelData(self, editor, model, index):
        if index.column() != 2:
            model.setData(index,QVariant(editor.text()))
        else:
            model.setData(index,QVariant(editor.data()))

class PathEditor(QWidget):
    def __init__(self, parent=None):
        print type(parent)
        super(PathEditor, self).__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAutoFillBackground(True)
        self._lm = QGridLayout()
        self._lm.setMargin(0)
        self._initGui()

    def focusOutEvent(self, evt):
        print repr(self) + ' lost focus';

    def _initGui(self):
        for x in range(3):
            combo_box = QComboBox()
            combo_box.addItem('Option 1','One')
            combo_box.addItem('Option 2','Two')
            combo_box.addItem('Option 3','Three')
            combo_box.setCurrentIndex(-1)
            self._lm.addWidget(combo_box, 0,x)

        self.setLayout(self._lm)

    def data(self):
        values = []
        for child in self.children():
            if isinstance(child, QComboBox):
                if child.currentIndex() != -1:

                    values.append(str((child.itemData(child.currentIndex())).toString()))
        res = ",".join(values)
        return res

if __name__ == '__main__':

        app = QApplication(sys.argv)
        data = ['One','Two','Three']
        v = testView(None,data = data)
        app.exec_()
___________________________