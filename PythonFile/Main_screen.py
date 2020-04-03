# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 50, 991, 661))
        self.listView.setObjectName("listView")
        self.Main_registerPatient = QtWidgets.QToolButton(self.centralwidget)
        self.Main_registerPatient.setGeometry(QtCore.QRect(345, 270, 191, 71))
        self.Main_registerPatient.setObjectName("Main_registerPatient")
        self.Main_search = QtWidgets.QToolButton(self.centralwidget)
        self.Main_search.setGeometry(QtCore.QRect(565, 270, 191, 71))
        self.Main_search.setObjectName("Main_search")
        self.Main_GP = QtWidgets.QToolButton(self.centralwidget)
        self.Main_GP.setGeometry(QtCore.QRect(565, 370, 191, 71))
        self.Main_GP.setObjectName("Main_GP")
        self.Main_logout = QtWidgets.QToolButton(self.centralwidget)
        self.Main_logout.setGeometry(QtCore.QRect(470, 480, 161, 41))
        self.Main_logout.setObjectName("Main_logout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(820, 660, 221, 51))
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.Main_appts = QtWidgets.QToolButton(self.centralwidget)
        self.Main_appts.setGeometry(QtCore.QRect(345, 370, 191, 71))
        self.Main_appts.setObjectName("Main_appts")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 120, 361, 71))
        self.label.setObjectName("label")
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
        self.Main_registerPatient.setText(_translate("MainWindow", "Register New Patient"))
        self.Main_search.setText(_translate("MainWindow", "Search Patients"))
        self.Main_GP.setText(_translate("MainWindow", "General Practice"))
        self.Main_logout.setText(_translate("MainWindow", "Log Out"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "User: Dr. John Smith"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Date: 3/4/2020 10:54 AM EST"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Main_appts.setText(_translate("MainWindow", "Appointments"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Medical Doctor</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
