# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 17:33:18 2014

@author: Pyltsin
"""

import numpy as np
import sys

from scipy.spatial import ConvexHull
from  PyQt4 import QtCore, QtGui, uic
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("gui/matplot.ui", self)
        points = np.random.rand(10000, 3)   # 30 random points in 2-D
#points1 = np.random.rand(20, 3)   # 30 random points in 2-D

#points*=points1
        print points
        
        hull = ConvexHull(points)
        
        print hull
        print hull.simplices
        print hull.vertices
        
        print u'Сокращение длины'
        print len(points), len(hull.vertices)
        fig = self.matplot.figure
        ax = fig.gca(projection='3d')
        ax.plot(points[:,0], points[:,1], points[:,2],'o')
        for simplex in hull.simplices:
            for i in range(3):
        #        print i
                a=i
                b=i+1
                if b>2:
                    b=0
                px=[points[simplex[a],0],points[simplex[b],0]]
                py=[points[simplex[a],1],points[simplex[b],1]]
                pz=[points[simplex[a],2],points[simplex[b],2]]
                
                ax.plot(px,py,pz, c='r', marker='o')
            
        
#        plt.show()
#        help(self.matplot)
#        subplot = self.matplot.getFigure().add_subplot(111)
#        
#        subplot.plot(x,y)
#        mw.draw()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())

