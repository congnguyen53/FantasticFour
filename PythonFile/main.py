from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import datetime
from Login import *
from Main_screen import *
from New_patient_registration import *
from Schedule import *
from patientsearch import *

class LoginScreen(QtWidgets.QMainWindow, Ui_LoginScreen):
    # Function for login button -- Add system to get and authenticate user/pass with database
    def Login(self):
        self.mainScreen = MainScreen()
        self.mainScreen.show()
        self.close()

    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)

        # Button Click Events
        self.loginButton.clicked.connect(self.Login)
        self.exitButton.clicked.connect(sys.exit)

class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):
    # Function for logout button -- no need for technical system since the only way to get back is through login system
    def Logout(self):
        logout = QMessageBox()
        logout.setWindowTitle("Confirm Logout")
        logout.setText("Are you sure you wish to log out?")
        logout.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        logout = logout.exec()

        if logout == QMessageBox.Yes:
            self.login = LoginScreen()
            self.login.show()
            self.close()

    # Function for opening new patient registration form
    def openNPR(self):
        self.NPR = NPRegistration()
        self.NPR.show()

    def openAppts(self):
        self.Appts = Appointments()
        self.Appts.show()

    def openPS(self):
        self.PS = PatientSearch()
        self.PS.show()

    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)

        # Button Click Events
        self.Main_logout.clicked.connect(self.Logout)
        self.Main_registerPatient.clicked.connect(self.openNPR)
        self.Main_appts.clicked.connect(self.openAppts)
        self.Main_search.clicked.connect(self.openPS)

class NPRegistration(QtWidgets.QMainWindow, Ui_NP_Registration):
    # Function to catch a close event and ensure the user does not need to save any information
    def closeEvent(self, event):
        close = QMessageBox()
        close.setWindowTitle("Are you sure?")
        close.setText("Any unsaved information will be lost. Are you sure you wish to cancel?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __init__(self, parent=None):
        super(NPRegistration, self).__init__(parent)
        self.setupUi(self)

        # Button Click Events
        self.NP_cancel.clicked.connect(self.close)

class Appointments(QtWidgets.QMainWindow, Ui_Appointments):
    def onSelectionChange(self):
        self.Schedule_list

    def __init__(self, parent=None):
        super(Appointments, self).__init__(parent)
        self.setupUi(self)

        self.Schedule_calendar.selectionChanged.connect(self.onSelectionChange)

class PatientWidget(QtWidgets.QWidget):
    # Function for each access button -- Add system that searches PID in DB and returns patient profile with that information
    def access(self):
        print("SUCCESS")

    def __init__(self, name, PID, DOB, lastVisit):
        super(PatientWidget, self).__init__()

        self.name = name
        self.PID = PID
        self.DOB = DOB
        self.lastVisit = lastVisit

        self.lbl = QtWidgets.QTextBrowser()
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setHtml(_translate("PatientSearch",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Name: "+self.name+"</span></p>\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Patient ID: "+self.PID+"</span></p>\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">DOB: "+self.DOB+"</span></p>\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Last Visit: "+self.lastVisit+"</span></p></body></html>"))
        self.lbl.setFixedWidth(301)
        self.lbl.setFixedHeight(101)


        self.accessBtn = QtWidgets.QPushButton("Access")
        self.accessBtn.setFixedWidth(191)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accessBtn.setFont(font)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(self.accessBtn)
        self.setLayout(self.hbox)

        self.accessBtn.clicked.connect(self.access)

class PatientSearch(QtWidgets.QMainWindow, Ui_PatientSearch):
    def updateSearch(self, text):
        for patient in self.patients:
            if text.lower() in patient.name.lower() or text.lower() in patient.PID.lower(): # Searchable by patient name or PID
                patient.show()
            else:
                patient.hide()

    def __init__(self, parent=None):
        super(PatientSearch, self).__init__(parent)
        self.setupUi(self)

        self.controls = QtWidgets.QWidget()
        self.controlsLayout = QtWidgets.QVBoxLayout()

        # Patient info for testing -- update so each list pulls values from SQL DB
        PATIENT_NAMES = ["Jenna Johnson", "Donald Trump", "Kobe Bryant", "Jenna Johnson", "Donald Trump", "Kobe Bryant"]
        PATIENT_DOB = ["01/21/1972", "06/14/1943", "12/12/1912", "01/21/1972", "06/14/1943", "12/12/1912",]
        PATIENT_IDs = ["jjohnson001", "dtrump420", "kbryantRIP", "jjohnson001", "dtrump420", "kbryantRIP"]
        PATIENT_LAST_VISIT = ["01/12/2222", "01/12/2222", "01/12/2222", "01/12/2222", "01/12/2222", "01/12/2222"]

        # List of each searchable patient widget -- these are not the actual patient objects
        self.patients = []

        # Create patient widget for each patient in database to search through
        i = 0
        while i != len(PATIENT_NAMES):
            item = PatientWidget(PATIENT_NAMES[i], PATIENT_IDs[i], PATIENT_DOB[i], PATIENT_LAST_VISIT[i])
            self.controlsLayout.addWidget(item)
            self.patients.append(item)
            i = i + 1


        # Spacer between each patient widget
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        # Scroll bar
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        # Container for patient widgets
        container = QtWidgets.QWidget()
        containerLayout = QtWidgets.QVBoxLayout()
        container.setLayout(containerLayout)

        # Search Bar
        self.searchBar = QtWidgets.QLineEdit()
        self.searchBar.setPlaceholderText("Search Patients...")
        self.searchBar.textChanged.connect(self.updateSearch)

        containerLayout.addWidget(self.searchBar)
        containerLayout.addWidget(self.scroll)
        self.setCentralWidget(container)
        self.setWindowTitle("Patient Search")

if __name__ == "__main__":
    # This code simply starts the program and opens it with the login page (Dialog())
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = LoginScreen()
    login.show()
    sys.exit(app.exec_())
