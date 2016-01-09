# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:29:17 2013

@author: puma
"""
from math import pi, cos, sin, tan, sqrt, atan
from table import *


def profiles_infile(files, number,typ):
    """Достает данные из файлов
    files - файл
    number - номер профиля
    typ - пока достает только 'dvut' или 'truba_pryam'"""
    num=str(int(number))
    table=tables_csv((str(files)),'float')
    if typ=='dvut':
        h=table.get_cell('h', num)
        b=table.get_cell('b', num)
        s=table.get_cell('s', num)
        t=table.get_cell('t', num)
        r1=table.get_cell('r1', num)
        r2=table.get_cell('r2', num)
        a1=table.get_cell('a1', num)
        prof=dvut(h=h/10., b=b/10., s=s/10., t=t/10., r1=r1/10., r2=r2/10., a1=atan(a1/100), title2='prokat')
    if typ=='truba_pryam':
        h=table.get_cell('h', num)
        b=table.get_cell('b', num)
        t=table.get_cell('t', num)
        r1=table.get_cell('r1', num)
        r2=table.get_cell('r2', num)
        prof=dvut(h=h/10., b=b/10., t=t/10., r1=r1/10., r2=r2/10., title2='prokat')

    return prof

class  profiles_simple(object):
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False, a1=False, a2=False, x1=False\
    , x2=False, y1=False, y2=False, r=False, r3=False, title2='prokat'):

        self.__h=float(h)
        self.__b=float(b)
        self.__s=float(s)
        self.__t=float(t)
        self.__r1=float(r1)
        self.__r2=float(r2)
        self.__a1=float(a1)
        self.__a2=float(a2)
        self.__x1=float(x1)
        self.__x2=float(x2)
        self.__y1=float(y1)
        self.__y2=float(y2)
        self.__r=float(r)
        self.__r3=float(r3)
        self.pi=3.14159265358979
        self.Pi=self.pi
        self.__title2=title2
    def title2(self):
        return self.__title2

    def title0(self):
        return 'simple'
    def h(self):
        return self.__h
    def b(self):
        return self.__b
    def s(self):
        return self.__s
    def t(self):
        return self.__t
    def r1(self):
        return self.__r1
    def r2(self):
        return self.__r2

    def r3(self):
        return self.__r3

    def a1(self):
        return self.__a1

    def a2(self):
        return self.__a2

    def x1(self):
        return self.__x1

    def x2(self):
        return self.__x2

    def y1(self):
        return self.__y1

    def y2(self):
        return self.__y2

    def r(self):
        return self.__r

    def jx(self):
        return False
    def jxy(self):
        return False
    def jy(self):
        return False
    def a(self):
        return False
    def p(self):
        if self.a()!=False:
            return self.a()/100/100*7850
        else:
            return False
    def get_tau(self):
        return False
    def get_sigma(self):
        return False
    def ix(self):
        return (self.jx()/self.a())**0.5
    def iy(self):
        return (self.jy()/self.a())**0.5
    def wx(self):
        return self.jx()/self.h()*2
    def wy(self):
        return self.jy()/self.b()*2
    def jxdy(self, y):
        return self.jx() + y ** 2 * self.a()
    def jydx(self, x):
        return self.jy() + x ** 2 * self.a()

    def solve(self):
        return 1
#    def jda(self, an):
#        jx1 = (self.jx() + self.jy())\
#        / 2 + (self.jx() - self.jy()) / 2 * cos(2 * an) - self.jxy() * sin(2 * an)
#        jy1 = (self.jx() + self.jy()) / 2 - (self.jx() - self.jy()) \
#        / 2 * cos(2 * an) + self.jxy() * sin(2 * an)
#        jxy1 = (self.jx() - self.jy()) / 2 * sin(2 * an) + self.jxy\
#        * cos(2 * an)
#        return jx1, jy1, jxy1

#Нет тестов

    def get_sigma_e(self, nn=1, n=0, m_x=0, m_y=0, w=0, q_x=0, q_y=0, t=0, sr=0):
        s=self.get_sigma(nn=nn, n=n, m_x=m_x, m_y=m_y, w=w)
        t=self.get_tau(nn=nn, q_x=q_x, q_y=q_y, t=t, sr=sr)
        return (s**2+3*t**2)**0.5

class rectangle(profiles_simple):
    """Прямоугольник, входные - h и b"""
    def __init__(self, h=False, b=False):
        super(rectangle, self).__init__(h=h,b=b)

    def input_data(self):
        return [u"h, см",u"b, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'Wx, см3': self.wx()
        ,u'Sx, см3': self.s2x()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'Wy, см3': self.wy()
        ,u'Sy, см3': self.s2y()
        ,u'iy, см': self.iy()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out
    def title(self):
        return 'rectangle'

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'Wx, см3'
        ,u'Sx, см3'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'Wy, см3'
        ,u'Sy, см3'
        ,u'iy, см'
        ,u'title'
        ,u'title0'  
        ]
        return out

    def a(self):
        return self.h()*self.b()
    def jx(self):
        return self.h()**3*self.b()/12
    def jy(self):
        return self.h()*self.b()**3/12
    def s2x(self):
        return self.h()**2*self.b()/2/4
    def s2y(self):
        return self.h()*self.b()**2/2/4
    def sx(self,y):
        return y**2*self.b()/2/4
    def sy(self, x):
        return self.h()*x**2/2/4
    def jxy(self):
        return 0
class quartercircle(profiles_simple):
    """четверть круга. входные - r """

    def a(self):
        return self.pi * self.r() ** 2 / 4
    def xi(self):
        return 4 * self.r() / 3 / self.pi
    def yi(self):
        return self.xi()
    def jx(self):
        return self.r() ** 4 / 16. * (self.pi - 64. / 9 / self.pi)
    def jy(self):
        return self.jx()
    def jxy(self):
        return self.r() ** 4 / 8. * (1 - 32. / 9 / self.pi)

class circleangle(profiles_simple):
    """круговой треугольник. входные - r"""
    def a(self):
        return self.r() ** 2 / 4. * (4 - self.pi)
    def xi(self):
        return (10 - 3 * self.pi) * self.r() / (12 - 3 * self.Pi)
    def yi(self):
        return self.xi()
    def jx(self):
        return (1. / 3 - self.pi / 16 - 1. / (9 * (4 - self.pi))) * self.r() ** 4
    def jy(self):
        return self.jx()
    def jxy(self):
        return self.r() ** 4 * (1. / 8 - 1 / (9. * (4 - self.pi)))

class quartercirclesolid(profiles_simple):
    """четверть срезаннаого кольца
    r - большой радиус
    r1 - малый радиус"""
    def a(self):
        return self.pi / 4. * (self.r() ** 2 - self.r1() ** 2)
    def xi(self):
        return self.r() - 4. / 3 / self.Pi * (self.r() ** 3 - self.r1() ** 3)\
        / (self.r() ** 2 - self.r1() ** 2)
    def yi(self):
        return self.xi()
    def jx(self):
        return self.Pi / 16 * (self.r() ** 4 - self.r1() ** 4) - 4 *\
        (self.r() ** 3 - self.r1() ** 3) ** 2 / (9 * self.Pi) / \
        (self.r() ** 2 - self.r1() ** 2)
    def jy(self):
        return self.jx()
    def jxy(self):
        return (self.r() ** 4 - self.r1() ** 4) / 8 - 4 * (self.r() ** 3 - self.r1() ** 3)\
        ** 2 / 9 / self.Pi / (self.r() ** 2 - self.r1() ** 2)
class anglerectangle(profiles_simple):
    """'прямоугольный треугольник
    ' b - ширина
    ' h - высота"""
    def a(self):
        return 1./2*self.b()*self.h()
    def xi(self):
        return 1./3*self.b()
    def yi(self):
        return 1./3 * self.h()
    def jx(self):
        return self.b() * self.h() ** 3 / 36
    def jy(self):
        return self.b() ** 3 * self.h() / 36
    def jxy(self):
        return -1. / 72 * self.b() ** 2 * self.h() ** 2

