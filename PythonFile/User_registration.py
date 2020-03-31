# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_registration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(679, 521)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 310, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 310, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.passRegisterLabel = QtWidgets.QLabel(Dialog)
        self.passRegisterLabel.setGeometry(QtCore.QRect(197, 230, 83, 22))
        self.passRegisterLabel.setObjectName("passRegisterLabel")
        self.userRegisterIn = QtWidgets.QLineEdit(Dialog)
        self.userRegisterIn.setGeometry(QtCore.QRect(290, 201, 182, 22))
        self.userRegisterIn.setText("")
        self.userRegisterIn.setObjectName("userRegisterIn")
        self.userRegisterLabel = QtWidgets.QLabel(Dialog)
        self.userRegisterLabel.setGeometry(QtCore.QRect(197, 201, 86, 22))
        self.userRegisterLabel.setObjectName("userRegisterLabel")
        self.passRegisterIn = QtWidgets.QLineEdit(Dialog)
        self.passRegisterIn.setGeometry(QtCore.QRect(290, 230, 182, 22))
        self.passRegisterIn.setObjectName("passRegisterIn")
        self.MD_title = QtWidgets.QLabel(Dialog)
        self.MD_title.setGeometry(QtCore.QRect(180, 60, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.MD_title.setFont(font)
        self.MD_title.setObjectName("MD_title")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(290, 260, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.passRegisterLabel_2 = QtWidgets.QLabel(Dialog)
        self.passRegisterLabel_2.setGeometry(QtCore.QRect(200, 260, 91, 22))
        self.passRegisterLabel_2.setObjectName("passRegisterLabel_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Create Profile"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.passRegisterLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.userRegisterLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Username</span></p></body></html>"))
        self.MD_title.setText(_translate("Dialog", "New User Registration"))
        self.comboBox.setItemText(0, _translate("Dialog", "--Select--"))
        self.comboBox.setItemText(1, _translate("Dialog", "Doctor"))
        self.comboBox.setItemText(2, _translate("Dialog", "Nurse"))
        self.comboBox.setItemText(3, _translate("Dialog", "Admin"))
        self.passRegisterLabel_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">User Type</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
