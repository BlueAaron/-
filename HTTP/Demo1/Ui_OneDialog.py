# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\Test1\OneDialog.ui'
#
# Created: Wed Jul 29 23:23:34 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Ui_OtherDialog as OtherDialog
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

class Ui_OneDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 70, 341, 211))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "弹出第二个弹窗", None))
        self.pushButton.clicked.connect(self.CreateOtherDialog)

    def CreateOtherDialog(self):
            #生成第二个窗体 注意这里我已经将 Ui_OtherDialog的类型设置为QDialog类型了
            self.OtherDialog = OtherDialog.Ui_OtherDialog()
            #调用第二个窗体的 setupUi函数 并将自己作为参数传入进去
            self.OtherDialog.setupUi(self)
            self.OtherDialog.show()
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_OneDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