class solid(profiles_simple):
    """круг"""
    def a(self):
        return self.Pi * (self.r() * 2) ** 2 / 4
    def xi(self):
        return self.r()
    def yi(self):
        return self.r()
    def jx(self):
        return self.Pi * (self.r() * 2) ** 4 / 64
    def jy(self):
        return self.jx()
    def jxy(self):
        return 0
class ring(profiles_simple):
    """'кольцо оно и есть кольцо
    ' r - большой радиус
    ' r1 - малый радиус  """
    def __init__(self,r=False, r1=False):
        super(ring, self).__init__(r=r,r1=r1)
        self.solve()
    def input_data(self):
        return [u"r, см",u"r1, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'Wx, см3': self.wx()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'Wy, см3': self.wy()
        ,u'iy, см': self.iy()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out
    def title(self):
        return 'ring'
    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'Wx, см3'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'Wy, см3'
        ,u'iy, см'
        ,u'title'
        ,u'title0'  
        ]
        return out

    def a(self):
        d = self.r() * 2
        a1 = self.r1() / self.r()
        a = self.Pi * d ** 2 / 4 * (1 - a1 ** 2)
        return a
    def xi(self):
        xi = self.r()
        return xi
    def yi(self):
        yi = self.r()
        return yi
    def jx(self):
        d = self.r() * 2
        a1 = self.r1() / self.r()
        return self.Pi * d ** 4 / 64 * (1 - a1 ** 4)
    def jy(self):
        return self.jx()
    def wx(self):
        return self.jx()/self.r()
    def wy(self):
        return self.wx()
    def jxy(self):
        return 0
        #для расчета устойчивости
    def t(self):
        return self.r()-self.r1()
    def s(self):
        return self.r()-self.r1()
    def hef(self):
        return (self.r()+self.r1())/2.
    def bef(self):
        return (self.r()+self.r1())/2.

class angle(profiles_simple):
    """треугольник  , b, h, x1 """
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False, a1=False, a2=False, x1=False\
    , x2=False, y1=False, y2=False, r=False):
        super(angle, self).__init__(h,b,s,t,r1,r2,a1,a2,x1,x2,y1,y2,r)
        self.__ba=float(x1)
        self.__bc = float(b) - self.__ba
        self.__d = (self.__ba - self.__bc) / 3
    def a(self):
        return 1. / 2 * self.b() * self.h()
    def yi(self):
        return 1. / 3 * self.h()
    def jx(self):
        return self.b() * self.h() ** 3 / 36
    def xi(self):
        return self.__ba - self.__d
    def jy(self):
        return self.h() * self.b() * (self.b() ** 2 - self.__ba * self.__bc) / 36

class circleseg(profiles_simple):
    """круговой сегмент. углы в радианах, a1, r"""
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False, a1=False, a2=False, x1=False\
    , x2=False, y1=False, y2=False, r=False):
        super(circleseg, self).__init__(h,b,s,t,r1,r2,a1,a2,x1,x2,y1,y2,r)
        self.__a = float(a1)
#        print a1, self.__a
        self.__ph = 2 * float(a1) - sin(2 *self.__a)
    def a(self):
        return self.r() ** 2 / 2 * self.__ph
    def xi(self):
        return self.r() * sin(self.__a)
    def yi(self):
        return 4 * self.r() * (sin(self.__a)) ** 3 / 3. / self.__ph
    def jx(self):
        at1=self.r() ** 4 / 16 * (4 * self.a1()- sin(4 * self.__a))
        at2=- 8. / 9 * self.r() ** 4 * (sin(self.__a)) ** 6
        at3=2*self.__a-sin(2*self.__a)
        return  at1+at2/at3

    def jy(self):
        j=self.r() ** 4 / 48 * (12 * self.a1() - 8 * sin(2 * self.__a)\
        + sin(4 * self.__a))
        return j
    def jxy(self):
        return 0

def jxdx(jx, a, dx):
    return jx+a*dx**2

def jda(jx, jy, jxy, a):
    jx1 = (jx + jy) / 2 + (jx - jy) / 2 * cos(2 * a) - jxy * sin(2 * a)
    jy1 = (jx + jy) / 2 - (jx - jy) / 2 * cos(2 * a) + jxy * sin(2 * a)
    jxy1 = (jx - jy) / 2 * sin(2 * a) + jxy * cos(2 * a)
    return jx1, jy1, jxy1
def jxydxdy(jxy, a, x, y):
    return jxy+y*x*a
def jxjy(jx, jy, jxy):
    if jx==jy:
        an=pi/4
    else:
        an=atan(-2 *jxy / (jx - jy)) / 2
    jx1 = (jx + jy) / 2 + 1. / 2 * ((jx  - jy) ** 2 + 4 * jxy ** 2)**0.5
    jy1 = (jx +jy) / 2 - 1. / 2 * ((jx - jy) **2 + 4 * jxy ** 2)**0.5
    return an, jx1, jy1

class krug(profiles_simple):
    """расчет закруглений. вводится 1/2 угла. y - от линии соед. крайние нижне точки"""
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False, a1=False, a2=False, x1=False\
    , x2=False, y1=False, y2=False, r=False):
        super(krug, self).__init__(h,b,s,t,r1,r2,a1,a2,x1,x2,y1,y2,r)
        self.solve()
    def solve(self):
        k=angle(b=2 * self.r() * sin(self.a1()),\
        h=tan(self.a1()) * self.r() * sin(self.a1()), x1=self.r() * sin(self.a1()))
#        print self.a1()
        s=circleseg(a1=self.a1(), r=self.r())
        a = k.a() - s.a()
        sy = s.yi() - self.r() * cos(self.a1())
        ky = k.yi()
        if a==0:
            yi=0
        else:
            yi = (k.a() * ky - sy * s.a()) / a
        xi = 0
        jy = k.jy() - s.jy()
        jx = jxdx(k.jx(), k.a(), yi - ky) - jxdx(s.jx(), s.a(), yi - sy)
        jxy = 0
        self.__a=a
        self.__xi=xi
        self.__yi=yi
        self.__jx=jx
        self.__jy=jy
        self.__jxy=jxy
        return True
    def a(self):
#        self.solve()
        return self.__a
    def xi(self):
#        self.solve()
        return self.__xi
    def yi(self):
#        self.solve()
        return self.__yi
    def jx(self):
#        self.solve()
        return self.__jx
    def jy(self):
#        self.solve()
        return self.__jy
    def jxy(self):
#        self.solve()
        return self.__jxy

class rotkrug(profiles_simple):
    """входные данные - r и a1"""
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False, a1=False, a2=False, x1=False\
    , x2=False, y1=False, y2=False, r=False):
        super(rotkrug, self).__init__(h,b,s,t,r1,r2,a1,a2,x1,x2,y1,y2,r)
        self.solve()
    def solve(self):
#        print self.a1()
        el=krug(r=self.r(), a1=self.a1())
        a=el.a()
        xi=el.xi()
        yi=el.yi()
        jx=el.jx()
        jy=el.jy()
        jxy=el.jxy()
        jyr, jxr, jxyr=jda(jx, jy, jxy, -(pi - self.a1()))
        yi = self.r() * sin(self.a1()) * tan(self.a1()) - yi
        xri = cos(self.a1()) * yi

        yri = sin(self.a1()) * yi
        self.__a=a
        self.__xi=yri
        self.__yi=xri
        self.__jx=jyr
        self.__jy=jxr
        self.__jxy=jxyr
    def a(self):
#        self.solve()
        return self.__a
    def xi(self):
#        self.solve()
        return self.__xi
    def yi(self):
