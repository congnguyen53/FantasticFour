# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Schedule.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Appointments(object):
    def setupUi(self, Appointments):
        Appointments.setObjectName("Appointments")
        Appointments.resize(1100, 800)
        Appointments.setMinimumSize(QtCore.QSize(1100, 800))
        Appointments.setMaximumSize(QtCore.QSize(1100, 800))
        self.centralwidget = QtWidgets.QWidget(Appointments)
        self.centralwidget.setObjectName("centralwidget")
        self.Schedule_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.Schedule_calendar.setGeometry(QtCore.QRect(20, 20, 691, 391))
        self.Schedule_calendar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Schedule_calendar.setGridVisible(True)
        self.Schedule_calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.Schedule_calendar.setDateEditEnabled(True)
        self.Schedule_calendar.setObjectName("Schedule_calendar")
        self.Schedule_list = QtWidgets.QListWidget(self.centralwidget)
        self.Schedule_list.setGeometry(QtCore.QRect(730, 20, 351, 721))
        self.Schedule_list.setObjectName("Schedule_list")
        scheduleHeader = QtWidgets.QListWidgetItem()
        scheduleHeader.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        scheduleHeader.setFont(font)
        self.Schedule_list.addItem(scheduleHeader)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 12, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Schedule_list.addItem(item)
        self.Schedule_appt = QtWidgets.QPushButton(self.centralwidget)
        self.Schedule_appt.setGeometry(QtCore.QRect(18, 420, 221, 31))
        self.Schedule_appt.setAutoFillBackground(False)
        self.Schedule_appt.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Schedule_appt.setObjectName("Schedule_appt")
        self.Schedule_meeting = QtWidgets.QPushButton(self.centralwidget)
        self.Schedule_meeting.setGeometry(QtCore.QRect(255, 420, 221, 31))
        self.Schedule_meeting.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.Schedule_meeting.setObjectName("Schedule_meeting")
        self.Schedul_other = QtWidgets.QPushButton(self.centralwidget)
        self.Schedul_other.setGeometry(QtCore.QRect(490, 420, 221, 31))
        self.Schedul_other.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.Schedul_other.setObjectName("Schedul_other")
        Appointments.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Appointments)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        Appointments.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Appointments)
        self.statusbar.setObjectName("statusbar")
        Appointments.setStatusBar(self.statusbar)

        self.retranslateUi(Appointments)
        QtCore.QMetaObject.connectSlotsByName(Appointments)

    def retranslateUi(self, Appointments):
        _translate = QtCore.QCoreApplication.translate
        Appointments.setWindowTitle(_translate("Appointments", "Appointments"))
        __sortingEnabled = self.Schedule_list.isSortingEnabled()
        self.Schedule_list.setSortingEnabled(False)

        date = datetime.datetime.now()
        localDate = date.strftime("%x")

        scheduleHeader = self.Schedule_list.item(0)
        scheduleHeader.setText(_translate("Appointments", "Schedule for "+localDate))
        item = self.Schedule_list.item(1)
        item.setText(_translate("Appointments", "6am--------------------------------------------"))
        item = self.Schedule_list.item(2)
        item.setText(_translate("Appointments", "6:15am Anne annual physical"))
        item = self.Schedule_list.item(4)
        item.setText(_translate("Appointments", "7am--------------------------------------------"))
        item = self.Schedule_list.item(6)
        item.setText(_translate("Appointments", "8am--------------------------------------------"))
        item = self.Schedule_list.item(7)
        item.setText(_translate("Appointments", "8:00am hematologists seminar @ briefing room"))
        item = self.Schedule_list.item(9)
        item.setText(_translate("Appointments", "9am--------------------------------------------"))
        item = self.Schedule_list.item(11)
        item.setText(_translate("Appointments", "10am-------------------------------------------"))
        item = self.Schedule_list.item(13)
        item.setText(_translate("Appointments", "11am-------------------------------------------"))
        item = self.Schedule_list.item(15)
        item.setText(_translate("Appointments", "12pm-------------------------------------------"))
        item = self.Schedule_list.item(16)
        item.setText(_translate("Appointments", "12:30pm Jared blood test"))
        item = self.Schedule_list.item(18)
        item.setText(_translate("Appointments", "1pm--------------------------------------------"))
        item = self.Schedule_list.item(20)
        item.setText(_translate("Appointments", "2pm--------------------------------------------"))
        item = self.Schedule_list.item(21)
        item.setText(_translate("Appointments", "2:15pm Lunch Break"))
        item = self.Schedule_list.item(23)
        item.setText(_translate("Appointments", "3pm--------------------------------------------"))
        item = self.Schedule_list.item(25)
        item.setText(_translate("Appointments", "4pm--------------------------------------------"))
        item = self.Schedule_list.item(27)
        item.setText(_translate("Appointments", "5pm--------------------------------------------"))
        item = self.Schedule_list.item(29)
        item.setText(_translate("Appointments", "6pm--------------------------------------------"))
        item = self.Schedule_list.item(31)
        item.setText(_translate("Appointments", "7pm--------------------------------------------"))
        item = self.Schedule_list.item(33)
        item.setText(_translate("Appointments", "8pm--------------------------------------------"))
        item = self.Schedule_list.item(35)
        item.setText(_translate("Appointments", "9pm--------------------------------------------"))
        item = self.Schedule_list.item(37)
        item.setText(_translate("Appointments", "10pm-------------------------------------------"))
        item = self.Schedule_list.item(39)
        item.setText(_translate("Appointments", "11pm-------------------------------------------"))
        item = self.Schedule_list.item(41)
        item.setText(_translate("Appointments", "12am-------------------------------------------"))
        self.Schedule_list.setSortingEnabled(__sortingEnabled)
        self.Schedule_appt.setText(_translate("Appointments", "Add Appointment"))
        self.Schedule_meeting.setText(_translate("Appointments", "Add Meeting"))
        self.Schedul_other.setText(_translate("Appointments", "Add Other"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Appointments = QtWidgets.QMainWindow()
    ui = Ui_Appointments()
    ui.setupUi(Appointments)
    Appointments.show()
    sys.exit(app.exec_())
