# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import datetime
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from New_patient_registration import *
from Login import *


class Ui_MainScreen(object):
    # Function for opening a new screen
    def openNPR(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NP_Registration()  # Use class name of GUI you want to open
        self.ui.setupUi(self.window)
        self.window.show()

    def logout(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        MainScreen.hide()

    def setupUi(self, MainScreen):
        font = QtGui.QFont()
        font.setPointSize(11)

        MainScreen.setObjectName("MD Home Page")
        MainScreen.resize(1100, 800)
        MainScreen.setMinimumSize(QtCore.QSize(1100, 800))
        MainScreen.setMaximumSize(QtCore.QSize(1100, 800))
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 50, 991, 661))
        self.listView.setObjectName("listView")
        self.Main_registerPatient = QtWidgets.QToolButton(self.centralwidget)
        self.Main_registerPatient.setGeometry(QtCore.QRect(345, 270, 191, 71))
        self.Main_registerPatient.setFont(font)
        self.Main_registerPatient.setObjectName("Main_registerPatient")

        # Click event for patient registration form
        self.Main_registerPatient.clicked.connect(self.openNPR)

        self.Main_search = QtWidgets.QToolButton(self.centralwidget)
        self.Main_search.setGeometry(QtCore.QRect(565, 270, 191, 71))
        self.Main_search.setFont(font)
        self.Main_search.setObjectName("Main_search")
        self.Main_GP = QtWidgets.QToolButton(self.centralwidget)
        self.Main_GP.setGeometry(QtCore.QRect(565, 370, 191, 71))
        self.Main_GP.setFont(font)
        self.Main_GP.setObjectName("Main_GP")
        self.Main_logout = QtWidgets.QToolButton(self.centralwidget)
        self.Main_logout.setGeometry(QtCore.QRect(470, 480, 161, 41))
        self.Main_logout.setFont(font)
        self.Main_logout.setObjectName("Main_logout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(860, 660, 181, 51))
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.addItem(item)
        self.Main_appts = QtWidgets.QToolButton(self.centralwidget)
        self.Main_appts.setGeometry(QtCore.QRect(345, 370, 191, 71))
        self.Main_appts.setFont(font)
        self.Main_appts.setObjectName("Main_appts")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 120, 361, 71))
        self.label.setObjectName("label")
        MainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        self.statusbar.setObjectName("statusbar")
        MainScreen.setStatusBar(self.statusbar)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        date = datetime.datetime.now()
        date = date.strftime("%c")

        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "MD Home Page"))
        self.Main_registerPatient.setText(_translate("MainScreen", "Register New Patient"))
        self.Main_search.setText(_translate("MainScreen", "Search Patients"))
        self.Main_GP.setText(_translate("MainScreen", "General Practice"))
        self.Main_logout.setText(_translate("MainScreen", "Log Out"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainScreen", "Dr. John Smith"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainScreen", date))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Main_appts.setText(_translate("MainScreen", "Appointments"))
        self.label.setText(_translate("MainScreen",
                                      "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Medical Doctor</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
