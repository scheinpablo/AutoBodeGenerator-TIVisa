from enum import Enum

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class UIConfigWaveGen(QMainWindow):
    def __init__(self, bode_manager):  # Conecta los componentes del .ui realizado en QT con el programa en python
        QMainWindow.__init__(self)
        loadUi('UIManagement/configureWaveGen.ui', self)
        self.setWindowTitle("Wave Generator Configuration")
        self.backButton.clicked.connect(self.back_action)
        self.continueButton.clicked.connect(self.continue_action)

        self.multipliers = {
            "Hz": 1,
            "kHz": 1000,
            "MHz": 1000000
        }

        self.visa_string = ""
        self.wave_form = WaveFormTypes.none
        self.start_freq = 0
        self.stop_freq = 0
        self.amplitude = 0
        self.bode_manager = bode_manager

    def back_action(self):
        self.bode_manager.show_prev_window()

    def continue_action(self):
        error = False
        # get visa string
        self.visa_string = self.visaStringWave.toPlainText()

        self.start_freq = int(round(self.startFreqBox.value() * self.multipliers[self.startFreqMult.currentText()],0))
        self.stop_freq = int(round(self.stopFreqBox.value() * self.multipliers[self.stopFreqMult.currentText()],0))
        self.amplitude = int(round(self.ampBox.value(),0))

        # get channels
        wave_form_text = str(self.waveFormBox.currentText())
        for wave_form_type in WaveFormTypes:
            if wave_form_text == wave_form_type.value:
                self.wave_form = wave_form_type.value

        if self.wave_form == WaveFormTypes.none.value:
            error = True
            self.errorLabel.setText("Select a valid wave form.")

        if self.stop_freq <= self.start_freq:
            error = True
            self.errorLabel.setText("Stop frequency must be higher than start frequency.")

        if not error:
            self.errorLabel.setText("")
            self.close()
            wave_form_configuration = {
                "visaString": self.visa_string,
                "waveForm": self.wave_form,
                "startFreq": self.start_freq,
                "stopFreq": self.stop_freq,
                "amplitude": self.amplitude
            }
            self.bode_manager.bode_configuration.wave_gen_config_params = wave_form_configuration
            self.bode_manager.show_next_window()


class WaveFormTypes(Enum):
    """ Wave Form Types """
    sineWave = "Sine Wave"
    squareWave = "Square Wave"
    triangleWave = "Triangle Wave"
    none = "No Wave"

