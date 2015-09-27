# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\Close.ui'
#
# Created: Sat May 16 04:00:16 2015
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

class Ui_CheckOutDialog(QtGui.QDialog):
    def setupUi(self, MainWindow):
        self.setObjectName(_fromUtf8("self"))
        self.resize(502, 406)
        self.MainWindow = MainWindow
        self.MenuItem = MainWindow.MenuItem
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(260, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 170, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(180, 170, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton.clicked.connect(self.CheckOut)
        self.pushButton_2.clicked.connect(self.Close)
        self.checkBox = QtGui.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(180, 230, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.retranslateUi(self)
        

    def CheckOut(self):
        Found = 0
        for Counter in self.MainWindow.CounterList:
            if Counter.No == int(self.lineEdit.text()) and Counter.Status == 1:
                Counter.Status = 0
                listpixmap = QtGui.QPixmap(':/Status/状态空闲.jpg')
                ListCon = QtGui.QIcon(listpixmap.scaled(QtCore.QSize(200, 200)))
                Counter.setIcon(ListCon)
                Found = 1
                Text = ''
                if self.checkBox.checkState() == QtCore.Qt.Checked:
                    Text = Text + '会员已打八折! 消费金额: ' + str(Counter.Consumption) + '*' + '0.8\n'
                    Counter.Consumption = Counter.Consumption * 0.8
                if Counter.Consumption < 25:
                    Counter.Consumption = 25
                Text = Text + '最终消费金额：' + str(Counter.Consumption)
                QtGui.QMessageBox.information(None,'提示',Text, QtGui.QMessageBox.Yes )
                Counter.MenuList = {}
                Counter.RefreshToolTip()
                self.close()
        if Found == 1:
            pass
        else:
            QtGui.QMessageBox.information(None,'提示','未找到对应的台号或状态不对', QtGui.QMessageBox.Yes )
    
    
    def Close(self):
        self.close()
        
    def retranslateUi(self, Dialog):
        self.setWindowTitle(_translate("Dialog", "结账", None))
        self.pushButton.setText(_translate("Dialog", "结账", None))
        self.pushButton_2.setText(_translate("Dialog", "取消", None))
        self.label.setText(_translate("Dialog", "台号", None))
        self.checkBox.setText(_translate("Dialog", "会员折扣", None))




