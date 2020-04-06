# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_screen import *

class Ui_Dialog(object):
    def exit(self):
        sys.exit()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 800)
        Dialog.setMinimumSize(QtCore.QSize(1100, 800))
        Dialog.setMaximumSize(QtCore.QSize(1100, 800))
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(369, 400, 151, 41))
        self.loginButton.setObjectName("loginButton")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(570, 400, 151, 41))
        self.exitButton.setObjectName("exitButton")

        #Click event for exit button to close system
        self.exitButton.clicked.connect(self.exit)

        self.MD_title = QtWidgets.QLabel(Dialog)
        self.MD_title.setGeometry(QtCore.QRect(440, 100, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title.setFont(font)
        self.MD_title.setObjectName("MD_title")
        self.MD_title2 = QtWidgets.QLabel(Dialog)
        self.MD_title2.setGeometry(QtCore.QRect(320, 170, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title2.setFont(font)
        self.MD_title2.setObjectName("MD_title2")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(370, 320, 351, 65))
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
        self.loginButton.raise_()
        self.MD_title.raise_()
        self.MD_title2.raise_()
        self.exitButton.raise_()
        self.formLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.MD_title.setText(_translate("Dialog", "Medical Doctor"))
        self.MD_title2.setText(_translate("Dialog", "Hospital Management Software"))
        self.usernameLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Username:</span></p></body></html>"))
        self.passwordLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Password: </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
