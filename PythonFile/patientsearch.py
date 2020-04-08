# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientsearch.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PatientSearch(object):
    def setupUi(self, PatientSearch):
        PatientSearch.setObjectName("PatientSearch")
        PatientSearch.resize(1100, 800)
        PatientSearch.setMinimumSize(QtCore.QSize(1100, 800))
        PatientSearch.setMaximumSize(QtCore.QSize(1100, 800))
        font = QtGui.QFont()
        font.setPointSize(14)
        PatientSearch.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PatientSearch)
        self.centralwidget.setObjectName("centralwidget")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(942, 30, 111, 31))
        self.searchButton.setObjectName("searchButton")
        self.PatientList = QtWidgets.QListView(self.centralwidget)
        self.PatientList.setGeometry(QtCore.QRect(35, 81, 1031, 601))
        self.PatientList.setObjectName("PatientList")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(995, 690, 71, 31))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(60, 100, 981, 111))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.groupBox_9)
        self.textBrowser_10.setGeometry(QtCore.QRect(10, 10, 201, 91))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.groupBox_9)
        self.textBrowser_11.setGeometry(QtCore.QRect(780, 70, 191, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_6.setGeometry(QtCore.QRect(780, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QtCore.QRect(35, 21, 1031, 51))
        self.searchBar.setClearButtonEnabled(True)
        self.searchBar.setObjectName("searchBar")
        self.searchBar.raise_()
        self.PatientList.raise_()
        self.searchButton.raise_()
        self.textEdit.raise_()
        self.groupBox_9.raise_()
        PatientSearch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PatientSearch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 37))
        self.menubar.setObjectName("menubar")
        PatientSearch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PatientSearch)
        self.statusbar.setObjectName("statusbar")
        PatientSearch.setStatusBar(self.statusbar)

        self.retranslateUi(PatientSearch)
        QtCore.QMetaObject.connectSlotsByName(PatientSearch)

    def retranslateUi(self, PatientSearch):
        _translate = QtCore.QCoreApplication.translate
        PatientSearch.setWindowTitle(_translate("PatientSearch", "PatientSearch"))
        self.searchButton.setText(_translate("PatientSearch", "Search"))
        self.textEdit.setHtml(_translate("PatientSearch", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">1 Results</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("PatientSearch", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Patient ID: Johnson66</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Name: Jane Johnson</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">DOB: 01-31-72</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("PatientSearch", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Last Updated: 01-19-19</span></p></body></html>"))
        self.pushButton_6.setText(_translate("PatientSearch", "Access"))
        self.searchBar.setPlaceholderText(_translate("PatientSearch", "Search Patients..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatientSearch = QtWidgets.QMainWindow()
    ui = Ui_PatientSearch()
    ui.setupUi(PatientSearch)
    PatientSearch.show()
    sys.exit(app.exec_())
