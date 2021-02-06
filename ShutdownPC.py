# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import py.resource


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_line = QtWidgets.QFrame(self.drop_shadow_frame)
        self.top_line.setMinimumSize(QtCore.QSize(0, 10))
        self.top_line.setMaximumSize(QtCore.QSize(16777215, 10))
        self.top_line.setAutoFillBackground(False)
        self.top_line.setStyleSheet("background-color: rgb(152, 220, 41);")
        self.top_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_line.setObjectName("top_line")
        self.verticalLayout.addWidget(self.top_line)
        self.top_title_contet = QtWidgets.QFrame(self.drop_shadow_frame)
        self.top_title_contet.setMinimumSize(QtCore.QSize(0, 50))
        self.top_title_contet.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_title_contet.setAutoFillBackground(False)
        self.top_title_contet.setStyleSheet("background-color: none")
        self.top_title_contet.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_title_contet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_title_contet.setObjectName("top_title_contet")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_title_contet)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.top_title_contet)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(152, 220, 41)")
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.top_title_contet)
        self.frame_btns.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_minimize.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/btn/minus_badged_delete_remove_icon_142925.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QtCore.QSize(35, 35))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_close.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/btn/close_win.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(35, 35))
        self.btn_close.setAutoDefault(False)
        self.btn_close.setDefault(False)
        self.btn_close.setFlat(False)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.top_title_contet)
        self.middle_content = QtWidgets.QFrame(self.drop_shadow_frame)
        self.middle_content.setAutoFillBackground(False)
        self.middle_content.setStyleSheet("background-color: none")
        self.middle_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle_content.setObjectName("middle_content")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.middle_content)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.middle_content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_content_home = QtWidgets.QFrame(self.page_home)
        self.frame_content_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_home.setObjectName("frame_content_home")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_content_home)
        self.gridLayout.setObjectName("gridLayout")
        self.line_7 = QtWidgets.QFrame(self.frame_content_home)
        self.line_7.setStyleSheet("color: rgb(152, 220, 41);")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(10)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_content_home)
        self.line_3.setStyleSheet("color: rgb(152, 220, 41);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(10)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_content_home)
        self.line_2.setStyleSheet("color: rgb(152, 220, 41);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 3, 2, 1)
        self.line_6 = QtWidgets.QFrame(self.frame_content_home)
        self.line_6.setWindowModality(QtCore.Qt.NonModal)
        self.line_6.setStyleSheet("color: rgb(152, 220, 41);")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(10)
        self.line_6.setMidLineWidth(0)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_content_home)
        self.frame.setMinimumSize(QtCore.QSize(190, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(152, 220, 41);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(152, 220, 41);\n"
"    background-color: rgb(10, 10, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(50, 50, 50, 150);\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(152, 220, 41);\n"
"    background-color: rgb(10, 10, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(50, 50, 50, 150);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.gridLayout.addWidget(self.frame, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_content_home)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(40)
        self.timeEdit.setFont(font)
        self.timeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeEdit.setStyleSheet("background-color: black;\n"
"color: rgb(152, 220, 41);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(False)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit.setProperty("showGroupSeparator", False)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(11, 37, 12)))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_content_home)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: black;\n"
"color: rgb(152, 220, 41);")
        self.dateEdit.setFrame(False)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 5), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_content_home)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("background-color: black;\n"
"color: rgb(152, 220, 41);")
        self.dateEdit_2.setFrame(False)
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setReadOnly(True)
        self.dateEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 7), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(False)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 6, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_content_home)
        self.stackedWidget.addWidget(self.page_home)
        self.page_timer = QtWidgets.QWidget()
        self.page_timer.setObjectName("page_timer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_timer)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_content_timer = QtWidgets.QFrame(self.page_timer)
        self.frame_content_timer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_timer.setObjectName("frame_content_timer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_content_timer)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.frame_content_timer)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(152, 220, 41);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem6)
        self.frame_6 = QtWidgets.QFrame(self.frame_content_timer)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.spinBox = QtWidgets.QSpinBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(25)
        self.spinBox.setFont(font)
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(152, 220, 41);")
        self.spinBox.setFrame(False)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setSuffix(" минут")
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(99999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_11.addWidget(self.spinBox)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout_11.addWidget(self.frame_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem9)
        self.frame_4 = QtWidgets.QFrame(self.frame_content_timer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("color: rgb(152, 220, 41);")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_6.addWidget(self.checkBox)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_11.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_content_timer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(20, 20, 20);\n"
"    color: rgb(152, 220, 41);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(50, 50, 50, 150);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/btn/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_11.addWidget(self.frame_3)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem14)
        self.line = QtWidgets.QFrame(self.frame_content_timer)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(152, 220, 41);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.frame_content_timer)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(152, 220, 41);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit_2.setMinimumSize(QtCore.QSize(55, 25))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(14)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setStyleSheet("background-color: black;\n"
"color: rgb(152, 220, 41);")
        self.timeEdit_2.setFrame(False)
        self.timeEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_2.setReadOnly(True)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit_2.setProperty("showGroupSeparator", False)
        self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 5), QtCore.QTime(23, 59, 0)))
        self.timeEdit_2.setTime(QtCore.QTime(23, 59, 0))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_4.addWidget(self.timeEdit_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.verticalLayout_11.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_content_timer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.verticalLayout_11.addWidget(self.frame_5)
        self.verticalLayout_7.addWidget(self.frame_content_timer)
        self.stackedWidget.addWidget(self.page_timer)
        self.page_date = QtWidgets.QWidget()
        self.page_date.setObjectName("page_date")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_date)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_content_date = QtWidgets.QFrame(self.page_date)
        self.frame_content_date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_date.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_date.setObjectName("frame_content_date")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_content_date)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.frame_content_date)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(152, 220, 41);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem19)
        self.frame_9 = QtWidgets.QFrame(self.frame_content_date)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_9)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(14)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(152, 220, 41);\n"
