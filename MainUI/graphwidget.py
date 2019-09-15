# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
# ------------------------------------------------------
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# Clase GraphWidget. Es la clase a la cual corresponden los rectángulos (widgets) donde se muestran los gráficos.
# Se asocian con un QWidget
class GraphWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.x_label = "Eje X"
        self.y_label = "Eje Y"
        self.title = " "
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)  # Canvas a agregar al widget
        self.toolbar = NavigationToolbar(self.canvas, self)  # cada gráfico tiene un toolbar con herramientos para
        # trabajar sobre él

        vertical_layout = QVBoxLayout()

        vertical_layout.addWidget(self.canvas)  # Se le agrega el canvas al widget
        vertical_layout.addWidget(self.toolbar)  # Se le agrega el toolbar al widget

        #
        self.canvas.axes = self.canvas.figure.add_subplot(111)  # Plotea el canvas. Si no se entiende que es el ploteo,
        # mirar
        # https://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111

        self.setLayout(vertical_layout)
