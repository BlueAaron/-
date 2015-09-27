# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CMIConfig.ui'
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
        Dialog.resize(400, 300)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 68, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 230, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(130, 30, 241, 181))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "CMIDemo1-IP:", None))
        self.label_2.setText(_translate("Dialog", "Oracle-URL:", None))
        self.label_3.setText(_translate("Dialog", "Oracle-USR:", None))
        self.label_4.setText(_translate("Dialog", "Oracle-PWD:", None))
        self.pushButton.setText(_translate("Dialog", "保存", None))
        self.pushButton_2.setText(_translate("Dialog", "取消", None))

