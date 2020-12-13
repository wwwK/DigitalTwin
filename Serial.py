import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox,QDialog
from UiDesign.serialUi_diag import Ui_Dialog
from PyQt5 import QtCore
import sqlite3

class SerialWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(SerialWindow, self).__init__()
        self.serialdiag = QDialog()
        self.setupUi(self.serialdiag)
        self.retranslateUi(self.serialdiag)
        #  窗口美化
        self.serialdiag.setWindowOpacity(0.95)  # 设置窗口透明度
        self.serialdiag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.closeButton.setFixedSize(15,15)
        self.miniumButton.setFixedSize(15,15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.fillText)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.I=0

    def start(self):
        self.timer.start(1000)
        #  测试数据库连接
        self.conn=sqlite3.connect('./DB/DigtalTwin.db')
        c=self.conn.cursor()
        cursor=c.execute('select * from mag')
        for row in cursor:
            print(row)
        self.plotElectricity.mpl.start_dynamic_plot()

    def stop(self):
        self.timer.stop()
        # self.db.close()
        self.conn.close()

    def fillText(self):
        self.AlineEdit.setText(str(self.I))
        self.I+=1




