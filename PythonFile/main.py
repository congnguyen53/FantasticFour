from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import datetime
from Login import *
from Main_screen import *
from New_patient_registration import *
from Schedule import *
from patientsearch import *
from PatientProfile import *
from adminhub import *
from VisitHistory import *
from OrderTest import *
from TestStatus import *
import pymysql
from random import randint
import logging

sqlpassword = "Cc!0936481998"
logging.basicConfig(filename='system.log',level=logging.DEBUG)

class LoginScreen(QtWidgets.QMainWindow, Ui_LoginScreen):
    # Function for login button -- Add system to get and authenticate user/pass with database
    def Login(self):
        # Iterate through each username/password to find a match. If matched, open main screen. If no matches then display error message.
        i = 0
        while i != len(self.usernames):
            if self.login_Username.text() == self.usernames[i] and self.login_Password.text() == self.passwords[i]:
                # Check user type
                if self.types[i] != 0:
                    self.mainScreen = MainScreen(self.fnames[i], self.lnames[i], self.login_Username.text())
                    self.mainScreen.show()
                    self.close()

                    # Log
                    self.date = datetime.datetime.now()
                    logging.info("***USER " + self.login_Username.text() + " has logged IN @ " + str(self.date))
                    break
                else:
                    self.adminhub = AdminHub(self.login_Username.text())
                    self.adminhub.show()
                    self.close()

                    # Log
                    self.date = datetime.datetime.now()
                    logging.info("***USER " + self.login_Username.text() + " has logged IN @ " + str(self.date))
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
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT * FROM logininfo")

        # Usernames and passwords pulled from database
        self.usernames = []
        self.passwords = []
        for username, password in self.c.fetchall():
            self.usernames.append(username)
            self.passwords.append(password)

        # User first and last names to display on main screen
        self.c.execute("SELECT firstName, lastName, userType FROM employee")
        self.fnames = []
        self.lnames = []
        self.types = []
        for firstName, lastName, user in self.c.fetchall():
            self.fnames.append(firstName)
            self.lnames.append(lastName)
            self.types.append(user)

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

            # Log
            self.date = datetime.datetime.now()
            logging.info("***USER " + self.user + " has logged OUT @ " + str(self.date))

    # Function for opening new patient registration form
    def openNPR(self):
        self.NPR = NPRegistration(self.user)
        self.NPR.show()

    def openAppts(self):
        self.Appts = Appointments()
        self.Appts.show()

    def openPS(self):
        self.PS = PatientSearch(self.user)
        self.PS.show()

    def __init__(self, fname, lname, user):
        super(MainScreen, self).__init__()
        self.setupUi(self)

        self.fname = fname
        self.lname = lname
        self.user = user

        self.nameLabel.setText(
        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">%s %s</span></p></body></html>"%(self.fname, self.lname))

        # Button Click Events
        self.Main_logout.clicked.connect(self.Logout)
        self.Main_registerPatient.clicked.connect(self.openNPR)
        self.Main_appts.clicked.connect(self.openAppts)
        self.Main_search.clicked.connect(self.openPS)

