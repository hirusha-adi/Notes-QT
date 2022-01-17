# import sys
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtUiTools import QUiLoader

# loader = QUiLoader()
# app = QtWidgets.QApplication(sys.argv)
# window = loader.load("Notes.ui", None)
# window.show()
# app.exec_()

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # main stuff
        self.NAME = "KQ-Pad"
        self.VERSION = "0.1"
        self.TITLE = self.NAME + " | " + self.VERSION

        # Needed for the functions to function
        self.fileName = None
        self.wordWrapMode = False

        # Code
        self.setWindowTitle(self.TITLE)
        self.setGeometry(300, 200, 800, 600)

        self.textEdit = QTextEdit(self)
        self.textEdit.setFont(QFont('Sanserif', 13))
        self.setCentralWidget(self.textEdit)

        self.setIcon()

        self.create_menu()
        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Format')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        # Main Menu: File
        # --------------------------------------------------------
        newFileAction = QAction("New", self)
        newFileAction.setShortcut('Ctrl+N')

        openAction = QAction("Open", self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openAction_Clicked)

        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.getSaveFileName
        saveAction = QAction("Save", self)
        saveAction.setShortcut('Ctrl+S')

        saveAsAction = QAction("Save", self)

        pageSetupAction = QAction("Page Setup", self)

        printAction = QAction('Print', self)
        printAction.setShortcut('Ctrl+P')

        exitAction = QAction("Exit", self)
        exitAction.setShortcut('Ctrl+X')
        exitAction.triggered.connect(self.exit_app)

        # Main Menu: Edit
        # --------------------------------------------------------
        undoAction = QAction("Undo", self)
        undoAction.setShortcut('Ctrl+Z')

        cutAction = QAction("Cut", self)
        cutAction.setShortcut('Ctrl+X')

        copyction = QAction("Copy", self)
        copyction.setShortcut('Ctrl+C')

        pasteAction = QAction("Paste", self)
        pasteAction.setShortcut('Ctrl+V')

        deleteAction = QAction("Delete", self)
        deleteAction.setShortcut('Del')

        findAction = QAction("Find", self)
        findAction.setShortcut('Ctrl+F')

        findNextAction = QAction("Find Next", self)
        findNextAction.setShortcut('F3')

        replaceAction = QAction("Replace", self)
        replaceAction.setShortcut('Ctrl+H')

        goToAction = QAction("Go To", self)
        goToAction.setShortcut('Ctrl+G')

        selectAllAction = QAction("Select All", self)
        selectAllAction.setShortcut('Ctrl+A')

        timeDateAction = QAction("Time/Date", self)
        timeDateAction.setShortcut('F5')

        # Main Menu: Format
        # --------------------------------------------------------
        wordWrapAction = QAction("Word Wrap", self)
        wordWrapAction.triggered.connect(self.wordWrapAction_Clicked)
        fontAction = QAction("Font...", self)

        # Main Menu: View
        # --------------------------------------------------------
        zoomInAction = QAction("Zoom In", self)
        zoomOutAction = QAction("Zoom Out", self)
        restoreDefaultZoomAction = QAction("Restore Default Zoom", self)
        statusBarAction = QAction("Status Bar", self)

        # Main Menu: Help
        # --------------------------------------------------------
        viewHelpAction = QAction("View Help", self)
        sendFeedbackAction = QAction("Send Feedback", self)
        aboutAction = QAction("About Notepad", self)

        # FINALLY, Adding everything
        # --------------------------------------------------------
        # File Menu
        fileMenu.addAction(newFileAction)  # new file
        fileMenu.addAction(openAction)  # open
        fileMenu.addAction(saveAction)  # save
        fileMenu.addAction(saveAsAction)  # save as
        fileMenu.addSeparator()  # seperator
        fileMenu.addAction(pageSetupAction)  # page setup
        fileMenu.addAction(printAction)  # print
        fileMenu.addSeparator()  # seperator
        fileMenu.addAction(exitAction)  # exit

        # Edit Menu
        editMenu.addAction(undoAction)  # undo
        editMenu.addSeparator()  # seperator
        editMenu.addAction(cutAction)  # cut
        editMenu.addAction(copyction)  # copy
        editMenu.addAction(pasteAction)  # paste
        editMenu.addAction(deleteAction)  # delete
        editMenu.addSeparator()  # seperator
        editMenu.addAction(findAction)  # find
        editMenu.addAction(findNextAction)  # find next
        editMenu.addAction(replaceAction)  # find
        editMenu.addAction(goToAction)  # find
        editMenu.addSeparator()  # seperator
        editMenu.addAction(selectAllAction)  # find
        editMenu.addAction(timeDateAction)  # find

        # Format Menu
        fontMenu.addAction(wordWrapAction)
        fontMenu.addAction(fontAction)

        # View Menu
        viewMenu.addAction(zoomInAction)  # zoom in
        viewMenu.addAction(zoomOutAction)  # zoom out
        # restore to default zoom level
        viewMenu.addAction(restoreDefaultZoomAction)
        viewMenu.addSeparator()  # seperator
        viewMenu.addAction(statusBarAction)  # status bar

        # Help Menu
        helpMenu.addAction(viewHelpAction)  # view help
        helpMenu.addAction(sendFeedbackAction)  # send feedback
        helpMenu.addSeparator()  # seperator
        helpMenu.addAction(aboutAction)  # about

    def _getFilenameToOpen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "Open File | " + self.TITLE,
            "",
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )
        return fileName

    def openAction_Clicked(self):
        # https://stackoverflow.com/questions/60977801/file-browser-with-pyside2-get-the-path-of-the-file-and-then-kill-the-gui
        self.fileName = self._getFilenameToOpen()
        if self.fileName:
            with open(file=self.fileName, mode="rt", encoding="utf-8") as fileOpen:
                fileOpenContent = fileOpen.read()
            self.textEdit.setPlainText(fileOpenContent)

    def _setWordWrapFalse(self):
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

    def _setWordWrapTrue(self):
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)

    def wordWrapAction_Clicked(self):
        if self.wordWrapMode == False:
            self._setWordWrapFalse()
            self.wordWrapMode = True

        elif self.wordWrapMode == True:
            self._setWordWrapTrue()
            self.wordWrapMode = False

    def exit_app(self):
        self.close()


myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()
