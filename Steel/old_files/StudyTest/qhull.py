# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 18:10:06 2014

@author: Pyltsin
"""
import numpy as np

from scipy.spatial import ConvexHull
points = np.random.rand(5, 3)   # 30 random points in 2-D
#points1 = np.random.rand(20, 3)   # 30 random points in 2-D

#points*=points1
print points

hull = ConvexHull(points)

print hull
print hull.simplices
print hull.vertices

print u'Сокращение длины'
print len(points), len(hull.vertices)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
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
    

plt.show()
