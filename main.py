# import sys
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtUiTools import QUiLoader

# loader = QUiLoader()
# app = QtWidgets.QApplication(sys.argv)
# window = loader.load("Notes.ui", None)
# window.show()
# app.exec_()

import sys
from datetime import datetime

import clipboard  # pip install clipboard
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtPrintSupport import *
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
        self.wordWrapMode = True
        self.currentZoom = 1

        # Code
        self.setWindowTitle(self.TITLE)
        self.setGeometry(300, 200, 800, 600)

        self.textEdit = QTextEdit(self)
        self.textEdit.setFont(QFont('Sanserif', 13))
        self.setCentralWidget(self.textEdit)
        self._setWordWrapFalse()
        if not(self.textEdit.isUndoRedoEnabled()):
            self.textEdit.setUndoRedoEnabled(enable=True)

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
        newFileAction.triggered.connect(self.newFileAction_Clicked)

        openAction = QAction("Open", self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openAction_Clicked)

        saveAction = QAction("Save", self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveAction_Clicked)

        saveAsAction = QAction("Save As", self)
        saveAsAction.setShortcut('Ctrl+Shift+S')
        saveAsAction.triggered.connect(self.saveAsAction_Clicked)

        printAction = QAction('Print', self)
        printAction.setShortcut('Ctrl+P')
        printAction.triggered.connect(self.printAction_Clicked)

        printPreviewAction = QAction("Print Preview", self)
        printPreviewAction.triggered.connect(self.printPreviewAction_Clicked)

        exitAction = QAction("Exit", self)
        exitAction.setShortcut('Ctrl+X')
        exitAction.triggered.connect(self.exit_app)

        # Main Menu: Edit
        # --------------------------------------------------------
        undoAction = QAction("Undo", self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.undoAction_Clicked)

        redoAction = QAction("Redo", self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.triggered.connect(self.redoAction_Clicked)

        cutAction = QAction("Cut", self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.triggered.connect(self.cutAction_Clicked)

        copyAction = QAction("Copy", self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.triggered.connect(self.copyAction_Clicked)

        pasteAction = QAction("Paste", self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.triggered.connect(self.pasteAction_Clicked)

        deleteAction = QAction("Delete", self)
        deleteAction.setShortcut('Del')
        deleteAction.triggered.connect(self.deleteAction_Clicked)
        deleteAction.setEnabled(False)

        findAction = QAction("Find", self)
        findAction.setShortcut('Ctrl+F')
        findAction.triggered.connect(self.findAction_Clicked)
        findAction.setEnabled(False)

        findNextAction = QAction("Find Next", self)
        findNextAction.setShortcut('F3')
        findNextAction.triggered.connect(self.findNextAction_Clicked)
        findNextAction.setEnabled(False)

        replaceAction = QAction("Replace", self)
        replaceAction.setShortcut('Ctrl+H')
        replaceAction.triggered.connect(self.replaceAction_Clicked)
        replaceAction.setEnabled(False)

        goToAction = QAction("Go To", self)
        goToAction.setShortcut('Ctrl+G')
        goToAction.triggered.connect(self.goToAction_Clicked)
        goToAction.setEnabled(False)

        selectAllAction = QAction("Select All", self)
        selectAllAction.setShortcut('Ctrl+A')
        selectAllAction.triggered.connect(self.selectAllAction_Clicked)

        timeDateAction = QAction("Time/Date", self)
        timeDateAction.setShortcut('F5')
        timeDateAction.triggered.connect(self.timeDateAction_Clicked)

        # Main Menu: Format
        # --------------------------------------------------------
        wordWrapAction = QAction("Word Wrap", self)
        wordWrapAction.triggered.connect(self.wordWrapAction_Clicked)

        fontAction = QAction("Font...", self)
        fontAction.triggered.connect(self.selectAllAction_Clicked)
        fontAction.setEnabled(False)

        # Main Menu: View
        # --------------------------------------------------------
        zoomInAction = QAction("Zoom In", self)
        zoomInAction.triggered.connect(self.zoomInAction_Clicked)

        zoomOutAction = QAction("Zoom Out", self)
        zoomOutAction.triggered.connect(self.zoomOutAction_Clicked)

        restoreDefaultZoomAction = QAction("Restore Default Zoom", self)
        restoreDefaultZoomAction.triggered.connect(
            self.restoreDefaultZoomAction_Clicked)
        restoreDefaultZoomAction.setEnabled(False)

        # Main Menu: Help
        # --------------------------------------------------------
        viewHelpAction = QAction("View Help", self)
        viewHelpAction.setEnabled(False)

        sendFeedbackAction = QAction("Send Feedback", self)
        sendFeedbackAction.setEnabled(False)

        aboutAction = QAction("About Notepad", self)
        aboutAction.setEnabled(False)

        # FINALLY, Adding everything
        # --------------------------------------------------------
        # File Menu
        fileMenu.addAction(newFileAction)  # new file
        fileMenu.addAction(openAction)  # open
        fileMenu.addAction(saveAction)  # save
        fileMenu.addAction(saveAsAction)  # save as
        fileMenu.addSeparator()  # seperator
        fileMenu.addAction(printAction)  # print
        fileMenu.addAction(printPreviewAction)  # print preview
        fileMenu.addSeparator()  # seperator
        fileMenu.addAction(exitAction)  # exit

        # Edit Menu
        editMenu.addAction(undoAction)  # undo
        editMenu.addAction(redoAction)  # redo
        editMenu.addSeparator()  # seperator
        editMenu.addAction(cutAction)  # cut
        editMenu.addAction(copyAction)  # copy
        editMenu.addAction(pasteAction)  # paste
        # editMenu.addAction(deleteAction)  # delete
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

        if self.fileName:
            with open(file=self.fileName, mode="rt", encoding="utf-8") as fileOpen:
                fileOpenContent = fileOpen.read()
            if self._getTextBoxContent() != fileOpenContent:
                self._newFileCheckSavedOrNot()

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

    def _getSaveAsFileName(self):
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.getSaveFileName
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self,
            "Save file | " + self.TITLE,
            "",
            "All Files(*);;Text Files (*.txt)")
        return fileName

    def _getTextBoxContent(self):
        return str(self.textEdit.toPlainText())

    def saveAsAction_Clicked(self):
        fileNameSave = self._getSaveAsFileName()
        if fileNameSave:
            self.fileName = fileNameSave
            with open(file=self.fileName, mode="wt", encoding="utf-8") as saveFile:
                saveFile.write(self._getTextBoxContent())

    def saveAction_Clicked(self):
        if self.fileName:
            with open(file=self.fileName, mode="wt", encoding="utf-8") as saveFile:
                saveFile.write(self._getTextBoxContent())
        else:
            self.saveAsAction_Clicked()

    def _saveOrExitwithoutSaving_checkbox(self):
        qm = QMessageBox
        ret = qm.question(
            self, '', "Do you want to save changes?", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.saveAction_Clicked()
        else:
            # self.newFileAction_Clicked()
            self._newFileActionSupport()

    def _newFileCheckSavedOrNot(self):
        if self.fileName:
            with open(file=self.fileName, mode="rt", encoding="utf-8") as fileOpen:
                fileOpenContent = fileOpen.read()
            if self._getTextBoxContent() != fileOpenContent:
                self._saveOrExitwithoutSaving_checkbox()
        else:
            self._saveOrExitwithoutSaving_checkbox()

    def _newFileActionSupport(self):
        try:
            self.saveAsAction_Clicked()
            if self.fileName:
                with open(file=self.fileName, mode="rt", encoding="utf-8") as fileOpen:
                    fileOpenContent = fileOpen.read()
                    self.textEdit.setPlainText(fileOpenContent)
        except Exception as e:
            print("Something is really wrong lol:", e)

    def newFileAction_Clicked(self):
        if self._getTextBoxContent():
            self._newFileCheckSavedOrNot()
        else:
            self._newFileActionSupport()

    def _printPreviewActionSupport(self, printer):
        self.textEdit.print_(printer)

    def printPreviewAction_Clicked(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self._printPreviewActionSupport)
        previewDialog.exec_()

    def printAction_Clicked(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def undoAction_Clicked(self):
        # https://doc.qt.io/archives/qtforpython-5.12/PySide2/QtWidgets/QTextEdit.html#PySide2.QtWidgets.PySide2.QtWidgets.QTextEdit.setUndoRedoEnabled
        self.textEdit.undo()

    def redoAction_Clicked(self):
        self.textEdit.redo()

    def cutAction_Clicked(self):
        self.textEdit.cut()

    def copyAction_Clicked(self):
        self.textEdit.copy()

    def pasteAction_Clicked(self):
        self.textEdit.paste()

    def deleteAction_Clicked(self):
        # oldCopied = clipboard.paste()
        # self.cutAction_Clicked()
        # clipboard.copy(str(oldCopied))
        pass

    def findAction_Clicked(self):
        # flag = QTextDocument.FindBackward
        # self.textEdit.find('A', flag)
        pass

    def findNextAction_Clicked(self):
        pass

    def replaceAction_Clicked(self):
        pass

    def goToAction_Clicked(self):
        pass

    def selectAllAction_Clicked(self):
        self.textEdit.selectAll()

    def timeDateAction_Clicked(self):
        timeNow = datetime.now()
        self.textEdit.insertPlainText(
            str(timeNow.strftime("%H:%M - %d/%m/%Y")))

    def fontAction_Clicked(self):
        pass

    def zoomInAction_Clicked(self):
        self.textEdit.zoomIn(1)
        self.currentZoom += 1

    def zoomOutAction_Clicked(self):
        self.textEdit.zoomOut(1)
        self.currentZoom -= 1

    def restoreDefaultZoomAction_Clicked(self):
        self.textEdit.zoomIn(self.currentZoom)

    def exit_app(self):
        self.close()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    myapp.exec_()
    sys.exit()
