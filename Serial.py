import sys
import serial  # 导入模块
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from UiDesign.serialUi_diag import Ui_Dialog
from PyQt5 import QtCore
import sqlite3
import pymysql
import GlobalVar
import random


class SerialWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(SerialWindow, self).__init__()
        self.serialdiag = QDialog()
        self.setupUi(self.serialdiag)
        self.retranslateUi(self.serialdiag)
        #  窗口美化
        self.serialdiag.setWindowOpacity(0.95)  # 设置窗口透明度
        self.serialdiag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.closeButton.setFixedSize(15, 15)
        self.miniumButton.setFixedSize(15, 15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerStart)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

    #     # 打开数据库连接
    #     db = pymysql.connect(host="172.20.112.146",port=3306,user="newroot", passwd="newroot", database="digitaltwin")
    #     createTable(db)
    #     insertData(db,0.0,0.0,0.0)
    #     # 关闭数据库连接
    #     db.close()

    def start(self):
        self.timer.start(1000)

        # AlineEdit填充变量
        self.I = 0

        # 串口接收对象
        try:
            # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
            portx = "COM3"
            # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
            bps = 115200
            # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
            timex = 5
            # 打开串口，并得到串口对象
            self.ser = serial.Serial(portx, bps, timeout=timex)

            print("串口详情参数：", self.ser)
            print(self.ser.port)  # 获取到当前打开的串口名
            print(self.ser.baudrate)  # 获取波特率
        except Exception as e:
            print("---打开端口异常---：", e)
        # 数据库对象
        self.db = pymysql.connect(host="172.20.85.220", port=3306, user="newroot", passwd="newroot",
                                  database="digitaltwin")
        # 跨文件变量初始化
        GlobalVar._init()

        # 画matplotlib
        self.plotElectricity.mpl.start_dynamic_plot()
        # self.plotV.mpl.start_dynamic_ploc()
        self.plotV.mpl.start_dynamic_plot()
        self.plotL.mpl.start_dynamic_plot()

    def stop(self):
        try:
            self.timer.stop()
            self.db.close()
            self.ser.close()
            self.plotElectricity.mpl.stop_dynamic_ploc()
            self.plotV.mpl.stop_dynamic_ploc()
            self.plotL.mpl.stop_dynamic_ploc()
        except Exception as e:
            print('---结束异常---',e)


    # timer每次调用的函数

    def timerStart(self):

        # self.readPort()
        self.simReadPort()
        self.saveToMysql()
        self.fillText()

    def fillText(self):

        self.AlineEdit.setText(str(self.data[0]))
        self.VlineEdit.setText(str(self.data[1]))
        self.LlineEdit.setText(str(self.data[2]))

    def saveToMysql(self):
        sql = "INSERT INTO WELDING (A, V, L) VALUES ('{0}','{1}', '{2}')".format(self.data[0], self.data[1], self.data[2])
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()

        except Exception as e:
            print('插入数据库失败：')
            print(e)
            self.db.rollback()

    def readPort(self):
        try:
            if self.ser.in_waiting:
                str = self.ser.read(self.ser.in_waiting).decode("gbk")
                print("收到数据：", str)
                alist = str.split(' ')
                alist = [float(i) for i in alist]
                print(alist)
                # 用来在这个文件中传递变量
                self.data = alist
                GlobalVar.set_value('I',alist[0])
                GlobalVar.set_value('V',alist[1])
                GlobalVar.set_value('L',alist[2])
        except Exception as e:
            print("---异常---：", e)

    def simReadPort(self):
        alist = [float(random.randint(0,10)) for i in range(3)]
        print(alist)
        # 用来在这个文件中传递变量
        self.data = alist
        GlobalVar.set_value('I', alist[0])
        GlobalVar.set_value('V', alist[1])
        GlobalVar.set_value('L', alist[2])


# # 以下是串口接收部分，有不懂的，learnSerial中有
# def listIfHavePort():
#     port_list = list(serial.tools.list_ports.comports())
#     print(port_list)
#     if len(port_list) == 0:
#         print('无可用串口')
#     else:
#         for i in range(0, len(port_list)):
#             print(port_list[i])
#
#
# def readPort():
#     try:
#
#         # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
#         portx = "COM3"
#         # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
#         bps = 115200
#         # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
#         timex = 5
#         # 打开串口，并得到串口对象
#         ser = serial.Serial(portx, bps, timeout=timex)
#         print("串口详情参数：", ser)
#
#         print(ser.port)  # 获取到当前打开的串口名
#         print(ser.baudrate)  # 获取波特率
#
#         # 循环接收数据，此为死循环，可用线程实现
#         while True:
#             if ser.in_waiting:
#                 str = ser.read(ser.in_waiting).decode("gbk")
#                 if (str == "exit"):  # 退出标志
#                     break
#                 else:
#                     print("收到数据：", str)
#                     alist = str.split(' ')
#                     alist = [float(i) for i in alist]
#                     print(alist)
#                     # for i in range(len(alist)):
#                     #     print(float(alist[i])+1)
#
#         print("---------------")
#         ser.close()  # 关闭串口
#
#
#     except Exception as e:
#         print("---异常---：", e)
