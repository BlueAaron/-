# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\Test1\OtherDialog.ui'
#
# Created: Wed Jul 29 23:23:34 2015
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

#第二个窗体 注意这里 Ui_OtherDialog的类型不是普通的object而是QDialog
class Ui_OtherDialog(QtGui.QDialog):
    def setupUi(self, OneDialog):
        self.setObjectName(_fromUtf8("OtherDialog"))
        self.resize(400, 300)
        self.plainTextEdit = QtGui.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 60, 301, 211))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 191, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        #将第一个窗体的对象赋值给一个自己的变量 self. 就是指的属于自己的东西
        self.OneDialog = OneDialog
        self.retranslateUi()
        

    def retranslateUi(self):
        self.setWindowTitle(_translate("OtherDialog", "OtherDialog", None))
        self.pushButton.setText(_translate("OtherDialog", "向第一个弹窗输出内容", None))
        self.pushButton.clicked.connect(self.PushText)
        
    def PushText(self):
        self.OneDialog.plainTextEdit.appendPlainText(self.plainTextEdit.toPlainText())


