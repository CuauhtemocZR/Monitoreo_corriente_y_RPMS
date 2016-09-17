# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Puerto.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(266, 127)
        self.PC = QtGui.QLineEdit(Dialog)
        self.PC.setGeometry(QtCore.QRect(160, 30, 51, 20))
        self.PC.setObjectName(_fromUtf8("PC"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Elephant"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.Guardar = QtGui.QPushButton(Dialog)
        self.Guardar.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.Guardar.setObjectName(_fromUtf8("Guardar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Puerto", None))
        self.label.setText(_translate("Dialog", "Puerto COM", None))
        self.Guardar.setText(_translate("Dialog", "Guardar", None))

