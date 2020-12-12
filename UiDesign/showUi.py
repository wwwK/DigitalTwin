import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QMessageBox
from UiDesign.Uied1 import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.diag=QMainWindow()
        self.setupUi(self.diag)
        self.retranslateUi(self.diag)
        self.portReceive.clicked.connect(self.openPort)

    def openPort(self):
        pass


if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWidow=MainWindow()
    mainWidow.diag.show()
    sys.exit(app.exec_())