class NPRegistration(QtWidgets.QMainWindow, Ui_NP_Registration):
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

    def insertQuery(self, id, lname, fname, DOB, age, sex, address, city, state, zip, primphone, secphone, insurance,
                    memID, eContactName, ePhone, eRelation):
        import datetime
        self.country = "United States"
        self.date = datetime.datetime.now()
        self.date = self.date.strftime("%Y%m%d")

        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.info = (id, lname, fname, DOB, age, sex, address, city, state, self.country, zip, primphone, secphone,
                     insurance, memID, eContactName, ePhone, eRelation, self.date, self.date)
        self.c.execute("INSERT INTO patientprofile (patientID, lastname, firstname, DOB, Age, Sex, streetaddress, "
                       "City, State, Country, Zip, primaryPhone, secondaryPhone, Insurance, MemberID, eContactName, "
                       "ePrimaryPhone, eRelation, dateVisited, dateCreated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", self.info)
        self.db.commit()

    def confirmMessage(self):
        message = QMessageBox()
        message.setWindowTitle("Patient Registered!")
        message.setText("Patient successfully registered!")
        message.addButton(QMessageBox.Ok)
        message.exec()

        self.hide()

        # Log
        self.date = datetime.datetime.now()
        logging.info("***USER " + self.user + " has created patient " + self.PID.upper() + " @ " + str(self.date))

    # Function for sacving and registering a new profile to the database and patient profile
    def saveInfo(self):
        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        try:
            # Get all info from input boxes
            # Create patient ID (first letter of first name + 3 first letters of last name + incrementing number value
            self.fname = self.NP_name_first.text()
            self.first = self.fname[0].lower()
            self.lname = self.NP_name_last.text()
            self.last = self.lname[0:3]
            # Get auto incrementing number (total patients plus one)
            self.c.execute("SELECT patientID FROM patientprofile")
            self.i = 0
            for id in self.c.fetchall():
                self.i = self.i + 1
            self.name = self.first + self.last.lower()
            self.PID = self.name + str(self.i + 1)
            self.DOB = self.NP_DOB.text()
            self.DOB = datetime.datetime.strptime(self.DOB, '%Y-%m-%d')
            self.now = datetime.datetime.now()
            self.age = self.now.year - self.DOB.year
            if self.NP_sex_M.isChecked() == True:
                self.sex = "M"
            else:
                self.sex = "F"
            self.address = self.NP_address.text()
            self.city = self.NP_city.text()
            self.state = self.NP_state.currentText()
            self.zip = int(self.NP_zip.text())
            self.primPhone = self.NP_prim_phone.text()
            self.secPhone = self.NP_sec_phone.text()
            self.insurance = self.NP_insurance.text()
            self.memberID = self.NP_memberID.text()
            self.eContactName = self.em_name.text()
            self.ePhone = self.em_prim_phone.text()
            self.eRelation = self.em_relationship.text()

            # Insert data into database
            self.insertQuery(self.PID, self.lname, self.fname, self.DOB, self.age, self.sex, self.address, self.city,
                             self.state, self.zip, self.primPhone, self.secPhone, self.insurance, self.memberID,
                             self.eContactName, self.ePhone, self.eRelation)
            # display confirmation and return to main screen
            self.confirmMessage()

        # catch error and display message
        except:
            invalidInput = QMessageBox()
            invalidInput.setWindowTitle("Invalid Input")
            invalidInput.setText("One or more fields were entered incorrectly. Please look over the form and ensure all values are correct.\n\n"
                                 "Fields with required formats:\n\t\t-DOB as \'YYYY-MM-DD\'\n\t\t-ZIP as a 6-digit whole number\n\t\t-Phone numbers as (888)888-8888")
            invalidInput.addButton(QMessageBox.Ok)
            invalidInput.exec()

    def __init__(self, user):
        super(NPRegistration, self).__init__()
        self.setupUi(self)
        self.user = user
        # Button Click Events
        self.NP_cancel.clicked.connect(self.close)
        self.NP_create.clicked.connect(self.saveInfo)

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
        self.Profile = PatientProfile(self.PID, self.user)
        self.Profile.show()

        # Log
        self.date = datetime.datetime.now()
        logging.info("***USER " + self.user + " has accessed patient " + self.PID.upper() + " @ " + str(self.date))

    def __init__(self, PID, fname, lname, DOB, lastVisit, user):
        super(PatientWidget, self).__init__()
        self.user = user
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

    def __init__(self, user):
        super(PatientSearch, self).__init__()
        self.setupUi(self)

        self.user = user

        self.controls = QtWidgets.QWidget()
        self.controlsLayout = QtWidgets.QVBoxLayout()

        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT patientID, firstName, lastName, DOB, dateVisited FROM patientprofile")

        # Patient info for testing -- update so each list pulls values from SQL DB
        self.PATIENT_ID = []
        self.PATIENT_FNAMES = []
        self.PATIENT_LNAMES = []
        self.PATIENT_DOB = []
        self.PATIENT_LAST_VISIT = []
        for pid, first, last, dob, date in self.c.fetchall():
            self.PATIENT_ID.append(pid)
            self.PATIENT_FNAMES.append(first)
            self.PATIENT_LNAMES.append(last)
            self.PATIENT_DOB.append(dob)
            self.PATIENT_LAST_VISIT.append(date.strftime("%m/%d/%Y"))



        # List of each searchable patient widget -- these are not the actual patient objects
        self.patients = []

        # Create patient widget for each patient in database to search through
        i = 0
        while i != len(self.PATIENT_ID):
            item = PatientWidget(self.PATIENT_ID[i], self.PATIENT_FNAMES[i], self.PATIENT_LNAMES[i], self.PATIENT_DOB[i], self.PATIENT_LAST_VISIT[i], self.user)
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

    def dateVisit(self):
        self.VisitHistory = VisitHistory(self.PID, self.user)
        self.VisitHistory.show()
        self.hide()

    def OrderTest(self):
        self.Order = OrderTest(self.PID)
        self.Order.show()

    def TestStatus(self):
        self.Status = TestStatus(self.PID, self.dateVisit)
        self.Status.show()

    def exit(self):
        self.close()

    def confirmMessage(self):
        message = QMessageBox()
        message.setWindowTitle("Patient Updated!")
        message.setText("Patient successfully updated!")
        message.addButton(QMessageBox.Ok)
        message.exec()

        # Log
        self.date = datetime.datetime.now()
        logging.info("***USER " + self.user + " has updated patient " + self.PID.upper() + " @ " + str(self.date))

    def insertQuery(self, lname, fname, DOB, age, weight, height, sex, address, city, state, country, zip, primphone, secphone, insurance,
                    memID, eName, ePhone, eRel, id):
        import datetime
        self.date = datetime.datetime.now()
        self.date = self.date.strftime("%Y-%m-%d")
        DOB = DOB.strftime("%Y-%m-%d")

        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.info = (lname, fname, DOB, age, weight, height, sex, address, city, state, country, zip, primphone, id)
        self.c.execute("UPDATE patientprofile SET lastname = %s, firstname = %s, DOB = %s, Age = %s, Weight = %s,"
                       "Height = %s, Sex = %s, streetaddress = %s, City = %s, State = %s, Country = %s, Zip = %s, "
                       "primaryPhone = %s WHERE patientID = %s", self.info)
        self.db.commit()

        #MySQL would not execut as a single function so it had to be split in 2
        self.info2 = (secphone, insurance, memID, eName, ePhone, eRel, id)
        self.c.execute("UPDATE patientprofile SET secondaryPhone = %s, Insurance = %s, MemberID = %s, eContactName = %s, "
                       "ePrimaryPhone = %s, eRelation = %s WHERE patientID = %s", self.info2)
        self.db.commit()

    def saveInfo(self):
        # DB connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        try:
            # Get all info from input boxes
            self.DOB = self.in_dob.text()
            self.DOB = datetime.datetime.strptime(self.DOB, "%Y-%m-%d")
            self.age = int(self.in_age.text())
            self.weight = int(self.in_weight.text())
            self.height = self.in_height.text()
            self.sex = self.in_sex.text()
            self.address = self.in_street.text()
            self.city = self.in_city.text()
            self.state = self.in_state.text()
            self.country = self.in_country.text()
            self.zip = int(self.in_zip.text())
            self.primPhone = self.in_primcontact.text()
            self.secPhone = self.in_seccontact.text()
            self.insurance = self.in_insurance.text()
            self.memberID = self.in_memid.text()
            self.eContactName = self.in_emername.text()
            self.ePhone = self.in_emerprimcontact.text()
            self.eRelation = self.in_emergencyrelation.text()

            # Insert data into database
            self.insertQuery(self.lname, self.fname, self.DOB, self.age, self.weight, self.height, self.sex, self.address, self.city,
                             self.state, self.country, self.zip, self.primPhone, self.secPhone, self.insurance, self.memberID,
                             self.eContactName, self.ePhone, self.eRelation, self.PID)
            # display confirmation and return to main screen
            self.confirmMessage()

        # catch error and display message
        except:
            invalidInput = QMessageBox()
            invalidInput.setWindowTitle("Invalid Input")
            invalidInput.setText(
                "One or more fields were entered incorrectly. Please look over the form and ensure all values are correct.\n\n"
                "Fields with required formats:\n\t\t-DOB as \'YYYY-MM-DD\'\n\t\t-ZIP as a 6-digit whole number\n\t\t-Phone numbers as (888)888-8888")
            invalidInput.addButton(QMessageBox.Ok)
            invalidInput.exec()

    def __init__(self, PID, user):
        super(PatientProfile, self).__init__()
        self.setupUi(self)
        self.PID = PID
        self.user = user

        # DB Connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT firstName, lastName, DOB, Age, Weight, Height, Sex, streetaddress, City, State, Country, Zip, primaryPhone, secondaryPhone, Insurance, MemberID, eContactName, eRelation, ePrimaryPhone, dateVisited FROM patientprofile WHERE patientID=%s", self.PID)
        for first, last, dob, age, weight, height, sex, street, city, state, country, zip, primphone, secphone, insur, memberid, econtactname, erela, eprimphone, datevisited in self.c.fetchall():
            self.fname = first
            self.lname = last
            self.DOB = dob

            self.Age = age
            self.Weight = weight
            self.Height = height
            self.Street = street
            self.Sex = sex
            self.City = city
            self.State = state
            self.Country = country
            self.Zip = zip
            self.PrimPhone = primphone
            self.SecPhone = secphone
            self.Insur = insur
            self.MemberID = memberid
            self.Econtactname = econtactname
            self.Erelation = erela
            self.Eprimphone = eprimphone
            self.LastestdateVisited = datevisited

        _translate = QtCore.QCoreApplication.translate
        # Edit patient profile based on info in database
        self.patientprofilestatus.setText("<html><head></head><body>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:9pt;'>Patient ID: " + self.PID + "</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Date Created: 07/18/19</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Last Updated: 05/05/20</span></p>"
                                            "</body></html>")
        # Button Click Events
        self.in_age.setText(str(self.Age))
        self.in_weight.setText(str(self.Weight))
        self.in_height.setText(str(self.Height))
        self.in_street.setText(str(self.Street))
        self.in_city.setText(str(self.City))
        self.in_state.setText(str(self.State))
        self.in_country.setText(str(self.Country))
        self.in_primcontact.setText(str(self.PrimPhone))
        self.in_seccontact.setText(str(self.SecPhone))
        self.in_insurance.setText(str(self.Insur))
        self.in_memid.setText(str(self.MemberID))
        self.in_emerprimcontact.setText(str(self.Eprimphone))
        self.in_emername.setText(str(self.Econtactname))
        self.in_emergencyrelation.setText(str(self.Erelation))
        self.in_zip.setText(str(self.Zip))
        self.in_sex.setText(str(self.Sex))
        self.headlinename.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head> "
                                             "<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+self.fname+" "+self.lname+"</p></body></html>"))

        self.saveButton.clicked.connect(self.saveInfo)
        self.button_mainmenu.clicked.connect(self.exit)
        self.button_ordertest.clicked.connect(self.OrderTest)
        self.button_teststatus.clicked.connect(self.TestStatus)

        # For 1st time patients, their weight and height will not have been filled in yet since they have never visited -- this prevents crash
        if self.Weight == None or self.Height == None:
            self.in_weight.setText("0")
            self.in_height.setText("0")
            self.NewVisit()
        else:
            self.dateVisitMedical(self.LastestdateVisited)

        #Open Date Visit
        self.button_datevisit.clicked.connect(self.dateVisit)

    def dateVisitMedical(self,dateVisited):
        self.date = dateVisited
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT visitNotes,diagnosis,testrequested, chiefComplaint, medicalhistory, Allergies, Symptoms, MedicationAssigned, Doctor,medication_oral, dose_oral, duration_oral, type_injection,note_injection FROM patientmedicalinfo WHERE dateVisited=%s AND PatientID=%s",
            (self.date,self.PID))
        for visit,dia,test, chief, medicalhis, aller,symp,medication,doctor,med_oral,dose_oral, duration_oral, type_injection,note_injection in self.c.fetchall():
            self.VisitNote = visit
            self.Diagnosis = dia
            self.TestRe = test
            self.ChiefCom = chief
            self.MedicalHis = medicalhis
            self.Aller = aller
            self.Symptomp = symp
            self.Medication = medication
            self.Doctor = doctor
            self.Med_oral = med_oral
            self.Dose_oral = dose_oral
            self.Duration_oral = duration_oral
            self.Type_injection = type_injection
            self.Note_injection = note_injection

        self.in_chiefcom.setPlainText(str(self.ChiefCom))
        self.in_doctor.setText("Dr "+str(self.Doctor))
        self.in_visitnote.setPlainText(str(self.VisitNote))
        self.in_medication.setPlainText(str(self.Medication))
        self.in_symptoms.setPlainText(str(self.Symptomp))
        self.in_medhistory.setPlainText(str(self.MedicalHis))
        self.in_allergies.setPlainText(str(self.Aller))
        self.in_reqtest.setPlainText(str(self.TestRe))
        self.in_diagnosis.setPlainText(str(self.Diagnosis))
        self.in_medicationadvised.setPlainText(str(self.Med_oral))
        self.in_doseadvised.setPlainText(str(self.Dose_oral))
        self.in_datemed.setText(str(self.date))
        self.in_notesinjection.setHtml(
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(self.Note_injection)+"</p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>")
        self.in_datetakeninjection.setText(str(self.date))


        self.patientprofilestatus.setText("<html><head></head><body>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:9pt;'>Patient ID: " + self.PID + "</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Date Visit: "+str(self.date)+"</span></p>"
                                            "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Last Updated: "+str(self.LastestdateVisited)+"</span></p>"
                                            "</body></html>")
    def NewVisit(self):
        self.in_chiefcom.setPlainText("")
        self.in_doctor.setText("")
        self.in_visitnote.setPlainText("")
        self.in_medication.setPlainText("")
        self.in_symptoms.setPlainText("")
        self.in_allergies.setPlainText("")
        self.in_reqtest.setPlainText("")
        self.in_diagnosis.setPlainText("")
        self.in_chiefcom.setPlainText("")
        self.in_visitnote.setPlainText("")
        self.in_medication.setPlainText("")
        self.in_symptoms.setPlainText("")
        self.in_medhistory.setPlainText("")
        self.in_allergies.setPlainText("")
        self.in_reqtest.setPlainText("")
        self.in_diagnosis.setPlainText("")
        self.in_medicationadvised.setPlainText("")
        self.in_doseadvised.setPlainText("")
        self.in_datemed.setText("")
        self.in_notesinjection.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + "" + "</p>\n"
                                                                                                                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>")

        self.date1 = datetime.datetime.now()
        self.date1 = self.date1.strftime("%Y-%m-%d")

        self.patientprofilestatus.setText("<html><head></head><body>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:9pt;'>Patient ID: " + self.PID + "</span></p>"
                                                                                                                                                    "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Date Visit: " + str(
            self.date1) + "</span></p>"
                          "<p style=\" margin-top:0px; margin-bottom:0px;\"><span style='font-size:8pt;'>Last Updated: " + str(
            self.LastestdateVisited) + "</span></p>"
                                       "</body></html>")

