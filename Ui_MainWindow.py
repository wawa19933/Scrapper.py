# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboSite = QtWidgets.QComboBox(self.centralwidget)
        self.comboSite.setObjectName("comboSite")
        self.horizontalLayout.addWidget(self.comboSite)
        self.buttonEnter = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEnter.setObjectName("buttonEnter")
        self.horizontalLayout.addWidget(self.buttonEnter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setObjectName("buttonStart")
        self.verticalLayout.addWidget(self.buttonStart)
        self.buttonParse = QtWidgets.QPushButton(self.centralwidget)
        self.buttonParse.setObjectName("buttonParse")
        self.verticalLayout.addWidget(self.buttonParse)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2)
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setObjectName("buttonClear")
        self.verticalLayout.addWidget(self.buttonClear)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuit.setObjectName("buttonQuit")
        self.verticalLayout.addWidget(self.buttonQuit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrapper"))
        self.buttonEnter.setText(_translate("MainWindow", "Enter"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.buttonParse.setText(_translate("MainWindow", "Parse"))
        self.button1.setText(_translate("MainWindow", "Button1"))
        self.button2.setText(_translate("MainWindow", "Button2"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.buttonQuit.setText(_translate("MainWindow", "&Quit"))

