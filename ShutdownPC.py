# -*- coding: utf-8 -*-

import sys
import subprocess
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

        self.old_task = False
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

        try:
            query_task = subprocess.check_output(['SCHTASKS', '/Query',
                                                  '/FO', 'LIST',
                                                  '/TN', 'ShutdownPC'],
                                                 shell=True,
                                                 stdin=subprocess.PIPE,
                                                 stderr=subprocess.PIPE).decode('cp866')
            result_query_list = query_task.split('\r\n')
            for elem in result_query_list:
                if elem.startswith('Время следующего запуска:'):
                    task_time_result = elem[26:].split(' ')
                    if not task_time_result[0] == 'N/A':
                        if len(task_time_result[1]) == 7:
                            task_time_result[1] = '0' + task_time_result[1]
                        self.TaskDate = QtCore.QDate()
                        self.TaskDate.setDate(int(task_time_result[0][6:]), int(task_time_result[0][3:5]),
                                              int(task_time_result[0][:2]))
                        self.TaskTime = QtCore.QTime()
                        self.TaskTime.setHMS(int(task_time_result[1][:2]), int(task_time_result[1][3:5]),
                                             int(task_time_result[1][6:]))
                        self.timer_started = True
                        self.checkBox.setEnabled(False)
                        self.pushButton_2.setEnabled(False)
                        self.pushButton_4.setEnabled(True)
                        self.spinBox.setReadOnly(True)
                        self.spinBox.hide()
                        self.checkBox.hide()
                        self.label_2.setText("Есть задача в планировщике")
                        self.frame_3.hide()
                        self.frame_7.show()
                        self.label_4.show()
                        self.timeEdit_2.setTime(self.TaskTime)
                        self.old_task = True
        except subprocess.CalledProcessError:
            pass

    def StartTimer(self):
        if self.spinBox.value() == 0:
            self.spinBox.setValue(1)
        if self.checkBox.isChecked():
            shutdown_time = self.timeEdit_2.time()
            shutdown_date = self.timeEdit.dateTime().date()
            if shutdown_time < self.timeEdit.time() or self.spinBox.value() == 1440:
                shutdown_date = self.timeEdit.dateTime().date().addDays(1)
            subprocess.Popen(['SCHTASKS', '/Create',
                              '/SC', 'ONCE',
                              '/TN', 'ShutdownPC',
                              '/TR', 'shutdown -s -t 0 -f -d p:0:0',
                              '/ST', shutdown_time.toString('hh:mm'),
                              '/SD', shutdown_date.toString('dd.MM.yyyy'),
                              '/F'],
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
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
        if self.checkBox.isChecked() or self.old_task:
            subprocess.Popen(['SCHTASKS', '/Delete',
                              '/TN', 'ShutdownPC',
                              '/F'],
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        self.checkBox.setEnabled(True)
        self.current_time_sec = 0
        self.timer_started = False
        self.timer2.stop()
        self.pushButton_2.setEnabled(True)
        self.spinBox.setReadOnly(False)
        self.frame_7.hide()
        self.frame_3.show()
        self.label_4.hide()
        self.spinBox.show()
        self.checkBox.show()
        self.label_2.setText("Выключить через")

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
                    subprocess.run(['shutdown', '-s', '-t', '0', '-f', '-d', 'p:0:0'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

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
