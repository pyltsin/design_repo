# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 20:00:01 2014

@author: Pyltsin
"""

import sys
from PyQt4 import QtCore, QtGui


class Example(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        msgBox = QtGui.QMessageBox()
        msgBox.setText('What to do?')
        msgBox.addButton(QtGui.QPushButton('Accept'), QtGui.QMessageBox.YesRole)
        msgBox.addButton(QtGui.QPushButton('Reject'), QtGui.QMessageBox.NoRole)
        msgBox.addButton(QtGui.QPushButton('Cancel'), QtGui.QMessageBox.RejectRole)
        ret = msgBox.exec_()
        
        print ret

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())