# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import matplotlib
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines
from matplotlib.collections import PatchCollection
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.mlab import griddata
import rcMaterial
import numpy as np
from PyQt4 import QtGui, QtCore, uic
from rcMesh import EmptySections as Sections
from rcMaterial import EmptyMaterials as Materials
import rcSolves

__author__ = 'Pyltsin'


class MainWindow(QtGui.QMainWindow):
    """init mainWindow"""

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi('gui/main_form_concrete.ui', self)
        self.connect_function()
        self.init_prop()
        self.changed()
        self.list_save_material = []
        self.list_save_section = []

    def test(self):
        print "test"

    def init_prop(self):
        self.box_number_ps1.setValue(3)
        self.box_number_ps2.setValue(3)
        self.box_number_ps2_long.setValue(3)

        self.change_count_row_any_table(3, self.table_ps1)
        self.change_count_row_any_table(3, self.table_ps2)
        self.change_count_row_any_table(3, self.table_ps2_long)

        self.dict_prop_section = {
            u"Прямоугольник": [[self.box_x1, True, 0], [self.box_x2, False, 0], [self.box_x3, False, 0],
                               [self.box_y1, True, 0], [self.box_y2, False, 0], [self.box_y3, False, 0],
                               [self.box_h, True, 1], [self.box_b, True, 1], [self.box_d, False, 0],
                               [self.box_nx, True, 10], [self.box_ny, True, 10], [self.box_k, True, 1],
                               [self.box_e, True, 0], [self.box_rx, True, 0], [self.box_ry, True, 0]],
            u"Треугольник": [[self.box_x1, True, 0], [self.box_x2, True, 1], [self.box_x3, True, 0],
                             [self.box_y1, True, 0], [self.box_y2, True, 0], [self.box_y3, True, 1],
                             [self.box_h, False, 0], [self.box_b, False, 0], [self.box_d, False, 0],
                             [self.box_nx, True, 10], [self.box_ny, True, 10], [self.box_k, True, 1],
                             [self.box_e, True, 0], [self.box_rx, True, 0], [self.box_ry, True, 0]],
            u"Круг": [[self.box_x1, True, 0], [self.box_x2, False, 0], [self.box_x3, False, 0],
                      [self.box_y1, True, 0], [self.box_y2, False, 0], [self.box_y3, False, 0],
                      [self.box_h, False, 0], [self.box_b, False, 0], [self.box_d, True, 10],
                      [self.box_nx, True, 10], [self.box_ny, True, 10], [self.box_k, True, 1],
                      [self.box_e, True, 0], [self.box_rx, True, 0], [self.box_ry, True, 0]],
            u"Точка": [[self.box_x1, True, 0], [self.box_x2, False, 0], [self.box_x3, False, 0],
                       [self.box_y1, True, 0], [self.box_y2, False, 0], [self.box_y3, False, 0],
                       [self.box_h, False, 0], [self.box_b, False, 0], [self.box_d, True, 1],
                       [self.box_nx, False, 1], [self.box_ny, False, 1], [self.box_k, True, 1],
                       [self.box_e, True, 0], [self.box_rx, True, 0], [self.box_ry, True, 0]]
        }
        self.list_section = self.dict_prop_section.keys()

        self.load_list_section()

        self.boxCountLoad.setValue(1)

        # не сделано, пока отключено:
        self.checkBoxPS2.setChecked(False)
        self.checkBoxPS2.setEnabled(False)

        self.checkBoxGraphics.setChecked(False)
        self.checkBoxGraphics.setEnabled(False)

    def connect_function(self):
        """connect"""
        # menu
        self.menuSolve.triggered.connect(self.solve)

        # connect for load
        self.boxCountLoad.valueChanged.connect(self.table_load_count_row)

        # connect with section

        self.widget_list_type_section.currentIndexChanged.connect(self.change_type_section)
        self.button_add_section.clicked.connect(self.add_section)
        self.button_save_section.clicked.connect(self.save_section)
        self.button_delete_section.clicked.connect(self.delete_section)
        self.button_load_section.clicked.connect(self.load_section)

        self.button_plot_section.clicked.connect(self.plot_section)
        # connect with material
        self.button_add_material.clicked.connect(self.add_material)
        self.button_save_material.clicked.connect(self.resave_material)
        self.button_delete_material.clicked.connect(self.delete_material)
        self.button_load_material.clicked.connect(self.load_material)

        self.list_type_material.currentIndexChanged.connect(self.change_type_material)
        self.change_type_material()

        self.box_number_ps1.valueChanged.connect(
                lambda: self.change_count_row_any_table(self.box_number_ps1.value(), self.table_ps1))
        self.box_number_ps2.valueChanged.connect(
                lambda: self.change_count_row_any_table(self.box_number_ps2.value(), self.table_ps2))
        self.box_number_ps2_long.valueChanged.connect(
                lambda: self.change_count_row_any_table(self.box_number_ps2_long.value(), self.table_ps2_long))

        self.button_dia_ps1.clicked.connect(lambda: self.plot_dia(self.table_ps1))
        self.button_dia_ps2.clicked.connect(lambda: self.plot_dia(self.table_ps2))
        self.button_dia_ps2_long.clicked.connect(lambda: self.plot_dia(self.table_ps2_long))

        #       connect checkBox with PS1, PS2
        self.checkBoxPS1.clicked.connect(self.changeCheckBoxSolve)
        self.checkBoxPS2.clicked.connect(self.changeCheckBoxSolve)
        self.checkBoxD.clicked.connect(self.changeCheckBoxSolve)
        self.checkBoxGraphics.clicked.connect(self.changeCheckBoxSolve)
        self.changeCheckBoxSolve()

    def get_nmxmy(self):
        return self.get_from_table(self.tableLoad)

    @staticmethod
    def get_from_table(widget):
        lst = []
        for j in xrange(widget.rowCount()):

            lst_temp = []
            for i in xrange(widget.columnCount()):

                text = widget.item(j, i).text()
                if "," in text:
                    text = text.replace(",", ".")
                    widget.item(j, i).setText(text)
                if not is_number(str(text.toUtf8())):
                    raise TypeErrorStrenght
                else:
                    lst_temp.append(float(text))
            lst.append(lst_temp)

        return lst

    def solve(self):
        try:
            # 0 - nmxmy
            lst_nmxmy = self.get_nmxmy()
            print 'lst_nmxmy', lst_nmxmy
            # 1 - create material
            # lst_material = []
            # for material_raw in self.list_save_material:
            #     lst_material.append(rcMaterial.GeneralMaterial(material_raw))
            rcsolve = rcSolves.Solves()
            for item in self.list_save_material:
                print item.kwargs

            if not self.list_save_material:
                raise TypeError(u"Не заданы материалы")

            rcsolve.load_list_materials(self.list_save_material)

            # # 2 - create figure

            if not self.list_save_section:
                raise TypeError(u"Не заданы сечения")

            error_section = True
            for item in self.list_save_section:
                if item.kwargs['type_section'] in [u'Круг', u'Прямоугольник', u'Треугольник']:
                    error_section = False

            if error_section:
                raise TypeError(u"Не заданы сечения")

            for item in self.list_save_section:
                print item.kwargs

            rcsolve.load_list_section(self.list_save_section)

            ## 3 dd
            rcsolve.formGenSC()

            typD = self.checkBoxD.isChecked()
            typStat = self.checkBoxStatOpr.isChecked()
            lx = self.doubleBoxLx.value()
            ly = self.doubleBoxLy.value()
            l = self.doubleBoxL.value()

            print typD, typStat, lx, ly, l
            outD, error, titleD = rcsolve.nuD(lst_nmxmy, typStat, lx, ly, l, typD)
            print outD, error, titleD

            # загрузка в TableD
            self.input_table_in(outD, self.tableLoadD, titleD)
            if error == True:
                raise TypeError(u'N>Ncr, расчет невозможен')

        # TODO расчет прочности
        except TypeErrorStrenght:
            self.show_error(u"Ошибка в таблице усилий")

            # except TypeError as e:
            #     self.show_error(e.args[0])

    @staticmethod
    def input_table_in(array, widget, title):
        lx, ly = np.shape(array)

        widget.setRowCount(lx)

        widget.setColumnCount(ly)

        widget.setHorizontalHeaderLabels(title)
        for x in xrange(lx):
            for y in xrange(ly):
                widget.setItem(x, y, QtGui.QTableWidgetItem(""))
                text = str(array[x][y])
                widget.item(x, y).setText(QtCore.QString(text))
                widget.item(x, y).setFlags(QtCore.Qt.ItemFlags(1 + 2 + 4 + 8 + 6 + 12 + 64))

    def plot_section(self):
        """plot all section in self.list_save_section"""
        fig = self.mpl_section.figure
        ax = fig.add_subplot(111)
        ax.clear()
        patches = []
        for sect in self.list_save_section:
            if unicode(sect.kwargs["type_section"]) == u"Прямоугольник":
                rect = mpatches.Rectangle((sect.kwargs["x1"], sect.kwargs["y1"]), sect.kwargs["b"], sect.kwargs["h"])
                ax.add_patch(rect)

            if unicode(sect.kwargs["type_section"]) == u"Круг":
                circle = mpatches.Circle((sect.kwargs["x1"], sect.kwargs["y1"]), radius=sect.kwargs["d"] / 2.,
                                         color=[0., 1, 0])

                ax.add_patch(circle)

            if unicode(sect.kwargs["type_section"]) == u"Точка":
                circle = mpatches.Circle((sect.kwargs["x1"], sect.kwargs["y1"]), radius=sect.kwargs["d"] / 2.,
                                         color=[0., 0.5, 0])

                ax.add_patch(circle)

            if unicode(sect.kwargs["type_section"]) == u"Треугольник":
                Path = mpath.Path
                path_data = [
                    (Path.MOVETO, [sect.kwargs["x1"], sect.kwargs["y1"]]),
                    (Path.LINETO, [sect.kwargs["x2"], sect.kwargs["y2"]]),
                    (Path.LINETO, [sect.kwargs["x3"], sect.kwargs["y3"]]),
                    (Path.LINETO, [sect.kwargs["x1"], sect.kwargs["y1"]])
                ]
                codes, verts = zip(*path_data)
                path = mpath.Path(verts, codes)
                patch = mpatches.PathPatch(path)
                ax.add_patch(patch)

        ax.relim()
        ax.autoscale_view(tight=True, scalex=True, scaley=True)
        self.mpl_section.draw()
        # autoscale
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        if xlim[1] - xlim[0] > ylim[1] - ylim[0]:
            ylim0 = (ylim[0] + ylim[1]) / 2. - (xlim[1] - xlim[0]) / 2.
            ylim1 = (ylim[0] + ylim[1]) / 2. + (xlim[1] - xlim[0]) / 2.
            ax.set_ylim(ylim0, ylim1)
        else:
            xlim0 = (xlim[0] + xlim[1]) / 2. - (ylim[1] - ylim[0]) / 2.
            xlim1 = (xlim[0] + xlim[1]) / 2. + (ylim[1] - ylim[0]) / 2.
            ax.set_xlim(xlim0, xlim1)
        self.mpl_section.draw()

    def get_data_section(self):
        try:
            if self.widget_list_material_for_section.currentIndex() == -1:
                raise DataError

            sect = Sections(type_section=self.widget_list_type_section.currentText(),
                            x1=self.box_x1.value(), x2=self.box_x2.value(), x3=self.box_x3.value(),
                            y1=self.box_y1.value(), y2=self.box_y2.value(), y3=self.box_y3.value(),
                            b=self.box_b.value(), h=self.box_h.value(), d=self.box_d.value(),
                            e=self.box_e.value(), rx=self.box_rx.value(), ry=self.box_ry.value(),
                            nx=self.box_nx.value(), ny=self.box_ny.value(),
                            mat=self.widget_list_material_for_section.currentText(),
                            k=self.box_k.value())
            return sect
        except DataError:
            raise DataError

    def add_section(self):
        try:
            sect = self.get_data_section()

            self.list_save_section.append(sect)
            self.refresh_list_section()
        except DataError:
            self.show_error(u"Ошибка в данных")

    def refresh_list_section(self):
        self.table_section.clear()

        self.table_section.setRowCount(len(self.list_save_section))

        list_header = ["type_section", "mat", "k", "x1", "x2", "x3",
                       "y1", "y2", "y3",
                       "b", "h", "d",
                       "e", "rx", "ry",
                       "nx", "ny"]
        self.table_section.setColumnCount(len(list_header))

        self.table_section.setHorizontalHeaderLabels(list_header)

        for num_y, sect in enumerate(self.list_save_section):
            for num_x, key in enumerate(list_header):
                self.table_section.setItem(num_y, num_x, QtGui.QTableWidgetItem('{}'.format(sect.kwargs[key])))
                self.table_section.item(num_y, num_x).setFlags(QtCore.Qt.ItemFlags(1 + 2 + 4 + 8 + 6 + 12 + 64))

    def delete_section(self):
        try:
            number = self.table_section.currentRow()
            if number == -1:
                raise IndexError
            self.list_save_section.pop(number)
            self.refresh_list_section()
        except IndexError:
            self.show_error(u"Не выбрано сечение")

    def save_section(self):
        try:
            sect = self.get_data_section()
            number = self.table_section.currentRow()
            if number == -1:
                raise IndexError
            self.list_save_section.pop(number)
            self.list_save_section.insert(number, sect)
            self.refresh_list_section()
        except DataError:
            self.show_error(u"Ошибка в данных")
        except IndexError:
            self.show_error(u"Не выбрано сечение")

    def load_section(self):
        try:
            index = self.table_section.currentRow()
            if index == -1:
                raise IndexError
            self.load_data_section(self.list_save_section[index])
        except IndexError:
            self.show_error(u"Не выбрано сечение")

    def load_data_section(self, sect):
        type_sect = sect.kwargs["type_section"]
        current_index_section = self.list_section.index(unicode(type_sect))
        self.widget_list_type_section.setCurrentIndex(current_index_section)
        self.change_type_section()

        self.box_x1.setValue(sect.kwargs["x1"])
        self.box_x2.setValue(sect.kwargs["x2"])
        self.box_x3.setValue(sect.kwargs["x3"])
        self.box_y1.setValue(sect.kwargs["y1"])
        self.box_y2.setValue(sect.kwargs["y2"])
        self.box_y3.setValue(sect.kwargs["y3"])
        self.box_b.setValue(sect.kwargs["b"])
        self.box_h.setValue(sect.kwargs["h"])
        self.box_d.setValue(sect.kwargs["d"])
        self.box_e.setValue(sect.kwargs["e"])
        self.box_rx.setValue(sect.kwargs["rx"])
        self.box_ry.setValue(sect.kwargs["ry"])
        self.box_nx.setValue(sect.kwargs["nx"])
        self.box_ny.setValue(sect.kwargs["ny"])

        self.box_k.setValue(sect.kwargs["k"])

        material_section = sect.kwargs["mat"]
        name_material_in_save_list = [mat.kwargs["name"] for mat in self.list_save_material]
        current_index_material = name_material_in_save_list.index(material_section)

        self.widget_list_material_for_section.setCurrentIndex(current_index_material)

    def load_list_section(self):
        self.widget_list_type_section.clear()
        self.widget_list_type_section.addItems(self.list_section)

    def change_type_section(self):
        text_section = unicode(self.widget_list_type_section.currentText())
        if text_section in self.dict_prop_section.keys():
            list_prop_section = self.dict_prop_section[text_section]
            for widget, prop_enabled, def_prop in list_prop_section:
                widget.setEnabled(prop_enabled)
                widget.setValue(def_prop)

    def get_data_material(self):
        data_table_ps1 = self.get_data(self.table_ps1) if self.box_dia_ps1.isEnabled() else []
        data_table_ps2 = self.get_data(self.table_ps2) if self.box_dia_ps2.isEnabled() else []
        data_table_ps2_long = self.get_data(self.table_ps2_long) if self.box_dia_ps2_long.isEnabled() else []

        # get_type
        type_material = rcMaterial.type_material["concrete"] if self.list_type_material.currentIndex() == 0 else \
            rcMaterial.type_material["steel"]
        # get_properties
        if type_material == rcMaterial.type_material["steel"]:
            e = self.box_es.value()
            e_ult = self.box_es_ult.value()
            e_crit = self.box_es_crit.value()
            e0_ult = None
            et = None
            creep_ps1 = self.list_creep_ps1.currentIndex()
            creep_crack = self.list_creep_crack.currentIndex()
            creep_deform = self.list_creep_deform.currentIndex()

        elif type_material == rcMaterial.type_material["concrete"]:
            e = self.box_eb.value()
            e_ult = self.box_eb2_ult.value()
            e_crit = self.box_eb_crit.value()
            e0_ult = self.box_eb0_ult.value()
            et = self.box_ebt2.value()
            creep_ps1 = None
            creep_crack = None
            creep_deform = None
        name = self.text_name_material.text()

        # noinspection PyUnboundLocalVariable
        mat = Materials(name=name, type_material=type_material, data_table_ps1=data_table_ps1,
                        data_table_ps2=data_table_ps2, data_table_ps2_long=data_table_ps2_long,
                        e=e, e_ult=e_ult, e_crit=e_crit, creep_ps1=creep_ps1, creep_crack=creep_crack,
                        creep_deform=creep_deform, e0_ult=e0_ult, et=et)
        return mat

    def resave_material(self):
        try:
            mat = self.get_data_material()
            resave_index = self.list_materials.currentRow()
            if resave_index == -1:
                raise IndexError
            self.list_save_material.pop(resave_index)
            self.list_save_material.insert(resave_index, mat)
            self.refresh_list_material()
        except TypeError:
            self.show_error(u"Недопустимые данные в таблице")
        except DataError:
            self.show_error(u"Нарушен порядок в таблице")
        except IndexError:
            self.show_error(u"Не выбран материал")

    def delete_material(self):
        try:
            resave_index = self.list_materials.currentRow()
            if resave_index == -1:
                raise IndexError
            self.list_save_material.pop(resave_index)
            self.refresh_list_material()
        except IndexError:
            self.show_error(u"Не выбран материал")

    def load_material(self):
        try:
            resave_index = self.list_materials.currentRow()
            if resave_index == -1:
                raise IndexError
            self.load_data_material(self.list_save_material[resave_index])
        except IndexError:
            self.show_error(u"Не выбран материал")

    def load_data_material(self, mat):
        try:
            data_table_null = [[0, 0], [0, 0], [0, 0]]
            if mat.kwargs["data_table_ps1"] != []:
                self.load_data(self.table_ps1, self.box_number_ps1, mat.kwargs["data_table_ps1"])
            else:
                self.load_data(self.table_ps1, self.box_number_ps1, data_table_null)

            if mat.kwargs["data_table_ps2"] != []:
                self.load_data(self.table_ps2, self.box_number_ps2, mat.kwargs["data_table_ps2"])
            else:
                self.load_data(self.table_ps2, self.box_number_ps2, data_table_null)

            if mat.kwargs["data_table_ps2_long"] != []:
                self.load_data(self.table_ps2_long, self.box_number_ps2_long, mat.kwargs["data_table_ps2_long"])
            else:
                self.load_data(self.table_ps2_long, self.box_number_ps2_long, data_table_null)

            self.list_type_material.setCurrentIndex(
                    0 if mat.kwargs["type_material"] == rcMaterial.type_material["concrete"] else 1)

            # set _properties
            if mat.kwargs["type_material"] == rcMaterial.type_material["steel"]:
                self.box_es.setValue(mat.kwargs["e"])
                self.box_es_ult.setValue(mat.kwargs["e_ult"])
                self.box_es_crit.setValue(mat.kwargs["e_crit"])
                self.list_creep_ps1.setCurrentIndex(mat.kwargs["creep_ps1"])
                self.list_creep_crack.setCurrentIndex(mat.kwargs["creep_crack"])
                self.list_creep_deform.setCurrentIndex(mat.kwargs["creep_deform"])

            elif mat.kwargs["type_material"] == rcMaterial.type_material["concrete"]:
                self.box_eb.setValue(mat.kwargs["e"])
                self.box_eb2_ult.setValue(mat.kwargs["e_ult"])
                self.box_eb_crit.setValue(mat.kwargs["e_crit"])
                self.box_eb0_ult.setValue(mat.kwargs["e0_ult"])
                self.box_ebt2.setValue(mat.kwargs["et"])

            self.text_name_material.setText(mat.kwargs["name"])

        except DataError:
            raise DataError
            # except TypeError:
            #     raise TypeError

    def load_data(self, table, box, data):
        try:
            table.setRowCount(len(data))
            table.setColumnCount(len(data[0]))
            box.setValue(len(data))
            for j in xrange(table.rowCount()):
                for i in xrange(table.columnCount()):
                    table.item(j, i).setText(QtCore.QString("{}".format(data[j][i])))
        except DataError:
            raise DataError
            # except TypeError:
            #     raise TypeError

    def add_material(self):
        # get_table
        try:
            mat = self.get_data_material()
            self.list_save_material.append(mat)
            self.refresh_list_material()
        except TypeError:
            self.show_error(u"Недопустимые данные в таблице")
        except DataError:
            self.show_error(u"Нарушен порядок в таблице")

    def refresh_list_material(self):
        list_name_materials = [mat.kwargs["name"] for mat in self.list_save_material]
        self.list_materials.clear()
        self.list_materials.addItems(list_name_materials)

        self.widget_list_material_for_section.clear()
        self.widget_list_material_for_section.addItems(list_name_materials)

        list_material_in_section = [sect.kwargs["mat"] for sect in self.list_save_section]
        for num in range(len(list_material_in_section)):

            if not (list_material_in_section[len(list_material_in_section) - 1 - num] in list_name_materials):
                del_sect = self.list_save_section.pop(len(list_material_in_section) - 1 - num)
                self.show_error(u"Удалено сечение: {}".format(del_sect.kwargs["type_section"]))
        self.refresh_list_section()

    def check_data(self, lst):
        first_row = lst[0]
        for item in lst[1:]:
            if item[0] > first_row[0]:
                first_row = item
            else:
                raise DataError

    def get_data(self, table):
        try:
            lst = []
            for j in xrange(table.rowCount()):

                lst_temp = []
                for i in xrange(table.columnCount()):

                    text = table.item(j, i).text()
                    if "," in text:
                        text = text.replace(",", ".")
                    if not is_number(str(text.toUtf8())):
                        raise TypeError
                    else:
                        lst_temp.append(float(text))
                lst.append(lst_temp)

            self.check_data(lst)
            return np.array(lst)
        except DataError:
            raise DataError
        except TypeError:
            raise TypeError

    def plot2dgraphics(self, mplot, data, title):
        fig = mplot.figure
        ax = fig.add_subplot(111)
        ax.clear()

        ax.plot(data[:, 0], data[:, 1])
        ax.set_xlabel(title[0])
        ax.set_ylabel(title[1])

        mplot.draw()

    def plot_dia(self, table):
        mplot = self.mpl_material
        try:
            data = self.get_data(table)
            self.plot2dgraphics(mplot, data, ["e", u"sigma, kg/cm^2"])
        except TypeError:
            self.show_error(u"Недопустимые данные в таблице")
        except DataError:
            self.show_error(u"Нарушен порядок в таблице")

    # noinspection PyArgumentList,PyTypeChecker
    def show_error(self, text):
        QtGui.QMessageBox.warning(self, QtCore.QString(u"Ошибка"), QtCore.QString(text))

    def change_count_row_any_table(self, i, widget):
        """изменяем кол-во строк при изенении счетчика"""
        widget.setRowCount(i)
        for j in range(widget.rowCount()):
            for k in range(widget.columnCount()):
                if widget.item(j, k) is None:
                    widget.setItem(j, k, QtGui.QTableWidgetItem('0'))

    def change_type_material(self):
        if self.list_type_material.currentIndex() == 0:
            bol = True
        else:
            bol = False

        self.box_concrete_prop.setEnabled(bol)
        self.box_steel_prop.setEnabled(not bol)

    def changeCheckBoxSolve(self):
        '''v1 работает при изменении что и как считаем'''
        #        первый случай - нет галок вообще
        if self.checkBoxPS1.isChecked() == False and self.checkBoxPS2.isChecked() == False and \
                        self.checkBoxGraphics.isChecked() == False:
            self.checkBoxPS1.setChecked(True)
            self.checkBoxD.setChecked(False)
            self.changeCheckBoxSolve()
        # если расчет прочности галка стоит:
        if self.checkBoxPS1.isChecked() == True:
            self.checkBoxD.setEnabled(True)
        else:
            self.checkBoxD.setEnabled(False)
            self.checkBoxD.setChecked(False)

        self.changeSolvePS1(self.checkBoxPS1.isChecked())
        self.changeSolvePS2(self.checkBoxPS2.isChecked())
        self.changeSolveD(self.checkBoxD.isChecked())
        self.changeSolveGraphics(self.checkBoxGraphics.isChecked())

    def changeSolveGraphics(self, bol):
        self.changed()

    def changeSolvePS1(self, bol):
        """v1 переключаем при расчете по 1 ps:
        """
        self.box_dia_ps1.setEnabled(bol)

        self.changed()

    def changeSolvePS2(self, bol):
        """v1 переключаем при расчете по 2 ps
    """
        self.box_dia_ps2.setEnabled(bol)
        self.box_dia_ps2_long.setEnabled(bol)
        self.boxPS2.setEnabled(bol)

        self.changed()

    def changeSolveD(self, bol):
        '''v1 переключаем при расчете по D
    '''

        self.changed()

        self.boxPSD.setEnabled(bol)

    def changed(self):
        print "changed"

    def table_load_count_row(self):
        self.change_count_row_any_table(self.boxCountLoad.value(), self.tableLoad)

    def change_count_row_any_table(self, i, widget):
        """изменяем кол-во строк при изенении счетчика"""
        widget.setRowCount(i)
        for j in range(widget.rowCount()):
            for k in range(widget.columnCount()):
                if widget.item(j, k) is None:
                    widget.setItem(j, k, QtGui.QTableWidgetItem('0'))


class DataError(Exception):
    pass


class TypeErrorStrenght(Exception):
    pass


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
