# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()
        # self.actionCloseApp.Triggered.connect(self.close_app)

    def load_ui(self):
        # https://stackoverflow.com/questions/14892713/how-do-you-load-ui-files-onto-python-classes-with-pyside/14894550#14894550
        # https://stackoverflow.com/questions/7144313/loading-qtdesigners-ui-files-in-pyside
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parents[1] / "ui/Mopho.ui")
        # path = os.fspath(Path(__file__).resolve().parents[1] / "ui/simpleui.ui")
        print(path)
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        self.ui.setGeometry(50, 40, 1280, 720)
        # Some change below based on https://pythonprogramming.net/basic-gui-pyqt-tutorial/
        # self.ui.setWindowTitle("not a DSI Mopho Editor yet")  # Done in ui file
        # self.ui.setWindowIcon(QtGui.QIcon(os.fspath(Path(__file__).resolve().parents[1] / "ui/logos/O_logo-32x32.png")))  # Probably done in ui file OSX don't show icon
        self.ui.show()

        # Close App from Menu
        self.ui.actionCloseApp.triggered.connect(self.close_app)

        ui_file.close()

    # TODO: where to put close_app(). Here or in another file
    def close_app(self):
        choice = QtWidgets.QMessageBox.question(self, "Exit Mopho Editor", "Are you sure you wanna leave the Mopho Editor?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    widget = MainWindow()
    # widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    mainw = main()
