# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\Open.ui'
#
# Created: Sat May 16 02:16:11 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Ui_CoffeeMainWindow import *
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

class Ui_OpenDialog(QtGui.QDialog):
    def setupUi(self,MainWindow):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(529, 412)
        self.MainWindow = MainWindow
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(260, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(210, 150, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 150, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.show()
        
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.Open)
        self.pushButton_2.clicked.connect(self.Close)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def Open(self):
        Found = 0
        for Counter in self.MainWindow.CounterList:
            if Counter.No == int(self.lineEdit.text()) and Counter.Status == 0:
                Counter.Status = 1
                listpixmap = QtGui.QPixmap(':/Status/状态忙碌.jpg')
                ListCon = QtGui.QIcon(listpixmap.scaled(QtCore.QSize(200, 200)))
                Counter.setIcon(ListCon)
                Counter.Consumption = 25
                Found = 1
                Counter.RefreshToolTip()
                self.close()
        if Found == 1:
            pass
        else:
            QtGui.QMessageBox.information(None,'提示','未找到对应的台号或状态不对', QtGui.QMessageBox.Yes )
            
    def Close(self):
        self.close()
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "开台", None))
        self.pushButton_2.setText(_translate("Dialog", "退出", None))
        self.label.setText(_translate("Dialog", "台号", None))

