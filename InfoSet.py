import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from UiDesign.InfoSetDiag import Ui_Dialog
from PyQt5 import QtCore


class InfoWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.diag = QDialog()
        self.setupUi(self.diag)
        self.retranslateUi(self.diag)
        #  窗口美化
        self.diag.setWindowOpacity(0.95)  # 设置窗口透明度
        self.diag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.closeButton.setFixedSize(15, 15)
        self.miniumButton.setFixedSize(15, 15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidow = InfoWindow()
    mainWidow.diag.show()
    sys.exit(app.exec_())
