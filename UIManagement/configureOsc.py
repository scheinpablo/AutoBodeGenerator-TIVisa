from enum import Enum

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class UIConfigOsc(QMainWindow):

    def __init__(self, bode_manager):  # Conecta los componentes del .ui realizado en QT con el programa en python
        QMainWindow.__init__(self)
        loadUi('UIManagement/configureOsc.ui', self)
        self.setWindowTitle("Oscilloscope Configuration")
        self.continueButton.clicked.connect(self.continue_action)
        self.backButton.clicked.connect(self.back_action)
        self.visa_string = ""
        self.channel_in = ChannelTypes.none
        self.channel_out = ChannelTypes.none
        self.probe_in = ProbeTypes.x1
        self.probe_out = ProbeTypes.x1
        self.bode_manager = bode_manager

    def back_action(self):
        self.bode_manager.show_prev_window()

    def continue_action(self):
        error = False
        # get visa string
        self.visa_string = self.visaStringOsc.toPlainText()

        # get channels
        channel_in_text = str(self.channelInBox.currentText())
        for channel in ChannelTypes:
            if channel_in_text == channel.value:
                self.channel_in = channel.value
        channel_out_text = str(self.channelOutBox.currentText())
        for channel in ChannelTypes:
            if channel_out_text == channel.value:
                self.channel_out = channel.value

        if self.channel_in == ChannelTypes.none.value or self.channel_out == ChannelTypes.none.value:
            error = True
            self.errorLabel.setText("Select a valid channel.")
        elif self.channel_in == self.channel_out:
            error = True
            self.errorLabel.setText("In & Out channels can't be the same.")

        # get probes
        if self.probeInCheck.isChecked():
            self.probe_in = ProbeTypes.x10

        if self.probeOutCheck.isChecked():
            self.probe_out = ProbeTypes.x10

        if not error:
            self.errorLabel.setText("")
            self.close()
            oscilloscope_configuration = {
                "visaString": self.visa_string,
                "channelIn": self.channel_in,
                "channelOut": self.channel_out,
                "probeIn": self.probe_in,
                "probeOut": self.probe_out,
            }
            self.bode_manager.bode_configuration.osc_config_params = oscilloscope_configuration
            self.bode_manager.show_next_window()


class ProbeTypes(Enum):
    """ ProbeTypes """
    x1 = "X1"
    x10 = "X10"


class ChannelTypes(Enum):
    """ ProbeTypes """
    channel1 = "CHANNEL1"
    channel2 = "CHANNEL2"
    channel3 = "CHANNEL3"
    channel4 = "CHANNEL4"
    none = "No Channel"



