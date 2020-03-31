# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 518)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(240, 340, 93, 28))
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(420, 340, 93, 28))
        self.registerButton.setObjectName("registerButton")
        self.MD_title = QtWidgets.QLabel(Dialog)
        self.MD_title.setGeometry(QtCore.QRect(260, 80, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title.setFont(font)
        self.MD_title.setObjectName("MD_title")
        self.MD_title2 = QtWidgets.QLabel(Dialog)
        self.MD_title2.setGeometry(QtCore.QRect(140, 150, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title2.setFont(font)
        self.MD_title2.setObjectName("MD_title2")
        self.loginFormPassIn = QtWidgets.QLineEdit(Dialog)
        self.loginFormPassIn.setGeometry(QtCore.QRect(334, 300, 182, 22))
        self.loginFormPassIn.setObjectName("loginFormPassIn")
        self.loginFormPassLabel = QtWidgets.QLabel(Dialog)
        self.loginFormPassLabel.setGeometry(QtCore.QRect(241, 300, 83, 22))
        self.loginFormPassLabel.setObjectName("loginFormPassLabel")
        self.loginFormUserIn = QtWidgets.QLineEdit(Dialog)
        self.loginFormUserIn.setGeometry(QtCore.QRect(334, 271, 182, 22))
        self.loginFormUserIn.setText("")
        self.loginFormUserIn.setObjectName("loginFormUserIn")
        self.loginFormUserLabel = QtWidgets.QLabel(Dialog)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.registerButton.setText(_translate("Dialog", "Register"))
        self.MD_title.setText(_translate("Dialog", "Medical Doctor"))
        self.MD_title2.setText(_translate("Dialog", "Hospital Management Software"))
        self.loginFormPassLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.loginFormUserLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Username</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
