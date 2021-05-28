from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from UiDesign.DigitalTwinShowUI import Ui_Dialog
from PyQt5 import QtCore
import socket
import time


class DigitalTwinShow(QDialog,Ui_Dialog):
    def __init__(self):
        super(DigitalTwinShow,self).__init__()
        self.digitalShowDiag=QDialog()
        self.setupUi(self.digitalShowDiag)
        self.retranslateUi(self.digitalShowDiag)
        #  窗口美化
        self.digitalShowDiag.setWindowOpacity(0.95)  # 设置窗口透明度
        self.digitalShowDiag.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.closeButton.setFixedSize(15, 15)
        self.miniumButton.setFixedSize(15, 15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        # 定义信号与槽
        self.showButton.clicked.connect(self.startIP)
        print(2)


    def startIP(self):
        print(3)
        try:
            client = socket.socket()  # 有一些默认参数，即可使用ipv4，这一句是声明socket类型和返回socket连接对象
            client.connect(("172.20.3.233", 6969))
        except:
            print("打开展示端口错误")
        commandList=("roslaunch ur_gazebo ur5.launch;",
                     "roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true;",
                     "roslaunch ur5_moveit_config moveit_rviz.launch config:=true;",
                     "rosrun utest scence_attachytbak.py ;")
        for command in commandList:
            try:
                client.send(command.encode(encoding="utf-8"))
                print("发送命令：" + command)
                time.sleep(10)
            except:
                print("发送命令失败")

        client.close()
        # while True:
        #     msg = input("massage:").strip()
        #
        #     if len(msg) == 0:
        #         continue
        #
        #     client.send(msg.encode(encoding='utf-8'))  # 不能发空的东西
        #
        #     data = client.recv(1024)
        #     print(data.decode())

