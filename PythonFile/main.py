from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import datetime
from Login import *
from Main_screen import *
from New_patient_registration import *
from Schedule import *
from patientsearch import *
from PatientProfile import *
import pymysql

class LoginScreen(QtWidgets.QMainWindow, Ui_LoginScreen):
    # Function for login button -- Add system to get and authenticate user/pass with database
    def Login(self):
        # Iterate through each username/password to find a match. If matched, open main screen. If no matches then display error message.
        i = 0
        while i != len(self.usernames):
            if self.login_Username.text() == self.usernames[i] and self.login_Password.text() == self.passwords[i]:
                self.mainScreen = MainScreen(self.fnames[i], self.lnames[i])
                self.mainScreen.show()
                self.close()
                break
            i = i + 1

        # i == len(self.usernames) means there were no matches so display error message
        if i == len(self.usernames):
            invalidLogin = QMessageBox()
            invalidLogin.setWindowTitle("Invalid Login")
            invalidLogin.setText("The username or password you entered is incorrect.\nPlease try again or contact an Administrator for assistance.")
            invalidLogin.addButton(QMessageBox.Ok)
            invalidLogin.exec()


    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)

        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd="sqlpassword", db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT * FROM logininfo")

        # Usernames and passwords pulled from database
        self.usernames = []
        self.passwords = []
        for username, password in self.c.fetchall():
            self.usernames.append(username)
            self.passwords.append(password)

        # User first and last names to display on main screen
        self.c.execute("SELECT firstName, lastName FROM employee")
        self.fnames = []
        self.lnames = []
        for firstName, lastName in self.c.fetchall():
            self.fnames.append(firstName)
            self.lnames.append(lastName)

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

    def __init__(self, fname, lname):
        super(MainScreen, self).__init__()
        self.setupUi(self)

        self.fname = fname
        self.lname = lname
        self.nameLabel.setText(self.fname + " " + self.lname)

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
        close.setText("Any unsaved information will be lost. Are you sure you wish to exit?")
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
        self.header = self.Schedule_list.item(0)
        self.selectedDate = self.Schedule_calendar.selectedDate()

        self.header.setText("Schedule for "+self.selectedDate.toString())


    def __init__(self, parent=None):
        super(Appointments, self).__init__(parent)
        self.setupUi(self)

        self.Schedule_calendar.selectionChanged.connect(self.onSelectionChange)

class PatientWidget(QtWidgets.QWidget):
    # Function for each access button -- Add system that searches self.PID in DB and opens patient profile with that information
    def access(self):
        self.Profile = PatientProfile(self.PID)

        self.Profile.show()

    def __init__(self, PID, fname, lname, DOB, lastVisit):
        super(PatientWidget, self).__init__()

        self.PID = PID
        self.fname = fname
        self.lname = lname
        self.DOB = str(DOB)
        self.lastVisit = lastVisit

        self.lbl = QtWidgets.QTextBrowser()
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("PatientSearch",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Name: "+self.fname+" "+self.lname+"</span></p>\n"
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
            if text.lower() in patient.fname.lower() or text.lower() in patient.lname.lower() or text.lower() in patient.PID.lower(): # Searchable by patient name or PID
                patient.show()
            else:
                patient.hide()

    def __init__(self, parent=None):
        super(PatientSearch, self).__init__(parent)
        self.setupUi(self)

        self.controls = QtWidgets.QWidget()
        self.controlsLayout = QtWidgets.QVBoxLayout()

        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd="sqlpassword", db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT patientID, firstName, lastName, DOB FROM patientprofile")
        # Patient info for testing -- update so each list pulls values from SQL DB
        self.PATIENT_ID = []
        self.PATIENT_FNAMES = []
        self.PATIENT_LNAMES = []
        self.PATIENT_DOB = []
        for pid, first, last, dob in self.c.fetchall():
            self.PATIENT_ID.append(pid)
            self.PATIENT_FNAMES.append(first)
            self.PATIENT_LNAMES.append(last)
            self.PATIENT_DOB.append(dob)

        self.PATIENT_LAST_VISIT = ["01/12/2222", "01/12/2222", "01/12/2222"]

        # List of each searchable patient widget -- these are not the actual patient objects
        self.patients = []

        # Create patient widget for each patient in database to search through
        i = 0
        while i != len(self.PATIENT_ID):
            item = PatientWidget(self.PATIENT_ID[i], self.PATIENT_FNAMES[i], self.PATIENT_LNAMES[i], self.PATIENT_DOB[i], self.PATIENT_LAST_VISIT[i])
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

class PatientProfile(QtWidgets.QMainWindow, Ui_PatientProfile):
    def closeEvent(self, event):
        close = QMessageBox()
        close.setWindowTitle("Are you sure?")
        close.setText("Any unsaved information will be lost. Are you sure you wish to exit?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def exit(self):
        self.close()

    def __init__(self, PID):
        super(PatientProfile, self).__init__()
        self.setupUi(self)

        self.PID = PID

        # DB Connection
        self.db = pymysql.connect(host="localhost", user="root", passwd="sqlpassword", db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT firstName, lastName FROM patientprofile WHERE patientID=%s", self.PID)

        for first, last in self.c.fetchall():
            self.fname = first
            self.lname = last

        # Edit patient profile based on info in database
        self.patientprofilestatus.setText("<html><head></head><body>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:10pt;'>Patient: " + self.fname + " " + self.lname + "</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:9pt;'>PID: " + self.PID + "</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Date Created: 07/18/19</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Last Updated: 05/05/20</span></p>"
                                            "</body></html>")
        # Button Click Events
        self.button_mainmenu.clicked.connect(self.exit)

if __name__ == "__main__":
    # This code simply starts the program and opens it with the login page (Dialog())
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = LoginScreen()
    login.show()
    sys.exit(app.exec_())