#        self.solve()
        return self.__yi
    def jx(self):
#        self.solve()
        return self.__jx
    def jy(self):
#        self.solve()
        return self.__jy
    def jxy(self):
#        self.solve()
        return self.__jxy




class dvut(profiles_simple):
    """универсальный расчет двутавров"""
#    '1 - расчет полки
#    '3 - расчет стенки
#    '4 - треуголник
#    '8 - отнимаемый круговой уголок
#    '12 - прибавляем круговой уголок
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False, a1=False, title2='prokat'):
        super(dvut, self).__init__(h=h,b=b,s=s,t=t,r1=r1,r2=r2,a1=a1, title2=title2)
        self.solve()
    def input_data(self):
        return [u"h, см",u"b, см",u"s, см",u"t, см",u"r1, см",u"r2, см",u"a, %/100"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'Wx, см3': self.wx()
        ,u'Sx, см3': self.s2x()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'Wy, см3': self.wy()
        ,u'Sy, см3': self.s2y()
        ,u'iy, см': self.iy()
        ,u'Jw, см6': self.jw()
        ,u'Jt, см4': self.jt()
        ,u'Jt_sp2013, см4': self.jt_sp()
        ,u'w1, см2': self.w1()
        ,u'Ww, см4': self.ww()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'Wx, см3'
        ,u'Sx, см3'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'Wy, см3'
        ,u'Sy, см3'
        ,u'iy, см'
        ,u'Jw, см6'
        ,u'Jt, см4'
        ,u'Jt_sp2013, см4'
        ,u'w1, см2'
        ,u'Ww, см4'
        ,u'title'
        ,u'title0'  
        ]
        return out

    def solve(self):
        t1 = (self.t() - (self.b() - self.s()) / 4 * tan(self.a1()))
        t2 = (self.b() - self.s()) / 2 * tan(self.a1())
        el1=rectangle(b=self.b(), h=t1)
        a1 = el1.a()

        jx1 = el1.jx()
        jy1 = el1.jy()

#        print('a1',a1)
        el3=rectangle(b=self.s(), h=self.h()-2*t1)
        a3 = el3.a()

        jx3 = el3.jx()
        jy3 = el3.jy()
#        print('a3',a3)


        el4=anglerectangle(b=(self.b() - self.s()) / 2, h=t2)
        a4 = el4.a()
        xi4 = el4.xi()
        yi4 =  el4.yi()
        jx4 = el4.jx()
        jy4 = el4.jy()
#        print('a4',a4)
#
        el8=rotkrug(r=self.r2(), a1=(pi / 2 - self.a1()) / 2)
        a8 = el8.a()
        xi8 = el8.yi()
        yi8 =  el8.xi()
        jx8 = el8.jy()
        jy8 = el8.jx()

#        xi8 = el8.xi()
#        yi8 =  el8.yi()
#        jx8 = el8.jx()
#        jy8 = el8.jy()
 #       print('a8',a8)

        el12=rotkrug(r=self.r1(), a1=(pi / 2 - self.a1()) / 2)
        a12 = el12.a()
        xi12 = el12.yi()
        yi12 =  el12.xi()
        jx12 = el12.jy()
        jy12 = el12.jx()

#        xi12 = el12.xi()
#        yi12 =  el12.yi()
#        jx12 = el12.jx()
#        jy12 = el12.jy()
 #       print('a12',a12)

        s=self.s()
        h=self.h()
        b=self.b()

        jx = jx3 + 2 * jxdx(jx1, a1, h / 2 - t1 / 2) + 4 * jxdx(jx4, a4, h / 2 - t1 - yi4) + 4 * jxdx(jx12, a12, h / 2 - t1 - t2 - yi12) - 4 * jxdx(jx8, a8, h / 2 - (t1 - yi8))


        jy = 2 * jy1 + jy3 + 4 * jxdx(jy4, a4, (s / 2 + xi4)) + 4 * jxdx(jy12, a12, s / 2 + xi12) - 4 * jxdx(jy8, a8, b / 2 - xi8)
        a = a1 * 2 + a3 + a4 * 4 - a8 * 4 + a12 * 4
        s2x = (a1 * (h / 2 - t1 / 2) + a3 / 2 * (h / 2 - t1) / 2 + 2 * a4 * (h / 2 - t1 - yi4) + 2 * a12 * (h / 2 - t1 - t2 - yi12) - 2 * a8 * (h / 2 - t1 + yi8))
        s2y = 2*(b/2*t1)*b/4 + s/2*(h-2*t1)*s/4 + 2*a4*(s / 2 + xi4) + 2 * a12*( s / 2 + xi12) - 2 * a8*( b / 2 - xi8)
#вдоль грани стенки
        sy1 = 2*((b/2-s/2)*t1)*(b/2-(b/2-s/2)/2)  + 2*a4*(s/2+ xi4) + 2 * a12*(s/2+ xi12) - 2 * a8*( b / 2 - xi8)
#        print ('4',jy)
#вдоль первого снизу изгиба параллельно полке, скругление не учитывается в запас расчета
        sx1=t1*b*(h/2-t1/2)
#вдоль второго изгиба, скругление не учитывается в запас расчета
        sx2=a1 * (h / 2 - t1 / 2) + t2*s*(h/2-(t2)/2-t1) + 2 * a4 * (h / 2 - t1 - yi4)  - 2 * a8 * (h / 2 - t1 + yi8)

        self.__a=a
        self.__jx=jx
        self.__jy=jy
        self.__s2x=s2x
        self.__s2y=s2y
        self.__sy1=sy1
        self.__sx1=sx1
        self.__sx2=sx2
        self.__t1=t1
        self.__t2=t2
#        print         ('3', self.__jy)
    def a(self):
#        self.solve()
        return self.__a
    def jx(self):
#        self.solve()
        return self.__jx
    def jy(self):
#        self.solve()
#        print ('2',self.__jy)
        return self.__jy
    def s2x(self):
#        self.solve()
        return self.__s2x
    def sx1(self):
#        self.solve()
        return self.__sx1
    def sx2(self):
#        self.solve()
        return self.__sx2
    def s2y(self):
#        self.solve()
        return self.__s2y
    def sy1(self):
#        self.solve()
        return self.__sy1
    def t1(self):
#        self.solve()
        return self.__t1
    def t2(self):
#        self.solve()
        return self.__t2

    def jw(self):
        t=self.t()
        b=self.b()
        h=self.h()
        d=self.s()
        r1=self.r2()
        r=self.r()
        k=tan(self.a1())
        t1=t+k*b/4
        h1=h-t1
        b1=b-2*r1
        c=d+2*r
        delta_jw=r1**2*h1**2*(0.00492*c**2+0.09699*d**2+0.0327*c*d-0.00123*b1**2-0.02425*b**2\
        -0.008715*b*b1)
        jw=h1**2*b**3/24*(t-k*b/8)
        jw=jw+delta_jw
        return jw
    def title(self):
        return 'dvut'



    def w1(self):
        b=self.b()
        k=tan(self.a1())

        t1=self.t()+k*b/4
        w1=self.b()/2*(self.h()-t1)/2
        return w1
    def ww(self):
        return self.jw()/self.w1()
        
    def wxmin(self):
        return self.wx()
    def wymin(self):
        return self.wy()
    def jt(self):
        h2=self.h()-2*(self.t1()+self.t2())
        b=self.b()
        tf=self.t()
        tw=self.s()
        return 1.3/3*(2*b*tf**3+h2*tw**3)
    def jt_sp(self):
        return self.jt()/1.3
    def aw(self):
        return self.s()*(self.h()-self.t()*2)
    def af(self):
        return self.b()*self.t()
    def afaw(self):
        return self.af()/self.aw()
    def hef(self):
