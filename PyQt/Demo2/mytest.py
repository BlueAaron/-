# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
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
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 60, 195, 22))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(40, 110, 204, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.widget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
        self.pushButton_2.setText(_translate("Dialog", "Canel", None))

