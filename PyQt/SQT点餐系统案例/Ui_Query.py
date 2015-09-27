# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\Query.ui'
#
# Created: Sun May 24 22:30:50 2015
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

class Ui_QueryDialog(QtGui.QDialog):
    def setupUi(self, MainWindow):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(535, 439)
        self.MainWindow = MainWindow
        self.MenuItem=MainWindow.MenuItem
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(90, 110, 351, 211))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(240, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(160, 60, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi()
        self.pushButton.clicked.connect(self.Query)
        
    def Query(self):
        self.textEdit.clear()
        if self.lineEdit.text():
            if self.MainWindow.CounterDict[self.lineEdit.text()].Status and self.MainWindow.CounterDict[self.lineEdit.text()].MenuList:
                for Item in self.MainWindow.CounterDict[self.lineEdit.text()].MenuList:
                    self.textEdit.append(self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[Item])
                self.textEdit.append( '消费总金额:'+str(self.MainWindow.CounterDict[self.lineEdit.text()].Consumption) )
            else:
                QtGui.QMessageBox.information(None,'提示','对应台号未开台或未点餐饮', QtGui.QMessageBox.Yes )
        else:
            QtGui.QMessageBox.information(None,'提示','台号未输入', QtGui.QMessageBox.Yes )
        
    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "查询", None))
        self.pushButton.setText(_translate("Dialog", "查看", None))
        self.label.setText(_translate("Dialog", "台号", None))