class AdminHub(QtWidgets.QMainWindow, Ui_AdminHub):
    def confirmMessage(self):
        # Confirm registration and display info for user
        message = QMessageBox()
        message.setWindowTitle("User Registered!")
        message.setText("User successfully registered! Remember these login credentials:\n\n\t"
                        "Username:\t" + self.username + "\n\tPassword:\t" + str(self.password) + "\n\n"
                        "DO NOT SHARE YOUR PASSWORD WITH ANYONE!")
        message.addButton(QMessageBox.Ok)
        message.exec()

    def registerUser(self):
        # Get info to save to database for registering new user
        self.name = self.in_name.text()
        self.name = self.name.split()
        self.fos = self.in_fieldofstudy.currentText()
        self.dep = self.in_department.currentText()
        self.dateJoin = datetime.datetime.now()
        self.dateJoin = self.dateJoin.strftime("%Y%m%d")
        self.DOB = self.in_dob.text()
        self.DOB = datetime.datetime.strptime(self.DOB, '%Y-%m-%d')
        self.type = self.in_usertype.currentText()
        if self.type == "Admin":
            self.type = 0
        elif self.type == "Doctor":
            self.type = 1
        else:
            self.type = 2

        # DB Connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()

        # Create username -- first 3 of last name plus 100 (increments only if another user has same name)
        self.num = 100
        self.last = self.name[1][0:3].lower()
        self.username = (self.last + str(self.num))
        # Check if user exists
        self.c.execute("SELECT username FROM employee")
        for user in self.c.fetchall():
            if self.username == user[0]:
                self.num = self.num + 1
                self.username = (self.last + str(self.num))

        self.info = (self.username, self.name[1], self.name[0], self.type, self.fos, self.dep, self.dateJoin, self.DOB)
        self.c.execute("INSERT INTO employee(username, lastname, firstname, userType, fieldofstudy, department, datejoined, DOB) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", self.info)
        self.db.commit()
        # Save user and generate password for logininfo
        self.password = randint(1000, 9999)
        self.info = (self.username, self.password)
        self.c.execute("INSERT INTO logininfo(username, password) VALUES(%s, %s)", self.info)
        self.db.commit()
        self.confirmMessage()

    def updateSearch(self, text):
        search = self.listWidget.findItems(text, Qt.MatchContains | Qt.MatchCaseSensitive)
        for i in search:
            print(i.text())

    def clearLog(self):
        self.listWidget.clear()
        self.f.truncate(0)

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

            # Log
            self.date = datetime.datetime.now()
            logging.info("***USER " + self.user + " has logged OUT @ " + str(self.date))
    def __init__(self, username):
        super(AdminHub, self).__init__()
        self.setupUi(self)

        # Load Log History
        self.f = open("system.log", "r+")
        for line in self.f:
            self.listWidget.addItem(line)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.listWidget.setFont(font)

        self.user = username

        # DB Connection
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute("SELECT firstname FROM employee WHERE username = '%s'" % self.user)

        for first in self.c.fetchone():
            self.first = first

        # Display name on welcome message
        self.label_4.setText(self.first + "!")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_4.setFont(font)

        # Button Click events
        self.button_register.clicked.connect(self.registerUser)
        self.lineEdit.textChanged.connect(self.updateSearch)
        self.clearButton.clicked.connect(self.clearLog)
        self.logout.clicked.connect(self.Logout)

