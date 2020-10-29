import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Markets import Markets
from conditions.ConditionManager import *


form_class = uic.loadUiType("resources\\main_window.ui")[0]


class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    # KOSPI, KOSDAQ 정보 읽어 오기.
    markets = Markets()
    condition_manager = ConditionManager(main_window, markets)

    app.exec_()

