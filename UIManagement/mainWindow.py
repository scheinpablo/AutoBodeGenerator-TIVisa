from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from UIManagement.BodeConfiguration import BodeConfiguration, BodeManager
from UIManagement.configureOsc import UIConfigOsc


class UIMainWindow(QMainWindow):

    def __init__(self):  # Conecta los componentes del .ui realizado en QT con el programa en python
        QMainWindow.__init__(self)
        loadUi('UIManagement/mainWindow.ui', self)
        self.setWindowTitle("Instrument Automation")
        self.bodeButton.clicked.connect(self.bode_config)
        self.impedanceAnalizerButton.clicked.connect(self.impedance_ana_config)
        self.acAnalysisButton.clicked.connect(self.ac_ana_config)

    def ac_ana_config(self):
        i = 0

    def impedance_ana_config(self):
        i = 0


    def bode_config(self):
        self.bode_manager = BodeManager()
        self.hide()


      