#        return self.h()-self.t1()*2-self.t2()*2-0
        return self.h()-self.t1()*2-self.t2()*2-2*self.r1()/tan(pi/4+self.a1()/2)
    def bef(self):
        return self.b()/2-self.s()/2-self.r1()/tan(pi/4+self.a1()/2)*cos(self.a1())
    def hw(self):
        return self.h()-self.t()*2

class truba_pryam(profiles_simple):
#    '1 - расчет полки
#    '3 - расчет стенки
#    '4 - треуголник
#    '8 - отнимаемый круговой уголок
#    '12 - прибавляем круговой уголок
    def __init__(self, h=False, b=False, t=False, r1=False, r2=False):
        super(truba_pryam, self).__init__(h=h,b=b,t=t,r1=r1,r2=r2)
        self.solve()
    def input_data(self):
        return [u"h, см",u"b, см",u"t, см",u"r1, см",u"r2, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'Wx, см3': self.wx()
        ,u'Sx, см3': self.s2x()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'Wy, см3': self.wy()
        ,u'Sy, см3': self.s2y()
        ,u'iy, см': self.iy()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'Wx, см3'
        ,u'Sx, см3'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'Wy, см3'
        ,u'Sy, см3'
        ,u'iy, см'
        ,u'title'
        ,u'title0'  
        ]
        return out

    def solve(self):
        b=self.b()
        h=self.h()
        t=self.t()
        r1=self.r1()
        r2=self.r2()
        
        self.__s=self.t()
#        print h,b,t,r1,r2

        #полка
        massiv1 = rectangle(b=b - t * 2, h=t)
        a1 = massiv1.a()
        xi1 = (b-t*2)/2
        yi1 = t/2
        jx1 = massiv1.jx()
        jy1 = massiv1.jy()


        massiv2 = rectangle(b=t, h=h)
        a3 = massiv2.a()
        xi3 = t/2
        yi3 = h/2
        jx3 = massiv2.jx()
        jy3 = massiv2.jy()


        massiv3 = circleangle(r=r2)
        a6 = massiv3.a()
        xi6 = massiv3.xi()
        yi6 = massiv3.yi()
        jx6 = massiv3.jx()
        jy6 = massiv3.jy()


        massiv4 = circleangle(r=r1)
        a9 = massiv4.a()
        xi9 = massiv4.xi()
        yi9 = massiv4.yi()
        jx9 = massiv4.jx()
        jy9 = massiv4.jy()

#        print 'a1', a1
#        print 'a3', a3
#
#        print 'a6', a6
#        print 'a9', a9

        self.__a = a1 * 2 + a3 * 2 - a6 * 4 + 4 * a9

        self.__jx = 2 * jxdx(jx1, a1, h / 2 - t / 2) + jx3 * 2 + 4 * jxdx(jx9, a9, h / 2 - t - yi9) - 4 * jxdx(jx6, a6, h / 2 - yi6)
        self.__jy = 2 * jxdx(jy3, a3, b / 2 - t / 2) + jy1 * 2 + 4 * jxdx(jy9, a9, b / 2 - t - xi9) - 4 * jxdx(jy6, a6, b / 2 - xi6)

        self.__s2x=a1*(h/2-t/2)+2*a3/2*h/4+2*a9*(h/2-t-yi9)-2*a6*(h/2-yi6)
        self.__s2y=a3*(b/2-t/2)+2*a1/2*(b/2-t)/2+2*a9*(b/2-t-xi9)-2*a6*(b/2-xi6)

        #в запас расчета дальше круговые срезы не учитываютcz

        self.__sx1=b*t*t/2
        self.__sy1=h*t*t/2
    def s(self):
        return self.__s
    def a(self):
#        self.solve()
        return self.__a
    def jx(self):
#        self.solve()
        return self.__jx
    def jy(self):
#        self.solve()
#        print ('2',self.__jy)
        return self.__jy
    def s2x(self):
#        self.solve()
        return self.__s2x
    def sx1(self):
#        self.solve()
        return self.__sx1

    def s2y(self):
#        self.solve()
        return self.__s2y
    def sy1(self):
#        self.solve()
        return self.__sy1
    def aw(self):
        return self.t()*(self.h()-self.t()*2)
    def af(self):
        return self.b()*self.t()
    def afaw(self):
        return self.af()/self.aw()/2
    def hef(self):
#        return self.h()-self.t1()*2-self.t2()*2-0
        return self.h()-self.t()*2-self.r1()*2
    def bef(self):
        return self.b()-self.t()*2-self.r1()*2
    def hw(self):
        return self.h()-self.t()*2
    def bw(self):
        return self.b()-self.t()*2
    def t1(self):
        return self.s()
    def t2(self):
        return 0
    def title(self):
        return 'korob'
#    def hw(self):
#        return self.h()-self.t()*2

class ugol(profiles_simple):
    """"Определяет характеристики обычного уголка
     r1 - между полками
     r2 - для гнутого уголка
     r3 - для края
    """

    def __init__(self, h=False, b=False, t=False, r1=False, r2=False, r3=False):
        super(ugol, self).__init__(h=h,b=b,t=t,r1=r1,r2=r2,r3=r3)
        self.solve()
    def input_data(self):
        return [u"h, см",u"b, см",u"t, см",u"r1, см",u"r2, см",u"r3, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'Wx, см3': self.wx()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'Wy, см3': self.wy()
        ,u'iy, см': self.iy()
        ,u'Jxy, см4': self.jxy()
        ,u'Jx0, см4': self.jx0()
        ,u'ix0, см': self.ix0()
        ,u'Jy0, см4': self.jy0()
        ,u'iy0, см': self.iy0()
        ,u'alpha': self.alpha()
        ,u'dx, см': self.dx()
        ,u'dy, см': self.dy()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'Wx, см3'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'Wy, см3'
        ,u'iy, см'
        ,u'Jxy, см4'
        ,u'Jx0, см4'
        ,u'ix0, см'
        ,u'Jy0, см4'
        ,u'iy0, см'
        ,u'alpha'
        ,u'dx, см'
        ,u'dy, см'
        ,u'title'
        ,u'title0'  
        ]
        return out
    def solve(self):
        h=self.h()
        b=self.b()
        s=self.t()
        t=self.t()
        r1=self.r1()
        r2=self.r2()
        r3=self.r3()

#        print h,b,s,t,r1,r2,r3
        massiv1 = rectangle(b=t, h=h)
        a1 = massiv1.a()
        xi1 = t/2
        yi1 = h/2
        jx1 = massiv1.jx()
        jy1 = massiv1.jy()
        jxy1 = massiv1.jxy()

        massiv2 = rectangle(b=b - t, h=t)
        a2 = massiv2.a()
        xi2 = (b-t)/2
        yi2 = t/2
        jx2 = massiv2.jx()
        jy2 = massiv2.jy()
        jxy2 = massiv2.jxy()

        massiv3 = circleangle(r=r3)
        a3 = massiv3.a()
        xi3 = massiv3.xi()
        yi3 = massiv3.yi()
        jx3 = massiv3.jx()
        jy3 = massiv3.jy()
        jxy3 = massiv3.jxy()

        massiv4 = circleangle(r=r1)
        a5 = massiv4.a()
        xi5 = massiv4.xi()
        yi5 = massiv4.yi()
        jx5 = massiv4.jx()
        jy5 = massiv4.jy()
        jxy5 = massiv4.jxy()

        massiv5 = circleangle(r=r2)
        a6 = massiv5.a()
        xi6 = massiv5.xi()
        yi6 = massiv5.yi()
        jx6 = massiv5.jx()
        jy6 = massiv5.jy()
        jxy6 = massiv5.jxy()

