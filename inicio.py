# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 0, 411, 271))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.VGraf = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.VGraf.setContentsMargins(0, -1, -1, -1)
        self.VGraf.setObjectName(_fromUtf8("VGraf"))
        self.qwtPlot_2 = Qwt5.QwtPlot(self.verticalLayoutWidget)
        self.qwtPlot_2.setObjectName(_fromUtf8("qwtPlot_2"))
        self.VGraf.addWidget(self.qwtPlot_2)
        self.lcdRPM = QtGui.QLCDNumber(self.centralwidget)
        self.lcdRPM.setGeometry(QtCore.QRect(10, 120, 64, 23))
        self.lcdRPM.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 85, 127);"))
        self.lcdRPM.setObjectName(_fromUtf8("lcdRPM"))
        self.lcdCorr = QtGui.QLCDNumber(self.centralwidget)
        self.lcdCorr.setGeometry(QtCore.QRect(30, 350, 64, 23))
        self.lcdCorr.setAcceptDrops(False)
        self.lcdCorr.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0,85, 127);"))
        self.lcdCorr.setObjectName(_fromUtf8("lcdCorr"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 272, 411, 261))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.VCor = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.VCor.setObjectName(_fromUtf8("VCor"))
        self.qwtPlot = Qwt5.QwtPlot(self.verticalLayoutWidget_2)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.VCor.addWidget(self.qwtPlot)
        self.Pcom = QtGui.QPushButton(self.centralwidget)
        self.Pcom.setGeometry(QtCore.QRect(640, 20, 75, 23))
        self.Pcom.setObjectName(_fromUtf8("Pcom"))
        self.Integra = QtGui.QPushButton(self.centralwidget)
        self.Integra.setGeometry(QtCore.QRect(640, 60, 75, 23))
        self.Integra.setObjectName(_fromUtf8("Integra"))
        self.Salir = QtGui.QPushButton(self.centralwidget)
        self.Salir.setGeometry(QtCore.QRect(640, 100, 75, 23))
        self.Salir.setObjectName(_fromUtf8("Salir"))
        self.Arrancar = QtGui.QPushButton(self.centralwidget)
        self.Arrancar.setGeometry(QtCore.QRect(200, 550, 75, 23))
        self.Arrancar.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Bauhaus 93\";"))
        self.Arrancar.setObjectName(_fromUtf8("Arrancar"))
        self.Detener = QtGui.QPushButton(self.centralwidget)
        self.Detener.setGeometry(QtCore.QRect(370, 550, 75, 23))
        self.Detener.setStyleSheet(_fromUtf8("font: 12pt \"Bauhaus 93\";\n"
"background-color: rgb(170, 0, 0);"))
        self.Detener.setObjectName(_fromUtf8("Detener"))
        self.motor = QtGui.QLabel(self.centralwidget)
        self.motor.setGeometry(QtCore.QRect(550, 170, 221, 211))
        self.motor.setObjectName(_fromUtf8("motor"))
        self.lcdVolt = QtGui.QLCDNumber(self.centralwidget)
        self.lcdVolt.setGeometry(QtCore.QRect(30, 380, 64, 23))
        self.lcdVolt.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0,85, 127);"))
        self.lcdVolt.setObjectName(_fromUtf8("lcdVolt"))
        self.lcdWatt = QtGui.QLCDNumber(self.centralwidget)
        self.lcdWatt.setGeometry(QtCore.QRect(30, 410, 64, 23))
        self.lcdWatt.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0,85, 127);"))
        self.lcdWatt.setObjectName(_fromUtf8("lcdWatt"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 350, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century751 BT"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 380, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century751 BT"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 410, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century751 BT"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century751 BT"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Interfaces Graficas", None))
        self.Pcom.setText(_translate("MainWindow", "Puerto COM", None))
        self.Integra.setText(_translate("MainWindow", "Integrantes", None))
        self.Salir.setText(_translate("MainWindow", "Salir", None))
        self.Arrancar.setText(_translate("MainWindow", "Arrancar", None))
        self.Detener.setText(_translate("MainWindow", "Detener", None))
        self.motor.setText(_translate("MainWindow", "TextLabel", None))
        self.label.setText(_translate("MainWindow", "A", None))
        self.label_2.setText(_translate("MainWindow", "V", None))
        self.label_3.setText(_translate("MainWindow", "W", None))
        self.label_4.setText(_translate("MainWindow", "RPM", None))

from PyQt4 import Qwt5
