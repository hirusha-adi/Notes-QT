# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designeriYbdmc.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        self.actionlol = QAction(MainWindow)
        self.actionlol.setObjectName(u"actionlol")

        self.action_12 = QAction(MainWindow)
        self.action_12.setObjectName(u"action_12")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 29))

        self.menutest = QMenu(self.menubar)
        self.menutest.setObjectName(u"menutest")

        self.menusefgsder = QMenu(self.menutest)
        self.menusefgsder.setObjectName(u"menusefgsder")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)

        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menutest.menuAction())

        self.menutest.addAction(self.menusefgsder.menuAction())

        self.menusefgsder.addAction(self.actionlol)
        self.menusefgsder.addAction(self.action_12)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))

        self.actionlol.setText(
            QCoreApplication.translate("MainWindow", u"lol", None))

        self.action_12.setText(
            QCoreApplication.translate("MainWindow", u"`12'", None))

        self.menutest.setTitle(
            QCoreApplication.translate("MainWindow", u"test", None))

        self.menusefgsder.setTitle(
            QCoreApplication.translate("MainWindow", u"sefgsder", None))

    # retranslateUi
