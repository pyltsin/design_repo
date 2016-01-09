# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 22:28:30 2014

@author: Pyltsin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 17:33:18 2014

@author: Pyltsin
"""

import numpy as np
import sys

from  PyQt4 import QtCore, QtGui, uic
import matplotlib.pyplot as plt; plt.rcdefaults()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("gui/matplot.ui", self)

        fig = self.matplot.figure
        ax=fig.add_subplot(111)   
        ax.clear()
        rect = mpatches.Rectangle((0,0),100,100)      
        ax.add_patch(rect)        
        
        rect = mpatches.Rectangle((100,100),250.,250.)      
        ax.add_patch(rect)        

        rect = mpatches.Rectangle((200,200),300,300)      
        ax.add_patch(rect)        


        ax.autoscale_view(tight=True, scalex=True, scaley=True)
        self.matplot.draw()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())

