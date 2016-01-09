# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 21:48:07 2014

@author: Pyltsin
"""
import profiles2 as profiles
from  PyQt4 import QtCore
import table as tables
import codes
import steel


class BasaSort(object):
    def __init__(self):
        self.__list_code = [u'СНиП II-23-81*', u'СП16.13330.2011']
        self.list_sort = [u'Прямоугольник', u'Двутавр', u'Швеллер', u'Уголок', u'Прямоугольная труба',
                          u'Труба', u'Уголки в тавр (длинные стор. - вверх)'
            , u'Уголки в тавр (длинные стор. - в бок)'
            , u'Уголки в крест']
        self.dict_sostav_sort = {5: 2, 6: 2, 7: 2}
        self.dict_sort = {u'Двутавр': 0, u'Швеллер': 1, u'Уголок': 2, u'Прямоугольная труба': 3,
                          u'Труба': 4, u'Уголки в тавр (длинные стор. - вверх)': 5
            , u'Уголки в тавр (длинные стор. - в бок)': 6
            , u'Уголки в крест': 7, u'Прямоугольник': 8}
        self.list_input = {0: profiles.dvut(1, 1, 1, 1, 1, 1, 0).input_data()
            , 1: profiles.shvel(h=1, b=1, s=1, t=1, r1=1, r2=1, a1=0, r3=1).input_data()
            , 2: profiles.ugol(h=1, b=1, t=0.1, r1=0, r2=0, r3=0).input_data()
            , 3: profiles.truba_pryam(h=1, b=1, t=0.1, r1=0, r2=0).input_data()
            , 4: profiles.ring(r=1, r1=0).input_data()
            , 5: profiles.sost_ugol_tavr_st_up(h=1, b=1, t=1, r1=0, r2=0, r3=0, dx=1).input_data()
            , 6: profiles.sost_ugol_tavr_st_right(h=1, b=1, t=1, r1=0, r2=0, r3=0, dx=1).input_data()
            , 7: profiles.sost_ugol_tavr_st_krest(h=1, b=1, t=1, r1=0, r2=0, r3=0, dx=1, dy=1).input_data()
            , 8: profiles.rectangle(1, 1).input_data()
                           }

        self.__add_data_sostav = {
            5: [[u'dx, см [0; 10]'], [0, 10]],
            6: [[u'dx, см [0; 10]'], [0, 10]],
            7: [[u'dx, см [0; 10]', u'dy, см [0; 10]'], [0, 10]]
        }

        self.__list_elements = [[u'Ферма', 0], [u'Балка', 1], [u'Колонна', 2]]
        self.__list4elements = [[0, 3, 5, 6, 7, 4], [0, 1, 3], [0, 3]]

        self.pictures_list = {0: 'SortamentPicture/dvut.png'
            , 1: 'SortamentPicture/shvel.png'
            , 2: 'SortamentPicture/ugol.png'
            , 3: 'SortamentPicture/korob.png'
            , 4: 'SortamentPicture/ring.png'
            , 5: 'SortamentPicture/sost_ugol_tavr_st_up.png'
            , 6: 'SortamentPicture/sost_ugol_tavr_st_right.png'
            , 7: 'SortamentPicture/sost_ugol_tavr_st_krest.png'
            , 8: 'SortamentPicture/rectangle.png'}

        self.__list4sortament = [
            [[u'Двутавры', 0], [u'Швеллеры', 1], [u'Уголки', 2], [u'Прямоугольные трубы', 3], [u'Трубы', 4]]
            , [[u"ГОСТ 8239-89 Двутавры с уклоном полок", u'SortamentData/GOST823989.csv'],
               [u"СТО АСЧМ 20-93 (Б) Двутавры с параллельными полками", u'SortamentData/stoaschm2093(b).csv'],
               [u"СТО АСЧМ 20-93 (Ш) Двутавры с параллельными полками", u'SortamentData/stoaschm2093(sh).csv'],
               [u"СТО АСЧМ 20-93 (К) Двутавры с параллельными полками", u'SortamentData/stoaschm2093(c).csv'],
               [u"ГОСТ 26020-83 (Б) Двутавры с параллельными полками", u'SortamentData/gost2602083(b).csv'],
               [u"ГОСТ 26020-83 (Ш) Двутавры с параллельными полками", u'SortamentData/gost2602083(sh).csv'],
               [u"ГОСТ 26020-83 (К) Двутавры с параллельными полками", u'SortamentData/gost2602083(c).csv'],
               [u"ГОСТ 26020-83 (Д) Двутавры с параллельными полками", u'SortamentData/gost2602083(d).csv'],
               [u"ГОСТ 19425-74* Двутавры специальные", u'SortamentData/gost1942574.csv'],
               [u"Двутавры пользователя", u'SortamentData/UserDvutavr.csv']]

            , [[u"ГОСТ 8240-97 (У) Швеллеры стальные горячекатанные", u'SortamentData/GOST824097(u).csv'],
               [u"ГОСТ 8240-97 (П) Швеллеры стальные горячекатанные", u'SortamentData/GOST824097(p).csv'],
               [u"ГОСТ 8278-83 Швеллеры гнутые (С235, С245)", u'SortamentData/GOST827883(l460).csv'],
               [u"ГОСТ 8278-83 Швеллеры гнутые (С255, С345)", u'SortamentData/GOST827883(r460).csv'],
               [u"Швеллеры пользователя", u'SortamentData/UserShvel.csv']]

            , [[u"ГОСТ 8509-93 Уголки равнополочные", u'SortamentData/GOST850993.csv'],
               [u"ГОСТ 8510-86 Уголки неравнополочные", u'SortamentData/GOST851086.csv'],
               [u"ГОСТ 19771-93 Уголки гнутые равнополочные (Run<460 Н/мм2, C235, C245)",
                u'SortamentData/GOST1977193(l460).csv'],
               [u"ГОСТ 19771-93 Уголки гнутые равнополочные (Run>460 Н/мм2, C255, C345)",
                u'SortamentData/GOST1977193(r460).csv'],
               [u"ГОСТ 19772-93 Уголки гнутые неравнополочные (Run<460 Н/мм2, C235, C245)",
                u'SortamentData/GOST1977293(l460).csv'],
               [u"ГОСТ 19772-93 Уголки гнутые неравнополочные (Run>460 Н/мм2, C255, C345)",
                u'SortamentData/GOST1977293(r460).csv'],
               [u"Уголки пользователя", u'SortamentData/UserUgol.csv']
               ]

            , [[u"ГОСТ 30245-2003 (Кв) Квадратные замкнутые сечения", u'SortamentData/gost302452003(k).csv'],
               [u"ГОСТ 30245-2003 (Прям) Прямоугольные замкнутые сечения", u'SortamentData/gost302452003(pr).csv'],
               [u"Прямоугольные сечения пользователя", u'SortamentData/UserKorob.csv']

               ]

            , [[u"ГОСТ 10704-91 Трубы электросварные прямошовные", u'SortamentData/gost1070491.csv'],
               [u"ГОСТ 8732-78 Трубы стальные бесшовные горячедеформированные", u'SortamentData/gost873278.csv'],
               [u"Трубы пользователя", u'SortamentData/UserTruba.csv']]

        ]

    def list_code(self):
        """Возвращает список нормативов"""
        return self.__list_code

    def data_solve(self, typ):
        """Возвращает список доп. исходных данных, реализовано только для ферм"""
        pr1 = profiles.truba_pryam(h=8, b=12, t=0.6, r2=1.2, r1=0.6)
        s = steel.steel_snip20107n('C345', pr1, 1)
        el = codes.elements(s, pr1, mux=300, muy=5000, lfact=1)
        forc = codes.force(n=200 * 1000 / 9.81, mx=100 * 1000 / 9.81 * 100, my=000 * 1000 / 9.81 * 100,
                           qx=500 * 1000 / 9.81)

        if typ == self.__list_elements[0][0]:
            sol = codes.ferma(el, forc, 1)
        elif typ == self.__list_elements[1][0]:
            sol = codes.beam(el, forc, [1, 1])

        return sol.add_data()

    def solvePP(self, code, element, typeSolve, typeSection, formSection, sortament, numberSection, steel, lstAddData,
                lstInputData, lstForce):
        '''Возвращает данные сложного расчета.
        Сложный расчет состоят из 2 частей - подбор и проверка., сначала пишем проверку'''
        if typeSolve == QtCore.QString(u'Проверка'):
            out = self.checkPP(code, element, typeSection, formSection, sortament, numberSection, steel, lstAddData,
                               lstInputData, lstForce)
        elif typeSolve == QtCore.QString(u'Подбор'):
            out = self.findPP(code, element, typeSection, formSection, sortament, numberSection, steel, lstAddData,
                              lstInputData, lstForce)
        return out

    def checkPP(self, code, element, typeSection, formSection, sortament, numberSection, stl, lstAddData, lstInputData,
                lstForce):
        '''Проверка сечений - для начала загружаем все даные и отправляем их в codes, 
        Исходные данные - отправляем в QString
        code -  имя норм (СНиП II-23-81*)
        element - название типа элемента (Ферма), 
        typeSection- название типа сечения (пока только ПРОКАТ)
        formSection - название сечения (Уголки в тавр (длинные стор. - вверх))
        sortament - текстом (QString) названия ГОСТа соратмента (ГОСТ 8509-93 Уголки равнополочные)
        numberSection - номер сечения (L20x20x3)
        steel - текстом (QString) сталь (C235)
        lstAddData - для сечения
        lstInputData - для расчета
        lstForce - усилия'''
        #        print lstInputData
        # Ставим флаг в фальш
        flag_sostav = False

        # записываем в typ_sec - название формы сечения, в y записываем номер сечения
        for x in self.dict_sort:
            if QtCore.QString(x) == formSection:
                y = self.dict_sort[x]
                typ_sec = x  # меняем текст на номер
                break

        # если номер в списке - меняем флаг
        if y in self.dict_sostav_sort:
            y = self.dict_sostav_sort[y]
            flag_sostav = True

        # ищем путь к искомому сортаменту
        for i in self.__list4sortament[1 + y]:
            if QtCore.QString(i[0]) == sortament:
                path = i[1]
                break

        # загружаем в табл дата данные сортаментов
        table = tables.tables_csv(path, 'float')
        table_data = table.get_table()


        # загружаем список исходных данных для ПРОФИЛЯ!!! - т.е. h, b, s, t, и т.д.

        input_data = self.input_data4sortament(self.dict_sort[typ_sec])
        len_input_data = len(input_data)

        for x in table_data[1:]:
            if numberSection == QtCore.QString(x[0]):
                if flag_sostav == False:
                    pr = self.output_data(typ_sec, x[1:-3])
                else:
                    add_ln = len_input_data - len(x[1:-3])
                    lst = x[1:-3] + lstAddData
                    pr = self.output_data(typ_sec, lst)
                break

        # загружаем сталь
        if code == QtCore.QString(self.__list_code[0]):
            s = steel.steel_snip1987(str(stl), pr, dim=1, typ_steel='prokat')
        elif code == QtCore.QString(self.__list_code[1]):
            s = steel.steel_snip20107n(str(stl), pr, dim=1)

        if s.ry() != 0:
            #        print s.ry()

            # НЕ раскидываем услия и передаем как список
            forc = codes.force(lstForce=lstForce)

            # создаем элемент ферма
            if element == QtCore.QString(self.__list_elements[0][0]):
                el = codes.elements(s, pr, mux=lstInputData[-5], muy=lstInputData[-4], lfact=lstInputData[-6])
                #            print inp[-1],inp[-2]
                sol = codes.FermaPP()
                sol.reinit(el, forc, yc=[lstInputData[-8], lstInputData[-7]])

                if code == QtCore.QString(self.__list_code[0]):
                    out = sol.outDataOld(lstInputData[-3], lstInputData[-2], lstInputData[-1])
                elif code == QtCore.QString(self.__list_code[1]):
                    out = sol.outDataN(lstInputData[-3], lstInputData[-2], lstInputData[-1])

            # создаем элемент балка
            elif element == QtCore.QString(self.__list_elements[1][0]):
                el = codes.elements(s, pr, mub=lstInputData[-5], lfact=lstInputData[-6])
                #            print inp[-1],inp[-2]
                sol = codes.BeamPP()
                sol.reinit(el, forc, yc=[lstInputData[-8]], ycb=lstInputData[-7])

                if code == QtCore.QString(self.__list_code[0]):
                    out = sol.outDataOld(lstInputData[-4], lstInputData[-3], lstInputData[-2], lstInputData[-1])
                elif code == QtCore.QString(self.__list_code[1]):
                    out = sol.outDataN(lstInputData[-4], lstInputData[-3], lstInputData[-2], lstInputData[-1])

            elif element == QtCore.QString(self.__list_elements[2][0]):
                el = codes.elements(s, pr, mux=lstInputData[3], muy=lstInputData[4], mub=lstInputData[5],
                                    lfact=lstInputData[2])
                #            print inp[-1],inp[-2]
                sol = codes.ColumnPP()
                sol.reinit(el, forc, yc=[lstInputData[0]], ycb=lstInputData[1])

                if code == QtCore.QString(self.__list_code[0]):
                    out = sol.outDataOld(lstInputData[-3], lstInputData[-2], lstInputData[-1])
                elif code == QtCore.QString(self.__list_code[1]):
                    out = sol.outDataN(lstInputData[-3], lstInputData[-2], lstInputData[-1])

            return out
        else:
            out = 0
            return out

    def findPP(self, code, element, typeSection, formSection, sortament, numberSection, steel, lstAddData, lstInputData,
               lstForce):
        pass

    def output_simple(self, code, type_element, typ_sec, gost, num_sect, stl, inp):
        """ Возвращает список выходных данных простого расчета,
            исходные данные:
            code - текстом (QString) имя норм (СНиП II-23-81*)
            type_element - текстом (QString) название типа элемента (Ферма)
            typ_sec - текстом (QString) название сечения (Уголки в тавр (длинные стор. - вверх))
            gost - текстом (QString) названия ГОСТа соратмента (ГОСТ 8509-93 Уголки равнополочные)
            num_sect - текстом (QString) номер сечения (L20x20x3)
            stl - текстом (QString) сталь (C235)
            inp - список дополнительных данных"""
        # ищем файл
        flag_sostav = False
        #        print 'basa', num_sect
        for x in self.dict_sort:
            if QtCore.QString(x) == typ_sec:
                y = self.dict_sort[x]
                typ_sec = x  # меняем текст на номер
                break
            #        print y, 'y'

        if y in self.dict_sostav_sort:
            y = self.dict_sostav_sort[y]  # меняем y на номер госта
            flag_sostav = True

        for i in self.__list4sortament[1 + y]:
            if QtCore.QString(i[0]) == gost:
                path = i[1]
                break
                # Грузим свойства прлфиля

        table = tables.tables_csv(path, 'float')
        table_data = table.get_table()
        # определяем кол-во профилей в файле

        input_data = self.input_data4sortament(self.dict_sort[typ_sec])
        len_input_data = len(input_data)

        #        print table_data
        #        print table_data[1:]

        for x in table_data[1:]:
            if num_sect == QtCore.QString(x[0]):
                if flag_sostav == False:
                    pr = self.output_data(typ_sec, x[1:-3])
                else:
                    add_ln = len_input_data - len(x[1:-3])
                    lst = x[1:-3] + inp[0:0 + add_ln]
                    pr = self.output_data(typ_sec, lst)
                break

        if code == QtCore.QString(self.__list_code[0]):
            s = steel.steel_snip1987(str(stl), pr, dim=1, typ_steel='prokat')
        elif code == QtCore.QString(self.__list_code[1]):
            s = steel.steel_snip20107n(str(stl), pr, dim=1)

        if s.ry() != 0:
            #        print s.ry()
            forc = codes.force()

            if type_element == QtCore.QString(self.__list_elements[0][0]):
                el = codes.elements(s, pr, mux=inp[-2], muy=inp[-1], lfact=inp[-3])
                #            print inp[-1],inp[-2]
                sol = codes.ferma(el, forc, [inp[-5], inp[-4]])

                if code == QtCore.QString(self.__list_code[0]):
                    out = sol.output_data_all_snip_old()
                elif code == QtCore.QString(self.__list_code[1]):
                    out = sol.output_data_all_snip_n()


            elif type_element == QtCore.QString(self.__list_elements[1][0]):
                el = codes.elements(s, pr, mub=inp[-5], lfact=inp[-6])
                #            print inp[-1],inp[-2]
                sol = codes.beam(el, forc, yc=[inp[-8]], ycb=inp[-7])

                if code == QtCore.QString(self.__list_code[0]):
                    out = sol.output_data_all_snip_old(inp[-4], inp[-3], inp[-2], inp[-1])
                elif code == QtCore.QString(self.__list_code[1]):
                    out = sol.output_data_all_snip_n(inp[-4], inp[-3], inp[-2], inp[-1])

            return out
        else:
            out = 0
            return out

    def add_data_sostav(self, name):
        if name != '':
            for x in self.dict_sort:
                if QtCore.QString(x) == name:
                    number = self.dict_sort[x]
                    break
            if number in self.dict_sostav_sort:
                #                print self.__add_data_sostav
                #                print number
                #                print self.__add_data_sostav[number], 'tut'
                return self.__add_data_sostav[number]
            else:
                return []
        else:
            return []

    def output_list_sect_num(self, sortament, name):
        if sortament != "" and name != "":
            for x in self.dict_sort:
                if name == QtCore.QString(x):
                    number = self.dict_sort[x]
                    break
            if number in self.dict_sostav_sort:
                number = self.dict_sostav_sort[number]

            for x in self.__list4sortament[number + 1]:
                if QtCore.QString(x[0]) == sortament:
                    fil = x[1]

            table_sect = tables.tables_csv(fil, 'float')
            list_sect = table_sect.get_title_column()
            return list_sect
        else:
            return ['']

    def output_list_sortament(self, name):
        if name != "":
            for x in self.dict_sort:
                if name == QtCore.QString(x):
                    number = self.dict_sort[x]
                    break
            if number in self.dict_sostav_sort:
                number = self.dict_sostav_sort[number]
            for x in self.__list4sortament[0]:
                if x[1] == number:
                    number_sort = x[1]
                    break
            lst = []
            for x in self.__list4sortament[number_sort + 1]:
                lst.append(x[0])
            list_sortament = lst
            return list_sortament
        else:
            return ['']

    def output_list_section(self, type_section):
        lst = []
        for x in self.output_list_elements():
            if QtCore.QString(type_section) == QtCore.QString(x[0]):
                numbers_element = self.output_list4elements()[x[1]]
                break
            #        print numbers_element
        for y in self.key_sortament():
            #            print y
            if self.output_dict_sort()[y] in numbers_element:
                lst.append(y)
        return lst

    def output_list_elements(self):
        return self.__list_elements

    def output_list4elements(self):
        return self.__list4elements

    def output_dict_sort(self):
        return self.dict_sort

    def output_data(self, i, inp):
        """Возвращает объект сечения.
        Исходные данные: i - название по dict_sort (или текст или номер), inp - список исходных данных для сечения
        Выходные: объект сечения"""
        #        print i, inp
        #        print type(i)
        x = None
        for label in self.dict_sort:
            if i == QtCore.QString(label) or i == label:
                x = self.dict_sort[label]
        if x == None:
            x = i
        if x == 0:
            #            print inp

            pr = profiles.dvut(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
        elif x == 1:
            pr = profiles.shvel(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6], inp[7])
        elif x == 2:
            #            print inp
            pr = profiles.ugol(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5])
        elif x == 3:
            #            print inp
            pr = profiles.truba_pryam(inp[0], inp[1], inp[2], inp[3], inp[4])
        elif x == 4:
            pr = profiles.ring(inp[0], inp[1])
        elif x == 5:
            #            print inp
            pr = profiles.sost_ugol_tavr_st_up(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
        elif x == 6:
            pr = profiles.sost_ugol_tavr_st_right(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
        elif x == 7:
            pr = profiles.sost_ugol_tavr_st_krest(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6], inp[7])
        elif x == 8:
            pr = profiles.rectangle(inp[0], inp[1])
        return pr

    def pict(self, i):
        #        print i
        for label in self.dict_sort:
            if i == QtCore.QString(label):
                x = self.dict_sort[label]
        return self.pictures_list[x]

    def input_data(self, i):

        for label in self.dict_sort:
            #            print type(i)
            #            print label
            if i == QtCore.QString(label):
                x = self.dict_sort[label]

        y = self.list_input[x]
        return y

    def lstPP(self, code, element):
        '''возвращает недосозданных класс элементов'''
        if code == QtCore.QString(self.__list_code[0]) or code == QtCore.QString(self.__list_code[1]):
            if element == QtCore.QString(self.__list_elements[0][0]):
                el = codes.FermaPP()
            elif element == QtCore.QString(self.__list_elements[1][0]):
                #                el=[1,[1,2]]
                el = codes.BeamPP()
            elif element == QtCore.QString(self.__list_elements[2][0]):
                el = codes.ColumnPP()
        return el

    def lstInputDataPP(self, code, element):
        '''Возвращает список данных для расчета с ограничителями'''
        #                el=[1,[1,2]]
        el = self.lstPP(code, element)
        lst = el.addData()
        return lst

    def lstLoadDataPP(self, code, element):
        '''Возвращает список данных для усилий'''
        el = self.lstPP(code, element)
        lst = el.lstForce()
        return lst

    def key_sortament(self):
        return self.list_sort

    def list4sortament(self):
        return self.__list4sortament

    def pict4sortament(self, i):
        return self.pictures_list[i]

    def input_data4sortament(self, i):
        """возвращает список входных данных для расчета сечения.
        входные данные - номер сечения по self.dict_sort"""
        return self.list_input[int(i)]
