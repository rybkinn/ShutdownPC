# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import py.resource
from py.main import Ui_MainWindow


class Ui_ShutdownPC(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)    # изменение размера окна
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def showTime(self):
        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())

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
