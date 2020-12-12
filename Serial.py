import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox,QDialog
from UiDesign.serialUi_diag import Ui_Dialog



class SerialWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(SerialWindow, self).__init__()
        # app = QApplication(sys.argv)
        self.serialdiag = QDialog()
        self.setupUi(self.serialdiag)
        self.retranslateUi(self.serialdiag)
        # self.serialdiag.show()
        # sys.exit(app.exec_())