class VisitHistory(QtWidgets.QMainWindow, Ui_VisitHistory):
    def __init__(self, PID, user):
        super(VisitHistory, self).__init__()
        self.setupUi(self)
        self.user = user
        self.PID = PID
        self.controls = QtWidgets.QWidget()
        self.controlsLayout = QtWidgets.QVBoxLayout()

        self.in_patientID_visithistory.setText(str(PID))
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT dateVisited FROM patientmedicalinfo WHERE patientID=%s",self.PID)
        self.dateVisited = []
        for date in self.c.fetchall():
            self.dateVisited.append(date)
        for i in range(len(self.dateVisited)):
            self.datevisithistory.addItem("")
            self.datevisithistory.setItemText(i+1,self.dateVisited[i][0].strftime("%m/%d/%Y"))

        #self.button_openvisithistory.clicked.connect(VisitHis.dateVisitMedical(self.dateVisited[index]))
        self.button_openvisithistory.clicked.connect(self.openDate)
    def openDate(self):
        index = self.datevisithistory.currentIndex() - 1
        self.Profile = PatientProfile(self.PID,self.user)
        if index >= 0:
            self.Profile.dateVisitMedical(self.dateVisited[index][0])
        else:
            self.Profile.NewVisit()
        self.Profile.show()
        self.close()

