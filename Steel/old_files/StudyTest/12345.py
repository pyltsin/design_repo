import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class OpenFile(QtGui.QMainWindow):
   def __init__(self, parent=None):
       QtGui.QMainWindow.__init__(self, parent)
       self.setGeometry(300, 300, 350, 300)
       self.setWindowTitle('OpenFile')
       self.textEdit = QtGui.QTextEdit()
       self.setCentralWidget(self.textEdit)
       self.statusBar()
       self.setFocus()
       exit = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
       exit.setShortcut('Ctrl+O')
       exit.setStatusTip('Open new File')
       self.connect(exit, QtCore.SIGNAL('triggered()'), self.showDialog)

       menubar = self.menuBar()
       file = menubar.addMenu('&File')
       file.addAction(exit)

   def showDialog(self):
       filename = QtGui.QFileDialog.getExistingDirectory(self, 'Open Folfer', '/home')

       self.textEdit.setText(filename)
       
app = QtGui.QApplication(sys.argv)
cd = OpenFile()
cd.show()
app.exec_()
