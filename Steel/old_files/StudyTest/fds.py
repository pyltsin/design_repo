def __init__(self, owner, itemslist):
    QtGui.QItemDelegate.__init__(self, owner)
    self.itemslist = itemslist

def paint(self, painter, option, index):        
    # Get Item Data
    value = index.data(QtCore.Qt.DisplayRole).toInt()[0]
    # fill style options with item data
    style = QtGui.QApplication.style()
    opt = QtGui.QStyleOptionComboBox()
    opt.currentText = str(self.itemslist[value])
    opt.rect = option.rect

    # draw item data as ComboBox
    style.drawComplexControl(QtGui.QStyle.CC_ComboBox, opt, painter)

def createEditor(self, parent, option, index):
    # create the ProgressBar as our editor.
    editor = QtGui.QComboBox(parent)
    editor.addItems(self.itemslist)
    editor.setCurrentIndex(0)
    editor.installEventFilter(self)         
    return editor

def setEditorData(self, editor, index):
    value = index.data(QtCore.Qt.DisplayRole).toInt()[0]
    editor.setCurrentIndex(value)

def setModelData(self,editor,model,index):
    value = editor.currentIndex()
    model.setData(index, QtCore.QVariant(value))

def updateEditorGeometry(self, editor, option, index):
    editor.setGeometry(option.rect)



class SequenceGridModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.parent = parent
        self.arraydata = datain
        self.headerdata = headerdata
    
    def flags(self, index):
        if index.column() == 13:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        return QtCore.QAbstractTableModel.flags(self, index)
    
    
    def data(self, index, role = QtCore.Qt.DisplayRole):
      if not index.isValid():
         if role == QtCore.Qt.UserRole:
            return None
         else:
            return QtCore.QVariant()
    
      value = QtCore.QVariant(self.arraydata[index.row()][index.column()])
    
      if QtCore.Qt.UserRole == role:
         return value
      elif role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
         return QtCore.QVariant(value)
      return QtCore.QVariant()



class SequenceGrid(QtGui.QTableView):
    def __init__(self, parent=None):
        QtGui.QTableView.__init__(self, parent) 
    
        self.selectedIndexes = []
        self.parent = parent
    
        self.checkValues = ['TODO', 'WAITING', 'RETAKE', 'OK']
    
        self.model = SequenceGridModel(self.data, header, self)
        self.setModel(self.model)
        self.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged)
        self.viewport().installEventFilter(self)
        self.setItemDelegateForColumn(13,ComboBoxDelegate(self, self.checkValues))
    
        self.setColumnWidth(13, 64)
