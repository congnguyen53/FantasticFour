# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_screen import *

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        font = QtGui.QFont()
        font.setPointSize(11)
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(1100, 800)
        LoginScreen.setMinimumSize(QtCore.QSize(1100, 800))
        LoginScreen.setMaximumSize(QtCore.QSize(1100, 800))
        self.loginButton = QtWidgets.QPushButton(LoginScreen)
        self.loginButton.setGeometry(QtCore.QRect(369, 430, 151, 41))
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.exitButton = QtWidgets.QPushButton(LoginScreen)
        self.exitButton.setGeometry(QtCore.QRect(570, 430, 151, 41))
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.MD_title = QtWidgets.QLabel(LoginScreen)
        self.MD_title.setGeometry(QtCore.QRect(440, 130, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title.setFont(font)
        self.MD_title.setObjectName("MD_title")
        self.MD_title2 = QtWidgets.QLabel(LoginScreen)
        self.MD_title2.setGeometry(QtCore.QRect(320, 200, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title2.setFont(font)
        self.MD_title2.setObjectName("MD_title2")
        self.formLayoutWidget = QtWidgets.QWidget(LoginScreen)
        self.formLayoutWidget.setGeometry(QtCore.QRect(370, 350, 351, 65))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.login_Username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login_Username.setObjectName("login_Username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login_Username)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.login_Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login_Password.setObjectName("login_Password")
        self.login_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.login_Password)
        self.listView = QtWidgets.QListView(LoginScreen)
        self.listView.setGeometry(QtCore.QRect(50, 50, 991, 661))
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.loginButton.raise_()
        self.MD_title.raise_()
        self.MD_title2.raise_()
        self.exitButton.raise_()
        self.formLayoutWidget.raise_()

        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "LoginScreen"))
        self.loginButton.setText(_translate("LoginScreen", "Login"))
        self.exitButton.setText(_translate("LoginScreen", "Exit"))
        self.MD_title.setText(_translate("LoginScreen", "Medical Doctor"))
        self.MD_title2.setText(_translate("LoginScreen", "Hospital Management Software"))
        self.usernameLabel.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:14pt;\">Username:</span></p></body></html>"))
        self.passwordLabel.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:14pt;\">Password: </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    LoginScreen = QtWidgets.QMainWindow()
    ui = Ui_LoginScreen()
    ui.setupUi(LoginScreen)
    LoginScreen.show()
    sys.exit(app.exec_())
