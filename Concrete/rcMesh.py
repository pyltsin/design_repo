# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 23:19:35 2014

@author: Pyltsin
"""
import unittest
import numpy as np


class EmptySections(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class Rectangles(object):
    '''Меш прямоугольников
    lstXY - список 2 точек [[0,0],[5,5]]
    lstN - список количества мешов [100,10]
    mat - добавка mat
    sign - коэффициент для площади
    e0rxry - добавка для e0rxr'''

    def __init__(self, lstXY, lstN, mat=0, sign=1, e0rxry=[0, 0, 0]):
        self.nx = float(lstN[0])
        self.ny = float(lstN[1])
        self.mat = int(mat)
        self.lstXY = lstXY
        self.b = abs(lstXY[1][0] - lstXY[0][0])
        self.h = abs(lstXY[1][1] - lstXY[0][1])
        self.x = lstXY[0][0]
        self.y = lstXY[0][1]
        self.sign = sign
        self.e0rxry = e0rxry

    def a(self):
        '''площадь'''
        return self.b * self.h * self.sign

    def sx(self):
        '''статический момент инерции относительно 0 отн. Y - для определения ц.т.Х'''
        return self.a() * (self.x + self.b / 2.)

    def sy(self):
        '''статический момент инерции относительно 0 отн. X - для определения ц.т.Y'''
        return self.a() * (self.y + self.h / 2.)

    def critPoint(self, e=0, rx=0, ry=0):
        '''Список критический точек - возвращает координаты ВСЕХ 4 точек'''
        b = self.b
        h = self.h
        x = self.x
        y = self.y
        mat = self.mat
        p1 = [x, y, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        p2 = [x + b, y + h, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        p3 = [x + b, y, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        p4 = [x, y + h, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        return [p1, p2, p3, p4]

    def ln(self):
        '''возвращает длину массива'''
        return int(self.nx * self.ny)

    def mesh(self):
        '''функция меша
        Возвращает список матриц:
        []  -  координаты Х
        [] - коордиранты Y
        [] - площадь
        [] - материал
        [] - e0
        [] - rx
        [] - ry'''
        #        gc.collect()
        h, b, x, y, nx, ny, mat = self.h, self.b, self.x, self.y, self.nx, self.ny, self.mat
        sign = self.sign
        db = b / nx
        dh = h / ny
        a = db * dh
        xone = np.ones(ny)
        xmatr = np.arange(nx)
        xmatr = np.meshgrid(xmatr, xone)
        xmatr = xmatr[0].flatten()

        #        xmatr-=(nx/2.)
        xmatr *= db
        xmatr += (x + db / 2)

        yone = np.ones(nx)
        ymatr = np.arange(ny)
        ymatr = np.meshgrid(ymatr, yone)
        ymatr = ymatr[0].transpose()
        ymatr = ymatr.flatten()

        ymatr *= dh
        ymatr += (y + dh / 2)

        amatr = np.ones(nx * ny)
        amatr *= (sign * a)

        matmatr = np.ones(nx * ny)
        matmatr *= mat

        e0 = np.ones(nx * ny)
        e0 *= self.e0rxry[0]
        rx = np.ones(nx * ny)
        rx *= self.e0rxry[1]
        ry = np.ones(nx * ny)
        ry *= self.e0rxry[2]

        return [xmatr, ymatr, amatr, matmatr, e0, rx, ry]

    def title(self):
        return 'Rectangles'


class Circles(object):
    '''Класс для работы с точками - используется для арматуры'''

    def __init__(self, lstXY, lstN=[], mat=0, sign=1, e0rxry=[0, 0, 0]):
        '''lst - [1,2,3] - x-1, y-2, d-3 
        lstN - не используется - только для совместимости
        mat - добавка mat
        sign - коэффициент для площади
        e0rxry - добавка для e0rxr'''

        self.nx = 1
        self.ny = 1
        self.lstXY = lstXY

        self.x = float(lstXY[0])
        self.y = float(lstXY[1])
        self.d = float(lstXY[2])

        self.mat = mat
        self.sign = sign
        self.e0rxry = e0rxry

    def a(self):
        '''возвращает 0 - так как точка не имеет a'''
        return 0

    def sx(self):
        '''возвращает 0 - так как точка не имеет Sx'''
        return 0

    def sy(self):
        '''возвращает 0 - так как точка не имеет Sy'''
        return 0

    def mesh(self):
        '''функция меша
        Возвращает список матриц:
        []  -  координаты Х
        [] - коордиранты Y
        [] - площадь
        [] - материал
        [] - e0
        [] - rx
        [] - ry'''

        a = 3.1415 * (self.d / 2.) ** 2 * self.sign
        matr = [[self.x], [self.y], [a], [self.mat], [self.e0rxry[0]], [self.e0rxry[1]], [self.e0rxry[2]]]
        return matr

    def critPoint(self, e=0, rx=0, ry=0):
        '''Список критический точек - возвращает координаты 1 точки '''
        x = self.x
        y = self.y
        mat = self.mat
        p1 = [x, y, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        return [p1]

    def title(self):
        return 'Circles'

    def ln(self):
        '''возвращает длину массива'''
        return 1


class SolidCircles(object):
    '''Меш круга
    lstXY - [1,2,3] 1- x, 2-y, 3-d 
    lstN - список количества мешов [100]
    mat - добавка mat
    sign - коэффициент для площади
    e0rxry - добавка для e0rxr'''

    def __init__(self, lstXY, lstN, mat=0, sign=1, e0rxry=[0, 0, 0]):

        self.nx = float(lstN[0])
        self.ny = self.nx

        self.x = float(lstXY[0])
        self.y = float(lstXY[1])
        self.d = float(lstXY[2])

        self.mat = int(mat)
        self.sign = sign
        self.e0rxry = e0rxry

    def a(self):
        return 3.1415 * (self.d / 2.) ** 2 * self.sign

    def sx(self):
        return self.a() * self.x

    def sy(self):
        return self.a() * self.y

    def title(self):
        return 'SolidCircles'

    def ln(self):
        '''возвращает длину массива'''
        return int(self.nx ** 2)

    def mesh(self):
        '''функция меша
        Возвращает список матриц:
        []  -  координаты Х
        [] - коордиранты Y
        [] - площадь
        [] - материал
        [] - e0
        [] - rx
        [] - ry'''

        d = self.d
        x = self.x
        y = self.y
        nx = self.nx
        ny = nx
        mat = self.mat

        #        print d, x, y, nx, ny, mat

        lst = []
        b = d / nx
        h = b
        r = d / 2.
        a = b * h
        dx = b / 2. - r
        r2 = r * r

        xone = np.ones(nx)
        xmatr = np.arange(nx)
        xmatr = np.meshgrid(xmatr, xone)
        xmatr = xmatr[0] * h + dx
        ymatr = xmatr.transpose()

        xmatr = xmatr.flatten()
        ymatr = ymatr.flatten()

        #        print xmatr
        #        print ymatr
        #        print r2


        rmatr = np.square(xmatr) + np.square(ymatr)
        rbool = (rmatr <= r2)

        #        print 'rbool'
        #        print rbool

        amatr = rbool.astype(float)
        amatr *= a

        #        print 'amatr'
        #        print amatr
        amatr *= self.sign

        matmatr = np.ones(nx * nx)
        matmatr *= mat

        xmatr += x
        ymatr += y

        e0 = np.ones(nx * ny)
        e0 *= self.e0rxry[0]
        rx = np.ones(nx * ny)
        rx *= self.e0rxry[1]
        ry = np.ones(nx * ny)
        ry *= self.e0rxry[2]

        lst = [xmatr, ymatr, amatr, matmatr, e0, rx, ry]
        #        print amatr
        #        print xmatr
        return lst

    def critPoint(self, e0t=0, rxt=0, ryt=0):
        '''Список критический точек - возвращает координаты 2 точки '''

        d = self.d
        rx = rxt + self.e0rxry[1]
        ry = ryt + self.e0rxry[2]

        #        print rx, ry
        if rx == 0 and ry == 0:
            y0 = d / 2.
            x0 = 0
        else:
            x0 = rx / (rx ** 2 + ry ** 2) ** 0.5 * d / 2.
            y0 = ry / (rx ** 2 + ry ** 2) ** 0.5 * d / 2.

        x = self.x
        y = self.y
        mat = self.mat
        p1 = [x + x0, y + y0, mat, self.e0rxry[0] + e0t, self.e0rxry[1] + rxt, self.e0rxry[2] + ryt]
        p2 = [x - x0, y - y0, mat, self.e0rxry[0] + e0t, self.e0rxry[1] + rxt, self.e0rxry[2] + ryt]
        p3 = [d / 2. + x, y, mat, self.e0rxry[0] + e0t, self.e0rxry[1] + rxt, self.e0rxry[2] + ryt]
        p4 = [-d / 2. + x, y, mat, self.e0rxry[0] + e0t, self.e0rxry[1] + rxt, self.e0rxry[2] + ryt]

        p5 = [x, d / 2. + y, mat, self.e0rxry[0] + e0t, self.e0rxry[1] + rxt, self.e0rxry[2] + ryt]

        p6 = [x, -d / 2. + y, mat, self.e0rxry[0] + e0t, self.e0rxry[1] + rxt, self.e0rxry[2] + ryt]

        return [p1, p2, p3, p4, p5, p6]


class Triangles(object):
    '''Меш треугольника
    lstXY - [1,2,3] 1- x, 2-y, 3-d 
    lstN - список количества мешов [100]
    mat - добавка mat
    sign - коэффициент для площади
    e0rxry - добавка для e0rxr'''

    def __init__(self, lstXY, lstN, mat=0, sign=1, e0rxry=[0, 0, 0]):
        self.nx = float(lstN[0])
        self.ny = float(lstN[1])
        self.mat = mat
        self.lstXY = lstXY
        self.sign = sign
        self.e0rxry = e0rxry

    def title(self):
        return 'Triangles'

    def ln(self):
        '''возвращает длину массива'''
        return int(self.nx * self.ny)

    def a(self):
        '''возвращает площадь'''
        x1 = self.lstXY[0][0]
        y1 = self.lstXY[0][1]

        x2 = self.lstXY[1][0]
        y2 = self.lstXY[1][1]

        x3 = self.lstXY[2][0]
        y3 = self.lstXY[2][1]

        a = 1. / 2. * abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) * self.sign

        return a

    def sx(self):
        return self.a() * (self.xcyc()[0])

    def sy(self):
        return self.a() * (self.xcyc()[1])

    def critPoint(self, e=0, rx=0, ry=0):
        '''Список критический точек - возвращает координаты 3 точки '''

        x1 = self.lstXY[0][0]
        y1 = self.lstXY[0][1]

        x2 = self.lstXY[1][0]
        y2 = self.lstXY[1][1]

        x3 = self.lstXY[2][0]
        y3 = self.lstXY[2][1]

        mat = self.mat
        p1 = [x1, y1, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        p2 = [x2, y2, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        p3 = [x3, y3, mat, self.e0rxry[0] + e, self.e0rxry[1] + rx, self.e0rxry[2] + ry]
        return [p1, p2, p3]

    def xcyc(self):
        '''координаты центра тяжести'''
        x1 = self.lstXY[0][0]
        y1 = self.lstXY[0][1]

        x2 = self.lstXY[1][0]
        y2 = self.lstXY[1][1]

        x3 = self.lstXY[2][0]
        y3 = self.lstXY[2][1]

        xc = (x1 + x2 + x3) / 3.
        yc = (y1 + y2 + y3) / 3.

        return xc, yc

    def mesh(self):
        '''функция меша
        Возвращает список матриц:
        []  -  координаты Х
        [] - коордиранты Y
        [] - площадь
        [] - материал
        [] - e0
        [] - rx
        [] - ry'''

        lstxy, nx, ny, mat, sign = self.lstXY, self.nx, self.ny, self.mat, self.sign
        xc = self.xcyc()[0]
        yc = self.xcyc()[1]

        kmatr = []
        bmatr = []
        for i in range(3):
            if (lstxy[i - 1][0] - lstxy[i][0]) != 0:
                kmatr.append((lstxy[i - 1][1] - lstxy[i][1]) / (lstxy[i - 1][0] - lstxy[i][0]))
                bmatr.append(lstxy[i - 1][1] - lstxy[i - 1][0] * kmatr[i])
            else:
                kmatr.append(None)
                bmatr.append(lstxy[i - 1][0])

        kkmatr = []
        for i in range(3):
            if kmatr[i] != None:
                if yc >= kmatr[i] * xc + bmatr[i]:
                    kkmatr.append(1)
                else:
                    kkmatr.append(0)
            else:
                if xc > bmatr[i]:
                    kkmatr.append(1)
                else:
                    kkmatr.append(0)

        b = max(abs(lstxy[2][0] - lstxy[1][0]), abs(lstxy[2][0] - lstxy[0][0]), abs(lstxy[1][0] - lstxy[0][0]))
        h = max(abs(lstxy[2][1] - lstxy[1][1]), abs(lstxy[2][1] - lstxy[0][1]), abs(lstxy[1][1] - lstxy[0][1]))

        xmin = lstxy[0][0]
        ymin = lstxy[0][1]
        for i in range(3):
            if lstxy[i][0] < xmin:
                xmin = lstxy[i][0]
            if lstxy[i][1] < ymin:
                ymin = lstxy[i][1]

        db = b / nx
        dh = h / ny

        dx = db / 2.
        dy = dh / 2.
        a = db * dh

        #        xmatr=[i for i in range(int(nx))]
        #        xmatr=np.concatenate((xmatr*int(ny-1), xmatr))
        ##        print xmatr
        xone = np.ones(ny)
        xmatr = np.arange(nx)

        xmatr = np.meshgrid(xmatr, xone)
        xmatr = xmatr[0].flatten()

        xmatr *= db
        xmatr += (dx + xmin)

        yone = np.ones(nx)
        ymatr = np.arange(ny)
        ymatr = np.meshgrid(ymatr, yone)
        ymatr = ymatr[0].transpose()
        ymatr = ymatr.flatten()

        ymatr *= dh
        ymatr += (dy + ymin)

        bol = [[], [], []]

        for i in range(3):
            if kmatr[i] != None:
                if kkmatr[i] == 1:
                    bol[i] = (ymatr >= kmatr[i] * xmatr + bmatr[i])
                else:
                    bol[i] = (ymatr < kmatr[i] * xmatr + bmatr[i])
            else:
                if kkmatr[i] == 1:
                    bol[i] = (xmatr >= bmatr[i])
                else:
                    bol[i] = (xmatr < bmatr[i])

        boolmatr = bol[0] * bol[1]

        boolmatr = boolmatr * bol[2]

        amatr = boolmatr + 0.00
        #        print amatr
        amatr *= (sign * a)
        matmatr = np.ones(nx * nx)
        matmatr *= mat

        e0 = np.ones(nx * ny)
        e0 *= self.e0rxry[0]
        rx = np.ones(nx * ny)
        rx *= self.e0rxry[1]
        ry = np.ones(nx * ny)
        ry *= self.e0rxry[2]


        #        lst=np.vstack((xmatr,ymatr,amatr, matmatr))
        #        print [xmatr,ymatr,amatr, matmatr,e0,rx,ry]
        return [xmatr, ymatr, amatr, matmatr, e0, rx, ry]


class Test(unittest.TestCase):
    def testRectangles1(self):
        print 'Rectangles 1'
        rect = Rectangles([[2, 1], [6, 5]], [1000, 1000])
        a = 4 * 4
        jx = 4 * 4 ** 3 / 12. + 4 * 4 * 3 * 3
        jy = 4 * 4 ** 3 / 12. + 4 * 4 * 4 * 4
        self.assertLess(abs(rect.a() - a) / a, 0.0001)
        self.assertLess(abs(rect.sx() - a * 4) / a, 0.0001)
        self.assertLess(abs(rect.sy() - a * 3) / a, 0.0001)

        meshRect = rect.mesh()
        aMesh = meshRect[2].sum()
        jxMesh = (meshRect[1] * meshRect[1] * meshRect[2]).sum()
        jyMesh = (meshRect[0] * meshRect[0] * meshRect[2]).sum()

        self.assertLess(abs(aMesh - a) / a, 0.001)
        self.assertLess(abs(jxMesh - jx) / jx, 0.005)
        self.assertLess(abs(jyMesh - jy) / jy, 0.005)

        self.assertEqual(rect.critPoint(),
                         [[2, 1, 0, 0, 0, 0], [6, 5, 0, 0, 0, 0], [6, 1, 0, 0, 0, 0], [2, 5, 0, 0, 0, 0]])

        rect = Rectangles([[2, 1], [6, 5]], [1000, 1000], 1, -1, [3, 4, 5])

        meshRect = rect.mesh()
        aMesh = meshRect[2].sum()
        self.assertLess(abs(meshRect[3][4] - 1), 0.001)
        self.assertLess(abs(meshRect[4][4] - 3), 0.001)
        self.assertLess(abs(meshRect[5][4] - 4), 0.001)
        self.assertLess(abs(meshRect[6][4] - 5), 0.001)

    def testRectangles2(self):
        print 'Rectangles 2'
        rect = Rectangles([[2, 3], [6, 5]], [2, 2], mat=1, sign=-2, e0rxry=[1.1, 2, 3])
        meshRect = rect.mesh()
        lst = [np.array([3., 5., 3., 5.]), np.array([3.5, 3.5, 4.5, 4.5]), np.array([-4., -4., -4., -4.]),
               np.array([1., 1., 1., 1.]), np.array([1.1, 1.1, 1.1, 1.1]), np.array([2., 2., 2., 2.]),
               np.array([3., 3., 3., 3.])]
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                self.assertEquals(meshRect[i][j], lst[i][j])
        self.assertEqual(rect.ln(), 4)

        self.assertEqual(rect.critPoint(),
                         [[2, 3, 1, 1.1, 2, 3], [6, 5, 1, 1.1, 2, 3], [6, 3, 1, 1.1, 2, 3], [2, 5, 1, 1.1, 2, 3]])
        self.assertEqual(rect.title(), 'Rectangles')

    def testCircles(self):
        print 'Circles'
        circl = Circles([1, 2, 3], mat=2, sign=-2, e0rxry=[4, 5, 6])
        self.assertEqual(circl.title(), 'Circles')
        self.assertEqual(circl.a(), 0)
        self.assertEqual(circl.sx(), 0)
        self.assertEqual(circl.sy(), 0)
        self.assertEqual(circl.mesh(), [[1.0], [2.0], [-14.136750000000001], [2], [4], [5], [6]])
        self.assertEqual(circl.ln(), 1)
        self.assertEqual(circl.critPoint(), [[1., 2., 2, 4, 5, 6]])

    def testSolidCircles(self):
        print 'SolidCircles'

        solidCircl = SolidCircles(lstXY=[0, 0, 2], lstN=[4], mat=5, sign=-6, e0rxry=[0, 3, 4])

        self.assertEqual(solidCircl.critPoint(), [[0.6, 0.8, 5, 0, 3, 4], [-0.6, -0.8, 5, 0, 3, 4],
                                                  [1.0, 0.0, 5, 0, 3, 4],
                                                  [-1.0, 0.0, 5, 0, 3, 4],
                                                  [0.0, 1.0, 5, 0, 3, 4],
                                                  [0.0, -1.0, 5, 0, 3, 4]])

        solidCircl = SolidCircles(lstXY=[1, 2, 4], lstN=[4], mat=5, sign=-6, e0rxry=[7, 2, 0])
        self.assertEqual(solidCircl.title(), 'SolidCircles')

        item = solidCircl.a()
        itemTrue = 2.0 * 2.0 * 3.14 * (-6)
        self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)

        item = solidCircl.sx()
        itemTrue = 2. * 2.0 * 3.14 * (-6) * 1
        self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)

        item = solidCircl.sy()
        itemTrue = 2.0 * 2.0 * 3.14 * (-6) * 2
        self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)

        self.assertEqual(solidCircl.ln(), 16)

        self.assertEqual(solidCircl.critPoint(), [[3.0, 2., 5, 7, 2, 0], [-1.0, 2., 5, 7, 2, 0],
                                                  [3.0, 2.0, 5, 7, 2, 0],
                                                  [-1.0, 2.0, 5, 7, 2, 0],
                                                  [1.0, 4.0, 5, 7, 2, 0],
                                                  [1.0, 0.0, 5, 7, 2, 0]])

        lst = [np.array([-0.5, 0.5, 1.5, 2.5, -0.5, 0.5, 1.5, 2.5, -0.5, 0.5, 1.5,
                         2.5, -0.5, 0.5, 1.5, 2.5]), np.array([0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 2.5, 2.5, 2.5,
                                                               2.5, 3.5, 3.5, 3.5, 3.5]),
               np.array([-0., -6., -6., -0., -6., -6., -6., -6., -6., -6., -6., -6., -0.,
                         -6., -6., -0.]), np.array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5.,
                                                    5., 5., 5.]),
               np.array([7., 7., 7., 7., 7., 7., 7., 7., 7., 7., 7., 7., 7.,
                         7., 7., 7.]), np.array([2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                                 2., 2., 2.]),
               np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                         0., 0., 0.])]

        mesh = solidCircl.mesh()
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                self.assertEquals(mesh[i][j], lst[i][j])

    def testTriangles(self):
        print 'Triangles'
        triangle = Triangles(lstXY=[[1, 0], [5, 0], [4, 3]], lstN=[5, 4], mat=5, sign=-1, e0rxry=[7, 2, 0])
        self.assertEqual(triangle.title(), 'Triangles')

        item = triangle.a()
        itemTrue = 4 * 3 / 2. * (-1)
        self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)

        item = triangle.sx()
        itemTrue = 4 * 3 / 2. * (-1) * 10 / 3.
        self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)

        item = triangle.sy()
        itemTrue = 4 * 3 / 2. * (-1) * 1.
        self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)

        self.assertEqual(triangle.ln(), 20)

        self.assertEqual(triangle.critPoint(), [[1, 0, 5, 7, 2, 0], [5, 0, 5, 7, 2, 0], [4, 3, 5, 7, 2, 0]])

        lst = [np.array([1.4, 2.2, 3., 3.8, 4.6, 1.4, 2.2, 3., 3.8, 4.6, 1.4,
                         2.2, 3., 3.8, 4.6, 1.4, 2.2, 3., 3.8, 4.6]),
               np.array([0.375, 0.375, 0.375, 0.375, 0.375, 1.125, 1.125, 1.125,
                         1.125, 1.125, 1.875, 1.875, 1.875, 1.875, 1.875, 2.625,
                         2.625, 2.625, 2.625, 2.625]),
               np.array([-0.6, -0.6, -0.6, -0.6, -0.6, -0., -0.6, -0.6, -0.6, -0.6, -0.,
                         -0., -0.6, -0.6, -0., -0., -0., -0., -0.6, -0.]),
               np.array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5.,
                         5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5.]),
               np.array([7., 7., 7., 7., 7., 7., 7., 7., 7., 7., 7., 7., 7.,
                         7., 7., 7., 7., 7., 7., 7.]), np.array([2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                                                 2., 2., 2., 2., 2., 2., 2.]),
               np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                         0., 0., 0., 0., 0., 0., 0.])]

        mesh = triangle.mesh()
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                item = mesh[i][j]
                itemTrue = lst[i][j]
                if itemTrue != 0:
                    self.assertLess(abs((item - itemTrue) / itemTrue), 0.001)
                else:
                    self.assertEqual(item, itemTrue)


if __name__ == "__main__":
    unittest.main()
