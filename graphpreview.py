import os
from tkinter import filedialog

import numpy
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import matplotlib as mpl
import csv


class UIGraphPreview(QMainWindow):

    def __init__(self, bode_manager):  # Conecta los componentes del .ui realizado en QT con el programa en python
        QMainWindow.__init__(self)
        loadUi('D:\PycharmProjects\TCVisa\graphpreview.ui', self)
        self.setWindowTitle("Graph Preview")
        self.ModuleWidget = self.graphwidget  # Objeto de la clase GraphWidget
        self.PhaseWidget = self.phaseGraph  # Objeto de la clase GraphWidget
        self.ModuleWidget.title = "Module"
        self.PhaseWidget.title = "Phase"
        self.ModuleWidget.x_label = "f [Hz]"
        self.PhaseWidget.x_label = "f [Hz]"
        self.PhaseWidget.y_label = "° [deg]"
        self.ModuleWidget.y_label = "|H| [dB]"
        self.ModuleWidget.canvas.axes.set_title(self.ModuleWidget.title)
        self.PhaseWidget.canvas.axes.set_title(self.PhaseWidget.title)
        self.saveButton.clicked.connect(self.save_action)
        self.__fix_axes_titles_position__(self.ModuleWidget)
        self.__fix_axes_titles_position__(self.PhaseWidget)
        self.bode_manager = bode_manager

    def plot_window(self):
        self.__plot_graph__(self.bode_manager.bode.frequencies, self.bode_manager.bode.module,
                            self.ModuleWidget)
        self.__plot_graph__(self.bode_manager.bode.frequencies, self.bode_manager.bode.phase,
                            self.PhaseWidget)

    # Funciones que configuran y muestran los titulos de los ejes.
    def __fix_axes_titles_position__(self, widget):
        self.__fix_y_title_position__(widget)
        self.__fix_x_title_position__(widget)

    def __fix_x_title_position__(self, widget):
        ticklabelpad = mpl.rcParams['xtick.major.pad']
        widget.canvas.axes.annotate(widget.x_label, xy=(1, 0), xytext=(20, -ticklabelpad),
                                    ha='left', va='top',
                                    xycoords='axes fraction', textcoords='offset points')

    def __fix_y_title_position__(self, widget):
        ticklabelpad = mpl.rcParams['ytick.major.pad']
        widget.canvas.axes.annotate(widget.y_label, xy=(0, 1), xytext=(-30, -ticklabelpad + 10),
                                    ha='left', va='bottom',
                                    xycoords='axes fraction', textcoords='offset points', rotation=0)

    # Función plot_graph. Se la llama de update_graph dibujar cada grafico.. Parametros: graph, valores del grafico a
    # mostrar; graph_widget: widget donde se añadirá el gráfico; color: color del gráfico.
    def __plot_graph__(self, x_values, y_values, graph_widget):

        graph_widget.canvas.axes.plot(x_values,  # Función principal que setea los gráficos a escala
                                      y_values,  # logarítmica con los valores indicados en los arrays.
                                      color='b', label='Best objective value')
        graph_widget.canvas.axes.set_xscale('log')
        graph_widget.canvas.axes.grid(True, which="both")

        graph_widget.canvas.draw()  # redibuja

    def save_action(self):

        myData = [['freqs', 'amp', 'phase']]

        for i in range(0, len(self.bode_manager.bode.frequencies)):
            myData.append([str(self.bode_manager.bode.frequencies[i]),
                           str(self.bode_manager.bode.module[i]),
                           str(self.bode_manager.bode.phase[i])])

        folder_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.save_csv(folder_path, myData, "auto_bode")
        self.errorLabel.setText("Mediciones guardadas.")

    def save_csv(self, folder_path, myData, name):
        i = 1
        if os.path.isfile(folder_path + "/" + name + ".csv"):
            while os.path.isfile(folder_path + "/" + name + "(" + str(i) + ").csv"):
                i = i + 1
            myFile = open(folder_path + "/" + name + "(" + str(i) + ").csv", 'w')
        else:
            myFile = open(folder_path + "/" + name + ".csv", 'w')

        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
