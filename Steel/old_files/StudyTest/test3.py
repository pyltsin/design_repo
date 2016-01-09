# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 22:43:18 2014

@author: Pyltsin
"""

from PyQt4 import QtGui, QtCore
import sys
 
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.table = QtGui.QTableWidget(10,5)
        self.clip = QtGui.QApplication.clipboard()
 
        self.setCentralWidget(self.table)
        self.move(30,30)
 
    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.table.selectedRanges()
                 
            if e.key() == QtCore.Qt.Key_V:#past
                first_row = selected[0].topRow()
                first_col = selected[0].leftColumn()
                 
                #copied text is split by '\n' and '\t' to paste to the cells
                for r, row in enumerate(self.clip.text().split('\n')):
                    for c, text in enumerate(row.split('\t')):
                        self.table.setItem(first_row+r, first_col+c, QtGui.QTableWidgetItem(text))
 
            elif e.key() == QtCore.Qt.Key_C: #copy
                s = ""
                for r in xrange(selected[0].topRow(),selected[0].bottomRow()+1):
                    for c in xrange(selected[0].leftColumn(),selected[0].rightColumn()+1):
                        try:
                            s += str(self.table.item(r,c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n" #eliminate last '\t'
                self.clip.setText(s)
 
def main(args):
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
     
    sys.exit(app.exec_())
 
     
     
if __name__ == "__main__":
    main(sys.argv)