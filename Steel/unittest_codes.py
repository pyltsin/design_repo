# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:52:37 2013

@author: puma
"""
import unittest

from profiles2 import *
from table import *

pi = 3.14159265358979

from  PyQt4 import QtCore
from steel import *

from codes import *

import basa_sort


class Test_mat(unittest.TestCase):
    def test_mat_steel_new1(self):
        el = dvut(h=400., b=130., t=11., s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        s = steel_snip20107n('C245', el)
        self.assertLess(abs(s.ry() - 2446.5) / 2446.5, 0.00002)
        self.assertLess(abs(s.ryn() - 2497.45) / 2497.45, 0.00002)
        self.assertLess(abs(s.ru() - 3669.72) / 3669.72, 0.00002)
        self.assertLess(abs(s.run() - 3771.66) / 3771.66, 0.00002)
        self.assertLess(abs(s.rs() - 1418.97) / 1418.97, 0.00002)
        self.assertLess(abs(s.rth() - 1834.86) / 1834.86, 0.00002)
        self.assertLess(abs(s.rthf() - 1223.25) / 1223.25, 0.00002)
        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)
        print 1

    def test_mat_steel_new2(self):
        el = dvut(h=400., b=130., t=2.5, s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        s = steel_snip20107n('C245', el, dim=1)
        ryn = 235 * 100 / 9.81
        ry = 230 * 100 / 9.81
        run = 370 * 100 / 9.81
        ru = 360 * 100 / 9.81

        self.assertLess(abs(s.ry() - ry) / ry, 0.00002)
        self.assertLess(abs(s.ryn() - ryn) / ryn, 0.00002)
        self.assertLess(abs(s.ru() - ru) / ru, 0.00002)
        self.assertLess(abs(s.run() - run) / run, 0.00002)
        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)
        print 2

    def test_mat_steel_old1(self):
        el = dvut(h=400., b=130., t=11., s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        s = steel_snip1987('C235', el)

        ryn = 235 * 100 / 9.81
        ry = 230 * 100 / 9.81
        run = 360 * 100 / 9.81
        ru = 350 * 100 / 9.81
        rs = 0.58 * ry
        rth = 0.5 * ru
        rthf = 0.5 * ry

        self.assertLess(abs(s.ry() - ry) / ry, 0.00002)
        self.assertLess(abs(s.ryn() - ryn) / ryn, 0.00002)
        self.assertLess(abs(s.ru() - ru) / ru, 0.00002)
        self.assertLess(abs(s.run() - run) / run, 0.00002)
        self.assertLess(abs(s.rs() - rs) / rs, 0.00002)
        self.assertLess(abs(s.rth() - rth) / rth, 0.00002)
        self.assertLess(abs(s.rthf() - rthf) / rthf, 0.00002)
        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)
        print 3

    def test_mat_steel_old2(self):
        el = dvut(h=400., b=130., t=4.1, s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        s = steel_snip1987('C235', el, dim=1, typ_steel='list')

        ryn = 215 * 100 / 9.81
        ry = 210 * 100 / 9.81
        run = 360 * 100 / 9.81
        ru = 350 * 100 / 9.81

        self.assertLess(abs(s.ry() - ry) / ry, 0.00002)
        self.assertLess(abs(s.ryn() - ryn) / ryn, 0.00002)
        self.assertLess(abs(s.ru() - ru) / ru, 0.00002)
        self.assertLess(abs(s.run() - run) / run, 0.00002)
        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)
        print 4

    def test_mat_steel_old3(self):
        ryn = 235 * 100 / 9.81
        ry = 230 * 100 / 9.81
        run = 360 * 100 / 9.81
        ru = 350 * 100 / 9.81
        rs = 0.58 * ry
        rth = 0.5 * ru
        rthf = 0.5 * ry
        s = steel_general(230, 235, 350, 360)
        self.assertLess(abs(s.ry() - ry) / ry, 0.00002)
        self.assertLess(abs(s.ryn() - ryn) / ryn, 0.00002)
        self.assertLess(abs(s.ru() - ru) / ru, 0.00002)
        self.assertLess(abs(s.run() - run) / run, 0.00002)
        self.assertLess(abs(s.rs() - rs) / rs, 0.00002)
        self.assertLess(abs(s.rth() - rth) / rth, 0.00002)
        self.assertLess(abs(s.rthf() - rthf) / rthf, 0.00002)
        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)
        print 5

    def test_mat_steel_old4(self):
        el = dvut(h=400., b=130., t=11., s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        s = steel_snip1987('C245', el)
        self.assertLess(abs(s.ry() - 2446.5) / 2446.5, 0.00002)
        self.assertLess(abs(s.ryn() - 2497.45) / 2497.45, 0.00002)
        self.assertLess(abs(s.ru() - 3669.72) / 3669.72, 0.00002)
        self.assertLess(abs(s.run() - 3771.66) / 3771.66, 0.00002)
        self.assertLess(abs(s.rs() - 1418.97) / 1418.97, 0.00002)
        self.assertLess(abs(s.rth() - 1834.86) / 1834.86, 0.00002)
        self.assertLess(abs(s.rthf() - 1223.25) / 1223.25, 0.00002)
        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)

        s = steel_snip1987('C345', el)
        self.assertLess(abs(s.ry() - 315 / 9.81 * 100) / 2446.5, 0.00002)
        self.assertLess(abs(s.ryn() - 325 / 9.81 * 100) / 2497.45, 0.00002)
        self.assertLess(abs(s.ru() - 460 / 9.81 * 100) / 3669.72, 0.00002)
        self.assertLess(abs(s.run() - 470 / 9.81 * 100) / 3771.66, 0.00002)

        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)

        el = dvut(h=400., b=130., t=61., s=9.5, r1=14., r2=6., a1=atan(12. / 100))
        s = steel_snip1987('C345', el, typ_steel='list')
        self.assertLess(abs(s.ry() - 270 / 9.81 * 100) / 2446.5, 0.00002)
        self.assertLess(abs(s.ryn() - 275 / 9.81 * 100) / 2497.45, 0.00002)
        self.assertLess(abs(s.ru() - 430 / 9.81 * 100) / 3669.72, 0.00002)
        self.assertLess(abs(s.run() - 440 / 9.81 * 100) / 3771.66, 0.00002)

        self.assertLess(abs(s.mu() - 0.3) / 0.3, 0.00002)
        self.assertLess(abs(s.e() - 2.0999 * 10 ** 6) / (2.0999 * 10 ** 6), 0.00002)
        print 6


class Test_code(unittest.TestCase):
    def test_elements(self):
        pr = dvut(h=600, b=190, t=17.8, s=12., r1=20., r2=08., a1=atan(12. / 100))
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr, mux=100, muy=200, mub=300, lfact=10, br=1, hr=2)

        self.assertEqual(el.lx(), 1000)
        self.assertEqual(el.ly(), 2000)
        self.assertEqual(el.lb(), 3000)
        self.assertEqual(el.lfact(), 10)
        self.assertEqual(el.br(), 1)
        self.assertEqual(el.hr(), 2)
        #        print el.profile.ix()

        self.assertLess(abs(el.lambdax() - 4.23170259) / 4.23170259, 0.00002)
        self.assertLess(abs(el.lambday() - 56.4765) / 56.4765, 0.00002)
        #        print (el.lambdax_())
        self.assertLess(abs(el.lambdax_() - 0.14454) / 0.14454, 0.001)
        self.assertLess(abs(el.lambday_() - 1.9291) / 1.9291, 0.001)
        print 7

    def test_force(self):
        forc = force(n=10, mx=20, my=30, w=40, qx=50, qy=60, t=70, sr=80, floc=90)
        self.assertEqual(forc.n, 10)
        self.assertEqual(forc.mx, 20)
        self.assertEqual(forc.my, 30)
        self.assertEqual(forc.w, 40)
        self.assertEqual(forc.qx, 50)
        self.assertEqual(forc.qy, 60)
        self.assertEqual(forc.t, 70)
        self.assertEqual(forc.sr, 80)
        self.assertEqual(forc.floc, 90)
        print 8


class Test_code_ferma(unittest.TestCase):
    def test_yc(self):
        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.yc()

        self.assertEqual(test, 1)

        sol = snipn(el, forc, [1, 0.95], 0.8)

        self.assertEqual(sol.yc1(), 1)
        self.assertEqual(sol.yc2(), 0.95)
        self.assertEqual(sol.ycb(), 0.8)

        print 9

    def test_yu(self):
        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.yu()

        self.assertEqual(test, 1.3)
        print 10

    def test_phi_n1(self):
        # двутавры        
        pr1 = dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C255', pr1)
        el = elements(s, pr1, mux=1, muy=1, mub=1, lfact=500)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phix()[0] - 0.946) / 0.946, 0.001)
        self.assertLess(abs(sol.phiy()[0] - 0.8579) / 0.8579, 0.001)

        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr, mux=1, muy=1, mub=1, lfact=7000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phiy()[0] - 0.781) / 0.781, 0.0001)
        self.assertLess(abs(sol.phi() - 0.781) / 0.781, 0.0001)

        self.assertLess(abs(sol.phix()[0] - 0.919) / 0.919, 0.0001)

        pr1 = dvut(h=520, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=35000. / 3000, muy=7000. / 3000, mub=1, lfact=3000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phi() - 0.28394) / 0.28394, 0.0001)

        pr1 = dvut(h=520, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=7000, muy=700, mub=1, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.phi() - 0.9654) / 0.9654, 0.0001)

        print 11

    def test_phi_n2(self):
        # короб
        pr1 = truba_pryam(h=500, b=400, t=20, r1=0, r2=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=35000. / 3000, muy=7000. / 3000, mub=1, lfact=3000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phi_n(4.)[0] - 0.475) / 0.475, 0.0001)

        self.assertLess(abs(sol.phi_n(5.)[0] - 0.304) / 0.304, 0.0001)

        self.assertLess(abs(sol.phi_n(3.)[0] - 0.704) / 0.704, 0.001)




        # ugol_tavr_st_up
        pr1 = sost_ugol_tavr_st_up(h=500, b=400, t=20, r1=0, r2=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=35000. / 3000, muy=7000. / 3000, mub=1, lfact=3000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phi_n(4.)[0] - 0.4016) / 0.4016, 0.001)

        self.assertLess(abs(sol.phi_n(5.)[0] - 0.289) / 0.289, 0.001)

        self.assertLess(abs(sol.phi_n(3.)[0] - 0.562) / 0.562, 0.001)

        # ugol_tavr_st_right

        pr1 = sost_ugol_tavr_st_right(h=500, b=400, t=20, r1=0, r2=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=35000. / 3000, muy=7000. / 3000, mub=1, lfact=3000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phi_n(4.)[0] - 0.4016) / 0.4016, 0.001)

        self.assertLess(abs(sol.phi_n(5.)[0] - 0.289) / 0.289, 0.001)

        self.assertLess(abs(sol.phi_n(3.)[0] - 0.562) / 0.562, 0.001)

        # ugol_tavr_st_krest

        pr1 = sost_ugol_tavr_st_krest(h=500, b=400, t=20, r1=0, r2=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=35000. / 3000, muy=7000. / 3000, mub=1, lfact=3000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phi_n(4.)[0] - 0.453) / 0.453, 0.001)

        self.assertLess(abs(sol.phi_n(5.)[0] - 0.304) / 0.304, 0.001)

        self.assertLess(abs(sol.phi_n(3.)[0] - 0.643) / 0.643, 0.001)

        print 12

    def test_phi_n_old1(self):
        pr1 = truba_pryam(h=500, b=400, t=5, r1=0, r2=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=35000. / 3000, muy=7000. / 3000, mub=1, lfact=3000)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phi_n_old(2.) - 0.812) / 0.812, 0.001)

        self.assertLess(abs(sol.phi_n_old(4.) - 0.435) / 0.435, 0.001)

        self.assertLess(abs(sol.phi_n_old(5.) - 0.2887) / 0.2887, 0.001)

        print 13

    def test_phi_n_old2(self):
        pr1 = truba_pryam(h=10, b=6, t=0.6, r1=0.6, r2=1.2)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=0.7, muy=1, mub=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.phix_old() - 0.81) / 0.81, 0.001)

        self.assertLess(abs(sol.phiy_old() - 0.385) / 0.385, 0.0013)

        self.assertLess(abs(sol.phi_old() - 0.385) / 0.385, 0.0013)

        print 14

    def test_q_fic(self):
        pr1 = truba_pryam(h=10, b=6, t=0.6, r1=0.6, r2=1.2)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=0.7, muy=1, mub=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.q_fic(500., 0.5) - 10.25) / 10.25, 0.001)
        self.assertLess(abs(sol.q_fic_old(500., 0.5) - 10.25) / 10.25, 0.001)

        print 15

    def test_local_buckle_h1(self):
        # двутавр
        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr, mux=1, muy=1, lfact=7000)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n()

        self.assertLess(abs(test[0] - 1.44 / 1.9979) / (1.44 / 1.9979), 0.001)
        self.assertLess(abs(test[1] - 1.997905) / 1.997905, 0.0001)
        self.assertLess(abs(test[2] - 1.44116298) / 1.44116298, 0.0001)

        el2 = elements(s, pr, mux=210000, muy=7000, lfact=1)
        sol2 = snipn(el2, forc, 1)
        test = sol2.local_buckl_h_n()
        self.assertLess(abs(test[1] - 2.3) / 2.3, 0.0001)

        el2 = elements(s, pr, mux=7000, muy=5000, lfact=1)
        sol2 = snipn(el2, forc, 1)
        test = sol2.local_buckl_h_n()
        self.assertLess(abs(test[1] - 1.6975) / 1.6975, 0.0001)

        print 16

    def test_local_buckle_h2(self):
        # короб
        pr1 = truba_pryam(h=10, b=6, t=0.6, r1=0.6, r2=1.2)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n()
        #        print test
        self.assertLess(abs(test[0] - 0.2645) / (0.2645), 0.001)
        self.assertLess(abs(test[1] - 1.6) / 1.6, 0.0001)
        self.assertLess(abs(test[2] - 0.4232) / 0.4232, 0.001)

        el2 = elements(s, pr1, mux=1, muy=1, lfact=100)
        sol2 = snipn(el2, forc, 1)
        test = sol2.local_buckl_h_n()
        self.assertLess(abs(test[1] - 1.287) / 1.287, 0.0001)

        el3 = elements(s, pr1, mux=1, muy=1, lfact=30)
        sol2 = snipn(el3, forc, 1)
        test = sol2.local_buckl_h_n()
        self.assertLess(abs(test[1] - 1.2) / 1.2, 0.0001)

        print 17

    def test_local_buckle_h3(self):
        # все, что сделано из уголков
        pr1 = sost_ugol_tavr_st_up(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n()
        #        print test
        self.assertLess(abs(test[0] - 1.08) / (1.08), 0.001)
        self.assertLess(abs(test[1] - 0.58744) / 0.58744, 0.0001)
        self.assertLess(abs(test[2] - 0.635) / 0.635, 0.001)

        el2 = elements(s, pr1, mux=1, muy=1, lfact=3000)
        sol = snipn(el2, forc, 1)
        test = sol.local_buckl_h_n()
        self.assertLess(abs(test[1] - 0.68) / 0.68, 0.0001)

        el3 = elements(s, pr1, mux=1, muy=1, lfact=30)
        sol = snipn(el3, forc, 1)
        test = sol.local_buckl_h_n()
        self.assertLess(abs(test[1] - 0.456) / 0.456, 0.0001)

        pr1 = sost_ugol_tavr_st_right(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n()
        #        print test

        self.assertLess(abs(test[1] - 0.656) / 0.656, 0.001)

        pr1 = sost_ugol_tavr_st_krest(h=10, b=10, t=1, r1=0, r2=0, r3=0, dx=1, dy=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n()
        self.assertLess(abs(test[1] - 0.554) / 0.554, 0.001)

        print 18

    def test_local_buckle_h_old1(self):
        # двутавр
        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr, mux=1, muy=1, lfact=7000)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n_old()

        self.assertLess(abs(test[0] - 1.44 / 1.9979) / (1.44 / 1.9979), 0.001)
        self.assertLess(abs(test[1] - 1.997905) / 1.997905, 0.0001)
        self.assertLess(abs(test[2] - 1.44116298) / 1.44116298, 0.0001)

        el2 = elements(s, pr, mux=210000, muy=7000, lfact=1)
        sol2 = snipn(el2, forc, 1)
        test = sol2.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 2.3) / 2.3, 0.0001)

        el2 = elements(s, pr, mux=7000, muy=5000, lfact=1)
        sol2 = snipn(el2, forc, 1)
        test = sol2.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 1.6975) / 1.6975, 0.0001)

        print 19

    def test_local_buckle_h_old2(self):
        # короб
        pr1 = truba_pryam(h=10, b=6, t=0.6, r1=0.6, r2=1.2)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n_old()
        #        print test
        self.assertLess(abs(test[0] - 0.2645) / (0.2645), 0.001)
        self.assertLess(abs(test[1] - 1.6) / 1.6, 0.0001)
        self.assertLess(abs(test[2] - 0.4232) / 0.4232, 0.001)

        el2 = elements(s, pr1, mux=1, muy=1, lfact=100)
        sol2 = snipn(el2, forc, 1)
        test = sol2.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 1.287) / 1.287, 0.0001)

        el3 = elements(s, pr1, mux=1, muy=1, lfact=30)
        sol2 = snipn(el3, forc, 1)
        test = sol2.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 1.2) / 1.2, 0.0001)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=5000, muy=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_h_n_old()[1] - 1.6) / 1.6, 0.001)

        #        print sol.local_buckl_h_n()[2]     


        print 20

    def test_local_buckl_h_old3(self):
        # все, что сделано из уголков
        pr1 = sost_ugol_tavr_st_up(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n_old()
        #        print test
        self.assertLess(abs(test[0] - 1.08) / (1.08), 0.001)
        self.assertLess(abs(test[1] - 0.58744) / 0.58744, 0.0001)
        self.assertLess(abs(test[2] - 0.635) / 0.635, 0.001)

        el2 = elements(s, pr1, mux=1, muy=1, lfact=3000)
        sol = snipn(el2, forc, 1)
        test = sol.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 0.68) / 0.68, 0.0001)

        el3 = elements(s, pr1, mux=1, muy=1, lfact=30)
        sol = snipn(el3, forc, 1)
        test = sol.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 0.456) / 0.456, 0.0001)

        pr1 = sost_ugol_tavr_st_right(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n_old()
        #        print test

        self.assertLess(abs(test[1] - 0.656) / 0.656, 0.001)

        pr1 = sost_ugol_tavr_st_krest(h=10, b=10, t=1, r1=0, r2=0, r3=0, dx=1, dy=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_h_n_old()
        self.assertLess(abs(test[1] - 0.554) / 0.554, 0.001)

        print 21

    def test_local_buckl_b1(self):
        # двутавр
        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr, mux=7000, muy=7000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()

        self.assertLess(abs(test[1] - 0.5879) / 0.5879, 0.0001)
        self.assertLess(abs(test[2] - 0.333615248) / 0.333615248, 0.0001)

        pr1 = dvut(h=42.0, b=40.0, t=0.4, s=.9, r1=0, r2=0, a1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1000, muy=1000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()
        self.assertLess(abs(test[2] - 1.63) / 1.63, 0.002)

        self.assertLess(abs(test[1] - 0.76) / 0.76, 0.001)
        self.assertLess(abs(test[0] - 2.1488) / 2.1488, 0.001)

        pr1 = dvut(h=42.0, b=40.0, t=4.0, s=.9, r1=0, r2=0, a1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()
        self.assertLess(abs(test[1] - 0.44) / 0.44, 0.001)

        pr1 = dvut(h=42.0, b=40.0, t=0.4, s=.9, r1=0, r2=0, a1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()
        #        print test
        self.assertLess(abs(test[1] - 0.4875) / 0.4875, 0.001)

        print 22

    def test_local_buckl_b2(self):
        # короб        
        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=300, muy=5000, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_b_n()[1] - 1.6) / 1.6, 0.001)

        #        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_b_n()[2] - 0.6306) / 0.6306, 0.001)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=3, muy=50, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_b_n()[1] - 1.2) / 1.2, 0.001)

        #        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_b_n()[2] - 0.6306) / 0.6306, 0.001)

        pr1 = truba_pryam(h=12, b=10, t=1, r2=0, r1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()

        self.assertLess(abs(test[1] - 1.456) / 1.456, 0.001)
        self.assertLess(abs(test[2] - 0.2673) / 0.2673, 0.001)

        pr1 = truba_pryam(h=12, b=10, t=1, r2=0, r1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=3000, muy=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()

        self.assertLess(abs(test[1] - 1.6) / 1.6, 0.001)

        pr1 = truba_pryam(h=12, b=10, t=1, r2=0, r1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=30, muy=30, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()

        self.assertLess(abs(test[1] - 1.2) / 1.2, 0.001)

        print 23

    def test_local_buckle_b3(self):
        # все, что сделано из уголков
        pr1 = sost_ugol_tavr_st_up(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()
        #        print test
        self.assertLess(abs(test[0] - 0.511) / (0.511), 0.002)
        self.assertLess(abs(test[1] - 0.58744) / 0.58744, 0.0001)
        self.assertLess(abs(test[2] - 0.3) / 0.3, 0.003)

        el2 = elements(s, pr1, mux=1, muy=1, lfact=3000)
        sol = snipn(el2, forc, 1)
        test = sol.local_buckl_b_n()
        self.assertLess(abs(test[1] - 0.68) / 0.68, 0.0001)

        el3 = elements(s, pr1, mux=1, muy=1, lfact=30)
        sol = snipn(el3, forc, 1)
        test = sol.local_buckl_b_n()
        self.assertLess(abs(test[1] - 0.456) / 0.456, 0.0001)

        pr1 = sost_ugol_tavr_st_right(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()
        #        print test

        self.assertLess(abs(test[1] - 0.656) / 0.656, 0.001)

        pr1 = sost_ugol_tavr_st_krest(h=10, b=10, t=1, r1=0, r2=0, r3=0, dx=1, dy=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n()
        self.assertLess(abs(test[1] - 0.554) / 0.554, 0.001)

        print 24

    def test_local_buckl_b_old1(self):
        # двутавр
        pr = dvut(h=420, b=400, t=20, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr)
        el = elements(s, pr, mux=7000, muy=7000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()

        self.assertLess(abs(test[1] - 0.5879) / 0.5879, 0.0001)
        self.assertLess(abs(test[2] - 0.333615248) / 0.333615248, 0.0001)

        pr1 = dvut(h=42.0, b=40.0, t=0.4, s=.9, r1=0, r2=0, a1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1000, muy=1000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()
        self.assertLess(abs(test[2] - 1.63) / 1.63, 0.002)

        self.assertLess(abs(test[1] - 0.76) / 0.76, 0.001)
        self.assertLess(abs(test[0] - 2.1488) / 2.1488, 0.001)

        pr1 = dvut(h=42.0, b=40.0, t=4.0, s=.9, r1=0, r2=0, a1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()
        self.assertLess(abs(test[1] - 0.44) / 0.44, 0.001)

        pr1 = dvut(h=42.0, b=40.0, t=0.4, s=.9, r1=0, r2=0, a1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()
        #        print test
        self.assertLess(abs(test[1] - 0.4875) / 0.4875, 0.001)

        print 25

    def test_local_buckl_b_old2(self):
        # короб        
        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=300, muy=5000, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_b_n_old()[1] - 1.6) / 1.6, 0.001)

        #        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_b_n_old()[2] - 0.6306) / 0.6306, 0.001)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=3, muy=50, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_b_n_old()[1] - 1.2) / 1.2, 0.001)

        #        print sol.local_buckl_h_n()[2]     
        self.assertLess(abs(sol.local_buckl_b_n_old()[2] - 0.6306) / 0.6306, 0.001)

        pr1 = truba_pryam(h=12, b=10, t=1, r2=0, r1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()

        self.assertLess(abs(test[1] - (1 + 0.2 * 2.64485)) / (1 + 0.2 * 2.64485), 0.001)
        self.assertLess(abs(test[2] - 0.2673) / 0.2673, 0.001)

        pr1 = truba_pryam(h=12, b=10, t=1, r2=0, r1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=3000, muy=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()

        self.assertLess(abs(test[1] - 1.6) / 1.6, 0.001)

        pr1 = truba_pryam(h=12, b=10, t=1, r2=0, r1=0)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=30, muy=30, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()

        self.assertLess(abs(test[1] - 1.2) / 1.2, 0.001)

        print 26

    def test_local_buckle_b_old3(self):
        # все, что сделано из уголков
        pr1 = sost_ugol_tavr_st_up(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()
        #        print test
        self.assertLess(abs(test[0] - 0.511) / (0.511), 0.002)
        self.assertLess(abs(test[1] - 0.58744) / 0.58744, 0.0001)
        self.assertLess(abs(test[2] - 0.3) / 0.3, 0.003)

        el2 = elements(s, pr1, mux=1, muy=1, lfact=3000)
        sol = snipn(el2, forc, 1)
        test = sol.local_buckl_b_n()
        self.assertLess(abs(test[1] - 0.68) / 0.68, 0.0001)

        el3 = elements(s, pr1, mux=1, muy=1, lfact=30)
        sol = snipn(el3, forc, 1)
        test = sol.local_buckl_b_n_old()
        self.assertLess(abs(test[1] - 0.456) / 0.456, 0.0001)

        pr1 = sost_ugol_tavr_st_right(h=20, b=10, t=1, r1=0, r2=0, r3=0, dx=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()
        #        print test

        self.assertLess(abs(test[1] - 0.656) / 0.656, 0.001)

        pr1 = sost_ugol_tavr_st_krest(h=10, b=10, t=1, r1=0, r2=0, r3=0, dx=1, dy=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1, muy=1, lfact=300)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_n_old()
        self.assertLess(abs(test[1] - 0.554) / 0.554, 0.001)

        print 27

    def test_basasort_output_simple_ferm(self):
        basa = basa_sort.BasaSort()

        code = QtCore.QString(u'СНиП II-23-81*')
        type_element = QtCore.QString(u'Ферма')
        typ_sec = QtCore.QString(u'Двутавр')
        gost = QtCore.QString(u"СТО АСЧМ 20-93 (К) Двутавры с параллельными полками")
        num_sect = QtCore.QString(u'40 К1')
        stl = QtCore.QString(u'C345')
        inp = [1, 1, 300, 3, 2]
        check = basa.output_simple(code, type_element, typ_sec, gost, num_sect, stl, inp)

        ry = 315 * 100 / 9.81
        a = 186.8
        phix = 0.813
        phiy = 0.77
        ru = 460 * 100 / 9.81
        e = 2.1 * 10 ** 6
        # дальше подряд все 24 штуки - проверка по старому снип
        un = check[0][0]
        res = phiy * ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = 0.628
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru * a / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 14093.9 / 9.81 * 1000 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[8][0]
        res = 10685 / 9.81 * 1000 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[10][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[11][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[16][0]
        res = 186.8
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[17][0]
        res = (56150 / 186.8) ** 0.5
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[18][0]
        res = (18920 / 186.8) ** 0.5
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[19][0]
        res = 51.9
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[20][0]
        res = 59.6
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[21][0]
        res = 0.554
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[22][0]
        res = 2.02
        self.assertLess(abs(un - res) / res, 0.0021)

        un = check[23][0]
        res = 1.12
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[24][0]
        res = 0.628
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[25][0]
        res = 0.59
        self.assertLess(abs(un - res) / res, 0.006)

        un = check[26][0]
        res = 0.37
        self.assertLess(abs(un - res) / res, 0.007)

        code = QtCore.QString(u'СП16.13330.2011')
        type_element = QtCore.QString(u'Ферма')
        typ_sec = QtCore.QString(u'Двутавр')
        gost = QtCore.QString(u"ГОСТ 26020-83 (Б) Двутавры с параллельными полками")
        num_sect = QtCore.QString(u'10Б1')
        stl = QtCore.QString(u'C255')
        inp = [1, 2, 100, 2, 1]
        check = basa.output_simple(code, type_element, typ_sec, gost, num_sect, stl, inp)

        ry = 240 * 100 / 9.81
        a = 10.32
        phix = 0.871
        phiy = 0.694
        ru = 360 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phiy * ry * a * 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = 0.287
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = 'b'
        self.assertEqual(un, res)

        un = check[6][0]
        res = 'b'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru * a / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 869.3 / 9.81 * 1000 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = 323.7 / 9.81 * 1000 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[11][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[14][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[18][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[19][0]
        res = (171 / 10.32) ** 0.5
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[20][0]
        res = (16 / 10.32) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[21][0]
        res = 49.1
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[22][0]
        res = 80.5
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[23][0]
        res = 0.287
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = 2.16
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[25][0]
        res = 0.62
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[26][0]
        res = 0.174
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[27][0]
        res = 0.6348
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[28][0]
        res = 0.1105
        self.assertLess(abs(un - res) / res, 0.001)

        print 28

    def test_ferma_output_data_all_snip_old(self):
        # проверка двутавров по старому снипу

        pr1 = dvut(10.0, 5.5, 0.45, 0.72, 0.7, 0.25, 0.119428926)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=0.5, muy=1.0, mub=1, lfact=500)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.95])
        check = sol.output_data_all_snip_old()

        ry = 230 * 100 / 9.81
        a = 12.05
        phix = 0.803
        phiy = 0.047
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phiy * ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = 0.226
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[5][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru / 1.3 * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 645.1 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = 14.5 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.95 / phix
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[10][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[11][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[16][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[17][0]
        res = (198 / 12.05) ** 0.5
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[18][0]
        res = (18 / 12.05) ** 0.5
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[19][0]
        res = 61.6
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[20][0]
        res = 410.61
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[21][0]
        res = 0.226
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = 2.3
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[23][0]
        res = 0.52
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[24][0]
        res = 0.116
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[25][0]
        res = 0.76
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[26][0]
        res = 0.0885
        self.assertLess(abs(un - res) / res, 0.004)

        # проверка трубы по старому снипу

        pr1 = truba_pryam(40.0, 20.0, 1.2, 2.4, 3.6)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=1., muy=0.5, mub=1, lfact=500)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.95])
        check = sol.output_data_all_snip_old()

        #        print 'l', el.lambdax_(),  el.lambday_()
        ry = 230 * 100 / 9.81
        a = 132.01
        phix = 0.914
        phiy = 0.932
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phix * ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = (40 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (1 + 0.2 * 1.1848)
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 21348 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[8][0]
        res = 29202 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[9][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[10][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phix * ry * a * 0.95 / phiy
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[11][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = 132.1
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = (26250 / 132.1) ** .5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[18][0]
        res = (8977 / 132.1) ** .5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[19][0]
        res = 35.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[20][0]
        res = 30.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[21][0]
        res = (40 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (1 + 0.2 * 1.1848)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[22][0]
        res = (1 + 0.2 * 1.1848)
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[23][0]
        res = (40 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[24][0]
        res = (20 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5 / 1.237
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[25][0]
        res = 1.0 + 0.2 * 35.465 * (ry / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[26][0]
        res = (20 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        # тавр с полками вверх


        pr1 = sost_ugol_tavr_st_up(10.0, 6.3, 0.6, 1.0, 0.0, 0.33, 1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=0.8, muy=0.9, mub=1, lfact=300)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.8])
        check = sol.output_data_all_snip_old()

        ry = 230 * 100 / 9.81
        a = 9.59 * 2
        lambda_x = 0.8 * 300 / 3.2
        lambda_y = 0.9 * 300 / 2.62
        phix = 0.736
        phiy = 0.536
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phiy * ry * a * 0.8 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 3.14 * 3.14 * e * 196.85 / (0.8 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[8][0]
        res = 3.14 * 3.14 * e * 131.88 / (0.9 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[9][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[10][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phiy
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[11][0]
        res = 80 * 1.79
        #        print res, un
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = 40 * 1.79
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[18][0]
        res = 2.62
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[19][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[20][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[21][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[22][0]
        res = 0.4 + 0.07 * lambda_y * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[23][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[24][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[25][0]
        res = 0.4 + 0.07 * lambda_y * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[26][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        # тавр с полками вбок

        pr1 = sost_ugol_tavr_st_right(10.0, 6.3, 0.6, 1.0, 0.0, 0.33, 1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=0.8, muy=0.9, mub=1, lfact=300)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.8])
        check = sol.output_data_all_snip_old()

        ry = 230 * 100 / 9.81
        a = 9.59 * 2
        lambda_x = 0.8 * 300 / 1.786
        lambda_y = 0.9 * 300 / 4.91
        phix = 0.356
        phiy = 0.834
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phix * ry * a * 0.8 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / 0.68
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[5][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 3.14 * 3.14 * e * 61.17 / (0.8 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[8][0]
        res = 3.14 * 3.14 * e * 463.22 / (0.9 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[9][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phix * ry * a * 0.8 / phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[10][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phix * ry * a * 0.8 / phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[11][0]
        res = 80 * 1.79
        #        print res, un
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = 40 * 1.79
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = 1.79
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[18][0]
        res = 4.91
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[19][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[20][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[21][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / 0.68
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[22][0]
        res = 0.68
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[23][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[24][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / 0.68
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[25][0]
        res = 0.68
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[26][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)


        # крест

        pr1 = sost_ugol_tavr_st_krest(10.0, 6.3, 0.6, 1.0, 0.0, 0.33, 1, 1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=0.8, muy=0.9, mub=1, lfact=300)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.8])
        check = sol.output_data_all_snip_old()

        ry = 230 * 100 / 9.81
        a = 9.59 * 2
        lambda_x = 0.8 * 300 / 4.91
        lambda_y = 0.9 * 300 / 2.62
        phix = 0.861
        phiy = 0.536
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6
        ix = 4.91
        iy = 2.62

        un = check[0][0]
        res = phiy * ry * a * 0.8 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[5][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 3.14 * 3.14 * e * ix ** 2 * a / (0.8 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[8][0]
        res = 3.14 * 3.14 * e * iy ** 2 * a / (0.9 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[9][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[10][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[11][0]
        res = 80 * 1.38
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = 40 * 1.38
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ix
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[18][0]
        res = iy
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[19][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[20][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[21][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[22][0]
        res = (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[23][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[24][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[25][0]
        res = (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[26][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        print 29

    def test_ferma_output_data_all_snip_n(self):
        # проверка двутавров по новому снипу

        pr1 = dvut(60.0, 19.0, 1.2, 1.78, 2.0, 0.8, 0.119428926)
        s = steel_snip20107n('C375', pr1, 1)
        el = elements(s, pr1, mux=1., muy=0.5, mub=1, lfact=500)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.95, 0.9])
        check = sol.output_data_all_snip_n()

        ry = 345 * 100 / 9.81
        a = 137.5
        phix = 0.96
        phiy = 0.665
        ru = 480 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phiy * ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = .80
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[5][0]
        res = 'b'
        self.assertEqual(un, res)

        un = check[6][0]
        res = 'b'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru / 1.3 * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 62466 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.0011)

        un = check[10][0]
        res = 5611 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.0011)

        un = check[12][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.9 / phiy
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[11][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[14][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[18][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[19][0]
        res = (76810 / 137.5) ** 0.5
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[20][0]
        res = (1725 / 137.5) ** 0.5
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 21.2
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[22][0]
        res = 70.6
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[23][0]
        res = 0.80
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[24][0]
        res = 2.21
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[25][0]
        res = 1.77
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[26][0]
        res = 0.253
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[27][0]
        res = 0.6489
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[28][0]
        res = 0.16411
        self.assertLess(abs(un - res) / res, 0.004)

        # проверка трубы по новому снипу

        pr1 = truba_pryam(40.0, 20.0, 1.2, 2.4, 3.6)
        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=1., muy=0.5, mub=1, lfact=500)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.95])
        check = sol.output_data_all_snip_n()

        #        print 'l', el.lambdax_(),  el.lambday_()
        ry = 320 * 100 / 9.81
        a = 132.01
        phix = 0.938
        phiy = 0.954
        ru = 460 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phix * ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = (40 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5 / 1.239
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = u'a'
        self.assertEqual(un, res)

        un = check[6][0]
        res = u'a'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 21348 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[10][0]
        res = 29202 * 1000 / 9.81 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[11][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phix * ry * a * 0.95 / phiy
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[13][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[14][0]
        res = u'-'
        self.assertEqual(un, res)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[18][0]
        res = 132.1
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[19][0]
        res = (26250 / 132.1) ** .5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[20][0]
        res = (8977 / 132.1) ** .5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[21][0]
        res = 35.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[22][0]
        res = 30.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[23][0]
        res = (40 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5 / 1.239
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[24][0]
        res = 1.0 + 0.2 * 30.322 * (ry / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[25][0]
        res = (40 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[26][0]
        res = (20 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5 / 1.28
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[27][0]
        res = 1.0 + 0.2 * 35.465 * (ry / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[28][0]
        res = (20 - 1.2 - 1.2 - 2.4 - 2.4) / 1.2 * (ry / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)


        # тавр с полками вверх


        pr1 = sost_ugol_tavr_st_up(10.0, 6.3, 0.6, 1.0, 0.0, 0.33, 1)
        s = steel_snip20107n('C235', pr1, 1)
        el = elements(s, pr1, mux=0.8, muy=0.9, mub=1, lfact=300)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.8])
        check = sol.output_data_all_snip_n()

        ry = 230 * 100 / 9.81
        a = 9.59 * 2
        lambda_x = 0.8 * 300 / 3.2
        lambda_y = 0.9 * 300 / 2.62
        phix = 0.653
        phiy = 0.486
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phiy * ry * a * 0.8 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = u'c'
        self.assertEqual(un, res)

        un = check[6][0]
        res = u'c'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 3.14 * 3.14 * e * 196.85 / (0.8 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[10][0]
        res = 3.14 * 3.14 * e * 131.88 / (0.9 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[11][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[12][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phiy
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[13][0]
        res = 80 * 1.79
        #        print res, un
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[14][0]
        res = 40 * 1.79
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[18][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[19][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[20][0]
        res = 2.62
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[21][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[22][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[23][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[24][0]
        res = 0.4 + 0.07 * lambda_y * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[25][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[26][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[27][0]
        res = 0.4 + 0.07 * lambda_y * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[28][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        # тавр с полками вбок

        pr1 = sost_ugol_tavr_st_right(10.0, 6.3, 0.6, 1.0, 0.0, 0.33, 1)
        s = steel_snip20107n('C235', pr1, 1)
        el = elements(s, pr1, mux=0.8, muy=0.9, mub=1, lfact=300)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.8])
        check = sol.output_data_all_snip_n()

        ry = 230 * 100 / 9.81
        a = 9.59 * 2
        lambda_x = 0.8 * 300 / 1.786
        lambda_y = 0.9 * 300 / 4.91
        phix = 0.341
        phiy = 0.772
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phix * ry * a * 0.8 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / 0.68
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[5][0]
        res = u'c'
        self.assertEqual(un, res)

        un = check[6][0]
        res = u'c'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 3.14 * 3.14 * e * 61.17 / (0.8 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[10][0]
        res = 3.14 * 3.14 * e * 463.22 / (0.9 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[11][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phix * ry * a * 0.8 / phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[12][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phix * ry * a * 0.8 / phiy
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[13][0]
        res = 80 * 1.79
        #        print res, un
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[14][0]
        res = 40 * 1.79
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[18][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[19][0]
        res = 1.79
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[20][0]
        res = 4.91
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[21][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[22][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[23][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / 0.68
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[24][0]
        res = 0.68
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[25][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[26][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / 0.68
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[27][0]
        res = 0.68
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[28][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)


        # крест

        pr1 = sost_ugol_tavr_st_krest(10.0, 6.3, 0.6, 1.0, 0.0, 0.33, 1, 1)
        s = steel_snip20107n('C235', pr1, 1)
        el = elements(s, pr1, mux=0.8, muy=0.9, mub=1, lfact=300)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = ferma(el, forc, [0.9, 0.8])
        check = sol.output_data_all_snip_n()

        ry = 230 * 100 / 9.81
        a = 9.59 * 2
        lambda_x = 0.8 * 300 / 4.91
        lambda_y = 0.9 * 300 / 2.62
        phix = 0.877
        phiy = 0.554
        ru = 350 * 100 / 9.81
        e = 2.1 * 10 ** 6
        ix = 4.91
        iy = 2.62

        un = check[0][0]
        res = phiy * ry * a * 0.8 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[5][0]
        res = u'b'
        self.assertEqual(un, res)

        un = check[6][0]
        res = u'b'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a * 0.9 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru * a * 0.9 / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 3.14 * 3.14 * e * ix ** 2 * a / (0.8 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = 3.14 * 3.14 * e * iy ** 2 * a / (0.9 * 300) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[11][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phix
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[12][0]
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * phiy * ry * a * 0.8 / phiy
        self.assertLess(abs(un - res) / res, 0.0015)

        un = check[13][0]
        res = 80 * 1.38
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[14][0]
        res = 40 * 1.38
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[18][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[19][0]
        res = ix
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[20][0]
        res = iy
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[21][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[22][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[23][0]
        res = (10. - 0.6 - 1.) / 0.6 * (ry / 2.1 / 10 ** 6) ** 0.5 / (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[24][0]
        res = (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[25][0]
        res = (10 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[26][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5 / (
            0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[27][0]
        res = (0.4 + 0.07 * lambda_y * (ry / e) ** 0.5)
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[28][0]
        res = (6.3 - 0.6 - 1.) / 0.6 * (230 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        self.assertLess(abs(un - res) / res, 0.003)

        print 30


class Test_code_beam(unittest.TestCase):
    def test_local_buckl_h_m(self):
        pr = dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        test = sol.local_buckl_h_m()

        ch = 5.173 / 3.2
        self.assertLess(abs(test[0] - ch) / ch, 0.0001)
        self.assertLess(abs(test[1] - 3.2) / 3.2, 0.0001)
        self.assertLess(abs(test[2] - 5.173) / 5.173, 0.0001)

        pr1 = dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C255', pr1)
        el = elements(s, pr1, mux=10000, muy=300, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=500 * 1000 / 9.81 * 100, my=500 * 1000 / 9.81 * 100, qx=100 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_h_m(1, 1)[1] - 3.2) / 3.2, 0.001)
        self.assertLess(abs(sol.local_buckl_h_m(1, 2)[1] - 2.2) / 2.2, 0.001)

        self.assertLess(abs(sol.local_buckl_h_m(2, 1)[1] - 3.5) / 3.2, 0.001)
        self.assertLess(abs(sol.local_buckl_h_m(2, 2)[1] - 2.5) / 2.2, 0.001)

        print 31

    def test_local_buckl_h_m_old(self):
        pr = dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        test = sol.local_buckl_h_m_old()

        ch = 5.173 / 3.2
        self.assertLess(abs(test[0] - ch) / ch, 0.0001)
        self.assertLess(abs(test[1] - 3.2) / 3.2, 0.0001)
        self.assertLess(abs(test[2] - 5.173) / 5.173, 0.0001)

        pr1 = dvut(h=40, b=40, t=2, s=2, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C255', pr1)
        el = elements(s, pr1, mux=10000, muy=300, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=500 * 1000 / 9.81 * 100, my=500 * 1000 / 9.81 * 100, qx=100 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.local_buckl_h_m_old(1, 1)[1] - 3.2) / 3.2, 0.001)
        self.assertLess(abs(sol.local_buckl_h_m_old(1, 2)[1] - 2.2) / 2.2, 0.001)

        self.assertLess(abs(sol.local_buckl_h_m_old(2, 1)[1] - 3.5) / 3.2, 0.001)
        self.assertLess(abs(sol.local_buckl_h_m_old(2, 2)[1] - 2.5) / 2.2, 0.001)

        print 32

    def test_local_buckl_b_m(self):
        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=300, muy=5000, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        ch = 0.6306 / 1.5
        self.assertLess(abs(sol.local_buckl_b_m()[0] - ch) / ch, 0.001)
        self.assertLess(abs(sol.local_buckl_b_m()[1] - 1.5) / 1.5, 0.001)
        self.assertLess(abs(sol.local_buckl_b_m()[2] - 0.6306) / 0.6306, 0.001)

        pr = dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=10)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_m()

        ch = 0.4572 / 0.5
        self.assertLess(abs(test[0] - ch) / ch, 0.0001)
        self.assertLess(abs(test[1] - 0.5) / 0.5, 0.0001)
        self.assertLess(abs(test[2] - 0.4572) / 0.4572, 0.0001)

        pr = shvel(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=10)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_m()

        l = (240 - 8.) / 10. * (320 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        ch = l / 0.5
        #        print test
        self.assertLess(abs(test[0] - ch) / ch, 0.0001)
        self.assertLess(abs(test[1] - 0.5) / 0.5, 0.0001)
        self.assertLess(abs(test[2] - l) / l, 0.0001)

        print 33

    def test_local_buckl_b_m_old(self):
        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)

        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mux=300, muy=5000, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=500 * 1000 / 9.81)
        sol = snipn(el, forc, 1)

        ch = 0.6306 / 1.5
        self.assertLess(abs(sol.local_buckl_b_m_old()[0] - ch) / ch, 0.001)
        self.assertLess(abs(sol.local_buckl_b_m_old()[1] - 1.5) / 1.5, 0.001)
        self.assertLess(abs(sol.local_buckl_b_m_old()[2] - 0.6306) / 0.6306, 0.001)

        pr = dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=10)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_m_old()

        ch = 0.4572 / 0.5
        self.assertLess(abs(test[0] - ch) / ch, 0.0001)
        self.assertLess(abs(test[1] - 0.5) / 0.5, 0.0001)
        self.assertLess(abs(test[2] - 0.4572) / 0.4572, 0.0001)

        pr = shvel(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=10)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.local_buckl_b_m_old()

        l = (240 - 8.) / 10. * (320 * 100 / 9.81 / 2.1 / 10 ** 6) ** 0.5
        ch = l / 0.5
        #        print test
        self.assertLess(abs(test[0] - ch) / ch, 0.0001)
        self.assertLess(abs(test[1] - 0.5) / 0.5, 0.0001)
        self.assertLess(abs(test[2] - l) / l, 0.0001)

        print 34

    def test_cxcyn(self):
        # двутавр
        pr = dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.cxcyn()[1] - 1.47) / 1.47, 0.0001)
        self.assertLess(abs(sol.cxcyn()[2] - 1.5) / 1.5, 0.0001)

        self.assertLess(abs(sol.cxcyn()[0] - 1.18) / 1.18, 0.0001)

        pr1 = dvut(h=520, b=400, t=10, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.08111) / 1.08111, 0.0001)

        pr1 = dvut(h=520, b=1500, t=5, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.05) / 1.05, 0.001)



        # короб
        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.08176) / 1.08176, 0.0001)
        self.assertLess(abs(sol.cxcyn()[1] - 1.1735) / 1.1735, 0.0001)
        self.assertLess(abs(sol.cxcyn()[2] - 1.5) / 1.5, 0.0001)

        pr1 = truba_pryam(h=8, b=24, t=0.6, r2=1.2, r1=0.6)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.0471) / 1.0471, 0.0001)
        self.assertLess(abs(sol.cxcyn()[1] - 1.2435) / 1.2435, 0.0001)
        self.assertLess(abs(sol.cxcyn()[2] - 1.5) / 1.5, 0.0001)

        pr1 = truba_pryam(h=8, b=6, t=0.6, r2=1.2, r1=0.6)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.1365) / 1.1365, 0.0001)
        self.assertLess(abs(sol.cxcyn()[1] - 1.108235) / 1.108235, 0.0001)
        self.assertLess(abs(sol.cxcyn()[2] - 1.5) / 1.5, 0.0001)


        # швеллер
        pr1 = shvel(h=15, b=10, t=0.5, s=1, r1=0, r2=0, a1=0)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.148) / 1.148, 0.0001)
        self.assertLess(abs(sol.cxcyn()[1] - 1.6) / 1.6, 0.0001)
        self.assertLess(abs(sol.cxcyn()[2] - 1.0) / 1.0, 0.0001)

        pr1 = shvel(h=7.5, b=10, t=0.5, s=1, r1=0, r2=0, a1=0)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn()[0] - 1.085) / 1.09, 0.001)
        self.assertLess(abs(sol.cxcyn()[1] - 1.6) / 1.6, 0.0001)
        self.assertLess(abs(sol.cxcyn()[2] - 1.0) / 1.0, 0.0001)

        print 35

    def test_cxcyn2(self):
        # двутавр
        pr = dvut(h=1070, b=240, t=10, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr)
        el = elements(s, pr, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.cxcyn_old()[1] - 1.47) / 1.47, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[2] - 1.5) / 1.5, 0.0001)

        self.assertLess(abs(sol.cxcyn_old()[0] - 1.18) / 1.18, 0.0001)

        pr1 = dvut(h=520, b=400, t=10, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.08111) / 1.08111, 0.0001)

        pr1 = dvut(h=520, b=1500, t=5, s=9, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=7000, muy=7000, mub=3000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.05) / 1.05, 0.001)



        # короб
        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.08176) / 1.08176, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[1] - 1.1735) / 1.1735, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[2] - 1.5) / 1.5, 0.0001)

        pr1 = truba_pryam(h=8, b=24, t=0.6, r2=1.2, r1=0.6)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.0471) / 1.0471, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[1] - 1.2435) / 1.2435, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[2] - 1.5) / 1.5, 0.0001)

        pr1 = truba_pryam(h=8, b=6, t=0.6, r2=1.2, r1=0.6)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.1365) / 1.1365, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[1] - 1.108235) / 1.108235, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[2] - 1.5) / 1.5, 0.0001)


        # швеллер
        pr1 = shvel(h=15, b=10, t=0.5, s=1, r1=0, r2=0, a1=0)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.148) / 1.148, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[1] - 1.6) / 1.6, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[2] - 1.0) / 1.0, 0.0001)

        pr1 = shvel(h=7.5, b=10, t=0.5, s=1, r1=0, r2=0, a1=0)
        el = elements(s, pr1, mux=10, muy=10, mub=300, lfact=1)
        forc = force(n=200 * 1000 / 9.81, mx=1 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100, qx=00 * 1000 / 9.81)
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.cxcyn_old()[0] - 1.085) / 1.09, 0.001)
        self.assertLess(abs(sol.cxcyn_old()[1] - 1.6) / 1.6, 0.0001)
        self.assertLess(abs(sol.cxcyn_old()[2] - 1.0) / 1.0, 0.0001)

        print 36

    def test_phib(self):
        pr1 = dvut(h=520, b=200, t=20, s=8, r1=0, r2=0, a1=0, title2='svar')

        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=7000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        # тип: 1 - балка, 2 -консиль
        # тип 1: 1- без закреплений, 2 - два и более, 3 - один по центру
        # тип 2: 1-сосредоточенная, 2 - сосредоточенная в четверти, 3 - равномерная
        # тип 3: 1- сжатый, 2 - расстянутый
        self.assertLess(abs(sol.psib(0.319, 1, 1, 1) - 1.7787) / 1.7787, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 1, 1, 2) - 5.0787) / 5.0787, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 1, 2, 1) - 1.7787) / 1.7787, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 1, 2, 2) - 5.0787) / 5.0787, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 1, 3, 1) - 1.62552) / 1.62552, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 1, 3, 2) - 3.8255) / 3.8255, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 2, 1, 1) - 2.27233) / 2.27233, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 3, 1, 1) - 3.9765775) / 3.9765775, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 3, 2, 1) - 2.590456) / 2.590456, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 3, 2, 2) - 3.635728) / 3.635728, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 3, 3, 1) - 2.590456) / 2.590456, 0.0001)
        self.assertLess(abs(sol.psib(0.319, 3, 3, 2) - 2.95403) / 2.95403, 0.0001)

        self.assertLess(abs(sol.psib(300, 1, 1, 1) - 15.15) / 15.15, 0.0001)
        self.assertLess(abs(sol.psib(300, 1, 1, 2) - 18.45) / 18.45, 0.0001)
        self.assertLess(abs(sol.psib(300, 1, 2, 1) - 15.15) / 15.15, 0.0001)
        self.assertLess(abs(sol.psib(300, 1, 2, 2) - 18.45) / 18.45, 0.0001)
        self.assertLess(abs(sol.psib(300, 1, 3, 1) - 12.72) / 12.72, 0.0001)
        self.assertLess(abs(sol.psib(300, 1, 3, 2) - 14.92) / 14.92, 0.0001)
        self.assertLess(abs(sol.psib(300, 2, 1, 1) - 12.45) / 12.45, 0.0001)
        self.assertLess(abs(sol.psib(300, 3, 1, 1) - 21.7875) / 21.7875, 0.0001)
        self.assertLess(abs(sol.psib(300, 3, 2, 1) - 14.193) / 14.193, 0.0001)
        self.assertLess(abs(sol.psib(300, 3, 2, 2) - 19.92) / 19.92, 0.0001)
        self.assertLess(abs(sol.psib(300, 3, 3, 1) - 14.193) / 14.193, 0.0001)
        self.assertLess(abs(sol.psib(300, 3, 3, 2) - 16.185) / 16.185, 0.0001)


        # тип 2: 4 - на конце консоли, 3 - равномерная
        # тип 3: 1- сжатый, 2 - расстянутый

        self.assertLess(abs(sol.psik(10, 1, 1) - 7) / 7, 0.0001)
        self.assertLess(abs(sol.psik(10, 1, 2) - 2.6) / 2.6, 0.0001)
        self.assertLess(abs(sol.psik(10, 3, 2) - 4.4904343) / 4.4904343, 0.0001)
        self.assertLess(abs(sol.psik(50, 1, 1) - 9.5) / 9.5, 0.0001)
        self.assertLess(abs(sol.psik(50, 1, 2) - 6.5) / 6.5, 0.0001)

        #        print (pr1.jy()/pr1.jx())
        #        print sol.phi_b(2,1,4,1)
        self.assertLess(abs(sol.phi_b(1, 1, 1, 1)[0] - 0.583120178122) / 0.583120178122, 0.0001)

        self.assertLess(abs(sol.phi_b(2, 1, 1, 1)[0] - 0.94089102707) / 0.94089102707, 0.001)



        # двутавр, старый снип        
        pr1 = dvut(h=52, b=20, t=2, s=.8, r1=0, r2=0, a1=0, title2='svar')

        s = steel_snip1987('C255', pr1, dim=1)
        el = elements(s, pr1, mux=7000, muy=700, mub=800, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.phi_b_old(1, 1, 3, 1)[0]
        check = 0.525
        self.assertLess(abs(test - check) / check, 0.001)

        pr1 = dvut(39.6, 19.9, 0.7, 1.1, 1.6, 0.0, 0.0)

        s = steel_snip1987('C255', pr1, dim=1)
        el = elements(s, pr1, mux=7000, muy=700, mub=800, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.phi_b_old(1, 1, 3, 1)[0]
        check = 0.393
        self.assertLess(abs(test - check) / check, 0.003)


        # короб, старый снип        

        pr1 = truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)

        s = steel_snip1987('C255', pr1, dim=1)
        el = elements(s, pr1, mux=7000, muy=700, mub=800, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        test = sol.phi_b_old(1, 1, 3, 1)
        self.assertEqual(test, [1, 1, 1, 0])

        # швеллер 
        pr1 = shvel(30.0, 10.0, 0.65, 1.1, 1.2, 0.5, 0.0, 0.1)

        s = steel_snip1987('C255', pr1, dim=1)
        el = elements(s, pr1, mux=7000, muy=700, mub=700, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        check = 0.2622
        test = sol.phi_b_old(1, 1, 3, 1)

        self.assertLess(abs(test[0] - check) / check, 0.003)

        pr1 = shvel(30.0, 10.0, 0.65, 1.1, 1.2, 0.5, 0.0, 0.1)

        s = steel_snip1987('C255', pr1, dim=1)
        el = elements(s, pr1, mux=7000, muy=700, mub=700, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        check = 0.245
        test = sol.phi_b(1, 1, 3, 1)

        self.assertLess(abs(test[0] - check) / check, 0.003)

        print 37

    def test_output_data_all_snip_old(self):
        # двутавр
        pr1 = dvut(60.0, 19.0, 1.2, 1.78, 2.0, 0.8, 0.119428926)
        s = steel_snip1987('C345', pr1, 1)
        el = elements(s, pr1, mub=0.5, lfact=1000)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = beam(el, forc, [0.95], 0.9)
        check = sol.output_data_all_snip_old(1, 1, 3, 1)

        ry = 315 * 100 / 9.81
        wx = 2560.3
        wy = 181.6
        phi = 0.479
        e = 2.1 * 10 ** 6
        rs = 183 * 100 / 9.81
        a = 138

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[3][0]
        res = 1.69 / 3.2
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[4][0]
        res = 0.479
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[5][0]
        res = 0.479
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[6][0]
        res = 2.27
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = 8.313
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[8][0]
        res = 1.12
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[9][0]
        res = 1.47
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = rs * 0.95 * 76810 * 1.2 / 1491 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[11][0]
        res = rs * 0.95 * 1725 * 1.78 * 2 / 156.05 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[12][0]
        n = (1.78 * 19 + 1.2 * (60 - 1.78 * 2) * 0.25) * ry
        phi = 0.522
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * n / phi
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[13][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[14][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 137.5
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 76810
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 1725
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 2560
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[19][0]
        res = 181
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 1490
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 156
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = 1.69 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[23][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = 1.69
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = 0.16 / 0.5
        self.assertLess(abs(un - res) / res, 0.02)

        un = check[26][0]
        res = 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[27][0]
        res = 0.16
        self.assertLess(abs(un - res) / res, 0.02)



        # Швеллер
        pr1 = shvel(24.0, 9.0, 0.56, 1.0, 1.05, 0.4, 0.0, 0.1)
        s = steel_snip1987('C345', pr1, 1)
        el = elements(s, pr1, mub=0.5, lfact=1000)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = beam(el, forc, [0.95], 0.9)
        check = sol.output_data_all_snip_old(1, 1, 3, 1)

        ry = 335 * 100 / 9.81
        wx = 241.73
        wy = 31.56
        e = 2.06 * 10 ** 6 * 10 / 9.81
        a = 30.6

        phi1 = (1.6 + 0.08 * 1.54 * 8.16 / 207.43 * (500. / 24) ** 2)
        at = 1.54 * 8.16 / 207.43 * (500. / 24.) ** 2
        phi = phi1 * 207.43 / 2900.78 * (24. / 500.) ** 2 * e / ry * 0.7
        rs = ry * 0.58
        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[3][0]
        res = ((9 - 0.56 - 1) / 1.) * (ry / e) ** 0.5 / 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[4][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[5][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[6][0]
        res = phi1
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = at
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[8][0]
        res = 1.09
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[9][0]
        res = 1.6
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = rs * 0.95 * 2901 * 0.56 / 138.76 / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[11][0]
        res = rs * 0.95 * 207 * 1. * 2 / 34.14 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        n = (9.0 * 1 + 0.56 * (24 - 1. * 2) * 0.25) * ry
        phi = 0.13
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * n / phi
        self.assertLess(abs(un - res) / res, 0.02)

        un = check[13][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[14][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 30.64
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 2901
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 207.56
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 241.76
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[19][0]
        res = 31.56
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 138.76
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 34.14
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = (24. - 2 - 1.05 - 0.1 * (9. / 2 - 0.56)) / 0.56 * (ry / e) ** 0.5 / 3.2
        self.assertLess(abs(un - res) / res, 0.08)

        un = check[23][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = (24. - 2.37 * 2) / 0.56 * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = ((9 - 0.56 - 1) / 1.) * (ry / e) ** 0.5 / 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[26][0]
        res = 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[27][0]
        res = ((9 - 0.56 - 1) / 1.) * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)


        # прямоугольник

        pr1 = truba_pryam(8.0, 6.0, 0.3, 0.3, 0.6)
        s = steel_snip1987('C345', pr1, 1)
        el = elements(s, pr1, mub=0.5, lfact=1000)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = beam(el, forc, [0.95], 0.9)
        check = sol.output_data_all_snip_old(1, 1, 3, 1)

        ry = 335 * 100 / 9.81
        wx = 17.5
        wy = 14.96
        e = 2.06 * 10 ** 6
        a = 7.808

        phi1 = 1
        at = 0
        phi = 1
        rs = ry * 0.58

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[3][0]
        res = ((6 - 0.3 * 2 - 0.3 * 2) / 0.3) * (ry / e) ** 0.5 / 1.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[4][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[5][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[6][0]
        res = phi1
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = at
        self.assertEquals(un, res)

        un = check[8][0]
        res = 1.15
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[9][0]
        res = 1.10
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[10][0]
        res = rs * 0.95 * 70.05 * 0.3 * 2 / 10.58 / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[11][0]
        res = rs * 0.95 * 44.89 * 0.3 * 2 / 8.69 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[13][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[14][0]
        res = 7.81
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 70.05
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 44.89
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 17.51
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 14.96
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[19][0]
        res = 10.58
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 8.69
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = (8 - 0.3 * 2 - 0.3 * 2) / 0.3 * (ry / e) ** 0.5 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[22][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[23][0]
        res = (8 - 0.3 * 2 - 0.3 * 2) / 0.3 * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[24][0]
        res = ((6 - 0.3 * 2 - 0.3 * 2) / 0.3) * (ry / e) ** 0.5 / 1.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = 1.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[26][0]
        res = ((6 - 0.3 * 2 - 0.3 * 2) / 0.3) * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        print 38

    def test_output_data_all_snip_n(self):
        # двутавр
        pr1 = dvut(60.0, 19.0, 1.2, 1.78, 2.0, 0.8, 0.119428926)
        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mub=0.5, lfact=1000)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = beam(el, forc, [0.95], 0.9)
        check = sol.output_data_all_snip_n(1, 1, 3, 1)

        ry = 320 * 100 / 9.81
        wx = 2560.3
        wy = 181.6
        phi = 0.44
        e = 2.1 * 10 ** 6
        rs = 186 * 100 / 9.81
        a = 138

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[3][0]
        res = (60 - 4.09 * 2) / 1.2 * (ry / e) ** .5 / 3.2
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[4][0]
        res = 0.44
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[5][0]
        res = 0.44
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[6][0]
        res = 2.116
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = 6.444
        self.assertLess(abs(un - res) / res, 0.006)

        un = check[8][0]
        res = 1.12
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[9][0]
        res = 1.47
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = rs * 0.95 * 76810 * 1.2 / 1491 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[11][0]
        res = rs * 0.95 * 1725 * 1.78 * 2 / 156.05 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        n = (1.78 * 19 + 1.2 * (60 - 1.78 * 2) * 0.25) * ry
        phi = 0.522
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * n / phi
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[13][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[14][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 137.5
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 76810
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 1725
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 2560
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[19][0]
        res = 181
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 1490
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 156
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = 1.69 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[23][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = 1.71
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = 0.16 / 0.5
        self.assertLess(abs(un - res) / res, 0.013)

        un = check[26][0]
        res = 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[27][0]
        res = 0.16
        self.assertLess(abs(un - res) / res, 0.013)



        # Швеллер
        pr1 = shvel(24.0, 9.0, 0.56, 1.0, 1.05, 0.4, 0.0, 0.1)
        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mub=0.5, lfact=1000)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = beam(el, forc, [0.95], 0.9)
        check = sol.output_data_all_snip_n(1, 1, 3, 1)

        ry = 320 * 100 / 9.81
        wx = 241.73
        wy = 31.56
        e = 2.06 * 10 ** 6 * 10 / 9.81
        a = 30.6

        phi1 = (1.6 + 0.08 * 1.54 * 7.29 / 207.43 * (500. / 24) ** 2)
        at = 1.54 * 7.29 / 207.43 * (500. / 24.) ** 2
        phi = phi1 * 207.43 / 2900.78 * (24. / 500.) ** 2 * e / ry * 0.7
        rs = ry * 0.58

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[3][0]
        res = ((9 - 0.56 - 1) / 1.) * (ry / e) ** 0.5 / 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[4][0]
        res = phi

        self.assertLess(abs(un - res) / res, 0.01)

        un = check[5][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[6][0]
        res = phi1
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[7][0]
        res = at
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[8][0]
        res = 1.09
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[9][0]
        res = 1.6
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = rs * 0.95 * 2901 * 0.56 / 138.76 / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[11][0]
        res = rs * 0.95 * 207 * 1. * 2 / 34.14 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        n = (9.0 * 1 + 0.56 * (24 - 1. * 2) * 0.25) * ry
        phi = 0.13
        res = 7.15 * 10 ** (-6) * (2330 - e / ry) * n / phi
        self.assertLess(abs(un - res) / res, 0.03)

        un = check[13][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[14][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 30.64
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 2901
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 207.56
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 241.76
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[19][0]
        res = 31.56
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 138.76
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 34.14
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = (24. - 2.37 * 2) / 0.56 * (ry / e) ** 0.5 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[23][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = (24. - 2.37 * 2) / 0.56 * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = ((9 - 0.56 - 1) / 1.) * (ry / e) ** 0.5 / 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[26][0]
        res = 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[27][0]
        res = ((9 - 0.56 - 1) / 1.) * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)


        # прямоугольник

        pr1 = truba_pryam(8.0, 6.0, 0.3, 0.3, 0.6)
        s = steel_snip20107n('C345', pr1, 1)
        el = elements(s, pr1, mub=0.5, lfact=1000)
        forc = force(n=800 * 1000 / 9.81, mx=435 * 1000 / 9.81 * 100, my=435 * 1000 / 9.81 * 100)
        sol = beam(el, forc, [0.95], 0.9)
        check = sol.output_data_all_snip_n(1, 1, 3, 1)

        ry = 320 * 100 / 9.81
        wx = 17.5
        wy = 14.96
        e = 2.06 * 10 ** 6
        a = 7.808

        phi1 = 1
        at = 0
        phi = 1
        rs = ry * 0.58

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[3][0]
        res = ((6 - 0.3 * 2 - 0.3 * 2) / 0.3) * (ry / e) ** 0.5 / 1.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[4][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[5][0]
        res = phi
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[6][0]
        res = phi1
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = at
        self.assertEquals(un, res)

        un = check[8][0]
        res = 1.15
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[9][0]
        res = 1.10
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[10][0]
        res = rs * 0.95 * 70.05 * 0.3 * 2 / 10.58 / 1000.
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[11][0]
        res = rs * 0.95 * 44.89 * 0.3 * 2 / 8.69 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[13][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[14][0]
        res = 7.81
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 70.05
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 44.89
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 17.51
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 14.96
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[19][0]
        res = 10.58
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 8.69
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = (8 - 0.3 * 2 - 0.3 * 2) / 0.3 * (ry / e) ** 0.5 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[22][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[23][0]
        res = (8 - 0.3 * 2 - 0.3 * 2) / 0.3 * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[24][0]
        res = ((6 - 0.3 * 2 - 0.3 * 2) / 0.3) * (ry / e) ** 0.5 / 1.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = 1.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[26][0]
        res = ((6 - 0.3 * 2 - 0.3 * 2) / 0.3) * (ry / e) ** 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        print 39

    def test_basasort_output_simple_beam(self):
        # СНиП
        basa = basa_sort.BasaSort()

        code = QtCore.QString(u'СНиП II-23-81*')
        type_element = QtCore.QString(u'Балка')
        typ_sec = QtCore.QString(u'Двутавр')
        gost = QtCore.QString(u"СТО АСЧМ 20-93 (К) Двутавры с параллельными полками")
        num_sect = QtCore.QString(u'40 К1')
        stl = QtCore.QString(u'C345')
        inp = [0.95, 0.9, 1000.0, 0.5, 1, 1, 3, 1]
        check = basa.output_simple(code, type_element, typ_sec, gost, num_sect, stl, inp)

        ry = 315 * 100 / 9.81
        wx = 2850
        wy = 950
        phi = 1
        e = 2.1 * 10 ** 6
        rs = 183 * 100 / 9.81
        a = 186.81

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[3][0]
        res = 0.745
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[4][0]
        res = 1.
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[5][0]
        res = 2.505
        self.assertLess(abs(un - res) / res, 0.0013)

        un = check[6][0]
        res = 1.831
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = 2.885
        self.assertLess(abs(un - res) / res, 0.0077)

        un = check[8][0]
        res = 1.05
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[9][0]
        res = 1.47
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = rs * 0.95 * 56145 * 1.1 / 1559 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[11][0]
        res = rs * 0.95 * 18920 * 2 * 1.8 / 720 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = 3659
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[13][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[14][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 186.8
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 56150
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 18920
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 2850
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[19][0]
        res = 950
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 1559
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 720
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = 1.12 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[23][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = 1.12
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = 0.745
        self.assertLess(abs(un - res) / res, 0.013)

        un = check[26][0]
        res = 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[27][0]
        res = 0.37
        self.assertLess(abs(un - res) / res, 0.013)

        # СП

        basa = basa_sort.BasaSort()

        code = QtCore.QString(u'СП16.13330.2011')
        type_element = QtCore.QString(u'Балка')
        typ_sec = QtCore.QString(u'Двутавр')
        gost = QtCore.QString(u"СТО АСЧМ 20-93 (К) Двутавры с параллельными полками")
        num_sect = QtCore.QString(u'40 К1')
        stl = QtCore.QString(u'C345')
        inp = [0.95, 0.9, 1000.0, 0.5, 1, 1, 3, 1]
        check = basa.output_simple(code, type_element, typ_sec, gost, num_sect, stl, inp)

        ry = 320 * 100 / 9.81
        wx = 2850
        wy = 950
        phi = 1
        e = 2.1 * 10 ** 6
        rs = 186 * 100 / 9.81

        un = check[0][0]
        res = wx * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[1][0]
        res = wy * ry * 0.95 / 100. / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[2][0]
        res = wx * ry * 0.9 / 100. * phi / 1000.
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[3][0]
        res = 0.745
        self.assertLess(abs(un - res) / res, 0.013)

        un = check[4][0]
        res = 1.
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[5][0]
        res = 2.396
        self.assertLess(abs(un - res) / res, 0.0013)

        un = check[6][0]
        res = 1.779
        self.assertLess(abs(un - res) / res, 0.0017)

        un = check[7][0]
        res = 2.237
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = 1.05
        self.assertLess(abs(un - res) / res, 0.005)

        un = check[9][0]
        res = 1.47
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = rs * 0.95 * 56145 * 1.1 / 1559 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[11][0]
        res = rs * 0.95 * 18920 * 2 * 1.8 / 720 / 1000.
        self.assertLess(abs(un - res) / res, 0.003)

        un = check[12][0]
        res = 3698
        self.assertLess(abs(un - res) / res, 0.007)

        un = check[13][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[14][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[15][0]
        res = 186.8
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[16][0]
        res = 56150
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[17][0]
        res = 18920
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[18][0]
        res = 2850
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[19][0]
        res = 950
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[20][0]
        res = 1559
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[21][0]
        res = 720
        self.assertLess(abs(un - res) / res, 0.004)

        un = check[22][0]
        res = 1.12 / 3.2
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[23][0]
        res = 3.2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = 1.12
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[25][0]
        res = 0.745
        self.assertLess(abs(un - res) / res, 0.013)

        un = check[26][0]
        res = 0.5
        self.assertLess(abs(un - res) / res, 0.01)

        un = check[27][0]
        res = 0.38
        self.assertLess(abs(un - res) / res, 0.013)

        print 40

    def test_basasort_output_simple_ferma_ring(self):
        # СНиП
        basa = basa_sort.BasaSort()

        code = QtCore.QString(u'СНиП II-23-81*')
        type_element = QtCore.QString(u'Ферма')
        typ_sec = QtCore.QString(u'Труба')
        gost = QtCore.QString(u"ГОСТ 10704-91 Трубы электросварные прямошовные")
        num_sect = QtCore.QString(u'1420x20.0')
        stl = QtCore.QString(u'C245')
        inp = [1, 0.95, 600, 4, 2]
        check = basa.output_simple(code, type_element, typ_sec, gost, num_sect, stl, inp)

        #        print check


        ry = 240 * 100 / 9.81
        a = 879.65
        lambda_x = 600 * 4 / 49.5
        lambda_y = lambda_x / 2
        phix = 0.86
        phiy = 0.95
        ru = 360 * 100 / 9.81
        e = 2.1 * 10 ** 6
        lambda_w = (1450. / 2 - 20. / 2) / 20. * (ry / e) ** 0.5
        lambda_uw = 3.14 / 2

        un = check[0][0]
        res = phix * ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[1][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = 1.195 * 2 / 3.14
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[6][0]
        res = ru * a / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[7][0]
        res = 3.14 * 3.14 * e * 2155572.38 / (600 * 4) ** 2 / 1000.

        self.assertLess(abs(un - res) / res, 0.002)

        un = check[8][0]
        res = 3.14 * 3.14 * e * 2155572.38 / (600 * 2) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[9][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[10][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[11][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[14][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[15][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[16][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[17][0]
        res = 49.50

        self.assertLess(abs(un - res) / res, 0.001)

        un = check[18][0]
        res = 49.50

        self.assertLess(abs(un - res) / res, 0.003)

        un = check[19][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[20][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[21][0]
        res = 1.195 * 2 / 3.14
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[22][0]
        res = 3.14 / 2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[23][0]
        res = 1.195
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[24][0]
        res = 1.195 * 2 / 3.14
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[25][0]
        res = 3.14 / 2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[26][0]
        res = 1.195
        self.assertLess(abs(un - res) / res, 0.001)

        # СП

        basa = basa_sort.BasaSort()

        code = QtCore.QString(u'СП16.13330.2011')
        type_element = QtCore.QString(u'Ферма')
        typ_sec = QtCore.QString(u'Труба')
        gost = QtCore.QString(u"ГОСТ 10704-91 Трубы электросварные прямошовные")
        num_sect = QtCore.QString(u'1420x20.0')
        stl = QtCore.QString(u'C245')
        inp = [1, 0.95, 600, 4, 2]
        check = basa.output_simple(code, type_element, typ_sec, gost, num_sect, stl, inp)

        #        print check


        ry = 240 * 100 / 9.81
        a = 879.65
        lambda_x = 600 * 4 / 49.5
        lambda_y = lambda_x / 2
        phix = 0.916
        phiy = 0.98
        ru = 360 * 100 / 9.81
        e = 2.1 * 10 ** 6

        un = check[0][0]
        res = phix * ry * a * 0.95 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[1][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[2][0]
        res = 1.195 * 2 / 3.14
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[3][0]
        res = phix
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[4][0]
        res = phiy
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[5][0]
        res = 'a'
        self.assertEqual(un, res)

        un = check[6][0]
        res = 'a'
        self.assertEqual(un, res)

        un = check[7][0]
        res = ry * a / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[8][0]
        res = ru * a / 1.3 / 1000.
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[9][0]
        res = 3.14 * 3.14 * e * 2155572.38 / (600 * 4) ** 2 / 1000.

        self.assertLess(abs(un - res) / res, 0.002)

        un = check[10][0]
        res = 3.14 * 3.14 * e * 2155572.38 / (600 * 2) ** 2 / 1000.
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[11][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[12][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[13][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[14][0]
        res = '-'
        self.assertEqual(un, res)

        un = check[15][0]
        res = 1.3
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[16][0]
        res = a * 7850. / 100 / 100
        self.assertLess(abs(un - res) / res, 0.0012)

        un = check[17][0]
        res = ry
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[18][0]
        res = a
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[19][0]
        res = 49.50

        self.assertLess(abs(un - res) / res, 0.001)

        un = check[20][0]
        res = 49.50

        self.assertLess(abs(un - res) / res, 0.003)

        un = check[21][0]
        res = lambda_x
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[22][0]
        res = lambda_y
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[23][0]
        res = 1.195 * 2 / 3.14
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[24][0]
        res = 3.14 / 2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[25][0]
        res = 1.195
        self.assertLess(abs(un - res) / res, 0.002)

        un = check[26][0]
        res = 1.195 * 2 / 3.14
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[27][0]
        res = 3.14 / 2
        self.assertLess(abs(un - res) / res, 0.001)

        un = check[28][0]
        res = 1.195
        self.assertLess(abs(un - res) / res, 0.001)

        print 41


class Test_column(unittest.TestCase):
    def test_nau_dvutavr(self):
        pr1 = dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        # , mux=0, muy=0, mub=0, lfact=0
        el = elements(s, pr1, mux=3500, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 1) - 1.25574) / 1.25574, 0.001)
        #
        #        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4, 1) - 1.344) / 1.344, 0.001)

        pr1 = dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=3500, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 1) - 1.20208) / 1.20208, 0.001)
        #
        #        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4, 1) - 1.2474) / 1.2474, 0.001)

        pr1 = dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=70000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 1) - 1.20208) / 1.20208, 0.001)
        #
        #        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4, 1) - 1.20208) / 1.20208, 0.001)

        pr1 = dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=70000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 1) - 1.25208) / 1.25208, 0.001)
        #
        #        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4, 1) - 1.25208) / 1.25208, 0.001)

        pr1 = dvut(h=520, b=400, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=70000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 1) - 1.3) / 1.3, 0.001)
        #
        #        print sol.nau(4.,1)        
        self.assertLess(abs(sol.nau(4, 1) - 1.3) / 1.3, 0.001)

        # nau 2
        pr1 = dvut(h=520, b=200, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=3500, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 0.91366) / 0.91366, 0.001)

        pr1 = dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=3500, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1) / 1, 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 0.88773) / 0.88773, 0.001)

        pr1 = dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=3500, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 0.932848) / 0.932848, 0.001)

        pr1 = dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=70000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 0.932848) / 0.932848, 0.001)

        pr1 = dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=70000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 0.88773) / 0.88773, 0.001)

        pr1 = dvut(h=520, b=350, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=70000, muy=700, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 0.94807) / 0.94807, 0.001)

        pr1 = dvut(h=520, b=50, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=700, muy=700000, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 1) / 1, 0.001)

        pr1 = dvut(h=520, b=100, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=700, muy=700000, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 1) / 1, 0.001)

        pr1 = dvut(h=520, b=350, t=20, s=8, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C245', pr1)
        el = elements(s, pr1, mux=700, muy=700000, mub=8000, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(10., 2) - 1.) / 1., 0.001)
        #
        #        print sol.nau(4.,2)        
        self.assertLess(abs(sol.nau(4, 2) - 1) / 1, 0.001)

        print 42

    def test_nau_korob(self):
        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=600, muy=600, mub=600, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)

        self.assertLess(abs(sol.nau(5.658, 1) - 1.20) / 1.20, 0.001)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=600, muy=600, mub=600, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.nau(9.287, 2) - 1.3) / 1.3, 0.001)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, mub=300, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.nau(4.334, 2) - 1.331) / 1.331, 0.001)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, mub=300, lfact=1)
        forc = force()
        sol = snipn(el, forc, 1)
        self.assertLess(abs(sol.nau(7.43, 2) - 1.319) / 1.319, 0.001)

        print 43

    def test_mef(self):
        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=600, muy=600, mub=600, lfact=1)
        forc = force(n=10000, mx=100000, my=100000)
        sol = snipn(el, forc, 1)
        #        print sol.mef(1)
        self.assertLess(abs(sol.mef(1)[0] - 3.671) / 3.671, 0.001)
        self.assertLess(abs(sol.mef(1)[1] - 1.2166) / 1.2166, 0.001)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=600, mub=300, lfact=1)
        forc = force(n=10000, mx=150000, my=100000)
        sol = snipn(el, forc, 1)
        #        print sol.mef(2)
        self.assertLess(abs(sol.mef(2)[0] - 6.440) / 6.440, 0.001)
        self.assertLess(abs(sol.mef(2)[1] - 1.3) / 1.3, 0.001)

        print 44

    def test_table_phi_e(self):
        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=600, muy=600, mub=600, lfact=1)
        forc = force(n=10000, mx=100000, my=100000)
        sol = snipn(el, forc, 1)
        res = sol.phi_etable(6.535, 121.9 * (230. / 206. / 1000) ** 0.5)
        self.assertLess(abs(res - 0.133) / 0.133, 0.001)

        res = sol.phi_etable(6.535, 15)
        #        print res
        self.assertLess(abs(res - 1 / 10. ** 13) / (1 / 10. ** 13), 0.001)

        res = sol.phi_etable(0.5, 0.3)
        #        print res
        self.assertLess(abs(res - 0.85) / (0.85), 0.001)

        res = sol.phi_etable(0.0, 4)
        #        print res
        self.assertLess(abs(res - 0.505) / (0.505), 0.001)

        res = sol.phi_etable(21, 4)
        #        print res
        self.assertLess(abs(res - 0.057) / (0.057), 0.001)

        print 45

    def test_phi_e(self):
        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, mub=300, lfact=1)
        forc = force(n=10000, mx=100000, my=100000)
        sol = snipn(el, forc, 1)
        res = sol.phi_e(1)[0]
        check = 0.267
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e(1)[1]
        check = 3.796
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e(1)[2]
        check = 1.258
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e(1)[3]
        check = 62.3 * (230. / 206. / 1000) ** 0.5
        self.assertLess(abs(res - check) / (check), 0.001)

        #        print sol.phi_e(2)


        res = sol.phi_e(2)[0]
        check = 0.133
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e(2)[1]
        check = 6.53
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e(2)[2]
        check = 1.319
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e(2)[3]
        check = 121.9 * (230. / 206. / 1000) ** 0.5
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip20107n('C255', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, mub=300, lfact=1)
        forc = force(n=10000., mx=10., my=10.)
        sol = snipn(el, forc, 1)

        #        print el.lambday_()  
        #        print sol.phi_e(2)
        #        print sol.phi_n(121.9*(240./206./1000)**0.5,2)
        res = sol.phi_e(2)[0]
        check = 0.439
        self.assertLess(abs(res - check) / (check), 0.001)

        print 46

    def test_phi_e_old(self):
        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, mub=300, lfact=1)
        forc = force(n=10000, mx=100000, my=100000)
        sol = snipn(el, forc, 1)
        res = sol.phi_e_old(1)[0]
        check = 0.267
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e_old(1)[1]
        check = 3.796
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e_old(1)[2]
        check = 1.258
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e_old(1)[3]
        check = 62.3 * (230. / 206. / 1000) ** 0.5
        self.assertLess(abs(res - check) / (check), 0.001)

        #        print sol.phi_e(2)


        res = sol.phi_e_old(2)[0]
        check = 0.133
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e_old(2)[1]
        check = 6.53
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e_old(2)[2]
        check = 1.319
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_e_old(2)[3]
        check = 121.9 * (230. / 206. / 1000) ** 0.5
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C235', pr1, dim=1)
        el = elements(s, pr1, mux=300, muy=300, mub=300, lfact=1)
        forc = force(n=10000, mx=10, my=0)
        #        print sol.phi_e_old(1)

        res = sol.phi_e_old(1)[0]
        check = 0.79937
        self.assertLess(abs(res - check) / (check), 0.001)

        print 47

    def test_c_phi_old(self):
        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=100, mub=100, lfact=1)
        forc = force(n=10000, mx=20000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()

        res = sol.c_old()[0]
        check = 0.835
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=100, mub=100, lfact=1)
        forc = force(n=10000, mx=200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()

        res = sol.c_old()[0]
        check = 0.309
        self.assertLess(abs(res - check) / (check), 0.0011)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=1000, muy=1000, mub=1000, lfact=1)
        forc = force(n=10000, mx=200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()

        res = sol.c_old()[0]
        check = 0.723
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c_old()[1]
        check = 0.74
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c_old()[2]
        check = 2.83
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=2000, muy=2000, mub=2000, lfact=1)
        forc = force(n=10000, mx=200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()

        res = sol.c_old()[0]
        check = 0.894
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c_old()[1]
        check = 0.894
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=30, b=20, t=2, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=1200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()
        #        print sol.phiy_old()

        res = sol.c_old()[0]
        check = 0.093
        self.assertLess(abs(res - check) / (check), 0.004)

        pr1 = dvut(h=30, b=20, t=2, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=800000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()
        #        print sol.phiy_old()

        res = sol.c_old()[0]
        check = 0.144
        self.assertLess(abs(res - check) / (check), 0.004)

        pr1 = truba_pryam(h=14.0, b=6., t=0.5, r1=0.5, r2=1)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=80000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c_old()
        #        print el.lambday_()
        #        print sol.phiy_old()

        res = sol.c_old()[1]
        check = 1
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.a_c_old(0.5)
        check = 0.6
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.a_c_old(2)
        check = 0.65
        self.assertLess(abs(res - check) / (check), 0.001)

        print 48

    def test_c_phi(self):
        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=100, mub=100, lfact=1)
        forc = force(n=10000, mx=20000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()

        res = sol.c()[0]
        check = 0.835
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=100, mub=100, lfact=1)
        forc = force(n=10000, mx=200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()

        res = sol.c()[0]
        check = 0.309
        self.assertLess(abs(res - check) / (check), 0.0011)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=1000, muy=1000, mub=1000, lfact=1)
        forc = force(n=10000, mx=200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()

        res = sol.c()[0]
        check = 0.706
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c()[1]
        check = 0.706
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c()[2]
        check = 2.83
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=1000, muy=1000, mub=1000, lfact=1)
        forc = force(n=10000, mx=320000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()

        res = sol.c()[0]
        check = 0.470
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c()[1]
        check = 0.551
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c()[2]
        check = 4.528
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=20, b=20, t=1, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=2000, muy=2000, mub=2000, lfact=1)
        forc = force(n=10000, mx=200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()

        res = sol.c()[0]
        check = 0.871
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.c()[1]
        check = 0.871
        self.assertLess(abs(res - check) / (check), 0.001)

        pr1 = dvut(h=30, b=20, t=2, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=1200000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()
        #        print sol.phiy()

        res = sol.c()[0]
        check = 0.092
        self.assertLess(abs(res - check) / (check), 0.004)

        pr1 = dvut(h=30, b=20, t=2, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=800000, my=0)
        sol = snipn(el, forc, 1)
        #        print sol.c()
        #        print el.lambday_()
        #        print sol.phiy()

        res = sol.c()[0]
        check = 0.143
        self.assertLess(abs(res - check) / (check), 0.004)

        print 49

    def test_phi_exy(self):
        pr1 = dvut(h=30, b=20, t=2, s=1, r1=0, r2=0, a1=0)
        s = steel_snip1987('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=70000, my=70000)
        sol = snipn(el, forc, 1)
        #        print sol.phi_exy_old()

        res = sol.phi_exy_old()[0]
        check = 0.343
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_exy_old()[1]
        check = 0.383
        self.assertLess(abs(res - check) / (check), 0.0012)

        res = sol.phi_exy_old()[2]
        check = 0.688
        self.assertLess(abs(res - check) / (check), 0.0012)

        pr1 = dvut(h=30, b=20, t=2, s=1, r1=0, r2=0, a1=0)
        s = steel_snip20107n('C345', pr1, dim=1)
        el = elements(s, pr1, mux=100, muy=200, mub=300, lfact=1)
        forc = force(n=10000, mx=70000, my=70000)
        sol = snipn(el, forc, 1)
        #        print sol.phi_exy_old()

        res = sol.phi_exy()[0]
        check = 0.342
        self.assertLess(abs(res - check) / (check), 0.001)

        res = sol.phi_exy()[1]
        check = 0.382
        self.assertLess(abs(res - check) / (check), 0.0013)

        res = sol.phi_exy()[2]
        check = 0.688
        self.assertLess(abs(res - check) / (check), 0.0012)

        print 50


if __name__ == "__main__":
    unittest.main()
