# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\SysFrame.ui'
#
# Created: Sat May 16 01:30:15 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(221, 353)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 30, 150, 61))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"方正喵呜体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 150, 61))
        self.label_2.setStyleSheet(_fromUtf8("font: 14pt \"方正喵呜体\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 170, 150, 151))
        self.frame.setStyleSheet(_fromUtf8("border-image: url(:/BroundBcak/头像.png);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", " 系统名称：好高\n级的"
"马小跳咖啡馆管理系统", None))
        self.label_2.setText(_translate("Form", "     最低消费：\n"
"你意想不到的25块", None))

import CoffeeManage_rc



