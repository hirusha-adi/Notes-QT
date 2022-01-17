import sys
from PySide2.QtWidgets import QApplication, QFileDialog


def get_filename():
    app = QApplication([])
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(
        None,
        "QFileDialog.getOpenFileName()",
        "",
        "All Files (*);;Text Files (*.txt)",
        options=options,
    )
    return fileName


if __name__ == "__main__":
    filename = get_filename()
    if filename:
        print(filename)
