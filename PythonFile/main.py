from PyQt5 import QtWidgets
from Login import *
from Main_screen import *
from New_patient_registration import *


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        #self.mainScreen = MainScreen()
        #self.loginButton.clicked.connect(self.mainScreen.show)
        self.loginButton.clicked.connect(self.close)


class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.login = Dialog()
        self.Main_logout.clicked.connect(self.login.show)
        self.Main_logout.clicked.connect(self.close)
        self.NPR = NPRegistration()
        self.Main_registerPatient.clicked.connect(self.NPR.show)

class NPRegistration(QtWidgets.QMainWindow, Ui_NP_Registration):
    def __init__(self, parent=None):
        super(NPRegistration, self).__init__(parent)
        self.setupUi(self)
        self.NP_cancel.clicked.connect(self.hide)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainScreen()
    w.show()
    sys.exit(app.exec_())