#        print 'a1', a1
#        print 'a2', a2
#        print 'a3', a3
#        print 'a5', a5
#        print 'a6', a6


        dx = (a1 * t / 2 + a2 * (b - (b - t) / 2) + a5 * (t + xi5) - a3 * (b - xi3) - a3 * (t - xi3) - a6 * xi6) / (a1 + a2 - 2 * a3 + a5 - a6)
        dy = (a1 * h / 2 + a2 * t / 2 + a5 * (t + yi5) - a3 * (t - yi3) - a3 * (h - yi3) - a6 * yi6) / (a1 + a2 + a5 - a6 - 2 * a3)
        a = a1 + a2 + a5 - a6 - 2 * a3
        jx = jxdx(jx1, a1, h / 2 - dy) + jxdx(jx2, a2, dy - t / 2) + jxdx(jx5, a5, dy - t - yi5) - jxdx(jx6, a6, dy - yi6) - jxdx(jx3, a3, dy - t + yi3) - jxdx(jx3, a3, h - dy - yi3)
        jy = jxdx(jy1, a1, dx - t / 2) + jxdx(jy2, a2, (b - (b - t) / 2 - dx)) + jxdx(jy5, a5, dx - t - xi5) - jxdx(jy6, a6, dx - xi6) - jxdx(jy3, a3, dx - t + xi3) - jxdx(jy3, a3, b - dx - xi3)


        jxy = jxydxdy(jxy1, a1, (dx - t / 2), -(h / 2 - dy)) + jxydxdy(jxy2, a2, -((b - (b - t) / 2) - dx), (dy - t / 2)) + jxydxdy(jxy5, a5, dx - t - xi5, dy - t - yi5) - jxydxdy(jxy3, a3, -(b - dx - xi3), dy - t + yi3) - jxydxdy(jxy3, a3, (dx - t + xi3), -(h - dy - yi3)) - jxydxdy(jxy6, a6, dx - xi6, dy - yi6)

#        print 'jxy', jxy
        massiv6 = jxjy(jx, jy, jxy)
        alpha = massiv6[0]
        jx0 = massiv6[1]
        jy0 = massiv6[2]

        ix0 = (jx0/a)**0.5
        iy0 = (jy0/a)**0.5


        self.__a=a
        self.__jx=jx
        self.__jy=jy

        self.__jxy=jxy

        self.__jx0=jx0
        self.__jy0=jy0

        self.__alpha=alpha

        self.__ix0=ix0
        self.__iy0=iy0

        self.__dx=dx
        self.__dy=dy

    def a(self):
        return self.__a
    def jx(self):
        return self.__jx
    def jy(self):
        return self.__jy
    def wy(self):
        w1=self.jy()/self.dx()
        w2=self.jy()/(self.b()-self.dx())
        if w1<w2:
            return w1
        else:
            return w2

    def wx(self):
        w1=self.jx()/self.dy()
        w2=self.jx()/(self.h()-self.dy())
        if w1<w2:
            return w1
        else:
            return w2
            
    def jxy(self):
        return self.__jxy
    def jx0(self):
        return self.__jx0
    def jy0(self):
        return self.__jy0
    def alpha(self):
        return self.__alpha
    def tanalpha(self):
        return tan(self.alpha())
    def ix0(self):
        return self.__ix0
    def iy0(self):
        return self.__iy0
    def hef(self):
        return self.h()-self.t()-self.r1()
    def bef(self):
        return self.b()-self.t()-self.r1()
    def dx(self):
        return self.__dx
    def dy(self):
        return self.__dy
    def title(self):
        return 'ugol'
        
class shvel(profiles_simple):
##'"""универсальный расчет швеллеров, r2 - отнимаем, r3 - для гнутого
## '   1 - расчет стенки
## '   2- расчет того что осталось от полки
## '   3 - треугольника
## '   4 - отнимаемой части
## '   5- прибавляемой части
##  '  6 - отнимаемая часть у гнутого швеллера
##  '  r3 - только для гнутого швеллера"""
    def __init__(self, h=False, b=False\
    , s=False, t=False, r1=False, r2=False,  r3=False, a1=False):
        super( shvel, self).__init__(h=h,b=b,s=s,t=t,r1=r1,r2=r2,a1=a1,r3=r3)
        self.solve()
    def input_data(self):
        return [u"h, см",u"b, см",u"s, см",u"t, см",u"r1, см",u"r2, см",u"r3, см",u"a, %/100"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'Wx, см3': self.wx()
        ,u'Sx, см3': self.s2x()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'Wy, см3': self.wy()
        ,u'Sy, см3': self.s2y()
        ,u'iy, см': self.iy()
        ,u'dx, см':self.dx()
        ,u'Jw, см6': self.jw()
        ,u'Jt, см4': self.jt()
        ,u'Jt_sp2013, см4': self.jt_sp()
        ,u'xa, см': self.xa()
        ,u'w1, см': self.w1()
        ,u'w2, см': self.w2()
        ,u'Ww1, см4': self.ww1()
        ,u'Ww2, см4': self.ww2()

        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out
    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'Wx, см3'
        ,u'Sx, см3'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'Wy, см3'
        ,u'Sy, см3'
        ,u'iy, см'
        ,u'dx, см'
        ,u'Jw, см6'
        ,u'Jt, см4'
        ,u'Jt_sp2013, см4'  
        ,u'xa, см' 
        ,u'w1, см'
        ,u'w2, см'
        ,u'Ww1, см4'
        ,u'Ww2, см4'
        ,u'title'
        ,u'title0'  
        ]
        return out

    def solve(self):
        h=self.h()
        b=self.b()
        s=self.s()
        t=self.t()
        r1=self.r1()
        r2=self.r2()
        r3=self.r3()
        alpha=self.a1()

        if alpha <> 0:
            t2 = (b - s) * tan(alpha)
            t1 = t - (b - s) / 2 * tan(alpha)
        else:
            t1 = t
            t2 = 0

        massiv1=rectangle(b=s, h=h)
        a1=massiv1.a()
        xi1=s/2
        yi1=h/2
        jx1=massiv1.jx()
        jy1=massiv1.jy()
        jxy1=0

        massiv2=rectangle(b=b-s, h=t1)
        a2=massiv2.a()
        xi2=(b-s)/2
        yi2=t1/2
        jx2=massiv2.jx()
        jy2=massiv2.jy()
        jxy2=0

        massiv3=anglerectangle(b=b - s, h=t2)
        a3=massiv3.a()
        xi3=massiv3.xi()
        yi3=massiv3.yi()
        jx3=massiv3.jx()
        jy3=massiv3.jy()
        jxy3=massiv3.jxy()

        massiv4=rotkrug(r=r2, a1=(pi / 2 - alpha) / 2)
        a4=massiv4.a()
        xi4=massiv4.xi()
        yi4=massiv4.yi()
        jx4=massiv4.jx()
        jy4=massiv4.jy()
        jxy4=massiv4.jxy()

        massiv5=rotkrug(r=r1, a1=(pi / 2 - alpha) / 2)
        a5=massiv5.a()
        xi5=massiv5.xi()
        yi5=massiv5.yi()
        jx5=massiv5.jx()
        jy5=massiv5.jy()
        jxy5=massiv5.jxy()

        massiv6=rotkrug(r=r3, a1=pi / 4)
        a6=massiv6.a()
        xi6=massiv6.xi()
        yi6=massiv6.yi()
        jx6=massiv6.jx()
        jy6=massiv6.jy()
        jxy6=massiv6.jxy()

#        print 'xi1', xi1
#        print 'xi2', xi2
#        print 'xi3', xi3
#        print 'xi4', xi4
#        print 'xi5', xi5
#        print 'xi6', xi6
#

        a = a1 + a2 * 2 + a3 * 2 + a4 * (-2) + 2 * a5 - 2 * a6
        xi = (a1 * s / 2 + a2 * 2 * (b - (b - s) / 2) + a3 * 2 * (s + xi3) - a4 * 2 * (b - xi4) + a5 * 2 * (s + xi5) - a6 * xi6 * 2) / a

        jx = jx1 + 2 * jxdx(jx2, a2, h / 2 - t1 / 2) + 2 * jxdx(jx3, a3, h / 2 - t1 - yi3) + 2 * jxdx(jx5, a5, h / 2 - t1 - t2 - yi5) - 2 * jxdx(jx4, a4, h / 2 - t1 + yi4) - 2 * jxdx(jx6, a6, h / 2 - yi6)
