# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import py.resource_rc
from py.main import Ui_MainWindow


class Ui_ShutdownPC(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.current_time_sec = 0
        self.timer_started = False
        self.pushButton_4.setEnabled(False)
        self.spinBox.setValue(1)
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.shutdown_timer = self.dateEdit_2.time()
        self.frame_7.hide()
        self.label_4.hide()
        self.timer2 = QtCore.QTimer(self)
        self.timer2.timeout.connect(self.timerFunc)

        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(self.StartTimer)
        # self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_4.clicked.connect(self.StopTimer)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)    # изменение размера окна
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def StartTimer(self):
        if self.spinBox.value() == 0:
            self.spinBox.setValue(1)
        if self.checkBox.isChecked():
            shutdown_time = self.timeEdit_2.time()
            shutdown_date = self.timeEdit.dateTime().date()
            if shutdown_time < self.timeEdit.time() or self.spinBox.value() == 1440:
                shutdown_date = self.timeEdit.dateTime().date().addDays(1)
            os.system('SCHTASKS /Create /SC ONCE /TN ShutdownPC /TR "shutdown -s -f" /ST {0} /SD {1} /F'.format(shutdown_time.toString('hh:mm'), shutdown_date.toString('dd.MM.yyyy')))
            self.label_4.setText("Можно закрыть программу")
        else:
            self.label_4.setText("Можно свернуть программу")
        self.pushButton_2.setEnabled(False)
        self.pushButton_4.setEnabled(True)
        self.frame_3.hide()
        self.frame_7.show()
        self.spinBox.setReadOnly(True)
        self.label_4.show()
        self.checkBox.setEnabled(False)
        self.timer_started = True
        self.timer2.start(1000)
        self.shutdown_timer = self.dateEdit_2.time().addSecs(self.spinBox.value() * 60)

    def StopTimer(self):
        if self.checkBox.isChecked():
            os.system('SCHTASKS /Delete /TN ShutdownPC /F')
        self.checkBox.setEnabled(True)
        self.current_time_sec = 0
        self.timer_started = False
        self.timer2.stop()
        self.pushButton_2.setEnabled(True)
        self.spinBox.setReadOnly(False)
        self.frame_7.hide()
        self.frame_3.show()
        self.label_4.hide()

    def timerFunc(self):
        self.current_time_sec += 1
        if self.current_time_sec == 60:
            set_value = int(self.spinBox.text().split(' ')[0]) - 1
            self.spinBox.setValue(set_value)
            self.current_time_sec = 0
            if self.spinBox.value() == 0:
                self.timer_started = False
                self.timer2.stop()
                self.pushButton_2.setEnabled(True)
                self.pushButton_4.setEnabled(False)
                self.frame_7.hide()
                self.frame_3.show()
                self.spinBox.setReadOnly(False)
                self.label_4.hide()
                if not self.checkBox.isChecked():
                    os.system("shutdown -s -f")

    def showTime(self):
        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        if not self.timer_started:
            self.timeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime().addSecs(self.spinBox.value() * 60))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ShutdownPC = Ui_ShutdownPC()
    ShutdownPC.show()
    sys.exit(app.exec_())
