# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmiMain.ui'
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
        Dialog.resize(763, 572)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 20, 671, 61))
        self.layoutWidget.setMinimumSize(QtCore.QSize(0, 55))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 55))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 55))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 55))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 55))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 55))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 55))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 100, 671, 401))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "注入", None))
        self.pushButton_2.setText(_translate("Dialog", "查询", None))
        self.pushButton_3.setText(_translate("Dialog", "删除", None))
        self.pushButton_4.setText(_translate("Dialog", "策略", None))
        self.pushButton_5.setText(_translate("Dialog", "配置", None))
        self.pushButton_6.setText(_translate("Dialog", "关于", None))