#        print h / 2, t1, yi3
        jy = jxdx(jy1, a1, xi - s / 2) + 2 * jxdx(jy2, a2, b - (b - s) / 2 - xi) + 2 * jxdx(jy3, a3, s + xi3 - xi) - 2 * jxdx(jy4, a4, b - xi4 - xi) + 2 * jxdx(jy5, a5, s + xi5 - xi) - 2 * jxdx(jy6, a6, xi - xi6)

        s2x = a1 / 2 * (h / 4) + a2 * (h / 2 - t1 / 2) + a3 * (h / 2 - t1 - yi3) - a4 * (h / 2 - t1 + yi4) + a5 * (h / 2 - t1 - t2 - yi5) - a6 * (h / 2 - yi6)

        txi=(b - xi) * tan(alpha)

        s2y=(b-xi)**2/2*t1*2.+2.*(b-xi)*1./3*(b-xi)/2*txi-a4*2* (b - xi4 - xi)

        self.__t1=t1*1.
        self.__t2=t2*1.
#
#        k = tan(alpha)
#
#        tf=t
#
#        tw=s
#        tf1=tf+k*(b-s)/2
#
#        tf2=tf-k*(b-s)/2
#        b1=b-s/2
#        h1=h-tf1
#        h2=h-2*tf
#        h3=h-tf2
#        ax=b1**2*h1/24/jx*((2*tf-0.05*tw)*(2*h3+h1)-0.1*b1*h3)
#
#        jt=1.12/3*(2*b*tf**3+h2*tw**3)
#        w1=ax*h1/2
#
#        w2=h1/2*(b1-ax)-k/2*b1*ax
#
#        jw=tw*h1*w1**2/3+2*tf*b1/3*(w1**2+w2**2-w1*w2)-k*b1**2/6*(w2**2-w1**2)

        k = tan(alpha)

        tf=t
        tw=s

        d = tw
        r = r2
        td = t1 - k * d / 2
        ta = td - k * r

        t1 = t + k / 2 * (b - d)

        tb = t2 + k * r1


        ha = h - ta
        b0 = b - d / 2
        t2 = t - k * b / 2
        h1 = h - t1
        hb = h - tb
        b1 = b0 - r1

        h2 = h - t2
        c = d / 2 + r

        hd = h - td
        ax = b0 ** 2 * h1 / 24 / jx * ((2 * t - 0.05 * d) * (2 * h2 + h1) - 0.1 * b0 * h2)

        deltaax = r1 * r1 * h1 / jx * (0.019838 * ha * c + 0.11198 * hd * d + 0.0427 * hd * c + 0.02135 * ha * d - 0.0049595 * hb * b1 - 0.05599 * h2 * b0 - 0.010675 * (h2 * b1 + hb * b0))

        if k == 0:
            deltaax = 0
#        deltaax=0

        ax = ax + deltaax
        w1 = ax * h1 / 2
        w2 = h1 / 2 * (b0 - ax) - k / 2 * b0 * ax

        jw = d * h1 * w1 * w1 / 3 + 2 * t * b0 / 3 * (w1 * w1 + w2 * w2 - w1 * w2) - k * b0 * b0 / 6 * (w2 * w2 - w1 * w1)

        s = (w1 + w2) / b0

        wb = w2 - s * r1
        wd = w1 - s * d / 2
        wa = wd - s * r

        deltajw = r1 * r1 * (0.07935 * wa * wa + 0.8958 * wd * wd + 0.3416 * wa * wd - 0.01984 * wb * wb - 0.22396 * w2 * w2 - 0.0854 * wb * w2)

        if k == 0:
            deltajw = 0

#        deltajw=0


#        print 'jw', jw
#        print 'deltajw', deltajw

        jw = deltajw + jw

        jt = 1.12 / 3 * (2 * b * tf ** 3 + (h - 2 * tf) * tw ** 3)

        jt_sp=jt/1.12
        xa=ax-d/2
        jt_sp=jt/1.12

        self.__xa=xa #

        self.__a=a
        self.__jx=jx
        self.__jy=jy

#
#        self.__t1=t1
#        self.__t2=t2

        self.__dx=xi

        self.__w1=w1  #
        self.__w2=w2    #

        self.__jw=jw  #
        self.__jt=jt  #
        self.__jt_sp=jt_sp  #

        self.__s2x=s2x
        self.__s2y=s2y
    def wy(self):
        w1=self.jy()/self.dx()
        w2=self.jy()/(self.b()-self.dx())
        if w1<w2:
            return w1
        else:
            return w2
    def w1(self):
        return self.__w1

    def w2(self):
        return self.__w2

    def ww1(self):
        return self.jw()/self.w1()

    def ww2(self):
        return self.jw()/self.w2()

    def a(self):

        return self.__a
    def jx(self):
        return self.__jx
    def jy(self):
        return self.__jy

    def jt(self):
        return self.__jt

    def jt_sp(self):
        return self.__jt_sp

    def jw(self):
        return self.__jw

    def s2x(self):
        return self.__s2x
    def s2y(self):
        return self.__s2y

    def w1(self):
        return self.__w1
    def w2(self):
        return self.__w2

    def t1(self):
        return self.__t1
    def t2(self):
        return self.__t2

    def xa(self):
        return self.__xa

    def aw(self):
        return self.s()*(self.h()-self.t()*2)
    def af(self):
        return self.b()*self.t()
    def afaw(self):
        return self.af()/self.aw()

    def hef(self):
#        return self.h()-self.t1()*2-self.t2()*2-0
#        print self.h()
#        print self.t1()
#        print self.t2()
#        print self.r1()/tan(pi/4+self.a1()/2)

        return self.h()-self.t1()*2-self.t2()*2-2*self.r1()/tan(pi/4+self.a1()/2)
    def bef(self):

        return self.b()-self.s()-self.r1()/tan(pi/4+self.a1()/2)*cos(self.a1())

    def dx(self):
        return self.__dx
    def title(self):
        return 'shvel'


class  profiles_sostav(object):
    def __init__(self, pr1=False, alpha1=False, x1=False, y1=False, mir1=False, pr2=False, x2=False, y2=False, alpha2=False, mir2=False, title=''):
#за перемещение от нижней левой точки
#если nir=1 то зеркально относиткльно оси Y




        self.user_init( pr1, alpha1, x1, y1, mir1, pr2, x2, y2, alpha2, mir2, title    )

    def user_init(self, pr1, alpha1, x1, y1, mir1, pr2, x2, y2, alpha2, mir2, title  ):

        self.pr1=pr1
        self.pr2=pr2
        self.__a1=float(alpha1)
        self.__a2=float(alpha2)
        self.__x1=float(x1)
        self.__x2=float(x2)
        self.__y1=float(y1)
        self.__y2=float(y2)
        self.__mir1=float(mir1)
        self.__mir2=float(mir2)

        self.__title=title
        self.__title0='sostav'



        self.solve()
    def solve(self):
        #определяем jxy,jx, jy, a, alpha, jx0, jy0, xi, yi

        a=self.pr1.a()+self.pr2.a()
#        print 'a_solve', a

        a1=self.alpha1()
        mir1=self.mir1()
        mir1=self.mir1()


        mir1=self.mir1()
        mir2=self.mir2()
#        print 'mir', mir1, mir2
#

        x1=self.x1()
        x2=self.x2()
