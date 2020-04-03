# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adjustuserscreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.in_username = QtWidgets.QTextEdit(self.centralwidget)
        self.in_username.setGeometry(QtCore.QRect(510, 360, 171, 31))
        self.in_username.setObjectName("in_username")
        self.in_name = QtWidgets.QTextEdit(self.centralwidget)
        self.in_name.setGeometry(QtCore.QRect(510, 200, 171, 31))
        self.in_name.setObjectName("in_name")
        self.in_department = QtWidgets.QComboBox(self.centralwidget)
        self.in_department.setGeometry(QtCore.QRect(510, 270, 73, 22))
        self.in_department.setObjectName("in_department")
        self.in_datejoined = QtWidgets.QDateEdit(self.centralwidget)
        self.in_datejoined.setGeometry(QtCore.QRect(510, 300, 110, 22))
        self.in_datejoined.setObjectName("in_datejoined")
        self.in_userbox = QtWidgets.QComboBox(self.centralwidget)
        self.in_userbox.setGeometry(QtCore.QRect(510, 440, 73, 22))
        self.in_userbox.setObjectName("in_userbox")
        self.in_userbox.addItem("")
        self.in_userbox.addItem("")
        self.in_userbox.addItem("")
        self.in_fieldofstudy = QtWidgets.QComboBox(self.centralwidget)
        self.in_fieldofstudy.setGeometry(QtCore.QRect(510, 240, 73, 22))
        self.in_fieldofstudy.setObjectName("in_fieldofstudy")
        self.in_password = QtWidgets.QTextEdit(self.centralwidget)
        self.in_password.setGeometry(QtCore.QRect(510, 400, 171, 31))
        self.in_password.setObjectName("in_password")
        self.in_dateofbirth = QtWidgets.QDateEdit(self.centralwidget)
        self.in_dateofbirth.setGeometry(QtCore.QRect(510, 330, 110, 22))
        self.in_dateofbirth.setObjectName("in_dateofbirth")
        self.button_registeradjust = QtWidgets.QToolButton(self.centralwidget)
        self.button_registeradjust.setGeometry(QtCore.QRect(510, 480, 93, 28))
        self.button_registeradjust.setObjectName("button_registeradjust")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 200, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 270, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 300, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 330, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 360, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 400, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.input_usertype = QtWidgets.QLabel(self.centralwidget)
        self.input_usertype.setGeometry(QtCore.QRect(410, 440, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_usertype.setFont(font)
        self.input_usertype.setObjectName("input_usertype")
        self.patientName = QtWidgets.QTextBrowser(self.centralwidget)
        self.patientName.setGeometry(QtCore.QRect(40, 30, 256, 101))
        self.patientName.setObjectName("patientName")
        self.patientInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.patientInfo.setGeometry(QtCore.QRect(310, 30, 261, 151))
        self.patientInfo.setObjectName("patientInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.in_userbox.setItemText(0, _translate("MainWindow", "Admin"))
        self.in_userbox.setItemText(1, _translate("MainWindow", "Doctor"))
        self.in_userbox.setItemText(2, _translate("MainWindow", "Nurse"))
        self.button_registeradjust.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Field of Study"))
        self.label_3.setText(_translate("MainWindow", "Department"))
        self.label_4.setText(_translate("MainWindow", "Date Joined"))
        self.label_5.setText(_translate("MainWindow", "Date of Birth"))
        self.label_6.setText(_translate("MainWindow", "Username"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.input_usertype.setText(_translate("MainWindow", "User Type"))
        self.patientName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Rebecca Johnson</span></p></body></html>"))
        self.patientInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Field of Study: Nutrition</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Department: Anesthesiology</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Date Joined: 03/03/09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Date of Birth: 5/21/80</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Username: joh001</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Password: 4122</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">User Type: Doctor</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
