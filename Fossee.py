#!/bin/python
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
import sys
import os

from PyQt5 import QtCore, QtWidgets

# test file to try adding features

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        ## To update Marker 1

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 541, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(19, 20, 491, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Path_Cpp = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Path_Cpp.setText("")
        self.Path_Cpp.setObjectName("Path_Cpp")
        self.gridLayout_2.addWidget(self.Path_Cpp, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.Accept_B = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Accept_B.setObjectName("Accept_B")
        self.gridLayout_2.addWidget(self.Accept_B, 6, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        self.Path_V = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Path_V.setText("")
        self.Path_V.setObjectName("Path_V")
        self.gridLayout_2.addWidget(self.Path_V, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.Output = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.Output.setEnabled(True)
        self.Output.setReadOnly(True)
        self.Output.setObjectName("Output")
        self.gridLayout_2.addWidget(self.Output, 5, 0, 1, 4)
        self.FilePicker_Cpp = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.FilePicker_Cpp.setObjectName("FilePicker_Cpp")
        self.gridLayout_2.addWidget(self.FilePicker_Cpp, 1, 3, 1, 1)
        self.FilePicker_V = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.FilePicker_V.setObjectName("FilePicker_V")
        self.gridLayout_2.addWidget(self.FilePicker_V, 3, 3, 1, 1)
        self.Clear_B = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Clear_B.setObjectName("Clear_B")
        self.gridLayout_2.addWidget(self.Clear_B, 6, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## To update Marker 1 end

## og

        # Actions to events
        self.FilePicker_Cpp.clicked.connect(self.PickFile_Cpp)
        self.FilePicker_V.clicked.connect(self.PickFile_V)
        self.Accept_B.clicked.connect(self.Accept)
        self.Clear_B.clicked.connect(self.Clear_all)

## og

    ## to update Marker 2

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Path_Cpp.setPlaceholderText(_translate("MainWindow", "/Path/to/file.cpp"))
        self.label.setText(_translate("MainWindow", "Select Cpp File"))
        self.Accept_B.setText(_translate("MainWindow", "Accept"))
        self.label_3.setText(_translate("MainWindow", " Generate Executable"))
        self.Path_V.setPlaceholderText(_translate("MainWindow", "/Path/to/file.v"))
        self.label_2.setText(_translate("MainWindow", "Select Verilog File"))
        self.FilePicker_Cpp.setText(_translate("MainWindow", "Select File"))
        self.FilePicker_V.setText(_translate("MainWindow", "Select File"))
        self.Clear_B.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
    ## to update Marker 2 end

    def PickFile_Cpp(self):
        try:
            filepath_Cpp = QFileDialog.getOpenFileName(self, 'Select File', "", "*.cpp;; *.c")
            self.Path_Cpp.setText(str(filepath_Cpp[0]))
        except:
            print("File not selected")

    def PickFile_V(self):
        try:
            filepath_V = QFileDialog.getOpenFileName(self, 'Select File', "", "*.v;; *.V")
            self.Path_V.setText(str(filepath_V[0]))
        except:
            print("File not selected")

    def Accept(self):
        try:
            if(os.path.exists(self.Path_Cpp.text()) and os.path.exists(self.Path_V.text())):
                self.Path_Cpp.setStyleSheet("color: black;")
                self.Path_V.setStyleSheet("color: black;")
                self.Command = "verilator --cc --exe --build -j 0 -Wall " + self.Path_Cpp.text() +  " " + self.Path_V.text() + " --Mdir $HOME/obj_dir/"
                self.run_c()
            else:
                self.Path_Cpp.setStyleSheet("color: red;")
                self.Path_V.setStyleSheet("color: red;")
        except:
            print("hello")

    def run_c(self):
        self.t = run_command(self.Command)
        self.Output.clear()
        self.Accept_B.setEnabled(False)
        self.Clear_B.setEnabled(False)
        self.Output.insertPlainText("Please wait...\n")
        self.t.start()
        self.t.P_progress.connect(self.Output_Area)
        self.t.finished.connect(self.after_run_c)

    def Output_Area(self,op):
        self.Output.insertPlainText(op)

    def after_run_c(self):
        self.Accept_B.setEnabled(True)
        self.Clear_B.setEnabled(True)

    def Clear_all(self):
        self.Path_Cpp.setText("")
        self.Path_V.setText("")
        self.Output.clear()

class run_command(QThread):
    P_progress = pyqtSignal(str)
    def __init__(self, command, parent=None):
        QThread.__init__(self, parent)
        self.command = command
    def start(self):
        QThread.start(self)
    def run(self):
        try:
            p = os.popen(self.command)
            if p:
                op = p.read()
                self.P_progress.emit(op)
        except:
            print("error in run_command")

# init the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
