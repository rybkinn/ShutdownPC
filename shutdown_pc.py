#!/usr/bin/env python3
import datetime
import os
import platform
import sys
import subprocess

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from py.main import Ui_MainWindow

VERSION = "v 1.1"


class UiShutdownPc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QtGui.QFontDatabase.addApplicationFont(
            "ui/resource/fonts/a_LCDNova.ttf")
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        self.label_bottom_2.setText(VERSION)

        self.run_system = platform.system()
        if self.run_system == 'Linux':
            self.checkBox.setText('Записать в систему')
            self.checkBox_2.setText('Записать в систему')

        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.clock_timer = QtCore.QTimer(self)
        self.clock_timer.timeout.connect(self.display_time)
        self.clock_timer.start(1000)

        self.spinBox.setSuffix(' мин')
        self.old_task = False
        self.current_time_sec = 0
        self.timer_started = False
        self.date_timer_started = False
        self.pushButton_4.setEnabled(False)
        self.spinBox.setValue(1)
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.shutdown_timer = self.dateEdit_2.time()
        self.frame_7.hide()
        self.label_4.hide()
        self.timer_by_time = QtCore.QTimer(self)
        self.timer_by_time.timeout.connect(self.timer_operation_by_time)

        self.pushButton_7.setEnabled(False)
        self.frame_11.hide()
        self.label_8.hide()
        sec = 60 - QtCore.QDateTime.currentDateTime().time().second()
        self.dateTimeEdit.setDateTime(
            QtCore.QDateTime.currentDateTime().addSecs(sec))
        self.timer_by_date = QtCore.QTimer(self)
        self.timer_by_date.timeout.connect(self.timer_operation_by_date)

        self.pushButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(self.start_timer_by_time)
        self.pushButton_3.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_4.clicked.connect(self.stop_timer_by_time)
        self.pushButton_6.clicked.connect(self.start_timer_by_date)
        self.pushButton_7.clicked.connect(self.stop_timer_by_date)
        self.pushButton_8.clicked.connect(self.close)
        self.pushButton_9.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_10.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # checks 'task scheduler' for a task
        if self.run_system == 'Windows':
            try:
                query_task = subprocess.check_output(
                    ['SCHTASKS', '/Query', '/FO', 'LIST', '/TN', 'ShutdownPC'],
                    shell=True,
                    stdin=subprocess.PIPE,
                    stderr=subprocess.PIPE).decode('cp866')
                result_query_list = query_task.split('\r\n')
                for task_parameter in result_query_list:
                    print("task_parameter => ", task_parameter)
                    if task_parameter.startswith('Время следующего запуска:'):
                        task_time_result = task_parameter[26:].split(' ')
                        if not task_time_result[0] == 'N/A':
                            if len(task_time_result[1]) == 7:
                                task_time_result[1] = '0' + task_time_result[1]
                            self.TaskDate = QtCore.QDate()
                            self.TaskDate.setDate(int(task_time_result[0][6:]),
                                                  int(task_time_result[0][3:5]),
                                                  int(task_time_result[0][:2]))
                            self.TaskTime = QtCore.QTime()
                            self.TaskTime.setHMS(int(task_time_result[1][:2]),
                                                 int(task_time_result[1][3:5]),
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

                            self.label_5.setText("Есть задача в планировщике")
                            self.frame_10.hide()
                            self.frame_11.show()
                            self.dateTimeEdit.setEnabled(False)
                            self.pushButton_6.setEnabled(False)
                            self.pushButton_7.setEnabled(True)
                            self.label_8.show()
                            self.checkBox_2.hide()
                            self.dateTimeEdit.setDate(self.TaskDate)
                            self.dateTimeEdit.setTime(self.TaskTime)
            except subprocess.CalledProcessError as error:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Ошибка с планировщиком задач.")
                msg.setText("Нету задачи в планировщике windows.")
                msg.setInformativeText(error)
                msg.exec_()

    def start_timer_by_time(self):
        """
        Starts a timer in the 'shutdown by time' window.
        """
        if self.spinBox.value() == 0:
            self.spinBox.setValue(1)
        if self.checkBox.isChecked():
            shutdown_time = self.timeEdit_2.time()
            shutdown_date = self.timeEdit.dateTime().date()
            if shutdown_time < self.timeEdit.time() or \
                    self.spinBox.value() == 1440:
                shutdown_date = self.timeEdit.dateTime().date().addDays(1)
            if self.run_system == 'Windows':
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
            elif self.run_system == 'Linux':
                # (Linux) старт выключения ПК по времени с добавлением в систему
                # os.system(f' echo {sudo_passwd} |
                # sudo -S shutdown -h -S +{self.spinBox.value()}')
                try:
                    os.system(f'shutdown -h +{self.spinBox.value()}')
                except PermissionError as error:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle("Ошибка с root правами")
                    msg.setText("Недостаточно прав на выполнение операции")
                    msg.setInformativeText(error)
                    msg.exec_()
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
        self.timer_by_time.start(1000)
        self.shutdown_timer = self.dateEdit_2.time().addSecs(
            self.spinBox.value() * 60)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(105, 105, 105);\n"
            "background-color: rgb(10, 10, 10);\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(50, 50, 50, 150);\n"
            "}")

    def stop_timer_by_time(self):
        """
        Stop a timer in the 'shutdown by time' window.
        """
        if self.run_system == 'Windows' and self.checkBox.isChecked() or \
                self.run_system == 'Windows' and self.old_task:
            subprocess.Popen(['SCHTASKS', '/Delete',
                              '/TN', 'ShutdownPC',
                              '/F'],
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        elif self.run_system == 'Linux' and self.checkBox.isChecked() or \
                self.run_system == 'Linux' and self.old_task:
            # (Linux) удаление выключения ПК по времени с добавлением в систему
            try:
                os.system('shutdown -c')
            except PermissionError as error:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Ошибка с root правами")
                msg.setText("Недостаточно прав на выполнение операции")
                msg.setInformativeText(error)
                msg.exec_()
        self.checkBox.setEnabled(True)
        self.current_time_sec = 0
        self.timer_started = False
        self.timer_by_time.stop()
        self.pushButton_2.setEnabled(True)
        self.spinBox.setReadOnly(False)
        self.frame_7.hide()
        self.frame_3.show()
        self.label_4.hide()
        self.spinBox.show()
        self.checkBox.show()
        self.label_2.setText("Выключить через")
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(220, 220, 220);\n"
            "background-color: rgb(10, 10, 10);\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(50, 50, 50, 150);\n"
            "}")

    def start_timer_by_date(self):
        """
        Starts a timer in the 'shutdown by date' window.
        """
        self.label_5.setText("Выключится в")
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(True)
        self.checkBox_2.setEnabled(False)
        self.dateTimeEdit.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(105, 105, 105);\n"
            "background-color: rgb(10, 10, 10);\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(50, 50, 50, 150);\n"
            "}")
        self.frame_10.hide()
        self.frame_11.show()
        self.label_8.show()
        self.date_timer_started = True
        if self.checkBox_2.isChecked():
            self.label_8.setText("Можно закрыть программу")
            shutdown_date = self.dateTimeEdit.dateTime()
            if self.run_system == 'Windows':
                subprocess.Popen(['SCHTASKS', '/Create',
                                  '/SC', 'ONCE',
                                  '/TN', 'ShutdownPC',
                                  '/TR', 'shutdown -s -t 0 -f -d p:0:0',
                                  '/ST', shutdown_date.toString('hh:mm'),
                                  '/SD', shutdown_date.toString('dd.MM.yyyy'),
                                  '/F'],
                                 shell=True,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            elif self.run_system == 'Linux':
                # (Linux) выключение ПК по дате с добавлением в систему
                __now_datetime = datetime.datetime.now()
                __diff_minutes = (self.dateTimeEdit.dateTime().toPyDateTime() -
                                  __now_datetime).total_seconds() / 60.0
                try:
                    os.system(f'shutdown -h +{int(__diff_minutes)}')
                except PermissionError as error:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle("Ошибка с root правами")
                    msg.setText("Недостаточно прав на выполнение операции")
                    msg.setInformativeText(error)
                    msg.exec_()
        else:
            self.label_8.setText("Можно свернуть программу")
            self.timer_by_date.start(1000)

    def stop_timer_by_date(self):
        """
        Stop a timer in the 'shutdown by date' window.
        """
        self.timer_by_date.stop()
        self.label_5.setText("Выключить в")
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(False)
        self.checkBox_2.setEnabled(True)
        self.dateTimeEdit.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(220, 220, 220);\n"
            "background-color: rgb(10, 10, 10);\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(50, 50, 50, 150);\n"
            "}")
        self.checkBox_2.show()
        self.frame_10.show()
        self.frame_11.hide()
        self.label_8.hide()
        self.date_timer_started = False
        if self.run_system == 'Windows' and self.checkBox_2.isChecked() or \
                self.run_system == 'Windows' and self.old_task:
            self.old_task = False
            subprocess.Popen(['SCHTASKS', '/Delete',
                              '/TN', 'ShutdownPC',
                              '/F'],
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            sec = 60 - QtCore.QDateTime.currentDateTime().time().second()
            self.dateTimeEdit.setDateTime(
                QtCore.QDateTime.currentDateTime().addSecs(sec))
        elif self.run_system == 'Linux' and self.checkBox_2.isChecked() or \
                self.run_system == 'Linux' and self.old_task:
            self.old_task = False
            # (Linux) удаление выключение ПК по дате с добавлением в систему
            sec = 60 - QtCore.QDateTime.currentDateTime().time().second()
            self.dateTimeEdit.setDateTime(
                QtCore.QDateTime.currentDateTime().addSecs(sec))
            try:
                os.system('shutdown -c')
            except PermissionError as error:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Ошибка с root правами")
                msg.setText("Недостаточно прав на выполнение операции")
                msg.setInformativeText(error)
                msg.exec_()

    def timer_operation_by_time(self):
        """
        Timer algorithm by time.
        """
        self.current_time_sec += 1
        if self.current_time_sec == 60:
            set_value = int(self.spinBox.text().split(' ')[0]) - 1
            self.spinBox.setValue(set_value)
            self.current_time_sec = 0
            if self.spinBox.value() == 0:
                self.timer_started = False
                self.timer_by_time.stop()
                self.pushButton_2.setEnabled(True)
                self.pushButton_4.setEnabled(False)
                self.frame_7.hide()
                self.frame_3.show()
                self.spinBox.setReadOnly(False)
                self.label_4.hide()
                if not self.checkBox.isChecked() and \
                        self.run_system == 'Windows':
                    subprocess.run(
                        ['shutdown', '-s', '-t', '0', '-f', '-d', 'p:0:0'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
                elif not self.checkBox.isChecked() and \
                        self.run_system == 'Linux':
                    # (Linux) выключение ПК по истечению таймера (на время)
                    try:
                        os.system('shutdown now')
                    except PermissionError as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setWindowTitle("Ошибка с root правами")
                        msg.setText("Недостаточно прав на выполнение операции")
                        msg.setInformativeText(error)
                        msg.exec_()

    def timer_operation_by_date(self):
        """
        Timer algorithm by date.
        """
        if QtCore.QDateTime.currentDateTime() >= \
                self.dateTimeEdit.dateTime() and self.run_system == 'Windows':
            self.timer_by_date.stop()
            subprocess.run(['shutdown', '-s', '-t', '0', '-f', '-d', 'p:0:0'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        elif QtCore.QDateTime.currentDateTime() >= \
                self.dateTimeEdit.dateTime() and self.run_system == 'Linux':
            self.timer_by_date.stop()
            # (Linux) выключение ПК по истечению таймера (на время)
            try:
                os.system('shutdown now')
            except PermissionError as error:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Ошибка с root правами")
                msg.setText("Недостаточно прав на выполнение операции")
                msg.setInformativeText(error)
                msg.exec_()

    def display_time(self):
        """
        Displays the current time and date.
        """
        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        if not self.timer_started:
            self.timeEdit_2.setDateTime(
                QtCore.QDateTime.currentDateTime().addSecs(
                    self.spinBox.value() * 60))
        if self.dateEdit.dateTime() > self.dateTimeEdit.dateTime():
            self.pushButton_6.setStyleSheet(
                "QPushButton {\n"
                "color: rgb(255, 0, 0);\n"
                "background-color: rgb(10, 10, 10);\n"
                "}\n"
                "QPushButton:hover {\n"
                "background-color: rgba(50, 50, 50, 150);\n"
                "}")
            self.pushButton_6.setEnabled(False)
        else:
            self.pushButton_6.setStyleSheet(
                "QPushButton {\n"
                "color: rgb(152, 220, 41);\n"
                "background-color: rgb(10, 10, 10);\n"
                "}\n"
                "QPushButton:hover {\n"
                "background-color: rgba(50, 50, 50, 150);\n"
                "}")
            self.pushButton_6.setEnabled(True)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ShutdownPC = UiShutdownPc()
    ShutdownPC.show()
    sys.exit(app.exec_())
