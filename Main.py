import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from left_layout.Target import *
import Market

form_class = uic.loadUiType("resources\\main_window.ui")[0]


class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.target = Target(self)


if __name__ == "__main__":

    # KOSPI, KOSDAQ 정보 읽어 오기.
    Market.init()

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()