#        print 'x', x1, x2



        a1=self.alpha1()
        a2=self.alpha2()
#        print 'alpha', self.alpha1(), self.alpha2()

        y1=self.__y1
        y2=self.__y2

        jxyi1=self.pr1.jxy()
        jxyi2=self.pr2.jxy()

        xi1=self.pr1.dx()
        xi2=self.pr2.dx()

        yi1=self.pr1.dy()
        yi2=self.pr2.dy()

        if mir1==1:
            jxyi1=-jxyi1
            xi1=-xi1
        if mir2==1:
            jxyi2=-jxyi2
            xi2=-xi2

        jxi1, jyi1, jxyi1=jda(self.pr1.jx(), self.pr1.jy(), jxyi1, -a1)


        jxi2, jyi2, jxyi2=jda(self.pr2.jx(), self.pr2.jy(),  jxyi2, -a2)

#        print u'после поворота'
#        print jxi1, jyi1, jxyi1
#        print jxi2, jyi2, jxyi2

#        print 'xi1, x1', xi1, x1
#        print 'xi2, x2', xi2, x2

        yi=(self.pr1.a()*(yi1+y1)+  self.pr2.a()*(yi2+y2))/a
        xi=(self.pr1.a()*(xi1+x1)+  self.pr2.a()*(xi2+x2))/a

#        print 'xi', xi
#        print 'yi', yi
#
        jx1=jxdx(jxi1, self.pr1.a(), yi1+y1-yi)
        jx2=jxdx(jxi2, self.pr2.a(), yi2+y2-yi)

        jx=jx1+jx2
#        print 'jx', jx

#        print xi1, x1, xi
#        print xi2, x2, xi
#        print u'сумма xi1', xi1+x1-xi
#        print u'сумма xi2', xi2+x2-xi

        jy1=jxdx(jyi1, self.pr1.a(), xi1+x1-xi)
        jy2=jxdx(jyi2, self.pr2.a(), xi2+x2-xi)

#        print 'jy1', jy1
#        print 'jy2', jy2

        jy=jy1+jy2


        jxy1=jxydxdy(jxyi1, self.pr1.a(), xi1+x1-xi, yi1+y1-yi)
        jxy2=jxydxdy(jxyi2, self.pr2.a(), xi2+x1-xi, yi2+y1-yi)


        jxy=jxy1+jxy2


#        print 'jy',jy
#        print 'jx',jx

        self.__a=a
        self.__jx=jx
        self.__jy=jy
        self.__jxy=jxy

        self.__xi=xi
        self.__yi=yi

        massiv6 = jxjy(jx, jy, jxy)
        self.__alpha = massiv6[0]
        self.__jx0 = massiv6[1]
        self.__jy0 = massiv6[2]

    def xi(self):
        return self.__xi

    def yi(self):
        return self.__yi

    def dx(self):
        return self.__dx

    def dy(self):
        return self.__dy

    def a(self):
        return self.__a

    def jx(self):
        return self.__jx

    def jxy(self):
        return self.__jxy

    def jy(self):
        return self.__jy


    def jx0(self):
        return self.__jx0

    def alpha(self):
        return self.__alpha

    def jy0(self):
        return self.__jy0


    def alpha2(self):
        return self.__a2

    def alpha1(self):
        return self.__a1

    def x1(self):
        return self.__x1

    def x2(self):
        return self.__x2

    def y1(self):
        return self.__y1

    def y2(self):
        return self.__y2

    def mir1(self):
        return self.__mir1

    def mir2(self):
        return self.__mir2


#    def alpha(self):
#        return self.__alpha

    def title0(self):
        return self.__title0

    def title(self):
        return self.__title


class  profiles_blank_sostav(object):
    def p(self):
        return self.a()*7850./100./100.


    def ix(self):
        return (self.jx()/self.a())**0.5
    def iy(self):
        return (self.jy()/self.a())**0.5
    def wx(self):
        return self.jx()/self.h()*2
    def wy(self):
        return self.jy()/self.b()*2

    def xi(self):
        return self.__xi

    def yi(self):
        return self.__yi


    def a(self):
        return self.__a

    def jx(self):
        return self.__jx

    def jxy(self):
        return self.__jxy

    def jy(self):
        return self.__jy



    def alpha1(self):
        return self.__alpha1

    def alpha2(self):
        return self.__alpha2

    def x1(self):
        return self.__x1

    def x2(self):
        return self.__x2

    def y1(self):
        return self.__y1

    def y2(self):
        return self.__y2

    def mir1(self):
        return self.__mir1

    def mir2(self):
        return self.__mir2

    def jx0(self):
        return self.__jx0

    def jy0(self):
        return self.__jy0

    def ix0(self):
        return self.__ix0

    def iy0(self):
        return self.__iy0



    def alpha(self):
        return self.__alpha


#    def alpha(self):
#        return self.__alpha

    def title0(self):
        return 'sostav'

    def title(self):
        return self.__title
        
    def def_char(self):
        self.__a=self.sostav.a()
        self.__jx=self.sostav.jx()
        self.__jy=self.sostav.jy  ()
        self.__jxy=self.sostav.jxy()

        self.__xi=self.sostav.xi()
        self.__yi=self.sostav.yi ()

        self.__alpha=self.sostav.alpha()
        self.__jx0=self.sostav.jx0()
        self.__jy0=self.sostav.jy0()

        self.__ix0=(self.sostav.jx0()/self.__a)**0.5
        self.__iy0=(self.sostav.jy0()/self.__a)**0.5


        self.__p=self.sostav.a()*7850/100/100
        
class sost_ugol_tavr_st_up(profiles_blank_sostav):
    """Расчет сечения сдвоенных уголков. Для неравнополочных - длинная сторона направлена вверх
    Входные данные - h, b, t,
    r1 - между полками,
    r3 - на концах полок,
    r2 - для гнутого уголка,
    dx - расстояние между уголками (толщина фасонки, которая ставится внутрь!)
    Выходные данные:
    A; Jx; Jy; Jxy; xi; yi
    title0 - sostav
    title - ugol_tavr_st_up
    """


    def __init__(self     , h=False, b=False\
    , t=False, r1=False, r2=False,  r3=False , dx=False):

 
        self.__s=t       
        self.pr1=ugol(h=h,b=b,t=t, r2=r2, r1=r1, r3=r3)
        self.pr2=self.pr1

#        print 'self.__at1', self.__at1

        self.__dx=float(dx)
        self.__dy=float(0.0)

        self.__x1=self.__dx/2.
        self.__x2=-self.__dx/2.

        self.__y1=float(0)
        self.__y2=float(0)
        self.__mir1=float(0)
        self.__mir2=float(1)
        self.__alpha1=float(0)
        self.__alpha2=float(0)



        self.__title='ugol_tavr_st_up'


        self.sostav=profiles_sostav( pr1=self.pr1, alpha1=self.__alpha1, x1=self.__x1, y1=self.__y1, mir1=self.__mir1  , pr2=self.pr2, x2=self.__x2, y2=self.__y2, alpha2=self.__alpha2, mir2=self.__mir2, title=self.__title)

        self.def_char()
        
        self.__h=h
        self.__b=b        
        self.__t=t  
        self.__r1=r1 
        self.__r2=r2        
        self.__r3=r3      
        self.__dx=dx  
        
    def title(self):
        return self.__title
    def input_data(self):
        return [u"h, см",u"b, см",u"t, см",u"r1, см",u"r2, см",u"r3, см",u"dx, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'iy, см': self.iy()
        ,u'xi, см': self.xi()
        ,u'yi, см': self.yi()
        ,u'Jx0, см4': self.jx0()
        ,u'ix0, см': self.ix0()
        ,u'Jy0, см4': self.jy0()
        ,u'iy0, см': self.iy0()
        ,u'alpha': self.alpha()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'iy, см'
        ,u'xi, см'
        ,u'yi, см'
        ,u'Jx0, см4'
        ,u'ix0, см'
        ,u'Jy0, см4'
        ,u'iy0, см'
        ,u'alpha'        
        ,u'title'
        ,u'title0'  
        ]
        return out

    def hef(self):
        return self.pr1.h()-self.pr1.t()-self.pr1.r1()
    def bef(self):
        return self.pr1.b()-self.pr1.t()-self.pr1.r1()

    def h(self):
        return self.__h
    def b(self):
        return self.__b
    def s(self):
        return self.__s
    def t(self):
        return self.__t
    def r1(self):
        return self.__r1
    def r2(self):
        return self.__r2

    def r3(self):
        return self.__r3


    def dx(self):
        return self.__dx

    def dy(self):
        return self.__dy


