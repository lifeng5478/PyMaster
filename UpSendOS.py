# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpSendOS.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(266, 468)
        mainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PortName = QtWidgets.QLabel(self.centralwidget)
        self.PortName.setObjectName("PortName")
        self.verticalLayout.addWidget(self.PortName)
        self.BaudSet = QtWidgets.QLabel(self.centralwidget)
        self.BaudSet.setObjectName("BaudSet")
        self.verticalLayout.addWidget(self.BaudSet)
        self.PackSet = QtWidgets.QLabel(self.centralwidget)
        self.PackSet.setObjectName("PackSet")
        self.verticalLayout.addWidget(self.PackSet)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PortComb = QtWidgets.QComboBox(self.centralwidget)
        self.PortComb.setObjectName("PortComb")
        self.verticalLayout_2.addWidget(self.PortComb)
        self.BaudComb = QtWidgets.QComboBox(self.centralwidget)
        self.BaudComb.setObjectName("BaudComb")
        self.BaudComb.addItem("")
        self.BaudComb.addItem("")
        self.BaudComb.addItem("")
        self.verticalLayout_2.addWidget(self.BaudComb)
        self.PackComb = QtWidgets.QComboBox(self.centralwidget)
        self.PackComb.setObjectName("PackComb")
        self.PackComb.addItem("")
        self.PackComb.addItem("")
        self.PackComb.addItem("")
        self.PackComb.addItem("")
        self.PackComb.addItem("")
        self.verticalLayout_2.addWidget(self.PackComb)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.OpenSerialB = QtWidgets.QPushButton(self.centralwidget)
        self.OpenSerialB.setObjectName("OpenSerialB")
        self.horizontalLayout.addWidget(self.OpenSerialB)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.McuBack = QtWidgets.QLabel(self.centralwidget)
        self.McuBack.setObjectName("McuBack")
        self.horizontalLayout_5.addWidget(self.McuBack)
        self.ClearB = QtWidgets.QPushButton(self.centralwidget)
        self.ClearB.setObjectName("ClearB")
        self.horizontalLayout_5.addWidget(self.ClearB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.MCUTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.MCUTextEdit.setObjectName("MCUTextEdit")
        self.verticalLayout_3.addWidget(self.MCUTextEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.FileP = QtWidgets.QLabel(self.centralwidget)
        self.FileP.setObjectName("FileP")
        self.horizontalLayout_4.addWidget(self.FileP)
        self.FilePath = QtWidgets.QLabel(self.centralwidget)
        self.FilePath.setObjectName("FilePath")
        self.horizontalLayout_4.addWidget(self.FilePath)
        self.OpenFileB = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFileB.setObjectName("OpenFileB")
        self.horizontalLayout_4.addWidget(self.OpenFileB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FileS = QtWidgets.QLabel(self.centralwidget)
        self.FileS.setObjectName("FileS")
        self.horizontalLayout_3.addWidget(self.FileS)
        self.FileSize = QtWidgets.QLabel(self.centralwidget)
        self.FileSize.setObjectName("FileSize")
        self.horizontalLayout_3.addWidget(self.FileSize)
        self.SendB = QtWidgets.QPushButton(self.centralwidget)
        self.SendB.setObjectName("SendB")
        self.horizontalLayout_3.addWidget(self.SendB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NowSend = QtWidgets.QLabel(self.centralwidget)
        self.NowSend.setObjectName("NowSend")
        self.horizontalLayout_2.addWidget(self.NowSend)
        self.BinText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BinText.sizePolicy().hasHeightForWidth())
        self.BinText.setSizePolicy(sizePolicy)
        self.BinText.setMinimumSize(QtCore.QSize(54, 14))
        self.BinText.setMaximumSize(QtCore.QSize(54, 16777215))
        self.BinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BinText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BinText.setTextFormat(QtCore.Qt.PlainText)
        self.BinText.setScaledContents(True)
        self.BinText.setObjectName("BinText")
        self.horizontalLayout_2.addWidget(self.BinText)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ProcessO = QtWidgets.QLabel(self.centralwidget)
        self.ProcessO.setObjectName("ProcessO")
        self.horizontalLayout_6.addWidget(self.ProcessO)
        self.PrograssBar = QtWidgets.QProgressBar(self.centralwidget)
        self.PrograssBar.setProperty("value", 0)
        self.PrograssBar.setObjectName("PrograssBar")
        self.horizontalLayout_6.addWidget(self.PrograssBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 266, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        mainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.actionversion1_0 = QtWidgets.QAction(mainWindow)
        self.actionversion1_0.setObjectName("actionversion1_0")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.actionversion1_0)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "文件传输上位机EditByLifeng"))
        self.PortName.setText(_translate("mainWindow", "端口号："))
        self.BaudSet.setText(_translate("mainWindow", "波特率："))
        self.PackSet.setText(_translate("mainWindow", "包大小："))
        self.BaudComb.setItemText(0, _translate("mainWindow", "9600"))
        self.BaudComb.setItemText(1, _translate("mainWindow", "19200"))
        self.BaudComb.setItemText(2, _translate("mainWindow", "115200"))
        self.PackComb.setItemText(0, _translate("mainWindow", "16"))
        self.PackComb.setItemText(1, _translate("mainWindow", "32"))
        self.PackComb.setItemText(2, _translate("mainWindow", "64"))
        self.PackComb.setItemText(3, _translate("mainWindow", "128"))
        self.PackComb.setItemText(4, _translate("mainWindow", "256"))
        self.OpenSerialB.setText(_translate("mainWindow", "打开串口"))
        self.McuBack.setText(_translate("mainWindow", "下位机反馈信息："))
        self.ClearB.setText(_translate("mainWindow", "清除窗口"))
        self.MCUTextEdit.setPlainText(_translate("mainWindow", "Hello"))
        self.FileP.setText(_translate("mainWindow", "文件名："))
        self.FilePath.setText(_translate("mainWindow", "FileName"))
        self.OpenFileB.setText(_translate("mainWindow", "打开文件"))
        self.FileS.setText(_translate("mainWindow", "文件大小："))
        self.FileSize.setText(_translate("mainWindow", "Size"))
        self.SendB.setText(_translate("mainWindow", "开始发送"))
        self.NowSend.setText(_translate("mainWindow", "当前发送："))
        self.BinText.setText(_translate("mainWindow", "0x01 0x02"))
        self.ProcessO.setText(_translate("mainWindow", "进程："))
        self.menu.setTitle(_translate("mainWindow", "菜单"))
        self.menu_2.setTitle(_translate("mainWindow", "关于"))
        self.action.setText(_translate("mainWindow", "保存"))
        self.actionversion1_0.setText(_translate("mainWindow", "version1.0"))
