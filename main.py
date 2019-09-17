from PyQt5 import QtWidgets

from MainUI.mainWindow import UIMainWindow


def start():
    app = QtWidgets.QApplication([])
    window = UIMainWindow()
    window.show()  # Se muestra la ventana
    app.exec()


if __name__ == "__main__":
    start()

