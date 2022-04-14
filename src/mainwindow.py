# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        # https://stackoverflow.com/questions/14892713/how-do-you-load-ui-files-onto-python-classes-with-pyside/14894550#14894550
        # https://stackoverflow.com/questions/7144313/loading-qtdesigners-ui-files-in-pyside
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parents[1] / "ui/Mopho.ui")
        # path = os.fspath(Path(__file__).resolve().parents[1] / "ui/simpleui.ui")
        print(path)
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        ui_window = loader.load(ui_file, self)
        ui_window.show()
        ui_file.close()

def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    widget = MainWindow()
    # widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    mainw = main()
