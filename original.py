# # -*- coding: utf-8 -*-

# ################################################################################
# # Form generated from reading UI file 'NotesnPYfYl.ui'
# ##
# # Created by: Qt User Interface Compiler version 5.15.2
# ##
# # WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################
# import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(822, 600)

        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionPage_Setup = QAction(MainWindow)
        self.actionPage_Setup.setObjectName(u"actionPage_Setup")
        self.actionPage_Setup_2 = QAction(MainWindow)
        self.actionPage_Setup_2.setObjectName(u"actionPage_Setup_2")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionFind = QAction(MainWindow)
        self.actionFind.setObjectName(u"actionFind")
        self.actionFind_Next = QAction(MainWindow)
        self.actionFind_Next.setObjectName(u"actionFind_Next")
        self.actionReplace = QAction(MainWindow)
        self.actionReplace.setObjectName(u"actionReplace")
        self.actionGo_To = QAction(MainWindow)
        self.actionGo_To.setObjectName(u"actionGo_To")
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionTime_Date = QAction(MainWindow)
        self.actionTime_Date.setObjectName(u"actionTime_Date")
        self.actionWord_Wrap = QAction(MainWindow)
        self.actionWord_Wrap.setObjectName(u"actionWord_Wrap")
        self.actionFont = QAction(MainWindow)
        self.actionFont.setObjectName(u"actionFont")
        self.actionZoom = QAction(MainWindow)
        self.actionZoom.setObjectName(u"actionZoom")
        self.actionStatus_Bar = QAction(MainWindow)
        self.actionStatus_Bar.setObjectName(u"actionStatus_Bar")
        self.actionView_Help = QAction(MainWindow)
        self.actionView_Help.setObjectName(u"actionView_Help")
        self.actionAbout_Notes = QAction(MainWindow)
        self.actionAbout_Notes.setObjectName(u"actionAbout_Notes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 0, 821, 551))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 822, 29))
        self.menuLogin = QMenu(self.menubar)
        self.menuLogin.setObjectName(u"menuLogin")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuFormat = QMenu(self.menubar)
        self.menuFormat.setObjectName(u"menuFormat")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuLogin.addAction(self.actionNew)
        self.menuLogin.addAction(self.actionOpen)
        self.menuLogin.addAction(self.actionSave)
        self.menuLogin.addAction(self.actionSave_As)
        self.menuLogin.addSeparator()
        self.menuLogin.addAction(self.actionPage_Setup_2)
        self.menuLogin.addAction(self.actionPrint)
        self.menuLogin.addSeparator()
        self.menuLogin.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_Next)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addAction(self.actionGo_To)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionTime_Date)
        self.menuFormat.addAction(self.actionWord_Wrap)
        self.menuFormat.addAction(self.actionFont)
        self.menuView.addAction(self.actionZoom)
        self.menuView.addAction(self.actionStatus_Bar)
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addAction(self.actionAbout_Notes)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Notes", None))
        self.actionNew.setText(
            QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(
            QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionPage_Setup.setText(
            QCoreApplication.translate("MainWindow", u"Page Setup", None))
        self.actionPage_Setup_2.setText(
            QCoreApplication.translate("MainWindow", u"Page Setup", None))
        self.actionPrint.setText(
            QCoreApplication.translate("MainWindow", u"Print", None))
        self.actionExit.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionUndo.setText(
            QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionCut.setText(
            QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCopy.setText(
            QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(
            QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionDelete.setText(
            QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionFind.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.actionFind_Next.setText(
            QCoreApplication.translate("MainWindow", u"Find Next", None))
        self.actionReplace.setText(
            QCoreApplication.translate("MainWindow", u"Replace", None))
        self.actionGo_To.setText(
            QCoreApplication.translate("MainWindow", u"Go To", None))
        self.actionSelect_All.setText(
            QCoreApplication.translate("MainWindow", u"Select All", None))
        self.actionTime_Date.setText(
            QCoreApplication.translate("MainWindow", u"Time/Date", None))
        self.actionWord_Wrap.setText(
            QCoreApplication.translate("MainWindow", u"Word Wrap", None))
        self.actionFont.setText(QCoreApplication.translate(
            "MainWindow", u"Font...", None))
        self.actionZoom.setText(
            QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.actionStatus_Bar.setText(
            QCoreApplication.translate("MainWindow", u"Status Bar", None))
        self.actionView_Help.setText(
            QCoreApplication.translate("MainWindow", u"View Help", None))
        self.actionAbout_Notes.setText(
            QCoreApplication.translate("MainWindow", u"About Notes", None))
        self.menuLogin.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(
            QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuFormat.setTitle(
            QCoreApplication.translate("MainWindow", u"Format", None))
        self.menuView.setTitle(
            QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self)

        # Initialize UI
        self.setupUi(self)

    def tr(self, text):
        return QObject.tr(self, text)

        # import sys
        # from PySide2 import QtCore, QtGui, QtWidgets
        # from PySide2.QtUiTools import QUiLoader

        # loader = QUiLoader()
        # app = QtWidgets.QApplication(sys.argv)
        # window = loader.load("Notes.ui", None)
        # window.show()
        # app.exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
