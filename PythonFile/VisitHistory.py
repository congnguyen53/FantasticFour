# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisitHistory.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 445)
        MainWindow.setMinimumSize(QtCore.QSize(345, 445))
        MainWindow.setMaximumSize(QtCore.QSize(345, 445))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 291, 71))
        self.textBrowser.setMinimumSize(QtCore.QSize(291, 71))
        self.textBrowser.setMaximumSize(QtCore.QSize(291, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.datevisithistory = QtWidgets.QComboBox(self.centralwidget)
        self.datevisithistory.setGeometry(QtCore.QRect(20, 130, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.datevisithistory.setFont(font)
        self.datevisithistory.setObjectName("datevisithistory")
        self.datevisithistory.addItem("")
        self.datevisithistory.addItem("")
        self.datevisithistory.addItem("")
        self.datevisithistory.addItem("")
        self.datevisithistory.addItem("")
        self.button_openvisithistory = QtWidgets.QToolButton(self.centralwidget)
        self.button_openvisithistory.setGeometry(QtCore.QRect(110, 300, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_openvisithistory.setFont(font)
        self.button_openvisithistory.setObjectName("button_openvisithistory")
        self.EmergencyContact = QtWidgets.QLabel(self.centralwidget)
        self.EmergencyContact.setGeometry(QtCore.QRect(20, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EmergencyContact.setFont(font)
        self.EmergencyContact.setObjectName("EmergencyContact")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 21))
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
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visit History</p></body></html>"))
        self.datevisithistory.setItemText(0, _translate("MainWindow", "07/22/19"))
        self.datevisithistory.setItemText(1, _translate("MainWindow", "09/11/19"))
        self.datevisithistory.setItemText(2, _translate("MainWindow", "11/01/19"))
        self.datevisithistory.setItemText(3, _translate("MainWindow", "02/15/20"))
        self.datevisithistory.setItemText(4, _translate("MainWindow", "04/03/20"))
        self.button_openvisithistory.setText(_translate("MainWindow", "Open"))
        self.EmergencyContact.setText(_translate("MainWindow", "MM/DD/YYYY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
