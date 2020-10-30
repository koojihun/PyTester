from PyQt5.QtWidgets import QMessageBox


class Dialog:

    def show_err(msg):
        box = QMessageBox()
        box.setWindowTitle("ERROR")
        box.setIcon(QMessageBox.Critical)
        box.setText("잘못된 동작입니다." + "\n" + msg)
        box.exec_()
