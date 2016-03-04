#!/usr/bin/python

import sys
from PyQt5 import QtCore, QtWidgets
from Ui_MainWindow import Ui_MainWindow

class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.comboSite.addItem("BMW 530")
        self.comboSite.addItem("BMW 525")

        self.buttonQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)


