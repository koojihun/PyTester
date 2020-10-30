from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Utils.Markets import Markets
from conditions.ConditionManager import *
import qdarkstyle
import sys


form_class = uic.loadUiType("resources\\main_window.ui")[0]


class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTester_v0.1")
        self.setWindowIcon(QIcon('resources/icon_1.png'))

        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self._timeout)

    def _timeout(self):
        self.statusBar().showMessage(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":

    app = QApplication(sys.argv)

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # or in new API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    main_window = MainWindow()

    main_window.show()

    # KOSPI, KOSDAQ 정보 읽어 오기.
    markets = Markets()
    condition_manager = ConditionManager(main_window, markets)

    app.exec_()
