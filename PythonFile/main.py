from PyQt5 import QtWidgets
from Login import *
from Main_screen import *
from New_patient_registration import *


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def openMain(self):
        self.mainScreen = MainScreen()
        self.mainScreen.show()
        self.hide()

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        self.loginButton.clicked.connect(self.openMain)


class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):
    def openLogin(self):
        self.NPR = Dialog()
        self.NPR.show()
        self.hide()

    def openNPR(self):
        self.NPR = NPRegistration()
        self.NPR.show()

    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.Main_logout.clicked.connect(self.openLogin)
        self.Main_registerPatient.clicked.connect(self.openNPR)

class NPRegistration(QtWidgets.QMainWindow, Ui_NP_Registration):
    def closeSelf(self):
        self.hide()

    def __init__(self, parent=None):
        super(NPRegistration, self).__init__(parent)
        self.setupUi(self)
        self.NP_cancel.clicked.connect(self.closeSelf)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())