class OrderTest(QtWidgets.QMainWindow, Ui_OrderTest):
    def __init__(self,PID):
        super(OrderTest, self).__init__()
        self.setupUi(self)
        self.PID = PID
        self.controls = QtWidgets.QWidget()
        self.controlsLayout = QtWidgets.QVBoxLayout()

        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.in_patid.setText(str(self.PID))
        self.in_patid_2.setText(str(self.PID))
        self.in_patid_3.setText(str(self.PID))
        self.in_patid_4.setText(str(self.PID))
        self.date = datetime.datetime.now()
        self.date = self.date.strftime("%Y-%m-%d")

        self.button_ordertest.clicked.connect(lambda:self.Order(0))
        self.button_ordertest_2.clicked.connect(lambda:self.Order(1))
        self.button_ordertest_3.clicked.connect(lambda:self.Order(2))
        self.button_ordertest4.clicked.connect(lambda:self.Order(3))



    def Order(self,index):
        self.patid = self.in_patid.text()
        self.status = "Ordered"
        if index == 0:
            self.maintype = "Hematologic"
            self.note = self.in_notes.toPlainText()
            self.prior = self.in_priority.currentText()
            self.type = self.in_type.currentText()
        elif index == 1:
            self.maintype = "Urine Test"
            self.note = self.in_notes_2.toPlainText()
            self.prior = self.in_priority_2.currentText()
            self.type = self.in_type_2.currentText()
        elif index == 2:
            self.maintype = "Stool Test"
            self.note = self.in_notes_3.toPlainText()
            self.prior = self.in_priority_3.currentText()
            self.type = self.in_type_3.currentText()
        else:
            self.maintype = "Radiologic"
            self.note = self.in_notes_4.toPlainText()
            self.prior = self.in_priority_4.currentText()
            self.type = self.in_type_4.currentText()

        self.info = (self.patid, self.maintype, self.type, self.date, self.prior, self.note, self.status)
        self.c.execute("INSERT INTO test(patientID,mainTestType,subType,dateOrder,Priority,Notes,Status) VALUES(%s, %s, %s, %s, %s, %s, %s)", self.info)
        self.db.commit()

        message = QMessageBox()
        message.setWindowTitle("Test Ordered!")
        message.setText("Lab test successfully ordered!")
        message.addButton(QMessageBox.Ok)
        message.exec()

