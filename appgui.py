# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PB.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1031, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.pulse_train_generator = QtWidgets.QWidget()
        self.pulse_train_generator.setObjectName("pulse_train_generator")
        self.width = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.width.setGeometry(QtCore.QRect(160, 100, 121, 31))
        self.width.setObjectName("width")
        self.label = QtWidgets.QLabel(self.pulse_train_generator)
        self.label.setGeometry(QtCore.QRect(20, 80, 91, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.separation = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.separation.setGeometry(QtCore.QRect(160, 150, 121, 31))
        self.separation.setObjectName("separation")
        self.label_3 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 111, 71))
        self.label_3.setObjectName("label_3")
        self.Num_of_pulse_trains = QtWidgets.QLCDNumber(self.pulse_train_generator)
        self.Num_of_pulse_trains.setGeometry(QtCore.QRect(780, 30, 81, 31))
        self.Num_of_pulse_trains.setObjectName("Num_of_pulse_trains")
        self.label_4 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_4.setGeometry(QtCore.QRect(630, 20, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.add_pulse_train = QtWidgets.QPushButton(self.pulse_train_generator)
        self.add_pulse_train.setGeometry(QtCore.QRect(90, 310, 121, 41))
        self.add_pulse_train.setObjectName("add_pulse_train")
        self.on_time = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.on_time.setGeometry(QtCore.QRect(160, 50, 121, 31))
        self.on_time.setObjectName("on_time")
        self.label_5 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 101, 71))
        self.label_5.setObjectName("label_5")
        self.num_of_pulses = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.num_of_pulses.setGeometry(QtCore.QRect(160, 200, 121, 31))
        self.num_of_pulses.setObjectName("num_of_pulses")
        self.label_6 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 121, 71))
        self.label_6.setObjectName("label_6")
        self.pulses_in_sequence = QtWidgets.QTextBrowser(self.pulse_train_generator)
        self.pulses_in_sequence.setGeometry(QtCore.QRect(320, 190, 681, 192))
        self.pulses_in_sequence.setObjectName("pulses_in_sequence")
        self.label_7 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_7.setGeometry(QtCore.QRect(570, 155, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 111, 71))
        self.label_8.setObjectName("label_8")
        self.channels = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.channels.setGeometry(QtCore.QRect(160, 250, 121, 31))
        self.channels.setObjectName("channels")
        self.label_9 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_9.setGeometry(QtCore.QRect(340, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_10.setGeometry(QtCore.QRect(360, 40, 81, 31))
        self.label_10.setObjectName("label_10")
        self.pulse_index = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.pulse_index.setGeometry(QtCore.QRect(450, 40, 121, 31))
        self.pulse_index.setObjectName("pulse_index")
        self.delete_pulse_train = QtWidgets.QPushButton(self.pulse_train_generator)
        self.delete_pulse_train.setGeometry(QtCore.QRect(400, 90, 141, 41))
        self.delete_pulse_train.setObjectName("delete_pulse_train")
        self.generate_instr = QtWidgets.QPushButton(self.pulse_train_generator)
        self.generate_instr.setGeometry(QtCore.QRect(320, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generate_instr.setFont(font)
        self.generate_instr.setObjectName("generate_instr")
        self.save_instr = QtWidgets.QPushButton(self.pulse_train_generator)
        self.save_instr.setGeometry(QtCore.QRect(550, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_instr.setFont(font)
        self.save_instr.setObjectName("save_instr")
        self.load_instr = QtWidgets.QPushButton(self.pulse_train_generator)
        self.load_instr.setGeometry(QtCore.QRect(780, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.load_instr.setFont(font)
        self.load_instr.setObjectName("load_instr")
        self.label_11 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_11.setGeometry(QtCore.QRect(350, 470, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.filename = QtWidgets.QLineEdit(self.pulse_train_generator)
        self.filename.setGeometry(QtCore.QRect(440, 470, 451, 31))
        self.filename.setObjectName("filename")
        self.label_12 = QtWidgets.QLabel(self.pulse_train_generator)
        self.label_12.setGeometry(QtCore.QRect(110, 370, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.status = QtWidgets.QTextBrowser(self.pulse_train_generator)
        self.status.setGeometry(QtCore.QRect(30, 400, 231, 111))
        self.status.setObjectName("status")
        self.clear = QtWidgets.QPushButton(self.pulse_train_generator)
        self.clear.setGeometry(QtCore.QRect(100, 520, 71, 21))
        self.clear.setObjectName("clear")
        self.tabWidget.addTab(self.pulse_train_generator, "")
        self.pb_control = QtWidgets.QWidget()
        self.pb_control.setObjectName("pb_control")
        self.messages = QtWidgets.QTextBrowser(self.pb_control)
        self.messages.setGeometry(QtCore.QRect(10, 50, 561, 281))
        self.messages.setObjectName("messages")
        self.label_13 = QtWidgets.QLabel(self.pb_control)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.pb_control)
        self.label_14.setGeometry(QtCore.QRect(670, 420, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.send_pb_instructions = QtWidgets.QPushButton(self.pb_control)
        self.send_pb_instructions.setGeometry(QtCore.QRect(300, 440, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.send_pb_instructions.setFont(font)
        self.send_pb_instructions.setObjectName("send_pb_instructions")
        self.close_pb = QtWidgets.QPushButton(self.pb_control)
        self.close_pb.setGeometry(QtCore.QRect(300, 350, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close_pb.setFont(font)
        self.close_pb.setObjectName("close_pb")
        self.init_pb = QtWidgets.QPushButton(self.pb_control)
        self.init_pb.setGeometry(QtCore.QRect(10, 350, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.init_pb.setFont(font)
        self.init_pb.setObjectName("init_pb")
        self.get_pb_status = QtWidgets.QPushButton(self.pb_control)
        self.get_pb_status.setGeometry(QtCore.QRect(10, 440, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.get_pb_status.setFont(font)
        self.get_pb_status.setObjectName("get_pb_status")
        self.start_pulse_sequence = QtWidgets.QPushButton(self.pb_control)
        self.start_pulse_sequence.setGeometry(QtCore.QRect(620, 50, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.start_pulse_sequence.setFont(font)
        self.start_pulse_sequence.setObjectName("start_pulse_sequence")
        self.stop_pulse_sequence = QtWidgets.QPushButton(self.pb_control)
        self.stop_pulse_sequence.setGeometry(QtCore.QRect(620, 220, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stop_pulse_sequence.setFont(font)
        self.stop_pulse_sequence.setObjectName("stop_pulse_sequence")
        self.clear_messages = QtWidgets.QPushButton(self.pb_control)
        self.clear_messages.setGeometry(QtCore.QRect(390, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clear_messages.setFont(font)
        self.clear_messages.setObjectName("clear_messages")
        self.tabWidget.addTab(self.pb_control, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pulse Width"))
        self.label_2.setText(_translate("MainWindow", "Add Pulse Train"))
        self.label_3.setText(_translate("MainWindow", "Pulse Separation"))
        self.label_4.setText(_translate("MainWindow", "Number of Pulse Trains"))
        self.add_pulse_train.setText(_translate("MainWindow", "Add Pulse Train"))
        self.label_5.setText(_translate("MainWindow", "Pulse On Time"))
        self.label_6.setText(_translate("MainWindow", "Number of Pulses"))
        self.label_7.setText(_translate("MainWindow", "Pulses in Sequence"))
        self.label_8.setText(_translate("MainWindow", "Channels"))
        self.label_9.setText(_translate("MainWindow", "Delete Pulse Train"))
        self.label_10.setText(_translate("MainWindow", "Pulse Index"))
        self.delete_pulse_train.setText(_translate("MainWindow", "Delete Pulse Train"))
        self.generate_instr.setText(_translate("MainWindow", "Generate Instructions"))
        self.save_instr.setText(_translate("MainWindow", "Save Instructions"))
        self.load_instr.setText(_translate("MainWindow", "Load Instructions"))
        self.label_11.setText(_translate("MainWindow", "Filename"))
        self.label_12.setText(_translate("MainWindow", "Status"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pulse_train_generator), _translate("MainWindow", "Pulse Train Generator"))
        self.label_13.setText(_translate("MainWindow", "Messages"))
        self.label_14.setText(_translate("MainWindow", "PB Clock Speed: 400 Mhz"))
        self.send_pb_instructions.setText(_translate("MainWindow", "Send Sequence to PulseBlaster"))
        self.close_pb.setText(_translate("MainWindow", "Close PulseBlaster"))
        self.init_pb.setText(_translate("MainWindow", "Initialize PulseBlaster"))
        self.get_pb_status.setText(_translate("MainWindow", "Get PulseBlaster Status"))
        self.start_pulse_sequence.setText(_translate("MainWindow", "Start Pulse Sequence"))
        self.stop_pulse_sequence.setText(_translate("MainWindow", "Stop Pulse Sequence"))
        self.clear_messages.setText(_translate("MainWindow", "Clear Messages"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pb_control), _translate("MainWindow", "Pulse-Blaster Control"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
