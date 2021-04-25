import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from UiDesign.Uied1 import Ui_MainWindow
import Serial
from PyQt5 import QtCore
import PreditWeldingMethod


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.diag = QMainWindow()
        self.setupUi(self.diag)
        self.retranslateUi(self.diag)
        # 子窗口
        self.preWeldingMethod=PreditWeldingMethod.PredictWeldingMethodWindow()
        self.serialWindow = Serial.SerialWindow()

        self.init()

    def init(self):
        #  窗口美化
        self.diag.setWindowOpacity(0.9)  # 设置窗口透明度
        self.diag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.closeButton.setFixedSize(15,15)
        self.miniumButton.setFixedSize(15,15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        #  按钮信号与槽的连接
        self.portReceive.clicked.connect(self.openPort)
        self.WeldingMethodPredict.clicked.connect(self.openWeldingMethod)



    def openPort(self):

        self.serialWindow.serialdiag.show()
        self.serialWindow.serialdiag.exec_()

    def openWeldingMethod(self):
        print(1)
        self.preWeldingMethod.preDiag.show()
        self.preWeldingMethod.preDiag.exec_()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidow = MainWindow()
    mainWidow.diag.show()
    sys.exit(app.exec_())