class TestStatus(QtWidgets.QMainWindow, Ui_Test):
    def  __init__(self, PID, Date):
        super(TestStatus, self).__init__()
        self.setupUi(self)
        self.PID = PID
        self.Date = Date
        self.controls = QtWidgets.QWidget()
        self.controlsLayout = QtWidgets.QVBoxLayout()
        self.db = pymysql.connect(host="localhost", user="root", passwd=sqlpassword, db="hospitaldb")
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT Status,max(dateOrder),mainTestType,subType,Notes,Priority FROM test WHERE patientID=%s", self.PID)
        for Status,dateOrder,mainTestType,subType,Notes,Priority in self.c.fetchall():
            self.status = Status
            self.DateOrder = dateOrder
            self.MainTest = mainTestType
            self.subTest = subType
            self.Note = Notes
            self.Pri = Priority

        self.in_patid.setHtml(           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(self.PID)+"</p></body></html>")
        self.in_teststatus.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(self.status)+"</p></body></html>")
        self.in_dateorder.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(self.DateOrder)+"</p></body></html>")
        self.in_type.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                             "p, li { white-space: pre-wrap; }\n"
                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8.25pt; color:#000000; background-color:#ffffff;\">"+str(self.MainTest)+" -  "+str(self.subTest)+"</span></p></body></html>")
        self.in_note.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                            "p, li { white-space: pre-wrap; }\n"
                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8.25pt; color:#000000; background-color:#ffffff;\">"+"Notes: "+str(self.Pri)+" -  "+str(self.Note)+"</span></p></body></html>")

if __name__ == "__main__":
    # This code simply starts the program and opens it with the login page (LoginScreen())
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = LoginScreen()
    login.show()
    sys.exit(app.exec_())
