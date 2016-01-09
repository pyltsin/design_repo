# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 22:25:55 2014

@author: Pyltsin
"""

import unittest

from profiles2 import *
from table import *

pi = 3.14159265358979

from profiles2 import *


class Test_profile(unittest.TestCase):
    def test_profiles_infile(self):
        el = profiles_infile(files='SortamentData/gost823989.csv', number='10', typ='dvut')
        self.assertEquals(el.h(), 1.00)
        print 1, "test_profiles_infile"

    def test_simple_profiles(self):
        el = profiles_simple(h=20, b=30 \
                             , s=40, t=50, r1=60, r2=70, a1=80, a2=90, x1=100 \
                             , x2=110, y1=120, y2=130, r=140, r3=150)
        self.assertEquals(el.h(), 20)
        self.assertEquals(el.b(), 30)
        self.assertEquals(el.s(), 40)
        self.assertEquals(el.t(), 50)
        self.assertEquals(el.r1(), 60)
        self.assertEquals(el.r2(), 70)
        self.assertEquals(el.r3(), 150)
        self.assertEquals(el.a1(), 80)
        self.assertEquals(el.a2(), 90)
        self.assertEquals(el.x1(), 100)
        self.assertEquals(el.x2(), 110)
        self.assertEquals(el.y1(), 120)
        self.assertEquals(el.y2(), 130)
        self.assertEquals(el.r(), 140)
        print 2, "test_simple_profiles"

    def test_rectangle(self):
        el = rectangle(20, 30)
        self.assertEquals(el.h(), 20)
        self.assertEquals(el.b(), 30)
        self.assertEquals(el.a(), 20 * 30)
        self.assertEquals(el.jx(), 20 ** 3 * 30 / 12)
        self.assertEquals(el.jy(), 30 ** 3 * 20 / 12)
        self.assertEquals(el.s2x(), 20 / 2 * 20 / 4 * 30)
        self.assertEquals(el.s2y(), 30 / 2 * 30. / 4 * 20)
        self.assertEquals(el.sx(5), 5. * 5 / 2 / 4 * 30)
        self.assertEquals(el.sy(5), 5. * 5 / 2 / 4 * 20)
        self.assertEquals(el.jxy(), 0)
        self.assertLess(abs(el.jxdy(5) - 35000) / abs(el.jxdy(5)), 0.0000001)
        self.assertLess(abs(el.jydx(5) - 60000) / abs(el.jydx(5)), 0.0000001)
        #        self.assertLess(abs(el.jxydxdy(5,6)-18000)/abs(el.jxydxdy(5,6)),0.0000001)


        self.assertEquals(el.input_data(), [u"h, см", u"b, см"])
        self.assertEquals(el.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'Wx, см3'
            , u'Sx, см3'
            , u'ix, см'
            , u'Jy, см4'
            , u'Wy, см3'
            , u'Sy, см3'
            , u'iy, см'
            , u'title'
            , u'title0'
                                             ])

        self.assertEquals(el.output_dict()[u'A, см2'], 20 * 30)
        self.assertEquals(el.output_dict()[u'Jx, см4'], 20 ** 3 * 30 / 12)
        self.assertEquals(el.output_dict()[u'Wx, см3'], 30 * 20 * 20 / 6)
        self.assertEquals(el.output_dict()[u'ix, см'], (20 ** 3 * 30. / 12 / 20 / 30) ** 0.5)
        self.assertEquals(el.output_dict()[u'Sx, см3'], 10 * 5 * 30)

        self.assertEquals(el.output_dict()[u'Jy, см4'], 20 * 30 ** 3 / 12)
        self.assertEquals(el.output_dict()[u'Wy, см3'], 30 * 30 * 20 / 6)
        self.assertEquals(el.output_dict()[u'iy, см'], (20 * 30. ** 3 / 12 / 20 / 30) ** 0.5)
        self.assertEquals(el.output_dict()[u'Sy, см3'], 15 * 7.5 * 20)
        self.assertEquals(el.output_dict()[u'P, кг/м'], 20 * 30 * 7850 / 100 / 100)
        self.assertEquals(el.output_dict()[u'title'], 'rectangle')
        self.assertEquals(el.output_dict()[u'title0'], 'simple')

        print 3, "test_rectangle"

    def test_quartercircle(self):
        el = quartercircle(r=15)
        self.assertLess(abs(el.a() - 15 * 15 * pi / 4), 0.00001)
        self.assertLess(abs(el.jx() - 0.05489 * 15 ** 4) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 0.05489 * 15 ** 4) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.xi() - 4. / 3 * 15 / pi), 0.00001)
        self.assertLess(abs(el.yi() - 4. / 3 * 15 / pi), 0.00001)
        self.assertLess(abs(el.jxy() + 0.01646 * 15 ** 4) / abs(el.jxy()), 0.001)
        print 4, "test_quartercircle"

    def test_circleangle(self):
        el = circleangle(r=15)
        self.assertLess(abs(el.a() - 48.2854) / 48.2854, 0.00001)
        self.assertLess(abs(el.xi() - 3.3505) / 3.3505, 0.00001)
        self.assertLess(abs(el.yi() - 3.3505) / 3.3505, 0.00001)
        self.assertLess(abs(el.jx() - 381.97783) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 381.97783) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jxy() + 224.7080) / abs(el.jxy()), 0.001)
        print 5, "test_circleangle"

    def test_quartercirclesolid(self):
        el = quartercirclesolid(r=15, r1=10)
        self.assertLess(abs(el.a() - 98.1748) / 98.1748, 0.00001)
        self.assertLess(abs(el.xi() - 6.9361) / 6.9361, 0.00001)
        self.assertLess(abs(el.yi() - 6.9361) / 6.9361, 0.00001)
        self.assertLess(abs(el.jx() - 1592.8845) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 1592.8845) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jxy() + 1305.7566) / abs(el.jxy()), 0.001)
        print 6, "test_quartercirclesolid"

    def test_anglerectangle(self):
        el = anglerectangle(b=15, h=10)
        self.assertLess(abs(el.a() - 15 * 10 / 2) / abs(el.a()), 0.00001)
        self.assertLess(abs(el.xi() - 5) / abs(el.xi()), 0.00001)
        self.assertLess(abs(el.yi() - 3.3333) / abs(el.yi()), 0.00001)
        self.assertLess(abs(el.jx() - 15. * 10 ** 3 / 36) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 15. ** 3 * 10 / 36) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jxy() + 15. ** 2 * 10 ** 2 / 72) / abs(el.jxy()), 0.001)
        print 7, "test_anglerectangle"

    def test_solid(self):
        el = solid(r=15)
        self.assertLess(abs(el.a() - 15 ** 2 * pi) / abs(el.a()), 0.00001)
        self.assertLess(abs(el.xi() - 15) / abs(el.xi()), 0.00001)
        self.assertLess(abs(el.yi() - 15) / abs(el.yi()), 0.00001)
        self.assertLess(abs(el.jx() - pi * 30 ** 4 / 64) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - pi * 30 ** 4 / 64) / abs(el.jx()), 0.001)
        self.assertEqual(el.jxy(), 0)
        print 8, "test_solid"

    def test_ring(self):
        el = ring(15, 10)

        self.assertLess(abs(el.t() - 5) / abs(el.t()), 0.00001)
        self.assertLess(abs(el.s() - 5) / abs(el.t()), 0.00001)
        self.assertLess(abs(el.bef() - 12.5) / abs(el.t()), 0.00001)

        self.assertLess(abs(el.hef() - 12.5) / abs(el.t()), 0.00001)

        self.assertLess(abs(el.a() - 15 ** 2 * pi + 10 ** 2 * pi) / abs(el.a()), 0.00001)
        self.assertLess(abs(el.xi() - 15) / abs(el.xi()), 0.00001)
        self.assertLess(abs(el.yi() - 15) / abs(el.yi()), 0.00001)
        self.assertLess(abs(el.jx() - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4)) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4)) / abs(el.jx()), 0.001)
        self.assertEqual(el.jxy(), 0)

        self.assertEqual(el.input_data(), [u"r, см", u"r1, см"])
        self.assertEqual(el.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'Wx, см3'
            , u'ix, см'
            , u'Jy, см4'
            , u'Wy, см3'
            , u'iy, см'
            , u'title'
            , u'title0'
                                            ])

        self.assertLess(
            abs(el.output_dict()[u'A, см2'] - 15 ** 2 * pi + 10 ** 2 * pi) / abs(el.output_dict()[u'A, см2']), 0.00001)

        self.assertLess(abs(el.output_dict()[u'Jx, см4'] - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4)), 0.00001)
        self.assertLess(abs(el.output_dict()[u'Wx, см3'] - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4) / 15.), 0.00001)
        self.assertLess(abs(el.output_dict()[u'ix, см'] ** 2 - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4) / (
        15 ** 2 * pi - 10 ** 2 * pi)), 0.00001)

        self.assertLess(abs(el.output_dict()[u'Jy, см4'] - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4)), 0.00001)
        self.assertLess(abs(el.output_dict()[u'Wy, см3'] - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4) / 15.), 0.00001)
        self.assertLess(abs(el.output_dict()[u'iy, см'] ** 2 - pi * 30 ** 4 / 64 * (1 - (10. / 15) ** 4) / (
        15 ** 2 * pi - 10 ** 2 * pi)), 0.00001)

        self.assertLess(
            abs(el.output_dict()[u'P, кг/м'] - 15 ** 2 * pi * 7850 / 10000 + 10 ** 2 * pi * 7850. / 100 / 100), 0.00001)

        self.assertEqual(el.output_dict()[u'title0'], 'simple')
        self.assertEqual(el.output_dict()[u'title'], 'ring')

        print 9, "test_ring"

    def test_angle(self):
        el = angle(b=10, h=12, x1=3)
        self.assertLess(abs(el.a() - 1 / 2. * 10 * 12) / abs(el.a()), 0.00001)
        self.assertLess(abs(el.xi() - 4.3333) / abs(el.xi()), 0.00001)
        self.assertLess(abs(el.yi() - 4) / abs(el.yi()), 0.00001)
        self.assertLess(abs(el.jx() - 480) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 263.333) / abs(el.jx()), 0.001)
        print 10, "test_angle"

    def test_circleseg(self):
        el = circleseg(a1=pi / 6, r=10)
        self.assertLess(abs(el.a() - 9.0586) / abs(el.a()), 0.00001)
        self.assertLess(abs(el.xi() - 5) / abs(el.xi()), 0.00001)
        self.assertLess(abs(el.yi() - 9.1994) / abs(el.yi()), 0.00001)
        self.assertLess(abs(el.jx() - 1.1183) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 46.0432) / abs(el.jx()), 0.001)
        self.assertEqual(el.jxy(), 0)
        print 11, "test_circleseg"

    def test_krug(self):
        el = krug(a1=pi / 6, r=10)
        self.assertLess(abs(el.a() - 5.3751) / abs(el.a()), 0.00001)
        self.assertEqual(el.xi(), 0.0000)
        self.assertLess(abs(el.yi() - 1.6753) / abs(el.yi()), 0.0001)
        self.assertLess(abs(el.jx() - 1.2085) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jy() - 14.0974) / abs(el.jx()), 0.001)
        self.assertEqual(el.jxy(), 0)

        print 12, " test_krug"

    def test_rotkrug(self):
        el = rotkrug(a1=pi / 6, r=10)
        self.assertLess(abs(el.a() - 5.3751) / abs(el.a()), 0.00001)
        self.assertLess(abs(el.yi() - 1.0491) / abs(el.yi()), 0.0001)
        self.assertLess(abs(el.xi() - 0.6057) / abs(el.xi()), 0.0001)
        self.assertLess(abs(el.jy() - 10.8752) / abs(el.jy()), 0.001)
        self.assertLess(abs(el.jx() - 4.4307) / abs(el.jx()), 0.001)
        self.assertLess(abs(el.jxy() + 5.5811) / abs(el.jxy()), 0.001)
        print 13, " test_rotkrug"

    def test_dvut(self):
        el = dvut(60, 19, 1.2, 1.78, 2, 0.8, atan(12. / 100))

        self.assertLess(abs(el.a() - 137.5384332) / abs(el.a()), 0.0000001)
        self.assertLess(abs(el.jy() - 1724.838581) / abs(el.jy()), 0.0000001)
        self.assertLess(abs(el.jx() - 76805.76144) / abs(el.jx()), 0.0000001)
        self.assertLess(abs(el.s2x() - 1490.827914) / abs(el.s2x()), 0.0000001)
        self.assertLess(abs(el.ix() - 23.6311503) / abs(el.ix()), 0.0000001)
        self.assertLess(abs(el.iy() - 3.5412957) / abs(el.iy()), 0.0000001)

        self.assertLess(abs(el.wx() - 2560.19204793) / abs(el.wx()), 0.0000001)
        self.assertLess(abs(el.wy() - 181.56195592) / abs(el.wy()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'P, кг/м'] - 137.5384332 / 100 / 100 * 7850) / abs(el.a()), 0.0000001)

        self.assertLess(abs(el.output_dict()[u'A, см2'] - 137.5384332) / abs(el.a()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'Jy, см4'] - 1724.838581) / abs(el.jy()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'Jx, см4'] - 76805.76144) / abs(el.jx()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'Sx, см3'] - 1490.827914) / abs(el.s2x()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'Sy, см3'] - 156.051) / abs(el.s2y()), 0.00002)

        self.assertLess(abs(el.output_dict()[u'ix, см'] - 23.6311503) / abs(el.ix()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'iy, см'] - 3.5412957) / abs(el.iy()), 0.0000001)

        self.assertLess(abs(el.output_dict()[u'Wx, см3'] - 2560.19204793) / abs(el.wx()), 0.0000001)
        self.assertLess(abs(el.output_dict()[u'Wy, см3'] - 181.56195592) / abs(el.wy()), 0.0000001)

        self.assertLess(abs(el.t1() - 1.246) / abs(el.t1()), 0.0000001)
        self.assertLess(abs(el.t2() - 1.068) / abs(el.t2()), 0.0000001)

        self.assertEqual(el.title(), 'dvut')

        self.assertLess(abs(el.s2y() - 156.051) / abs(el.s2y()), 0.00002)

        self.assertLess(abs(el.sy1() - 145.25) / abs(el.sy1()), 0.00002)

        self.assertLess(abs(el.sx1() - 695.471) / abs(el.sx1()), 0.00002)

        self.assertLess(abs(el.sx1() - 690) / abs(el.sx1()), 0.01)

        self.assertLess(abs(el.sx2() - 995.595417) / abs(el.sx2()), 0.00002)

        self.assertLess(abs(el.sx2() - 1001.057) / abs(el.sx2()), 0.01)

        self.assertLess(abs(el.wxmin() - 2560.19204793) / abs(el.wx()), 0.0000001)
        self.assertLess(abs(el.wymin() - 181.56195592) / abs(el.wy()), 0.0000001)

        self.assertLess(abs(el.hef() - 51.8234) / abs(el.hef()), 0.000002)
        self.assertLess(abs(el.bef() - 7.1383) / abs(el.bef()), 0.000002)

        self.assertLess(abs(el.aw() - 67.73) / abs(el.aw()), 0.0002)

        self.assertLess(abs(el.af() - 33.82) / abs(el.af()), 0.000002)

        self.assertLess(abs(el.afaw() - 33.82 / 67.73) / abs(el.afaw()), 0.0002)
        print 14, " test_dvut"

    def test_dvut2(self):
        el = dvut(h=360., b=130., t=16., s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        self.assertLess(abs(el.jx() - 15339.998 * 10 ** 4) / abs(el.jx()), 0.001)
        #        print(el.jw()/10**6)
        self.assertLess(abs(el.jw() - 146500 * 10 ** 6) / abs(el.jw()), 0.001)
        self.assertLess(abs(el.output_dict()[u"Jw, см6"] - 146500 * 10 ** 6) / abs(el.jw()), 0.001)

        el2 = dvut(h=450, b=150, t=18, s=10.5, r1=16, r2=7, a1=atan(12. / 100))
        #        print(el2.jw()/10**6)
        self.assertLess(abs(el2.jw() - 398400 * 10 ** 6) / abs(el2.jw()), 0.001)

        el3 = dvut(h=240, b=110, t=14, s=8.2, r1=10.5, r2=4, a1=atan(12. / 100))

        #        print el3.jt()
        self.assertLess(abs(el3.jt() - 31.22 * 10 ** 4) / abs(el3.jt()), 0.005)
        self.assertLess(abs(el3.output_dict()[u"Jt, см4"] - 31.22 * 10 ** 4) / abs(el3.jt()), 0.005)
        self.assertLess(abs(el3.output_dict()[u"Jt_sp2013, см4"] - 31.22 * 10 ** 4 / 1.3) / abs(el3.jt()), 0.005)

        e14 = dvut(h=60.0, b=19.0, t=1.78, s=1.2, r1=2, r2=0.8, a1=atan(12. / 100))
        self.assertEqual(e14.input_data(), [u"h, см", u"b, см", u"s, см", u"t, см", u"r1, см", u"r2, см", u"a, %/100"])
        self.assertEqual(e14.output_list(), [u'P, кг/м', u'A, см2', u'Jx, см4', u'Wx, см3', u'Sx, см3', u'ix, см'
            , u'Jy, см4', u'Wy, см3', u'Sy, см3', u'iy, см', u'Jw, см6', u'Jt, см4', u'Jt_sp2013, см4', u'w1, см2',
                                             u'Ww, см4', u'title', u'title0'])
        self.assertLess(abs(e14.output_dict()[u"A, см2"] - 137.53) / abs(137.53), 0.001)
        self.assertLess(abs(e14.output_dict()[u"P, кг/м"] - 137.53 * 7850 / 100 / 100) / abs(137.53 * 7850 / 100 / 100),
                        0.001)
        self.assertLess(abs(e14.output_dict()[u"Jx, см4"] - 76805.) / abs(76805), 0.001)
        self.assertLess(abs(e14.output_dict()[u"Wx, см3"] - 76805. / 30.) / abs(76805. / 30), 0.001)
        self.assertLess(abs(e14.output_dict()[u"Sx, см3"] - 68.77 * 21.6787) / abs(68.77 * 21.6787), 0.001)
        self.assertLess(abs(e14.output_dict()[u"ix, см"] - (76805. / 137.53) ** 0.5) / abs((76805. / 137.53) ** 0.5),
                        0.001)

        self.assertLess(abs(e14.output_dict()[u"Jy, см4"] - 1724.8386) / abs(1724.8386), 0.001)
        self.assertLess(abs(e14.output_dict()[u"Wy, см3"] - 1724.8386 / 9.5) / abs(1724.8386 / 9.5), 0.001)
        self.assertLess(abs(e14.output_dict()[u"Sy, см3"] - 68.77 * 2.2692) / abs(68.77 * 2.2692), 0.001)
        self.assertLess(
            abs(e14.output_dict()[u"iy, см"] - (1724.8386 / 137.53) ** 0.5) / abs((1724.8386 / 137.53) ** 0.5), 0.001)

        e14 = dvut(h=18, b=9.0, t=0.81, s=0.51, r1=0.9, r2=0.35, a1=atan(12. / 100))
        self.assertLess(abs(e14.output_dict()[u"Jw, см6"] - (5780)) / abs(5780), 0.005)
        self.assertLess(abs(e14.output_dict()[u"Jt, см4"] - (5.09)) / abs(5.09), 0.007)
        self.assertLess(abs(e14.output_dict()[u"Jt_sp2013, см4"] - (5.09 / 1.3)) / abs(5.09 / 1.3), 0.007)

        self.assertLess(abs(e14.output_dict()[u"w1, см2"] - (38.07)) / abs(38.07), 0.001)
        self.assertLess(abs(e14.output_dict()[u"Ww, см4"] - (151.82)) / abs(151.82), 0.001)

        self.assertEqual(e14.output_dict()[u"title"], 'dvut')
        self.assertEqual(e14.output_dict()[u"title0"], 'simple')

        print 15, " test_dvut2"

    def test_function(self):
        self.assertEqual(jxdx(5, 6, 7), 299)
        self.assertLess((jda(11.25, 31.25, 0, 45. / 180 * pi)[0] - 21.25) / 21.25, 0.00002)
        self.assertLess((jda(11.25, 31.25, 0, 45. / 180 * pi)[1] - 21.25) / 21.25, 0.00002)
        self.assertLess((jda(11.25, 31.25, 0, 45. / 180 * pi)[2] - 10.) / 10., 0.00002)
        print 16, "test_function"

    #         self.assertLess(abs(el.get_sigma_e()-3.5412957)/abs(el.get_sigma_e()),0.0000001)

    def test_korob(self):

        pr1 = truba_pryam(12, 8, 0.6, 0.6, 1.2)
        #        print pr1.a()
        self.assertLess(abs(pr1.a() - 21.63) / 21.63, 0.001)
        #        print pr1.jx()
        self.assertLess(abs(pr1.jx() - 405.9) / 405.9, 0.001)
        #        print pr1.jy()
        self.assertLess(abs(pr1.jy() - 215) / 215, 0.001)
        #        print pr1.s2x()
        self.assertLess(abs(pr1.s2x() - 42.1) / 42.1, 0.001)
        #        print pr1.s2y()
        self.assertLess(abs(pr1.s2y() - 31.77) / 31.77, 0.001)
        #        print pr1.s2x()
        self.assertLess(abs(pr1.sx1() - 1.44) / 1.44, 0.001)
        #        print pr1.s2y()
        self.assertLess(abs(pr1.sy1() - 2.16) / 2.16, 0.001)

        self.assertLess(abs(pr1.aw() - 06.48) / 06.48, 0.001)

        self.assertLess(abs(pr1.af() - 4.8) / 4.8, 0.001)

        self.assertLess(abs(pr1.afaw() - 0.741 / 2) / 0.741 * 2, 0.001)

        self.assertLess(abs(pr1.hef() - 9.6) / 9.6, 0.001)

        self.assertLess(abs(pr1.bef() - 5.6) / 5.6, 0.001)

        self.assertEqual(pr1.title(), 'korob')

        pr1 = truba_pryam(h=5, b=2.5, t=0.2, r2=0.4, r1=0.2)
        self.assertEqual(pr1.input_data(), [u"h, см", u"b, см", u"t, см", u"r1, см", u"r2, см"])
        self.assertEqual(pr1.output_list(),
                         [u'P, кг/м', u'A, см2', u'Jx, см4', u'Wx, см3', u'Sx, см3', u'ix, см', u'Jy, см4'
                             , u'Wy, см3'
                             , u'Sy, см3'
                             , u'iy, см'
                             , u'title'
                             , u'title0'
                          ])

        self.assertLess(abs(pr1.output_dict()[u'P, кг/м'] - 2.149) / 2.149, 0.001)
        self.assertLess(abs(pr1.output_dict()[u'A, см2'] - 2.737) / 2.737, 0.001)

        self.assertLess(abs(pr1.output_dict()[u'Jx, см4'] - 8.384) / 8.384, 0.001)
        self.assertLess(abs(pr1.output_dict()[u'Wx, см3'] - 3.353) / 3.353, 0.001)
        self.assertLess(abs(pr1.output_dict()[u'Sx, см3'] - 2.134) / 2.134, 0.002)
        self.assertLess(abs(pr1.output_dict()[u'ix, см'] - 1.75) / 1.75, 0.001)

        self.assertLess(abs(pr1.output_dict()[u'Jy, см4'] - 2.809) / 2.809, 0.001)
        self.assertLess(abs(pr1.output_dict()[u'Wy, см3'] - 2.247) / 2.247, 0.001)
        self.assertLess(abs(pr1.output_dict()[u'Sy, см3'] - 1.311) / 1.311, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'iy, см'] - 1.013) / 1.013, 0.001)

        self.assertEqual(pr1.output_dict()['title'], 'korob')

        self.assertEqual(pr1.output_dict()['title0'], 'simple')

        print 17, "test_korob"

    def test_ugol(self):
        print 18, "test_ugol"

        pr1 = ugol(18, 18, 1.5, 1.6, 0., 0.53)

        #        print pr1.ix0()
        #        print pr1.iy0()
        #
        self.assertLess(abs(pr1.a() - 52.18) / 52.18, 0.0001)
        self.assertLess(abs(pr1.jx() - 1607.36) / 1607.36, 0.0001)
        self.assertLess(abs(pr1.jy() - 1607.36) / 1607.36, 0.0001)
        self.assertLess(abs(pr1.jxy() + 947.6) / 947.6, 0.0001)
        self.assertLess(abs(pr1.jx0() - 2555) / 2555, 0.0001)
        self.assertLess(abs(pr1.jy0() - 659.73) / 659.73, 0.0001)
        self.assertLess(abs(pr1.alpha() - atan(1)) / 1, 0.0001)
        self.assertLess(abs(pr1.ix0() - 6.997578) / 6.997578, 0.0001)
        self.assertLess(abs(pr1.iy0() - 3.5558) / 3.5558, 0.0001)

        self.assertLess(abs(pr1.hef() - (18 - 1.5 - 1.6)) / 1, 0.0001)
        self.assertLess(abs(pr1.bef() - (18 - 1.5 - 1.6)) / 1, 0.0001)

        self.assertLess(abs(pr1.dx() - 5.01) / 5.01, 0.0001)
        self.assertLess(abs(pr1.dy() - 5.01) / 5.01, 0.0001)

        pr1 = ugol(h=11, b=7, t=0.65, r2=0, r1=1.0, r3=0.33)

        #        print pr1.ix0()
        #        print pr1.dy()
        #
        self.assertLess(abs(pr1.a() - 11.4454) / 11.4454, 0.0001)
        self.assertLess(abs(pr1.jx() - 142.42) / 142.42, 0.0001)
        self.assertLess(abs(pr1.jy() - 45.61) / 45.61, 0.0001)
        self.assertLess(abs(pr1.jxy() + 46.435) / 46.435, 0.0001)
        #        self.assertLess(abs(pr1.jx0()-2555)/2555,0.0001)
        self.assertLess(abs(pr1.jy0() - 26.937) / 26.937, 0.0001)
        self.assertLess(abs(pr1.tanalpha() - 0.40208) / 0.40208, 0.0001)
        #        self.assertLess(abs(pr1.ix0()-6.997578)/6.997578,0.0001)
        self.assertLess(abs(pr1.iy0() - 1.53413) / 1.53413, 0.0001)

        self.assertLess(abs(pr1.hef() - (11 - 0.65 - 1.0)) / 1, 0.0001)
        self.assertLess(abs(pr1.bef() - (7 - 0.65 - 1.0)) / 1, 0.0001)

        self.assertLess(abs(pr1.dx() - 1.58348) / 1.58348, 0.0001)
        self.assertLess(abs(pr1.dy() - 3.545982) / 3.55, 0.0001)

        pr1 = ugol(h=12, b=12, t=0.6, r2=0.9 + 0.6, r1=0.9, r3=0.0)

        #        print pr1.dx()
        #        print pr1.jxy()
        #
        self.assertLess(abs(pr1.a() - 13.73) / 13.73, 0.0001)
        self.assertLess(abs(pr1.jx() - 197.46) / 197.46, 0.0001)
        self.assertLess(abs(pr1.jy() - 197.46) / 197.46, 0.0001)
        #        self.assertLess(abs(pr1.jxy()+346.44)/346.44,0.0001)
        self.assertLess(abs(pr1.jx0() - 320.48) / 320.48, 0.0001)
        self.assertLess(abs(pr1.jy0() - 74.44) / 74.44, 0.0001)
        self.assertLess(abs(pr1.tanalpha() - 1) / 1, 0.0001)
        self.assertLess(abs(pr1.ix0() - 4.83114) / 4.83114, 0.0001)
        self.assertLess(abs(pr1.iy0() - 2.32837) / 2.32837, 0.0001)

        self.assertLess(abs(pr1.hef() - (12 - 0.6 - 0.9)) / 1, 0.0001)
        self.assertLess(abs(pr1.bef() - (12 - 0.6 - 0.9)) / 1, 0.0001)

        self.assertLess(abs(pr1.dx() - 3.293973) / 3.29, 0.0001)
        self.assertLess(abs(pr1.dy() - 3.293973) / 3.29, 0.0001)

        pr1 = ugol(h=6.3, b=4, t=0.4, r2=0, r1=0.7, r3=0.23)

        self.assertEquals(pr1.input_data(), [u"h, см", u"b, см", u"t, см", u"r1, см", u"r2, см", u"r3, см"])

        self.assertEquals(pr1.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'Wx, см3'
            , u'ix, см'
            , u'Jy, см4'
            , u'Wy, см3'
            , u'iy, см'
            , u'Jxy, см4'
            , u'Jx0, см4'
            , u'ix0, см'
            , u'Jy0, см4'
            , u'iy0, см'
            , u'alpha'
            , u'dx, см'
            , u'dy, см'
            , u'title'
            , u'title0'
                                              ])

        self.assertLess(abs(pr1.output_dict()[u'P, кг/м'] - 3.173) / 3.173, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'A, см2'] - 4.042) / 4.042, 0.003)
        #        print pr1.output_dict()[u'Jx, см4']
        self.assertLess(abs(pr1.output_dict()[u'Jx, см4'] - 16.33) / 16.33, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'Wx, см3'] - 3.83) / 3.83, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'ix, см'] - 2.01) / 2.01, 0.003)

        self.assertLess(abs(pr1.output_dict()[u'Jy, см4'] - 5.16) / 5.16, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'Wy, см3'] - 1.67) / 1.67, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'iy, см'] - 1.13) / 1.13, 0.003)

        self.assertLess(abs(pr1.output_dict()[u'Jxy, см4'] + 5.25) / 5.25, 0.003)

        self.assertLess(abs(pr1.output_dict()[u'Jx0, см4'] - 18.42) / 18.42, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'ix0, см'] - 2.13) / 2.13, 0.003)

        self.assertLess(abs(pr1.output_dict()[u'Jy0, см4'] - 3.07) / 3.07, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'iy0, см'] - 0.87) / 0.87, 0.003)

        self.assertLess(abs(pr1.output_dict()[u'alpha'] - 0.37) / 0.37, 0.03)

        self.assertLess(abs(pr1.output_dict()[u'dx, см'] - 0.91) / 0.91, 0.003)
        self.assertLess(abs(pr1.output_dict()[u'dy, см'] - 2.03) / 2.03, 0.003)

        self.assertEquals(pr1.output_dict()[u'title'], u'ugol')

        self.assertEquals(pr1.output_dict()[u'title0'], u'simple')

    def test_shvel(self):
        print 19, "test_shvel"

        pr1 = shvel(27, 9.5, 0.6, 1.05, 1.1, 0.45, 0.0, atan(0.1))

        self.assertEquals(pr1.input_data(),
                          [u"h, см", u"b, см", u"s, см", u"t, см", u"r1, см", u"r2, см", u"r3, см", u"a, %/100"])

        self.assertEquals(pr1.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'Wx, см3'
            , u'Sx, см3'
            , u'ix, см'
            , u'Jy, см4'
            , u'Wy, см3'
            , u'Sy, см3'
            , u'iy, см'
            , u'dx, см'
            , u'Jw, см6'
            , u'Jt, см4'
            , u'Jt_sp2013, см4'
            , u'xa, см'
            , u'w1, см'
            , u'w2, см'
            , u'Ww1, см4'
            , u'Ww2, см4'
            , u'title'
            , u'title0'
                                              ])

        self.assertLess(abs(pr1.output_dict()[u'P, кг/м'] / 7850 * 100 * 100 - 35.2313888) / 35.2313888, 0.0001)

        self.assertLess(abs(pr1.output_dict()[u'A, см2'] - 35.2313888) / 35.2313888, 0.0001)
        self.assertLess(abs(pr1.output_dict()[u'Jx, см4'] - 4163.337068) / 4163.337068, 0.0001)
        self.assertLess(abs(pr1.output_dict()[u'Jy, см4'] - 261.7465238) / 261.7465238, 0.0001)

        self.assertLess(abs(pr1.output_dict()[u'ix, см'] ** 2 * 35.231 - 4163.337068) / 4163.337068, 0.0001)
        self.assertLess(abs(pr1.output_dict()[u'iy, см'] ** 2 * 35.231 - 261.7465238) / 261.7465238, 0.0001)

        self.assertLess(abs(pr1.output_dict()[u'Wx, см3'] * 13.5 - 4163.337068) / 4163.337068, 0.0001)
        self.assertLess(abs(pr1.output_dict()[u'Wy, см3'] * (9.5 - 2.474374) - 261.7465238) / 261.7465238, 0.0001)

        self.assertLess(abs(pr1.output_dict()[u'Wy, см3'] - 37.27) / 37.27, 0.001)

        self.assertLess(abs(pr1.output_dict()[u'Sx, см3'] - 17.6157 * 10.0824) / 177.608, 0.0001)
        self.assertLess(abs(pr1.output_dict()[u'Sy, см3'] - 21.8614 * 1.8719) / 40.922, 0.001)
        self.assertLess(abs(pr1.output_dict()[u'Sy, см3'] - 6.685 * 2 * 3.0632) / 40.922, 0.001)

        self.assertLess(abs(pr1.output_dict()[u'dx, см'] - 2.474374) / 2.47, 0.0001)

        self.assertLess(abs(pr1.output_dict()[u'Jw, см6'] - 30070) / 30070, 0.02)
        self.assertLess(abs(pr1.output_dict()[u'Jt, см4'] - 10.2) / 10.2, 0.002)
        self.assertLess(abs(pr1.output_dict()[u'Jt_sp2013, см4'] - 10.2 / 1.12) / 10.2 * 1.12, 0.002)

        self.assertLess(abs(pr1.output_dict()[u'w1, см'] - 37.8) / 37.8, 0.04)
        self.assertLess(abs(pr1.output_dict()[u'w2, см'] - 78.2) / 78.2, 0.04)

        self.assertLess(abs(pr1.output_dict()[u'Ww1, см4'] - 796.1) / 796.1, 0.02)
        self.assertLess(abs(pr1.output_dict()[u'Ww2, см4'] - 384.6) / 384.6, 0.04)

        self.assertEquals(pr1.output_dict()[u'title'], 'shvel')
        self.assertEquals(pr1.output_dict()[u'title0'], 'simple')

        self.assertLess(abs(pr1.a() - 35.2313888) / 35.2313888, 0.0001)
        self.assertLess(abs(pr1.jx() - 4163.337068) / 4163.337068, 0.0001)
        self.assertLess(abs(pr1.jy() - 261.7465238) / 261.7465238, 0.0001)

        self.assertLess(abs(pr1.dx() - 2.474374) / 2.47, 0.0001)

        self.assertLess(abs(pr1.s2x() - 177.608) / 177.608, 0.0001)
        self.assertLess(abs(pr1.s2y() - 40.9452) / 40.9452, 0.0001)

        self.assertLess(abs(pr1.t1() - 0.605) / .605, 0.0001)
        self.assertLess(abs(pr1.t2() - 0.89) / 0.89, 0.0001)

        self.assertLess(abs(pr1.hef() - 22.02) / 22.02, 0.0001)
        self.assertLess(abs(pr1.bef() - 7.91) / 7.91, 0.0001)

        pr1 = shvel(h=20, b=10, t=0.6, s=0.6, r2=0, r1=0.9, r3=0.9 + 0.6, a1=atan(0.0))

        #        print pr1.jy()
        #        print pr1.jx()
        #        print pr1.dx()

        self.assertLess(abs(pr1.a() - 22.66) / 22.66, 0.0001)
        self.assertLess(abs(pr1.jx() - 1400.82) / 1400.82, 0.0001)
        self.assertLess(abs(pr1.jy() - 224.37) / 224.37, 0.0001)

        self.assertLess(abs(pr1.dx() - 2.794946) / 2.79, 0.0001)

        self.assertLess(abs(pr1.s2x() - 81.64) / 81.64, 0.0001)
        self.assertLess(abs(pr1.s2y() - 31.148) / 31.148, 0.0001)

        self.assertLess(abs(pr1.t1() - 0.6) / .001, 0.0001)
        self.assertLess(abs(pr1.t2() - 0.0) / 0.001, 0.0001)

        self.assertLess(abs(pr1.hef() - 17) / 17, 0.0001)
        self.assertLess(abs(pr1.bef() - 8.5) / 8.5, 0.0001)

        pr1 = shvel(h=30, b=8.5, t=1.35, s=0.75, r2=0.0, r1=0.0, r3=0.0, a1=atan(0.1))

        #        print pr1.jt()

        self.assertLess(abs(pr1.w1() - 37.21) / 37.21, 0.03)
        self.assertLess(abs(pr1.w2() - 76.54) / 76.54, 0.03)

        self.assertLess(abs(pr1.xa() - 2.26) / 2.26, 0.03)

        self.assertLess(abs(pr1.jw() - 36645) / 36645, 0.01)

        self.assertLess(abs(pr1.jt() - 20.39) / 20.39, 0.03)

        pr1 = shvel(h=30, b=10, t=1.1, s=0.65, r2=0.5, r1=1.2, r3=0.0, a1=atan(0.1))

        #        print pr1.jt()
        self.assertLess(abs(pr1.w1() - 43.3) / 43.3, 0.04)
        self.assertLess(abs(pr1.w2() - 92.8) / 92.8, 0.03)
        self.assertLess(abs(pr1.xa() - 2.72) / 2.72, 0.041)

        self.assertLess(abs(pr1.jw() - 45640) / 45640, 0.03)

        self.assertLess(abs(pr1.jt() - 12.8) / 12.8, 0.03)

        self.assertLess(abs(pr1.jt_sp() - 12.8 / 1.12) / 12.8, 0.03)

        self.assertLess(abs(pr1.output_dict()[u'Jw, см6'] - 45640) / 45640, 0.03)

        self.assertLess(abs(pr1.output_dict()[u'Jt, см4'] - 12.8) / 12.8, 0.03)

        self.assertLess(abs(pr1.output_dict()[u'Jt_sp2013, см4'] - 12.8 / 1.12) / 12.8, 0.03)

        pr1 = shvel(h=30, b=10, t=1.1, s=0.65, r2=0.7, r1=1.2, r3=0.0, a1=atan(0.0))

        #        print pr1.jw()
        self.assertLess(abs(pr1.w1() - 46.7) / 46.7, 0.05)
        self.assertLess(abs(pr1.w2() - 93.1) / 93.1, 0.03)
        self.assertLess(abs(pr1.xa() - 2.9) / 2.9, 0.05)

        self.assertLess(abs(pr1.jw() - 59795) / 59795, 0.03)

        self.assertLess(abs(pr1.jt() - 12.8) / 12.8, 0.03)

        self.assertLess(abs(pr1.jt_sp() - 12.8 / 1.12) / 12.8, 0.03)

    def test_sostav(self):
        print 20, "test_sostav"

        pr1 = ugol(h=18, b=18, t=1.5, r2=0, r1=1.6, r3=0.53)
        pr2 = ugol(h=18, b=18, t=1.5, r2=0, r1=1.6, r3=0.53)

        pr = profiles_sostav(pr1=pr1, alpha1=0, x1=0.3, y1=0, mir1=0, pr2=pr2, alpha2=0, x2=-0.3, y2=0, mir2=1)
        pr.solve()
        #        print pr1.jy()
        #        print pr1.jx()
        #        print pr.alpha()

        self.assertLess(abs(pr.a() - 52.18 * 2) / 52.18 / 2, 0.0001)
        self.assertLess(abs(pr.jx() - 1607.36 * 2) / 1607.36 / 2, 0.0001)
        self.assertLess(abs(pr.jy() - 6157.265) / 6157.265, 0.0001)

        self.assertLess(abs(pr.xi() - 0) / 0.001, 0.0001)
        self.assertLess(abs(pr.yi() - 5.01) / 5.01, 0.0001)

        self.assertLess(abs(pr.xi() - 0) / 0.001, 0.0001)
        self.assertLess(abs(pr.yi() - 5.01) / 5.01, 0.0001)

        pr1 = ugol(h=16, b=10, t=1.0, r2=0.0, r1=1.3, r3=0.43)

        pr = profiles_sostav(pr1=pr1, alpha1=pi, x1=0.3, y1=0.3, mir1=0, pr2=pr1, alpha2=0, x2=-0.3 - 2.28 * 2,
                             y2=-0.3 - 5.23 * 2, mir2=0)
        pr.solve()
        #        print pr.jxy()

        self.assertLess(abs(pr.a() - 25.283 * 2) / 25.283 / 2, 0.0001)
        self.assertLess(abs(pr.jx() - 2879.35) / 2879.35, 0.0001)
        self.assertLess(abs(pr.jy() - 744.73) / 744.73, 0.0001)
        self.assertLess(abs(pr.jxy() - 295) / 295, 0.005)

        self.assertLess(abs(pr.y1() - (0.3)) / 0.0001, 0.0001)
        self.assertLess(abs(pr.y2() - (-0.3 - 5.23 * 2)) / 0.0001, 0.005)

        pr = profiles_sostav(pr1=pr1, alpha1=pi / 2, x1=5.23 - 2.28 + .3, y1=-5.23 + 2.28, mir1=0, pr2=pr1,
                             alpha2=-pi / 2, x2=-5.23 + 2.28 - .3, y2=-5.23 + 2.28, mir2=1)
        pr.solve()
        #        print pr.jy()

        self.assertLess(abs(pr.xi() - 0) / 0.001, 0.0001)
        self.assertLess(abs(pr.yi() - 2.2827) / 2.2827, 0.0001)

        self.assertLess(abs(pr.alpha1() - pi / 2) / 0.0001, 0.0001)
        self.assertLess(abs(pr.alpha2() + pi / 2) / 0.0001, 0.0001)
        self.assertLess(abs(pr.x1() - (5.23 - 2.28 + .3)) / 0.0001, 0.0001)
        self.assertLess(abs(pr.x2() - (-5.23 + 2.28 - .3)) / 0.0001, 0.005)
        self.assertLess(abs(pr.y1() - (-5.23 + 2.28)) / 0.0001, 0.0001)
        self.assertLess(abs(pr.y2() - (-5.23 + 2.28)) / 0.0001, 0.005)
        self.assertLess(abs(pr.mir1() - 0) / 0.00001, 0.0001)
        self.assertLess(abs(pr.mir2() - 1) / 0.0001, 0.005)

        self.assertLess(abs(pr.a() - 25.283 * 2) / 25.283 / 2, 0.0001)
        self.assertLess(abs(pr.jx() - 204.09 * 2) / 204.09 / 2, 0.0001)
        self.assertLess(abs(pr.jy() - 2879.35) / 2879.35, 0.001)
        self.assertLess(abs(pr.jxy() - 0) / 0.0001, 0.001)

    def test_sost_ugol_tavr_st_up(self):
        print 21, "test_sost_ugol_tavr_st_up"

        pr = sost_ugol_tavr_st_up(80, 50, 5, 8, 0, 2.7, 10)
        self.assertEquals(pr.bef(), 50.0 - 5 - 8)
        self.assertEquals(pr.hef(), 80.0 - 5 - 8)
        self.assertLess(abs(pr.a() - 1272) / 1272, 0.001)
        self.assertLess(abs(pr.jx() - 832700) / 832700, 0.0001)
        self.assertLess(abs(pr.jy() - 592266) / 592266, 0.0001)
        self.assertLess(abs(pr.xi() - 0) / 0.001, 0.0001)
        self.assertLess(abs(pr.yi() - 26.0) / 26.0, 0.0001)

        pr = sost_ugol_tavr_st_up(h=8, b=6, t=0.6, r1=0.8, r2=0, r3=0.27, dx=1)

        self.assertEquals(pr.input_data(), [u"h, см", u"b, см", u"t, см", u"r1, см", u"r2, см", u"r3, см", u"dx, см"])
        self.assertEquals(pr.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'ix, см'
            , u'Jy, см4'
            , u'iy, см'
            , u'xi, см'
            , u'yi, см'
            , u'Jx0, см4'
            , u'ix0, см'
            , u'Jy0, см4'
            , u'iy0, см'
            , u'alpha'
            , u'title'
            , u'title0'
                                             ])
        self.assertLess(abs(pr.output_dict()[u'P, кг/м'] - 6.395 * 2) / 6.395 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'A, см2'] - 8.146 * 2) / 8.146 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'Jx, см4'] - 52.06 * 2) / 52.06 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'ix, см'] ** 2 * 8.146 * 2 - 52.06 * 2) / 52.06 / 2, 0.001)
        jy = 25.18 * 2 + (0.5 + 1.49) ** 2 * 2 * 8.146
        self.assertLess(abs(pr.output_dict()[u'Jy, см4'] - jy) / jy, 0.001)
        self.assertLess(abs(pr.output_dict()[u'iy, см'] ** 2 * 8.146 * 2 - jy) / jy, 0.001)

        self.assertLess(abs(pr.output_dict()[u'xi, см']), 0.001)

        self.assertLess(abs(pr.output_dict()[u'yi, см'] - 2.47) / 2.47, 0.002)

        self.assertLess(abs(pr.output_dict()[u'Jy0, см4'] - 52.06 * 2) / 52.06 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'iy0, см'] ** 2 * 8.146 * 2 - 52.06 * 2) / 52.06 / 2, 0.001)

        self.assertLess(abs(pr.output_dict()[u'Jx0, см4'] - jy) / jy, 0.001)
        self.assertLess(abs(pr.output_dict()[u'ix0, см'] ** 2 * 8.146 * 2 - jy) / jy, 0.001)

        self.assertEquals(pr.output_dict()[u'alpha'], 0.00)
        self.assertEquals(pr.output_dict()[u'title'], 'ugol_tavr_st_up')
        self.assertEquals(pr.output_dict()[u'title0'], 'sostav')

    def test_sost_ugol_tavr_st_right(self):
        print 22, "test_sost_ugol_tavr_st_right"

        pr = sost_ugol_tavr_st_right(80, 50, 5, 8, 0, 2.7, 10)
        #        print 'pr.yi()',pr.yi()

        self.assertEquals(pr.bef(), 50.0 - 5 - 8)
        self.assertEquals(pr.hef(), 80.0 - 5 - 8)

        self.assertLess(abs(pr.a() - 1272) / 1272, 0.001)
        self.assertLess(abs(pr.jx() - 253600) / 253600, 0.0001)
        self.assertLess(abs(pr.jy() - 2054200) / 2054200, 0.0001)
        self.assertLess(abs(pr.xi() - 0) / 0.0001, 0.0001)

        self.assertLess(abs(pr.yi() - 11.322) / 11.322, 0.0001)

        pr = sost_ugol_tavr_st_right(h=8, b=6, t=0.6, r1=0.8, r2=0, r3=0.27, dx=1)

        self.assertEquals(pr.input_data(), [u"h, см", u"b, см", u"t, см", u"r1, см", u"r2, см", u"r3, см", u"dx, см"])
        self.assertEquals(pr.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'ix, см'
            , u'Jy, см4'
            , u'iy, см'
            , u'xi, см'
            , u'yi, см'
            , u'Jx0, см4'
            , u'ix0, см'
            , u'Jy0, см4'
            , u'iy0, см'
            , u'alpha'
            , u'title'
            , u'title0'
                                             ])

        self.assertLess(abs(pr.output_dict()[u'P, кг/м'] - 6.395 * 2) / 6.395 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'A, см2'] - 8.146 * 2) / 8.146 / 2, 0.001)

        self.assertLess(abs(pr.output_dict()[u'Jx, см4'] - 25.18 * 2) / 25.18 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'ix, см'] ** 2 * 8.146 * 2 - 25.18 * 2) / 25.18 / 2, 0.001)

        jy = 52.06 * 2 + (0.5 + 2.47) ** 2 * 2 * 8.146
        self.assertLess(abs(pr.output_dict()[u'Jy, см4'] - jy) / jy, 0.002)
        self.assertLess(abs(pr.output_dict()[u'iy, см'] ** 2 * 8.146 * 2 - jy) / jy, 0.002)

        self.assertLess(abs(pr.output_dict()[u'xi, см']), 0.001)

        self.assertLess(abs(pr.output_dict()[u'yi, см'] - 1.49) / 1.49, 0.002)

        self.assertLess(abs(pr.output_dict()[u'Jy0, см4'] - 25.18 * 2) / 25.18 / 2, 0.001)
        self.assertLess(abs(pr.output_dict()[u'iy0, см'] ** 2 * 8.146 * 2 - 25.18 * 2) / 25.18 / 2, 0.001)

        self.assertLess(abs(pr.output_dict()[u'Jx0, см4'] - jy) / jy, 0.002)
        self.assertLess(abs(pr.output_dict()[u'ix0, см'] ** 2 * 8.146 * 2 - jy) / jy, 0.002)

        self.assertEquals(pr.output_dict()[u'alpha'], 0.00)
        self.assertEquals(pr.output_dict()[u'title'], 'ugol_tavr_st_right')
        self.assertEquals(pr.output_dict()[u'title0'], 'sostav')

    def test_sost_ugol_tavr_st_krest(self):
        print 23, "test_sost_ugol_tavr_st_krest"

        pr = sost_ugol_tavr_st_krest(80, 50, 5, 8, 0, 2.7, 10, 20)

        self.assertEquals(pr.bef(), 50.0 - 5 - 8)
        self.assertEquals(pr.hef(), 80.0 - 5 - 8)
        #        print 'pr.jx0()',pr.jx0()
        #        print 'pr.jy0()',pr.jy0()
        #        print 'pr.alpha()',pr.alpha()
        self.assertLess(abs(pr.a() - 1272) / 1272, 0.001)
        self.assertLess(abs(pr.jx() - 2480100) / 2480100, 0.0001)
        self.assertLess(abs(pr.jy() - 592300) / 592300, 0.0001)

        self.assertLess(abs(pr.jxy() - 483100) / 483100, 0.0001)

        self.assertLess(abs(pr.xi() - 0) / 0.0001, 0.0001)
        self.assertLess(abs(pr.yi() - 0) / 0.0001, 0.0001)

        self.assertLess(abs(pr.jx0() - 2596951.0526) / 2596951.0526, 0.0002)
        self.assertLess(abs(pr.jy0() - 475821.0692) / 475821.0692, 0.0002)

        self.assertEquals(pr.input_data(),
                          [u"h, см", u"b, см", u"t, см", u"r1, см", u"r2, см", u"r3, см", u"dx, см", u"dy, см"])
        self.assertEquals(pr.output_list(), [u'P, кг/м'
            , u'A, см2'
            , u'Jx, см4'
            , u'ix, см'
            , u'Jy, см4'
            , u'iy, см'
            , u'xi, см'
            , u'yi, см'
            , u'Jx0, см4'
            , u'ix0, см'
            , u'Jy0, см4'
            , u'iy0, см'
            , u'alpha'
            , u'title'
            , u'title0'
                                             ])

        #        print pr.output_dict()[u'P, кг/м']
        self.assertLess(abs(pr.output_dict()[u'P, кг/м'] - 1272. / 100 / 100 * 7850) / (1272. / 100 / 100 * 7850),
                        0.001)
        self.assertLess(abs(pr.output_dict()[u'A, см2'] - 1272) / 1272, 0.001)

        self.assertLess(abs(pr.output_dict()[u'Jx, см4'] - 2480100) / 2480100, 0.001)
        self.assertLess(abs(pr.output_dict()[u'ix, см'] ** 2 * 1272 - 2480100) / 2480100, 0.001)

        self.assertLess(abs(pr.output_dict()[u'Jy, см4'] - 592300) / 592300, 0.001)
        self.assertLess(abs(pr.output_dict()[u'iy, см'] ** 2 * 1272 - 592300) / 592300, 0.001)

        self.assertLess(abs(pr.output_dict()[u'xi, см'] - 0) / 0.0001, 0.0001)
        self.assertLess(abs(pr.output_dict()[u'yi, см'] - 0) / 0.0001, 0.0001)

        self.assertLess(abs(pr.output_dict()[u'Jx0, см4'] - 2596951.0526) / 2596951.0526, 0.001)
        self.assertLess(abs(pr.output_dict()[u'ix0, см'] ** 2 * 1272 - 2596951.0526) / 2596951.0526, 0.001)

        self.assertLess(abs(pr.output_dict()[u'Jy0, см4'] - 475821.0692) / 475821.0692, 0.001)
        self.assertLess(abs(pr.output_dict()[u'iy0, см'] ** 2 * 1272 - 475821.0692) / 475821.0692, 0.001)

        self.assertLess(abs(pr.output_dict()[u'alpha'] + 0.24) / 0.24, 0.02)

        self.assertEquals(pr.output_dict()[u'title'], 'ugol_tavr_st_krest')
        self.assertEquals(pr.output_dict()[u'title0'], 'sostav')

    def test_basa(self):
        print 24, "test_basa"

        inp = [5, 4, 3, 2, 1, 0.5, 0.2, 0.1]
        from basa_sort import BasaSort
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            b = BasaSort()
            data = b.output_data(i, inp)
            x = i
            if x == 0:
                pr = dvut(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
            elif x == 1:
                pr = shvel(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6], inp[7])
            elif x == 2:
                pr = ugol(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5])
            elif x == 3:
                pr = truba_pryam(inp[0], inp[1], inp[2], inp[3], inp[4])
            elif x == 4:
                pr = ring(inp[0], inp[1])
            elif x == 5:
                pr = sost_ugol_tavr_st_up(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
            elif x == 6:
                pr = sost_ugol_tavr_st_right(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
            elif x == 7:
                pr = sost_ugol_tavr_st_krest(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6], inp[7])
            elif x == 8:
                pr = rectangle(inp[0], inp[1])
            self.assertEquals(data.output_dict(), pr.output_dict())


# """Сделать проверку уголка, прямоугольной трубы и обычной трубы по полному списку"""
if __name__ == "__main__":
    unittest.main()
