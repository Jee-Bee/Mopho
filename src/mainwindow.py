# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from . import varlists as vl



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # define global vars from varlists
        self.clock_status = vl.ClockStatus
        self.midi_sysex_dump = vl.MidiSysExDump
        # define standard vars from varlists
        self.all_parameters = vl.AllParameters
        self.osc_shape = vl.OscShape
        self.glide_mode = vl.GlideMode
        self.key_assign = vl.KeyAssign
        self.lfo_frequency = vl.LfoFrequency
        self.lfo_shape = vl.LfoShape
        self.modulation_destinations = vl.ModulationDestinations
        self.modulation_sources = vl.ModelationSources
        self.push_note = vl.PushNote
        self.push_mode = vl.PushMode
        self.clock_divide = vl.ClockDivide
        self.appregiator_list = vl.AppregiatorList
        self.sequencer_trigger = vl.SeqTrigger
        self.catagory = vl.catagory

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

        # fill dropdown menus
        # Osc
        self.ui.coB_GlideMode.addItems(self.glide_mode)
        self.ui.coB_KeyMode.addItems(self.key_assign)
        # Envelope3
        self.ui.coB_Env3Dest.addItems(self.modulation_destinations)
        # Lfo
        self.ui.coB_LfoS1.addItems(self.lfo_shape)
        self.ui.coB_LfoD1.addItems(self.modulation_destinations)
        self.ui.coB_LfoS2.addItems(self.lfo_shape)
        self.ui.coB_LfoD2.addItems(self.modulation_destinations)
        self.ui.coB_LfoS3.addItems(self.lfo_shape)
        self.ui.coB_LfoD3.addItems(self.modulation_destinations)
        self.ui.coB_LfoS4.addItems(self.lfo_shape)
        self.ui.coB_LfoD4.addItems(self.modulation_destinations)
        # Modulators
        self.ui.coB_ModSource1.addItems(self.modulation_sources)
        self.ui.coB_ModDest1.addItems(self.modulation_destinations)
        self.ui.coB_ModSource2.addItems(self.modulation_sources)
        self.ui.coB_ModDest2.addItems(self.modulation_destinations)
        self.ui.coB_ModSource3.addItems(self.modulation_sources)
        self.ui.coB_ModDest3.addItems(self.modulation_destinations)
        self.ui.coB_ModSource4.addItems(self.modulation_sources)
        self.ui.coB_ModDest4.addItems(self.modulation_destinations)

        self.ui.coB_ModModWheelDest.addItems(self.modulation_destinations)
        self.ui.coB_ModPressDest.addItems(self.modulation_destinations)
        self.ui.coB_ModBreathDest.addItems(self.modulation_destinations)
        self.ui.coB_ModVelocDest.addItems(self.modulation_destinations)
        self.ui.coB_ModFootDest.addItems(self.modulation_destinations)
        # Appreggiator
        self.ui.coB_Appr.addItems(self.appregiator_list)
        # Push It
        self.ui.coB_PiNote.addItems(self.push_note)
        self.ui.coB_PiMode.addItems(self.push_mode)
        # Program
        # - Bank and location  # TODO
        self.ui.coB_ProgCatagory.addItems(self.catagory)
        # Button Assingment
        self.ui.coB_AssKn1.addItems(self.all_parameters)
        self.ui.coB_AssKn2.addItems(self.all_parameters)
        self.ui.coB_AssKn3.addItems(self.all_parameters)
        self.ui.coB_AssKn4.addItems(self.all_parameters)

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