"border-style: none;")
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 27), QtCore.QTime(14, 8, 7)))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.NoSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_9.addWidget(self.dateTimeEdit)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem21)
        self.verticalLayout_10.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_content_date)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2.setStyleSheet("color: rgb(152, 220, 41);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_8.addWidget(self.checkBox_2)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem23)
        self.verticalLayout_10.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_content_date)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem24)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_6.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(20, 20, 20);\n"
"    color: rgb(152, 220, 41);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(50, 50, 50, 150);\n"
"}")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem25)
        self.verticalLayout_10.addWidget(self.frame_10)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem26)
        self.line_8 = QtWidgets.QFrame(self.frame_content_date)
        self.line_8.setStyleSheet("color: rgb(152, 220, 41);")
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(1)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_10.addWidget(self.line_8)
        self.label_8 = QtWidgets.QLabel(self.frame_content_date)
        font = QtGui.QFont()
        font.setFamily("a_LCDNova")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.verticalLayout_8.addWidget(self.frame_content_date)
        self.stackedWidget.addWidget(self.page_date)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.middle_content)
        self.bottom_content = QtWidgets.QFrame(self.drop_shadow_frame)
        self.bottom_content.setMinimumSize(QtCore.QSize(0, 40))
        self.bottom_content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bottom_content.setStyleSheet("background-color: none")
        self.bottom_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_content.setObjectName("bottom_content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_bottom = QtWidgets.QFrame(self.bottom_content)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_label_bottom)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_bottom = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        self.label_bottom.setFont(font)
        self.label_bottom.setStyleSheet("color: rgb(152, 220, 41);")
        self.label_bottom.setObjectName("label_bottom")
        self.verticalLayout_3.addWidget(self.label_bottom)
        self.horizontalLayout_2.addWidget(self.frame_label_bottom)
        self.frame_grip = QtWidgets.QFrame(self.bottom_content)
        self.frame_grip.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_grip.setStyleSheet("padding: 5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.bottom_content)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Shutdown PC"))
        self.label.setText(_translate("MainWindow", "Установить выключение"))
        self.pushButton.setText(_translate("MainWindow", "По таймеру"))
        self.pushButton_3.setText(_translate("MainWindow", "На время"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "MMMM . dd"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "dddd"))
        self.label_2.setText(_translate("MainWindow", "Выключить через"))
        self.checkBox.setText(_translate("MainWindow", "Добавить в планировщик"))
        self.pushButton_2.setText(_translate("MainWindow", "Запуск"))
        self.label_3.setText(_translate("MainWindow", "ПК выключится в"))
        self.label_4.setText(_translate("MainWindow", "Можно закрывать программу"))
        self.label_5.setText(_translate("MainWindow", "Выключить в"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd   MMMM   HH:mm"))
        self.checkBox_2.setText(_translate("MainWindow", "Добавить в планировщик"))
        self.pushButton_6.setText(_translate("MainWindow", "Запуск"))
        self.label_8.setText(_translate("MainWindow", "Можно закрывать программу"))
        self.label_bottom.setText(_translate("MainWindow", "By: Rybkin N. I."))

    #     def moveWindow(event):
    #         if event.buttons() == QtCore.Qt.LeftButton:
    #             MainWindow.move(MainWindow.pos() + event.globalPos() - MainWindow.dragPos)
    #             MainWindow.dragPos = event.globalPos()
    #             event.accept()
    #
    # def mousePressEvent(self, event):
    #     MainWindow.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
