import PyQt5
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import *
import sys
import os
import subprocess
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        ## Set up UI
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 20, 511, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.FilePicker_Cpp = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.FilePicker_Cpp.setObjectName("FilePicker_Cpp")
        self.gridLayout_2.addWidget(self.FilePicker_Cpp, 5, 3, 1, 1)
        self.FilePicker_V = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.FilePicker_V.setObjectName("FilePicker_V")
        self.gridLayout_2.addWidget(self.FilePicker_V, 3, 3, 1, 1)
        self.Clear_B = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Clear_B.setObjectName("Clear_B")
        self.gridLayout_2.addWidget(self.Clear_B, 10, 3, 1, 1)
        self.Accept_B = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Accept_B.setObjectName("Accept_B")
        self.gridLayout_2.addWidget(self.Accept_B, 10, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)
        self.Path_V = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Path_V.setText("")
        self.Path_V.setObjectName("Path_V")
        self.gridLayout_2.addWidget(self.Path_V, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.Path_Cpp = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Path_Cpp.setText("")
        self.Path_Cpp.setObjectName("Path_Cpp")
        self.gridLayout_2.addWidget(self.Path_Cpp, 5, 1, 1, 1)
        self.Output = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.Output.setEnabled(True)
        self.Output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Output.setReadOnly(True)
        self.Output.setObjectName("Output")
        self.gridLayout_2.addWidget(self.Output, 9, 0, 1, 4)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setAcceptDrops(False)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Link = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Link.setAcceptDrops(False)
        self.Link.setAutoFillBackground(False)
        self.Link.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Link.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Link.setTextFormat(QtCore.Qt.MarkdownText)
        self.Link.setScaledContents(False)
        self.Link.setOpenExternalLinks(True)
        self.Link.setObjectName("Link")
        self.verticalLayout.addWidget(self.Link)
        self.Install_Output = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.Install_Output.setReadOnly(True)
        self.Install_Output.setObjectName("Install_Output")
        self.verticalLayout.addWidget(self.Install_Output)
        self.Push_to_install = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Push_to_install.setEnabled(True)
        self.Push_to_install.setObjectName("Push_to_install")
        self.verticalLayout.addWidget(self.Push_to_install)
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

        # Actions to events
        self.link_Actions()
    
    def link_Actions(self):
        self.FilePicker_Cpp.clicked.connect(self.PickFile_Cpp)
        self.FilePicker_V.clicked.connect(self.PickFile_V)
        self.Accept_B.clicked.connect(self.Accept)
        self.Clear_B.clicked.connect(self.Clear_all)
        self.Push_to_install.clicked.connect(self.install_v)
        self.Check_verilator()
        
    ## to update Marker 2
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FilePicker_Cpp.setText(_translate("MainWindow", "Select File"))
        self.FilePicker_V.setText(_translate("MainWindow", "Select File"))
        self.Clear_B.setText(_translate("MainWindow", "Clear"))
        self.Accept_B.setText(_translate("MainWindow", "Accept"))
        self.label_2.setText(_translate("MainWindow", "Select Verilog File"))
        self.label_3.setText(_translate("MainWindow", " Generate Executable"))
        self.Path_V.setPlaceholderText(_translate("MainWindow", "/Path/to/file.v"))
        self.label.setText(_translate("MainWindow", "Select Cpp File"))
        self.Path_Cpp.setPlaceholderText(_translate("MainWindow", "/Path/to/file.cpp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Generate"))
        self.Link.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><a href=\"https://verilator.org/guide/latest/install.html\"><span style=\" text-decoration: underline; color:#2980b9;\">How to install Verilator from Source </span></a>(Recomended for custom install process)</p></body></html>"))
        self.Install_Output.setPlainText(_translate("MainWindow", "Prerequisites for Ubuntu base : \n"
            "(Resolve dependancies befor compiling from source)\n"
            "----------------------------------------------------------------------------\n"
            "$ sudo apt-get install git perl python3 make autoconf g++ flex bison ccache\n"
            "$ sudo apt-get install libgoogle-perftools-dev numactl perl-doc\n"
            "$ sudo apt-get install libfl2  \n"
            "$ sudo apt-get install libfl-dev  \n"
            "$ sudo apt-get install zlibc zlib1g zlib1g-dev  \n"
            "\n"
            "Note: If using non-ubuntu based system use the provided package manager to install\n"))
        self.Push_to_install.setText(_translate("MainWindow", "Install latest release of Verilator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Installation"))

    def PickFile_Cpp(self):
        try:
            filepath_Cpp = QFileDialog.getOpenFileName(None, 'Select File', "", "*.cpp;; *.c")
            self.Path_Cpp.setText(str(filepath_Cpp[0]))
        except:
            self.Output_Area("Cpp File not selected")

    def PickFile_V(self):
        try:
            filepath_V = QFileDialog.getOpenFileName(None, 'Select File', "", "*.v;; *.V")
            self.Path_V.setText(str(filepath_V[0]))
        except:
            self.Output_Area("V File not selected")
    
    def Accept(self):
        try:
            if(self.Path_Cpp.text()=="" and self.Path_V.text()!="" and os.path.exists(self.Path_V.text())):
                self.Output_dir = str(QFileDialog.getExistingDirectory(None, 'Select Output Directory'))
                self.Command = "verilator --binary -j -Wall " + self.Path_V.text() + " --Mdir " + self.Output_dir              
                self.Pass_file_to_command()
            elif(os.path.exists(self.Path_Cpp.text()) and os.path.exists(self.Path_V.text())):
                self.Output_dir = str(QFileDialog.getExistingDirectory(None, 'Select Output Directory'))
                self.Command = "verilator --cc --exe --build -j 0 -Wall " +\
                                self.Path_Cpp.text() +  " " + \
                                self.Path_V.text() + " --Mdir " + self.Output_dir
                self.Pass_file_to_command()
            else:
                self.Path_Cpp.setStyleSheet("color: red;")
                self.Path_V.setStyleSheet("color: red;")
        except:
            QMessageBox.warning(None,"Error!!","Error in Accept funtion")

    def Pass_file_to_command(self):
        self.Path_Cpp.setStyleSheet("color: black;")
        self.Path_V.setStyleSheet("color: black;")
        self.run_c()

    def run_c(self):
        self.t1 = run_command(self.Command)
        #self.Output.clear()
        self.Accept_B.setEnabled(False)
        self.Clear_B.setEnabled(False)
        self.Output_Area("Please wait...\n")
        self.t1.start()
        self.t1.P_progress.connect(self.Output_Area)
        self.t1.finished.connect(self.after_run_c)

    def Output_Area(self,op):
        self.Output.insertPlainText(op)

    def after_run_c(self):
        self.Output_Area("\nOutput in " + self.Output_dir + "\n")
        self.Command =  self.Output_dir + "/Vour"
        self.Output_Area("\nOutput of " + self.Command + ": \n\n")
        self.t2 = run_command(self.Command)
        self.t2.start()
        self.t2.P_progress.connect(self.Output_Area)
        self.t2.finished.connect(self.enable_B)

    def enable_B(self):
        self.Accept_B.setEnabled(True)
        self.Clear_B.setEnabled(True)

    def Clear_all(self):
        self.Path_V.setText("")
        self.Path_Cpp.setText("")
        self.Output.clear()

    def Check_verilator(self):
        verilator_path = subprocess.getoutput("whereis verilator").split()
        verilator_path.pop(0)
        verilator_version = subprocess.getoutput("verilator --version").split()
        verilator_version.pop(0)
        

        if("/usr/bin/verilator" in verilator_path or "/usr/share/verilator" in verilator_path or "/usr/local/bin/verilator" in verilator_path):
            print("Verilator installed")
            self.Accept_B.setEnabled(True)
            self.Clear_B.setEnabled(True)
            if("5.002" in verilator_version or "5.004" in verilator_version or "5.006" in verilator_version):
                self.Output_Area("Installed Verilator version: " + \
                                  subprocess.getoutput("verilator --version") + "\n")
                self.Push_to_install.setEnabled(False)
            else:
                QMessageBox.warning(None,"ERROR!","Outdated Version of Verilator installed, \
                                    commands might not work as inteded")
                self.Push_to_install.setEnabled(True)
        else:
            self.Accept_B.setEnabled(False)
            self.Clear_B.setEnabled(False)
            self.Output_Area("Please Install Verilator befor using this tool...\n")
            QMessageBox.warning(None,"ERROR!","Verilator not installed")

    def install_v(self):
        try:
            self.Push_to_install.setEnabled(False)
            self.Install_Output.clear()

            c=[  "# echo '# Please wait... cloning https://github.com/verilator/verilator'"
                ,"git clone https://github.com/verilator/verilator ; echo '# repo cloned...'"
                ,"unset VERILATOR_ROOT"
                ,"pwd ; cd ./verilator/ ; echo '# changing dir to verilator/' ; git checkout stable ; autoconf ; ./configure"
                ,"echo '# please wait... This may take some time'"
                ,"cd ./verilator/ ; make"
                ,"echo 'installing make...'"
                ,"cd ./verilator/ ; pkexec --keep-cwd make install ; sleep 2"
                ,"echo '# verilator installed...'"
                ,"verilator --version"]
                # make install
            self.c0 = install_verilator(str(c[0]))
            self.c1 = install_verilator(str(c[1]))
            self.c2 = install_verilator(str(c[2]))
            self.c3 = install_verilator(str(c[3]))
            self.c4 = install_verilator(str(c[4]))
            self.c5 = install_verilator(str(c[5]))
            self.c6 = install_verilator(str(c[6]))
            self.c7 = install_verilator(str(c[7]))
            self.c8 = install_verilator(str(c[8]))
            self.c9 = install_verilator(str(c[9]))

            self.c0.P_progress.connect(self.install_status)
            self.c1.P_progress.connect(self.install_status)
            self.c2.P_progress.connect(self.install_status)
            self.c3.P_progress.connect(self.install_status)
            self.c4.P_progress.connect(self.install_status)
            self.c5.P_progress.connect(self.install_status)
            self.c6.P_progress.connect(self.install_status)
            self.c7.P_progress.connect(self.install_status)
            self.c8.P_progress.connect(self.install_status)
            self.c9.P_progress.connect(self.install_status)

            self.c0.start()
            self.c0.finished.connect(self.c1.start)
            self.c1.finished.connect(self.c2.start)
            self.c2.finished.connect(self.c3.start)
            self.c3.finished.connect(self.c4.start)
            self.c4.finished.connect(self.c5.start)
            self.c5.finished.connect(self.c6.start)
            self.c6.finished.connect(self.c7.start)
            self.c7.finished.connect(self.c8.start)
            self.c8.finished.connect(self.c9.start)
            self.c9.finished.connect(self.after_install_v)
        except:
            print("errot during installation")

    def install_status(self,status):
        self.Install_Output.insertPlainText(status)

    def after_install_v(self):
        self.Accept_B.setEnabled(True)
        self.Clear_B.setEnabled(True)
        self.Check_verilator()

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
            QMessageBox.warning(None,"Invalid Commands!","Error in run_command")

class install_verilator(QThread):
    P_progress = pyqtSignal(str)                
    def __init__(self, command, parent=None):
        QThread.__init__(self, parent)
        self.command = command
    def start(self):
        QThread.start(self)
    def run(self):
        try:
            p = subprocess.run(str(self.command),shell=True,capture_output=True)
            status = p.stdout.decode()
            if p:
                print(status)
                self.P_progress.emit(status)
        except:
            QMessageBox.warning(None,"Invalid Install Commands!","Error in install_verilator")

# init the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
