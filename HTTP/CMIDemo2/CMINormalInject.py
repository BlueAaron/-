# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CMINormalInject.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import CMIPost

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
    def setupUi(self, Dialog,Main):
        self.Dialog=Dialog
        #主界面对象
        self.Main=Main
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 54, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 54, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(140, 180, 91, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 180, 71, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(40, 60, 89, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 60, 89, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(280, 60, 89, 16))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 29, 291, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(90, 100, 91, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(2147483647)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(90, 140, 91, 22))
        self.spinBox_2.setMinimum(-1)
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(90, 220, 91, 22))
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(86400)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 260, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 260, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.startInject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "URL", None))
        self.label_2.setText(_translate("Dialog", "SPID", None))
        self.label_3.setText(_translate("Dialog", "AreaID", None))
        self.label_4.setText(_translate("Dialog", "TimeOut", None))
        self.checkBox.setText(_translate("Dialog", "CheckResult", None))
        self.checkBox_2.setText(_translate("Dialog", "Sign", None))
        self.radioButton.setText(_translate("Dialog", "Normal", None))
        self.radioButton_2.setText(_translate("Dialog", "Directory", None))
        self.radioButton_3.setText(_translate("Dialog", "Filelist", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))

    def startInject(self):
        self.Main.printLog(u'提交请求')

        url=self.lineEdit.text()

        if self.radioButton.isChecked():
            # type='Normal'
            type=172
        if self.radioButton_2.isChecked():
            # type='Directory'
            type=172
        if self.radioButton_3.isChecked():
            # type='Filelist'
            type=178

        areaid=self.spinBox_2.text()

        if self.checkBox_2.isChecked():
            # sign='sign'
            spid=self.spinBox.text()
        else:
            # sign='no sign'
            spid=2000000000

        if self.checkBox.isChecked():
            # checkresult='check result'
            checkresult=True
        else:
            # checkresult='no check'
            checkresult=False

        timeout=self.spinBox_3.text()

        #print url,type,spid,areaid,sign,checkresult,timeout

        post=CMIPost.CMIPost(url,type,spid,areaid,checkresult,timeout,self.Main)
        post.sedpost()
        self.Dialog.close()

