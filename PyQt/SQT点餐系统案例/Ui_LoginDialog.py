# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\LoginDialog.ui'
#
# Created: Sun May 10 02:02:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import CoffeeManage_rc
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

class Ui_LoginDialog(QtGui.QDialog):
    def keyPressEvent(self, QEvent):
        if QEvent.key() == QtCore.Qt.Key_Escape:
            Ret = QtGui.QMessageBox.information(None,'退出','欢迎使用，即将退出！', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if Ret == QtGui.QMessageBox.Yes:
                self.close()
            else:
                pass
        if QEvent.key() == QtCore.Qt.Key_Return or QEvent.key() == QtCore.Qt.Key_Enter:
            self.Login()
            
    def setupUi(self):
        self.LoginSuccess = -1
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(639, 451)
        self.setStyleSheet(_fromUtf8("QDialog{border-image: url(:/BroundBcak/登录背景图1.jpg);}"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(170, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(260, 150, 171, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 210, 171, 41))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "登录", None))
        self.label.setText(_translate("Dialog", "用户名", None))
        self.label_2.setText(_translate("Dialog", "密码", None))
        self.pushButton_2.setText(_translate("Dialog", "退出", None))
        self.pushButton.clicked.connect(self.Login)
        self.pushButton_2.clicked.connect(self.CloseApp)

    def CloseApp(self):
        QtGui.QMessageBox.information(None,'退出','欢迎使用，即将退出！', QtGui.QMessageBox.Yes )
        self.LoginSuccess = -1
        exit(-1)
        
    def Login(self):
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == '123456':
            QtGui.QMessageBox.information(None,'登入成功','欢迎登录使用！', QtGui.QMessageBox.Yes )
            self.LoginSuccess = 1
            self.close()
        else:
            QtGui.QMessageBox.warning(None,'登入失败','账号或密码错误！', QtGui.QMessageBox.Yes )
            self.LoginSuccess = -1
