from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from UiDesign.preWelding import Ui_Dialog
from PyQt5 import QtCore
import sys
import numpy
import machineLearning.weldCode.learnMethod
import machineLearning.weldCode.learnPara

class PredictWeldingMethodWindow(QDialog,Ui_Dialog):
    def __init__(self):
        super(PredictWeldingMethodWindow,self).__init__()
        self.preDiag=QDialog()
        self.setupUi(self.preDiag)
        self.retranslateUi(self.preDiag)
        #  窗口美化
        self.preDiag.setWindowOpacity(0.95)  # 设置窗口透明度
        self.preDiag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.closeButton.setFixedSize(15, 15)
        self.miniumButton.setFixedSize(15, 15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        # 定义信号与槽
        self.startButton.clicked.connect(self.startMethod)
        self.startParaButton.clicked.connect(self.startPara)


    def startMethod(self):
        height=float(self.height.text())
        width=float(self.width.text())
        method=machineLearning.weldCode.learnMethod.preWelding(height,width)
        # print(method)
        if(method[[0]]==0.0):
            self.method.setText("埋弧焊")
        else:
            self.method.setText("二氧化碳气体保护焊")
    def startPara(self):
        height=float(self.height.text())
        width=float(self.width.text())
        hansi=machineLearning.weldCode.learnPara.perPara(height,width,1)
        self.HanSi.setText(str(float(hansi[[0]])))
        A=machineLearning.weldCode.learnPara.perPara(height,width,3)
        V=machineLearning.weldCode.learnPara.perPara(height,width,4)
        self.DianLiu.setText(str(float(A[[0]])))
        self.DianYa.setText(str(float(V[[0]])))

