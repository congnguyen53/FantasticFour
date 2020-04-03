# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loghistorypage.ui'
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
        self.patientName = QtWidgets.QTextBrowser(self.centralwidget)
        self.patientName.setGeometry(QtCore.QRect(20, 20, 256, 71))
        self.patientName.setObjectName("patientName")
        self.patientInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.patientInfo.setGeometry(QtCore.QRect(290, 20, 151, 71))
        self.patientInfo.setObjectName("patientInfo")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(160, 120, 761, 431))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 738, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.historyLogs = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.historyLogs.setGeometry(QtCore.QRect(0, 0, 751, 451))
        self.historyLogs.setObjectName("historyLogs")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.button_printLogs = QtWidgets.QToolButton(self.centralwidget)
        self.button_printLogs.setGeometry(QtCore.QRect(830, 560, 93, 28))
        self.button_printLogs.setObjectName("button_printLogs")
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
        self.patientName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Jane Doe</span></p></body></html>"))
        self.patientInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Patient ID: Jdoe1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">DOB: 07-31-98</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Date Created: 07/18/19</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Last Updated: 05/05/20</span></p></body></html>"))
        self.historyLogs.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">***Patient Profile created by</span><span style=\" font-size:12pt; text-decoration: underline;\"> Nurse Rebecca Johnson</span><span style=\" font-size:12pt;\">. </span><span style=\" font-size:12pt; font-weight:600;\">[21:33:06] 02/13/20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">***</span><span style=\" font-size:12pt; text-decoration: underline;\"> Nurse Rebecca Johnson </span><span style=\" font-size:12pt;\">Assessed the </span><span style=\" font-size:12pt; text-decoration: underline;\">Patient Jane Doe</span><span style=\" font-size:12pt;\">. </span><span style=\" font-size:12pt; font-weight:600;\">[21:33:51] 02/13/20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">***Patient Information tab accessed by </span><span style=\" font-size:12pt; text-decoration: underline;\"> Nurse Rebecca Johnson</span><span style=\" font-size:12pt;\">. </span><span style=\" font-size:12pt; font-weight:600;\">[21:34:05] 02/13/20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">***</span><span style=\" font-size:12pt; text-decoration: underline;\">Doctor Stevenson</span><span style=\" font-size:12pt;\"> has editted the patients symptoms. </span><span style=\" font-size:12pt; font-weight:600;\">[08:46:54] 02/14/20</span></p></body></html>"))
        self.button_printLogs.setText(_translate("MainWindow", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
