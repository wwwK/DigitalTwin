from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from UiDesign.preWelding import Ui_Dialog
from PyQt5 import QtCore
import sys

class PredictWeldingMethodWindow(QDialog,Ui_Dialog):
    def __init__(self):
        super(PredictWeldingMethodWindow,self).__init__()
        self.preDiag=QDialog()
        self.setupUi(self.preDiag)
        self.retranslateUi(self.preDiag)
        #  窗口美化
        self.preDiag.setWindowOpacity(0.95)  # 设置窗口透明度
        self.preDiag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.closeButton.setFixedSize(15, 15)
        # self.miniumButton.setFixedSize(15, 15)
        # self.closeButton.setStyleSheet(
        #     '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        # self.miniumButton.setStyleSheet(
        #     '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')


