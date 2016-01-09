# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 17:49:22 2014

@author: admin
"""
from table import tables_csv
import numpy as np
from scipy import interpolate
import unittest


class GeneralMaterial(object):
    '''возвращает функцию по интерполяции по графику (общему)
typPS - тип предельного состояния'''

    def __init__(self, matObject):
        dictMat = matObject.kwargs

        self.name = dictMat["name"]  # название материала
        self.type_material = dictMat["type_material"]  # "steel" , "concrete"
        self.data_table_ps1 = dictMat["data_table_ps1"]  # таблица в виде списка для расчетной ситуации
        self.data_table_ps2 = dictMat["data_table_ps2"]  # таблица в виде списка для норативной ситуации
        self.data_table_ps2_long = dictMat["data_table_ps2_long"]  # таблица в виде списка для длительной норативной ситуации
        self.e = dictMat["e"]  # модуль деформации начальный
        self.e_ult = dictMat["e_ult"]  # предельое
        self.e_crit = dictMat["e_crit"]  # дальше можно не решать
        self.creep = dictMat["creep"]  # 0 - нет, 1 - да
        self.e0_ult = dictMat["e0_ult"]  # для бетона
        self.et = dictMat["et"]  # для бетона для определения трещин - дальше напряжения падают до 0

    def generate_ps1(self):
        self.general_generate(self.data_table_ps1)

    def generate_ps2(self):
        self.general_generate(self.data_table_ps2)

    def generate_ps2long(self):
        self.general_generate(self.data_table_ps2_long)

    def general_generate(self, table):
        x = []
        y = []
        for point in table:
            if point[0] < self.et or self.type_material == "steel":
                x.append(point[0])
                y.append(point[1])

        if not x:
            x.append(0)
            y.append(0)

        if self.type_material == "steel":
            x.append(x[-1] * 1000000.)
            y.append(y[-1])
        else:
            x.append(self.et)
            y.append(0)

        x.insert(0, -self.e_crit * 1000000.)
        y.insert(0, y[0])

        x = np.array(x)
        y = np.array(y)

        ev = []

        for i in xrange(len(x)):
            if x[i] != 0:
                ev.append(y[i] / x[i])
            else:
                ev.append(y[i - 1] / x[i - 1])

        self.x = x
        self.y = y
        self.yEv = np.array(ev)  # угол наклона касательной от 0
        self.ky = []
        self.kyEv = []
        for i in range(len(x) - 1):
            self.ky.append(
                (self.y[i + 1] - self.y[i]) / (self.x[i + 1] - self.x[i]))  # наклон касательной от точки к точки
            self.kyEv.append((self.yEv[i + 1] - self.yEv[i]) / (self.x[i + 1] - self.x[i]))  # наклон касательной к yEv
        self.ky = np.array(self.ky)
        self.kyEv = np.array(self.kyEv)

        self.dx = self.e










class Reinforced(object):
    '''Класс для работы с арматурой и всем что с ней связано'''

    def __init__(self):

        self.norme = False
        self.approxSP = False
        self.typ = 'A'
        self.a = False
        self.ys = False
        self.ysc = 1
        self.ysi = 1

    def initProperties(self):
        '''расчет и запись исходных значений для отображения, возвращает список;
        если approx=True - по аппроксимации, по а и ys
        eсли norme=52: то по списку по a
        eсли norme=63: то по списку по a'''
        if self.approxSP == True:
            return self.propertiesApproxSP()
        else:
            if self.norme == 52:
                return self.propertiesSP52()
            elif self.norme == 63:
                return self.propertiesSP63()

    def setA(self, txt):
        '''назначить typm rn'''
        self.typ = txt[0]
        self.a = int(txt[1:])

    def propertiesApproxSP(self):
        '''аппроксимирующие функции определния характеристик бетона с A240'''
        a = self.a
        ys = self.ys

        rsn = a * 100 / 9.81
        rs = rsn / ys

        rs /= self.ysi

        if self.typ == u'K':
            es = 1.95 * 10 ** 5 * 100 / 9.81
        else:
            es = 2.0 * 10 ** 5 * 100 / 9.81

        if a >= 600:
            es2 = 0.015
        else:
            es2 = 0.025

        rsw = rs * 0.8
        if rsw >= 300 * 100 / 9.81:
            rsw = 300 * 100 / 9.81

        self.rsn, self.rs, self.rsw, self.es, self.es2 = rsn, rs, rsw, es, es2
        return rsn, rs, rsw, es, es2

    #    def functDiaLst(self, lst):
    #        '''Возвращает функцию по интерполяции по списку  - НЕТ ПРОВЕРКИ'''
    #        x=lst[0]
    #        y=lst[1]
    #        x=np.array(x)
    #
    #        y=np.array(y)
    #
    #
    #        funSigma=interpolate.interp1d(x,y, kind='linear')
    #        ev=[]
    #        for i in range(len(x)):
    #            if x[i]!=0:
    #                ev.append(y[i]/x[i])
    #            else:
    #                if i+1>len(x):
    #                    ev.append(y[i-1]/x[i-1])
    #                else:
    #                    ev.append(y[i+1]/x[i+1])
    #        funEv=interpolate.interp1d(x,ev, kind='linear')
    #
    #        return [funSigma, funEv]

    def functDia(self, typPS):
        '''возвращает функцию по интерполяции по графику (общему)
        typPS - тип предельного состояния'''

        if typPS == 1:
            r = self.rs
        else:
            r = self.rsn

        rc = r * self.ysc

        if self.a < 600:
            es0 = r / self.es
            esc0 = rc / self.es
        else:
            es0 = r / self.es + 0.002
            esc0 = rc / self.es + 0.002
        if self.a < 600:
            x = [-self.es2, -esc0, 0, es0, self.es2]
            y = [-rc, -rc, 0, r, r]
        else:
            es1 = 0.9 * r / self.es
            esc1 = 0.9 * rc / self.es
            sigmas1 = 0.9 * r
            sigmas2 = 1.1 * r

            sigmasc1 = 0.9 * rc
            sigmasc2 = 1.1 * rc

            #            es0=r/self.es
            es3 = 2 * (es0 - es1) + es1
            esc3 = 2 * (esc0 - esc1) + esc1

            #            e3=(self.es2-es1)/1.1+es1
            x = [-self.es2, -esc3, -esc1, 0, es1, es3, self.es2]
            y = [-sigmasc2, -sigmasc2, -sigmasc1, 0, sigmas1, sigmas2, sigmas2]

        x.append(x[-1] * 1000000.)
        y.append(y[-1])

        x.insert(0, x[0] * 1000000.)
        y.insert(0, y[0])

        x = np.array(x)
        y = np.array(y)

        ev = []

        for i in range(len(x)):
            if x[i] != 0:
                ev.append(y[i] / x[i])
            else:
                ev.append(y[i - 1] / x[i - 1])

        self.x = x
        self.y = y
        self.yEv = np.array(ev)
        self.ky = []
        self.kyEv = []
        for i in range(len(x) - 1):
            self.ky.append((self.y[i + 1] - self.y[i]) / (self.x[i + 1] - self.x[i]))
            self.kyEv.append((self.yEv[i + 1] - self.yEv[i]) / (self.x[i + 1] - self.x[i]))
        self.ky = np.array(self.ky)
        self.kyEv = np.array(self.kyEv)

        self.dx = self.e()

    def listSP52(self):
        '''возвращает список доступных классов по СП52'''
        fil = tables_csv(filename='MaterialData\\reinfSP52.csv', typ='none')
        return fil.get_title_column()

    def listSP63(self):
        '''возвращает список доступных классов по СП63'''
        fil = tables_csv(filename='MaterialData\\reinfSP63.csv', typ='none')
        return fil.get_title_column()

    def propertiesSP52(self):
        name = self.typ + str(self.a)
        fil = tables_csv(filename='MaterialData\\reinfSP52.csv', typ='float')
        table = fil.get_table()
        index = False
        for i in table[1:]:
            #            print name, i[0]
            if name == i[0]:
                index = i
        if index != False:
            self.rsn, self.rs, self.rsw, self.es, self.es2, self.ys = index[1:]
            self.rs /= self.ysi
            self.rsw /= self.ysi

            self.rsn *= (100 / 9.81)
            self.rs *= (100 / 9.81)
            self.rsw *= (100 / 9.81)
            self.es *= (100 / 9.81)

            return self.rsn, self.rs, self.rsw, self.es, self.es2

    def propertiesSP63(self):
        name = self.typ + str(self.a)
        fil = tables_csv(filename='MaterialData\\reinfSP63.csv', typ='float')
        table = fil.get_table()
        index = False
        for i in table[1:]:
            if name == i[0]:
                index = i
        if index != False:
            self.rsn, self.rs, self.rsw, self.es, self.es2, self.ys = index[1:]
            self.rs /= self.ysi
            self.rsw /= self.ysi

            self.rsn *= (100 / 9.81)
            self.rs *= (100 / 9.81)
            self.rsw *= (100 / 9.81)
            self.es *= (100 / 9.81)

            if (self.a == 600 and self.typ == 'A') or (self.a == 500 and self.typ == 'B'):
                self.ysc = 0.95
            else:
                self.ysc = 1

            return self.rsn, self.rs, self.rsw, self.es, self.es2

    def title(self):
        return 'Reinforced'

    def kk(self, lste):
        '''критерий разрушения по металлу - i/self.es2'''

        k = 0
        for i in lste:
            kTemp = abs(i / self.es2)
            if k < kTemp:
                k = kTemp
        return [k, self.es2, min(lste), max(lste)]

    def kkStart(self, lste):
        return self.kk(lste)

    def e(self):
        return self.es


class Concrete(object):
    '''Класс для работы с бетоном и всем что с ней связано'''

    def __init__(self):
        self.norme = False
        self.approxSP = False
        self.phi = 75
        self.b = False
        self.yb = 1
        self.c1 = False
        self.c2 = False

    def e(self):
        return self.eb

    def initProperties(self):
        '''расчет и запись исходных значений для отображения, возвращает список;
        если approx=True - по аппроксимации, по а и ys
        eсли norme=52: то по списку по a
        eсли norme=63: то по списку по a'''
        if self.approxSP == True:
            return self.propertiesApproxSP()
        else:
            if self.norme == 52:
                return self.propertiesSP52()
            elif self.norme == 63:
                return self.propertiesSP63()

    def propertiesSP52(self):
        self.ephi()
        name = unicode(self.b)
        fil = tables_csv(filename='MaterialData\\concreteSP52.csv', typ='float')
        table = fil.get_table()
        index = False
        for i in table[1:]:
            if name == i[0]:
                index = i
        if index != False:
            self.rbn, self.rbtn, self.rb, self.rbt, self.eb = index[1:]
            self.rbn *= (100 / 9.81)
            self.rbtn *= (100 / 9.81)
            self.rb *= (100 / 9.81 / self.yb)
            self.rbt *= (100 / 9.81 / self.yb)
            self.eb *= (100 / 9.81)

            return self.rbn, self.rb, self.rbtn, self.rbt, self.eb, self.eb0, self.eb2, self.eb1red, self.ebt0, self.ebt2, self.ebt1red, self.ebl0, self.ebl2, self.ebl1red, self.eblt0, self.eblt2, self.eblt1red, self.phi_crc

    def propertiesSP63(self):
        self.ephi()
        name = unicode(self.b)
        fil = tables_csv(filename='MaterialData\\concreteSP63.csv', typ='float')
        table = fil.get_table()
        index = False
        for i in table[1:]:
            if name == i[0]:
                index = i
        if index != False:
            self.rbn, self.rbtn, self.rb, self.rbt, self.eb = index[1:]

            self.rbn *= (100 / 9.81)
            self.rbtn *= (100 / 9.81)
            self.rb *= (100 / 9.8 / self.yb)
            self.rbt *= (100 / 9.81 / self.yb)
            self.eb *= (100 / 9.81)

            return self.rbn, self.rb, self.rbtn, self.rbt, self.eb, self.eb0, self.eb2, self.eb1red, self.ebt0, self.ebt2, self.ebt1red, self.ebl0, self.ebl2, self.ebl1red, self.eblt0, self.eblt2, self.eblt1red, self.phi_crc

    def listSP52(self):
        '''возвращает список доступных классов по СП52'''
        fil = tables_csv(filename='MaterialData\\concreteSP52.csv', typ='none')
        return fil.get_title_column()

    def listSP63(self):
        '''возвращает список доступных классов по СП63'''
        fil = tables_csv(filename='MaterialData\\concreteSP63.csv', typ='none')
        return fil.get_title_column()

    #    def functDiaLst(self, lst):
    #        '''Возвращает функцию по интерполяции по списку'''
    #        x=lst[0]
    #        y=lst[1]
    #        x=np.array(x)
    #
    #        y=np.array(y)
    #
    #
    #        funSigma=interpolate.interp1d(x,y, kind='linear')
    #        ev=[]
    #        for i in range(len(x)):
    #            if x[i]!=0:
    #                ev.append(y[i]/x[i])
    #            else:
    #                if i+1>len(x):
    #                    ev.append(y[i-1]/x[i-1])
    #                else:
    #                    ev.append(y[i+1]/x[i+1])
    #        funEv=interpolate.interp1d(x,ev, kind='linear')
    #
    #        return [funSigma, funEv]

    def title(self):
        return 'Concrete'

    def functDia(self, typDia, typPS, typTime, typR, typRT):
        '''Отдача функции расчета sigma по e или v по e
        typDia - тип диаграммы для бетонна, 
        typPS - тип предельного состояния, 
        typTime - long или short для бетона, 
        typR - для бетона, если 1 - просто режется все -, если 2 - после последнего значения - до 0, другое - продлеваем до max, 
        typRT - для бетона, если 1 - просто режется все +, если 2 - после последнего значения - до 0, другое - продлеваем до max'''

        rbn, rb, rbtn, rbt, eb = self.rbn, self.rb, self.rbtn, self.rbt, self.eb
        eb0, eb2, eb1red, ebt0, ebt2, ebt1red = self.eb0, self.eb2, self.eb1red, self.ebt0, self.ebt2, self.ebt1red
        ebl0, ebl2, ebl1red, eblt0, eblt2, eblt1red = self.ebl0, self.ebl2, self.ebl1red, self.eblt0, self.eblt2, self.eblt1red
        phi_crc = self.phi_crc

        if typPS == 1:
            r = rb
            rt = rbt
        elif typPS == 2:
            r = rbn
            rt = rbtn

        if typTime == 'short':

            e0 = eb0
            et0 = ebt0

            e2 = eb2
            et2 = ebt2

            e1red = eb1red
            et1red = ebt1red
        elif typTime == 'long':

            r = r * 0.9
            rt = rt * 0.9
            eb = eb / (1 + phi_crc)

            e0 = ebl0
            et0 = eblt0

            e2 = ebl2
            et2 = eblt2

            e1red = ebl1red
            et1red = eblt1red

        if typDia == 2:
            x = [-e2, -e1red, 0, et1red, et2]
            y = [-r, -r, 0, rt, rt]
        elif typDia == 3:
            x = [-e2, -e0, -0.6 * r / eb, 0, 0.6 * rt / eb, et0, et2]
            y = [-r, -r, -0.6 * r, 0, 0.6 * rt, rt, rt]

        if typR == 1:
            n = 0
            for i in x:
                if i < 0:
                    y[n] = 0
                n += 1
        elif typR == 2:
            x.insert(0, x[0] * 1.001)
            y.insert(0, 0)

        if typRT == 1:
            n = 0
            for i in x:
                if i > 0:
                    y[n] = 0
                n += 1
        elif typRT == 2:
            x.append(x[-1] * 1.001)
            y.append(0)

        x.append(x[-1] * 1000000.)
        y.append(y[-1])

        x.insert(0, x[0] * 1000000.)
        y.insert(0, y[0])

        x = np.array(x)
        y = np.array(y)

        ev = []
        for i in range(len(x)):
            if x[i] != 0:
                ev.append(y[i] / x[i])
            else:
                ev.append(y[i - 1] / x[i - 1])

        self.x = x
        self.y = y
        self.yEv = np.array(ev)
        self.ky = []
        self.kyEv = []
        for i in range(len(x) - 1):
            self.ky.append((self.y[i + 1] - self.y[i]) / (self.x[i + 1] - self.x[i]))
            self.kyEv.append((self.yEv[i + 1] - self.yEv[i]) / (self.x[i + 1] - self.x[i]))
        self.ky = np.array(self.ky)
        self.kyEv = np.array(self.kyEv)

        self.dx = self.e()

    def propertiesApproxSP(self):
        '''аппроксимирующие функции определния характеристик бетона с В10'''
        b = self.b

        if b > 10 and b < 60:
            if b >= 70:
                ybb = 1 / (360 - b) * 300
            else:
                ybb = 1
            yb1 = 1.3 * ybb
            ybt1 = 1.5 * ybb

            rbn = max(b * (0.765 - 0.001 * b), 0.71 * b)
            rb = rbn / yb1

            #    rbtn=0.232*b**(2./3)*0.776
            rbtn = 0.232 * (rbn) ** (2. / 3) * 0.956 * 1.01
            rbt = rbtn / ybt1

            eb = 55000 * b / (19. + b / 0.9) / 1000 * 1.03

            rbn *= (100. / 9.81)
            rb *= (100. / 9.81)
            rbtn *= (100. / 9.81 / self.yb)
            rbt *= (100. / 9.81 / self.yb)
            eb *= 10000.

            self.rbn, self.rb, self.rbtn, self.rbt, self.eb = rbn, rb, rbtn, rbt, eb

            self.ephi()
            return self.rbn, self.rb, self.rbtn, self.rbt, self.eb, self.eb0, self.eb2, self.eb1red, self.ebt0, self.ebt2, self.ebt1red, self.ebl0, self.ebl2, self.ebl1red, self.eblt0, self.eblt2, self.eblt1red, self.phi_crc

    def ephi(self):
        b = float(self.b)
        phi = self.phi

        eb0 = 0.002
        ebt0 = 0.0001

        if b <= 60:
            eb2 = 0.0035
        else:
            eb2 = (0.0033 - 0.0028) / (70 - 100) * (b - 100) + 0.0028

        eb1red = 0.0015

        ebt2 = 0.00015
        ebt1red = 0.00008

        if phi > 75:
            ebl0 = 3
            ebl2 = 4.2
            ebl1red = 2.4

            eblt0 = 0.21
            eblt2 = 0.27
            eblt1red = 0.19
        elif phi <= 75 and phi >= 40:
            ebl0 = 3.4
            ebl2 = 4.8
            ebl1red = 2.8

            eblt0 = 0.24
            eblt2 = 0.31
            eblt1red = 0.22
        else:
            ebl0 = 4
            ebl2 = 5.6
            ebl1red = 3.4

            eblt0 = 0.28
            eblt2 = 0.36
            eblt1red = 0.26

        ebl0 /= 1000.
        ebl2 /= 1000.
        ebl1red /= 1000.

        eblt0 /= 1000.
        eblt2 /= 1000.
        eblt1red /= 1000.

        linMatrB = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 100])
        linMatr75 = np.array([2.8, 2.4, 2., 1.8, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1., 1.])
        linMatr4075 = np.array([3.9, 3.4, 2.8, 2.5, 2.3, 2.1, 1.9, 1.8, 1.6, 1.5, 1.4, 1.4])
        linMatr40 = np.array([5.6, 4.8, 4.0, 3.6, 3.2, 3., 2.8, 2.6, 2.4, 2.2, 2., 2.])
        funPhi75 = interpolate.interp1d(linMatrB, linMatr75, kind='linear')
        funPhi4075 = interpolate.interp1d(linMatrB, linMatr4075, kind='linear')
        funPhi40 = interpolate.interp1d(linMatrB, linMatr40, kind='linear')

        if b > 60:
            if phi > 75:
                phi_crc = 1.
            elif phi <= 75 and phi >= 40:
                phi_crc = 1.4
            else:
                phi_crc = 2.0
        else:
            if phi > 75:
                phi_crc = funPhi75(b)
            elif phi <= 75 and phi >= 40:
                phi_crc = funPhi4075(b)
            else:
                phi_crc = funPhi40(b)

        self.eb0, self.eb2, self.eb1red, self.ebt0, self.ebt2, self.ebt1red = eb0, eb2, eb1red, ebt0, ebt2, ebt1red
        self.ebl0, self.ebl2, self.ebl1red, self.eblt0, self.eblt2, self.eblt1red = ebl0, ebl2, ebl1red, eblt0, eblt2, eblt1red
        self.phi_crc = phi_crc

    def kk(self, lste):
        '''критерий разрушения по бетону -  если есть разные знаки - i/self.eb2'''
        emin = min(lste)
        emax = max(lste)
        if emax > 0 and emin < 0:
            m = self.eb2
            k = abs(emin / self.eb2)
        elif emax < 0 and emin < 0:
            m = self.eb2 - (self.eb2 - self.eb0) * emax / emin
            k = abs(emin / m)
        else:
            k = 0
            m = 0
        return [k, m, emin, emax]

    def kkStart(self, lste):
        emin = min(lste)
        emax = max(lste)
        m = self.eb2
        k = abs(emin / self.eb2)
        return [k, m, emin, emax]


class Test(unittest.TestCase):
    def testConcrete52(self):
        print 'Concrete 52'
        con = Concrete()
        con.norme = 52
        con.b = 25
        con.initProperties()

        test = [u'10', u'15', u'20', u'25', u'30', u'35', u'40', u'45', u'50', u'55', u'60']
        check = con.listSP52()
        self.assertEqual(test, check)
        #        print con.listSP52()

        test = con.rbn
        check = 188
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rb
        check = 148
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rbtn
        check = 15.8
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rbt
        check = 10.7
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb
        check = 306000
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb0
        check = 0.002
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb2
        check = 0.0035
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb1red
        check = 0.0015
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt0
        check = 0.0001
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt2
        check = 0.00015
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt1red
        check = 0.00008
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl0
        check = 0.0034
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl2
        check = 0.0048
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl1red
        check = 0.0028
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt0
        check = 0.00024
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt2
        check = 0.00031
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt1red
        check = 0.00022
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.phi_crc
        check = 2.5
        self.assertLess(abs(test - check) / check, 0.01)

        self.assertEqual(con.title(), 'Concrete')

    def testConcrete63(self):
        print 'Concrete 63'
        con = Concrete()
        con.norme = 63
        con.b = 25
        con.initProperties()

        #        print con.listSP63()

        test = [u'10', u'12.5', u'15', u'20', u'25', u'30', u'35', u'40', u'45', u'50', u'55', u'60', u'70', u'80',
                u'90', u'100']
        check = con.listSP63()
        self.assertEqual(test, check)

        test = con.rbn
        check = 188
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rb
        check = 148
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rbtn
        check = 15.8
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rbt
        check = 10.7
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb
        check = 306000
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb0
        check = 0.002
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb2
        check = 0.0035
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb1red
        check = 0.0015
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt0
        check = 0.0001
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt2
        check = 0.00015
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt1red
        check = 0.00008
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl0
        check = 0.0034
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl2
        check = 0.0048
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl1red
        check = 0.0028
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt0
        check = 0.00024
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt2
        check = 0.00031
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt1red
        check = 0.00022
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.phi_crc
        check = 2.5
        self.assertLess(abs(test - check) / check, 0.01)

    def testConcreteApprox(self):
        print 'Concrete Approx'
        con = Concrete()
        con.approxSP = True
        con.b = 25
        con.initProperties()

        test = con.rbn
        check = 188
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.rb
        check = 148
        self.assertLess(abs(test - check) / check, 0.02)

        test = con.rbtn
        check = 15.8
        self.assertLess(abs(test - check) / check, 0.02)

        test = con.rbt
        check = 10.7
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb
        check = 306000
        self.assertLess(abs(test - check) / check, 0.02)

        test = con.eb0
        check = 0.002
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb2
        check = 0.0035
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eb1red
        check = 0.0015
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt0
        check = 0.0001
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt2
        check = 0.00015
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebt1red
        check = 0.00008
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl0
        check = 0.0034
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl2
        check = 0.0048
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.ebl1red
        check = 0.0028
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt0
        check = 0.00024
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt2
        check = 0.00031
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.eblt1red
        check = 0.00022
        self.assertLess(abs(test - check) / check, 0.01)

        test = con.phi_crc
        check = 2.5
        self.assertLess(abs(test - check) / check, 0.01)

    def testConcreteDia(self):
        '''Отдача функции расчета sigma по e или v по e
        typDia - тип диаграммы для бетонна, 
        typPS - тип предельного состояния, 
        typTime - long или short для бетона, 
        typR - для бетона, если 1 - просто режется все -, если 2 - после последнего значения - до 0, другое - продлеваем до max, 
        typRT - для бетона, если 1 - просто режется все +, если 2 - после последнего значения - до 0, другое - продлеваем до max'''

        print 'Concrete Dia'
        con = Concrete()
        con.approxSP = True
        con.b = 25
        con.initProperties()
        con.functDia(typDia=2, typPS=1, typTime='short', typR=3, typRT=3)
        print "typDia=2, typPS=1, typTime='short', typR=3, typRT=3"
        #        print con.x

        lstx = [-3.5 * 10 ** 3, -0.0035, - 0.0015, 0, 0.00008, 0.00015, 150]
        for i in range(len(lstx)):
            test = con.x[i]
            check = lstx[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.01)
            else:
                self.assertLess(abs(test - check), 0.01)


                #        print con.y

        lsty = [-148, -148, -148, 0, 10.7, 10.7, 10.7]
        for i in range(len(lstx)):
            test = con.y[i]
            check = lsty[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

        lstyEv = []
        for i in range(len(lstx)):
            if lstx[i] == 0:
                lstyEv.append(lstyEv[i - 1])
            else:
                lstyEv.append(float(lsty[i]) / lstx[i])

                #        print con.yEv
                #        print lstyEv

        for i in range(len(lstx)):
            test = con.yEv[i]
            check = lstyEv[i]
            if test != 0:
                #                print test, check
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

        lstky = []
        lstkyEv = []
        for i in range(len(lstx) - 1):
            lstky.append((lsty[i + 1] - lsty[i]) / (lstx[i + 1] - lstx[i]))
            lstkyEv.append((lstyEv[i + 1] - lstyEv[i]) / (lstx[i + 1] - lstx[i]))

        for i in range(len(lstx) - 1):
            test = con.kyEv[i]
            check = lstkyEv[i]
            if test != 0:
                #                print test, check
                self.assertLess(abs((test - check) / check), 0.04)
            else:
                self.assertLess(abs(test - check), 0.02)

        for i in range(len(lstx) - 1):
            test = con.yEv[i]
            check = lstyEv[i]
            if test != 0:
                #                print test, check
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

                #        print con.ky
                #        print con.kyEv
        con.functDia(typDia=3, typPS=2, typTime='long', typR=1, typRT=2)
        print "typDia=3, typPS=2, typTime='long', typR=1, typRT=2"
        #        print con.x
        #        print con.y

        lstx = [-4.8 * 10 ** 3, -0.0048, -0.0034, -0.6 * 185 / 3.06 / 10 ** 5 * 0.9 * 3.5, 0,
                0.9 * 0.6 * 10.7 * 1.5 / 3.06 / 10 ** 5 * 3.5, 0.00024, 0.00031, 0.00031 * 1.001, 310]
        for i in range(len(lstx)):
            test = con.x[i]
            check = lstx[i]
            #            print test, check
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.04)
            else:
                self.assertLess(abs(test - check), 0.01)


                #        print con.y

        lsty = [0, 0, 0, 0, 0, 10.7 * 0.6 * 0.9 * 1.5, 10.7 * 0.9 * 1.5, 10.7 * 0.9 * 1.5, 0, 0]
        for i in range(len(lstx)):
            test = con.y[i]
            check = lsty[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

        con.functDia(typDia=3, typPS=1, typTime='short', typR=2, typRT=1)
        print "typDia=3, typPS=1, typTime='short', typR=2, typRT=1"
        #        print con.x
        #        print con.y

        lstx = [-3500., -0.0035035, -0.0035, -0.002, -0.6 * 148 / 3. / 10 ** 5, 0, 10.7 * 0.6 / 3. / 10 ** 5, 0.0001,
                0.00015, 150.]
        for i in range(len(lstx)):
            test = con.x[i]
            check = lstx[i]
            #            print test, check
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.04)
            else:
                self.assertLess(abs(test - check), 0.01)


                #        print con.y

        lsty = [0, 0, -148, -148, -0.6 * 148, 0, 0, 0, 0, 0]
        for i in range(len(lstx)):
            test = con.y[i]
            check = lsty[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

    def testReinforced52(self):
        print 'Reinforced 52'
        rein = Reinforced()
        rein.norme = 52
        rein.typ = 'A'
        rein.a = 400
        rein.ysi = 0.7
        rein.initProperties()

        #        print rein.listSP52()

        test = [u'A240', u'A300', u'A400', u'A500', u'B500']
        check = rein.listSP52()
        self.assertEqual(test, check)

        test = rein.rsn
        check = 4000
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.rs
        check = 4000 / 1.1 / 0.7
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.rsw
        check = 4000 / 1.1 * 0.8 / 0.7
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.es
        check = 2.06 * 10 ** 6
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.es2
        check = 0.025
        self.assertLess(abs(test - check) / check, 0.02)

    def testReinforced63(self):
        print 'Reinforced 63'
        rein = Reinforced()
        rein.norme = 63
        rein.typ = 'A'
        rein.a = 400
        rein.ysi = 1.3
        rein.initProperties()

        #        print rein.listSP52()

        test = [u'A240', u'A400', u'A500', u'A600', u'A800', u'A1000', u'B500']
        check = rein.listSP63()
        self.assertEqual(test, check)

        test = rein.rsn
        check = 4000
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.rs
        check = 400 / 1.15 * 100 / 9.81 / 1.3
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.rsw
        check = 400 / 1.15 * 100 / 9.81 * 0.8 / 1.3
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.es
        check = 2.06 * 10 ** 6
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.es2
        check = 0.025
        self.assertLess(abs(test - check) / check, 0.02)

        self.assertEqual('Reinforced', rein.title())

    def testReinforcedApprox(self):
        print 'Reinforced Approx'
        rein = Reinforced()
        rein.approxSP = True
        rein.typ = 'A'
        rein.a = 400
        rein.ys = 1.1
        rein.ysi = 0.8
        rein.initProperties()

        test = rein.rsn
        check = 4000
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.rs
        check = 4000 / 1.1 / 0.8
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.rsw
        check = 300 * 100 / 9.81
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.es
        check = 2.06 * 10 ** 6
        self.assertLess(abs(test - check) / check, 0.02)

        test = rein.es2
        check = 0.025
        self.assertLess(abs(test - check) / check, 0.02)

    def testReinforcedDia(self):
        print 'Reinforced Dia'
        print "typDia=2, typPS=1"
        rein = Reinforced()
        rein.norme = 52
        rein.typ = 'A'
        rein.a = 400
        rein.initProperties()
        rein.functDia(typPS=1)

        #        print rein.x
        #
        #        print rein.y
        #        print rein.yEv
        #
        #        print rein.ky
        #        print rein.kyEv

        lstx = [-2.5 * 10 ** 4, -0.025, -400 * 100 / 9.81 / 2.1 / 10 ** 6 / 1.1, 0,
                400 * 100 / 9.81 / 2.1 / 10 ** 6 / 1.1, 0.025, 25000]
        for i in range(len(lstx)):
            test = rein.x[i]
            check = lstx[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.01)
            else:
                self.assertLess(abs(test - check), 0.01)

        lsty = [-3640, -3640, -3640, 0, 3640, 3640, 3640]
        for i in range(len(lstx)):
            test = rein.y[i]
            check = lsty[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.025)
            else:
                self.assertLess(abs(test - check), 0.025)

        lstyEv = []
        for i in range(len(lstx)):
            if lstx[i] == 0:
                lstyEv.append(lstyEv[i - 1])
            else:
                lstyEv.append(float(lsty[i]) / lstx[i])

                #        print con.yEv
                #        print lstyEv

        for i in range(len(lstx)):
            test = rein.yEv[i]
            check = lstyEv[i]
            if test != 0:
                #                print test, check
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

        lstky = []
        lstkyEv = []
        for i in range(len(lstx) - 1):
            lstky.append((lsty[i + 1] - lsty[i]) / (lstx[i + 1] - lstx[i]))
            lstkyEv.append((lstyEv[i + 1] - lstyEv[i]) / (lstx[i + 1] - lstx[i]))

        for i in range(len(lstx) - 1):
            test = rein.kyEv[i]
            check = lstkyEv[i]
            if test != 0:
                #                print test, check
                self.assertLess(abs((test - check) / check), 0.04)
            else:
                self.assertLess(abs(test - check), 0.02)

        for i in range(len(lstx) - 1):
            test = rein.yEv[i]
            check = lstyEv[i]
            if test != 0:
                #                print test, check
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

        print "typDia=3, typPS=2"

        rein.norme = 63
        rein.typ = 'A'
        rein.a = 600
        rein.initProperties()
        rein.functDia(typPS=2)

        est = 0.9 * 600 * 10 / (2.06 * 10 ** 6) + 2 * (0.002 + 0.1 * 600 * 10 / 2.06 / 10 ** 6)
        #        print rein.x
        #
        #        print rein.y
        #        print rein.yEv
        #
        #        print rein.ky
        #        print rein.kyEv

        lstx = [-0.015 * 10 ** 6, -0.015, -est, -0.9 * 600 * 100 / 9.8 / (2.06 * 10 ** 6) * 0.95, 0,
                0.9 * 600 * 100 / 9.8 / (2.06 * 10 ** 6), est, 0.015, 0.015 * 10 ** 6]
        for i in range(len(lstx)):
            test = rein.x[i]
            check = lstx[i]
            #            print test, check
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.02)
            else:
                self.assertLess(abs(test - check), 0.02)

        r = 600 * 100 / 9.81
        lsty = [-r * 1.1 * 0.95, -r * 1.1 * 0.95, -r * 1.1 * 0.95, -0.9 * r * 0.95, 0, 0.9 * r, r * 1.1, r * 1.1,
                r * 1.1]
        for i in range(len(lstx)):
            test = rein.y[i]
            check = lsty[i]
            if test != 0:
                self.assertLess(abs((test - check) / check), 0.025)
            else:
                self.assertLess(abs(test - check), 0.025)


if __name__ == "__main__":
    unittest.main()
