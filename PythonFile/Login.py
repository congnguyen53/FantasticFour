# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PySide2.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_screen import Ui_MainScreen

class Ui_Login(object):
    #Define this function
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainScreen() #Use class name of GUI you want to open
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 518)
        self.loginButton = QtWidgets.QPushButton(MainWindow)
        self.loginButton.setGeometry(QtCore.QRect(240, 340, 93, 28))
        self.loginButton.setObjectName("loginButton")

        #Click event - loginButton is object name, openWindow is function name
        self.loginButton.clicked.connect(self.openWindow)

        self.registerButton = QtWidgets.QPushButton(MainWindow)
        self.registerButton.setGeometry(QtCore.QRect(420, 340, 93, 28))
        self.registerButton.setObjectName("registerButton")
        self.MD_title = QtWidgets.QLabel(MainWindow)
        self.MD_title.setGeometry(QtCore.QRect(260, 80, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title.setFont(font)
        self.MD_title.setObjectName("MD_title")
        self.MD_title2 = QtWidgets.QLabel(MainWindow)
        self.MD_title2.setGeometry(QtCore.QRect(140, 150, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title2.setFont(font)
        self.MD_title2.setObjectName("MD_title2")
        self.loginFormPassIn = QtWidgets.QLineEdit(MainWindow)
        self.loginFormPassIn.setGeometry(QtCore.QRect(334, 300, 182, 22))
        self.loginFormPassIn.setObjectName("loginFormPassIn")
        self.loginFormPassLabel = QtWidgets.QLabel(MainWindow)
        self.loginFormPassLabel.setGeometry(QtCore.QRect(241, 300, 83, 22))
        self.loginFormPassLabel.setObjectName("loginFormPassLabel")
        self.loginFormUserIn = QtWidgets.QLineEdit(MainWindow)
        self.loginFormUserIn.setGeometry(QtCore.QRect(334, 271, 182, 22))
        self.loginFormUserIn.setText("")
        self.loginFormUserIn.setObjectName("loginFormUserIn")
        self.loginFormUserLabel = QtWidgets.QLabel(MainWindow)
        self.loginFormUserLabel.setGeometry(QtCore.QRect(241, 271, 86, 22))
        self.loginFormUserLabel.setObjectName("loginFormUserLabel")
        self.loginButton.raise_()
        self.MD_title.raise_()
        self.MD_title2.raise_()
        self.registerButton.raise_()
        self.loginFormPassIn.raise_()
        self.loginFormPassLabel.raise_()
        self.loginFormUserIn.raise_()
        self.loginFormUserLabel.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.registerButton.setText(_translate("Dialog", "Register"))
        self.MD_title.setText(_translate("Dialog", "Medical Doctor"))
        self.MD_title2.setText(_translate("Dialog", "Hospital Management Software"))
        self.loginFormPassLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.loginFormUserLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Username</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