class sost_ugol_tavr_st_right(profiles_blank_sostav):
    """Расчет сечения сдвоенных уголков. Для неравнополочных - длинная сторона направлена вбок
    Входные данные - h, b, t,
    r1 - между полками,
    r3 - на концах полок,
    r2 - для гнутого уголка,
    dx - расстояние между уголками (толщина фасонки, которая ставится внутрь!)
    Выходные данные:
    A; Jx; Jy; Jxy; xi; yi
    title0 - sostav
    title - ugol_tavr_st_right
    """

    def __init__(self     , h=False, b=False\
    , t=False, r1=False, r2=False,  r3=False , dx=False):

        self.__s=t       

        self.__h=h
        self.__b=b        
        self.__t=t  
        self.__r1=r1 
        self.__r2=r2        
        self.__r3=r3      
        self.__dx=dx 
        
        self.pr1=ugol(h=h,b=b,t=t, r2=r2, r1=r1, r3=r3)
        self.pr2=self.pr1

        self.__alpha1=float(pi/2)
        self.__alpha2=float(-pi/2)
        self.__dx=float(dx)
        self.__dy=float(0)

        self.__x1=self.__dx/2+self.pr1.dy()-self.pr1.dx()
        self.__x2=-self.__dx/2-self.pr2.dy()+self.pr2.dx()

        self.__y1=-self.pr1.dy()+self.pr1.dx()
        self.__y2=-self.pr2.dy()+self.pr2.dx()

        self.__mir1=float(0)
        self.__mir2=float(1)



        self.__title='ugol_tavr_st_right'


        self.sostav=profiles_sostav( pr1=self.pr1, alpha1=self.__alpha1, x1=self.__x1, y1=self.__y1, mir1=self.__mir1  , pr2=self.pr2, x2=self.__x2, y2=self.__y2, alpha2=self.__alpha2, mir2=self.__mir2, title=self.__title)

        self.def_char()
    def title(self):
        return self.__title
    def input_data(self):
        return [u"h, см",u"b, см",u"t, см",u"r1, см",u"r2, см",u"r3, см",u"dx, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'iy, см': self.iy()
        ,u'xi, см': self.xi()
        ,u'yi, см': self.yi()
        ,u'Jx0, см4': self.jx0()
        ,u'ix0, см': self.ix0()
        ,u'Jy0, см4': self.jy0()
        ,u'iy0, см': self.iy0()
        ,u'alpha': self.alpha()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'iy, см'
        ,u'xi, см'
        ,u'yi, см'
        ,u'Jx0, см4'
        ,u'ix0, см'
        ,u'Jy0, см4'
        ,u'iy0, см'
        ,u'alpha'
        ,u'title'
        ,u'title0'  
        ]
        return out
    def hef(self):
        return self.pr1.h()-self.pr1.t()-self.pr1.r1()
    def bef(self):
        return self.pr1.b()-self.pr1.t()-self.pr1.r1()
    def h(self):
        return self.__h
    def b(self):
        return self.__b
    def s(self):
        return self.__s
    def t(self):
        return self.__t
    def r1(self):
        return self.__r1
    def r2(self):
        return self.__r2

    def r3(self):
        return self.__r3


    def dx(self):
        return self.__dx

    def dy(self):
        return self.__dy


class sost_ugol_tavr_st_krest(profiles_blank_sostav):
    """Расчет сечения уголков вкрест
    Входные данные - h, b, t,
    r1 - между полками,
    r3 - на концах полок,
    r2 - для гнутого уголка,
    dx - расстояние по горизонтали между уголками (толщина фасонки, которая ставится внутрь!)
    dy - расстояние по вертикали между уголками (толщина фасонки, которая ставится внутрь!)
    Выходные данные:
    A; Jx; Jy; Jxy; xi; yi
    title0 - sostav
    title - ugol_tavr_st_krest
    """


    def __init__(self     , h=False, b=False\
    , t=False, r1=False, r2=False,  r3=False , dx=False, dy=False):
        self.__s=t       

        self.__h=h
        self.__b=b        
        self.__t=t  
        self.__r1=r1 
        self.__r2=r2        
        self.__r3=r3      
        self.__dx=dx 
        self.__dy=dy 
        
        self.pr1=ugol(h=h,b=b,t=t, r2=r2, r1=r1, r3=r3)
        self.pr2=self.pr1

        self.__alpha1=float()
        self.__alpha2=float(pi)
        self.__dx=float(dx)
        self.__dy=float(dy)

        self.__x1=self.__dx/2
        self.__x2=-self.__dx/2-2*self.pr2.dx()

        self.__y1=self.__dy/2
        self.__y2=-self.__dy/2-2*self.pr2.dy()

        self.__mir1=float(0)
        self.__mir2=float(0)



        self.__title='ugol_tavr_st_krest'

        self.sostav=profiles_sostav( pr1=self.pr1, alpha1=self.__alpha1, x1=self.__x1, y1=self.__y1, mir1=self.__mir1  , pr2=self.pr2, x2=self.__x2, y2=self.__y2, alpha2=self.__alpha2, mir2=self.__mir2, title=self.__title)

        self.def_char()
    def input_data(self):
        return [u"h, см",u"b, см",u"t, см",u"r1, см",u"r2, см",u"r3, см",u"dx, см",u"dy, см"]
    def output_dict(self):
        out={u'P, кг/м': self.p()
        ,u'A, см2': self.a()
        ,u'Jx, см4': self.jx()
        ,u'ix, см': self.ix()
        ,u'Jy, см4': self.jy()
        ,u'iy, см': self.iy()
        ,u'xi, см': self.xi()
        ,u'yi, см': self.yi()
        ,u'Jx0, см4': self.jx0()
        ,u'ix0, см': self.ix0()
        ,u'Jy0, см4': self.jy0()
        ,u'iy0, см': self.iy0()
        ,u'alpha': self.alpha()
        ,u'title': self.title()   
        ,u'title0': self.title0()  
        }
        return out

    def output_list(self):
        out=[u'P, кг/м'
        ,u'A, см2'
        ,u'Jx, см4'
        ,u'ix, см'
        ,u'Jy, см4'
        ,u'iy, см'
        ,u'xi, см'
        ,u'yi, см'
        ,u'Jx0, см4'
        ,u'ix0, см'
        ,u'Jy0, см4'
        ,u'iy0, см'
        ,u'alpha'
        ,u'title'
        ,u'title0'  
        ]
        return out
    def title(self):
        return self.__title
        
    def hef(self):
        return self.pr1.h()-self.pr1.t()-self.pr1.r1()
    def bef(self):
        return self.pr1.b()-self.pr1.t()-self.pr1.r1()
    def h(self):
        return self.__h
    def b(self):
        return self.__b
    def s(self):
        return self.__s
    def t(self):
        return self.__t
    def r1(self):
        return self.__r1
    def r2(self):
        return self.__r2

    def r3(self):
        return self.__r3


    def dx(self):
        return self.__dx

    def dy(self):
        return self.__dy
