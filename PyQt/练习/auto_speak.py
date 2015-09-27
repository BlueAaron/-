# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto_speak.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(608, 369)
        Form.setStyleSheet(_fromUtf8(""))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 611, 381))
        self.frame_2.setMouseTracking(True)
        self.frame_2.setStyleSheet(_fromUtf8("* {\n"
"background-image: url(:/background/background.jpg);\n"
"font: 9pt \"苏新诗卵石体\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton::hover{\n"
"border:0px;\n"
"}  \n"
"QToolButton {\n"
"background:transparent;\n"
"}"))
        self.frame_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 180, 421, 91))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background:transparent;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.toolButton_5 = QtGui.QToolButton(self.frame_2)
        self.toolButton_5.setGeometry(QtCore.QRect(270, 290, 81, 31))
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.toolButton_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolButton_5.setStyleSheet(_fromUtf8("border:0px;\n"
"background:transparent;\n"
"font: 75 25pt \"经典细空艺\";\n"
"color: rgb(255, 255, 255);"))
        self.toolButton_5.setIconSize(QtCore.QSize(60, 60))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(25, 100, 50, 30))
        self.label.setMinimumSize(QtCore.QSize(50, 30))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: italic 9pt \"苏新诗卵石体\";\n"
"background:transparent;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 100, 120, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(120, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(25, 140, 50, 30))
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: italic 9pt \"苏新诗卵石体\";\n"
"background:transparent;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(90, 140, 120, 30))
        self.spinBox.setMinimumSize(QtCore.QSize(120, 30))
        self.spinBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.spinBox.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.toolButton_2 = QtGui.QToolButton(self.frame_2)
        self.toolButton_2.setGeometry(QtCore.QRect(145, 23, 100, 75))
        self.toolButton_2.setMinimumSize(QtCore.QSize(100, 60))
        self.toolButton_2.setStyleSheet(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/tool_receive/longtaizi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(60, 50))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton = QtGui.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(25, 23, 100, 75))
        self.toolButton.setMinimumSize(QtCore.QSize(100, 60))
        self.toolButton.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/tool_speak/humeiyao.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(60, 50))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_3 = QtGui.QToolButton(self.frame_2)
        self.toolButton_3.setGeometry(QtCore.QRect(265, 23, 100, 75))
        self.toolButton_3.setMinimumSize(QtCore.QSize(100, 60))
        self.toolButton_3.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/tool_anlei/xuancaie.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(60, 50))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_4 = QtGui.QToolButton(self.frame_2)
        self.toolButton_4.setGeometry(QtCore.QRect(385, 23, 100, 75))
        self.toolButton_4.setMinimumSize(QtCore.QSize(100, 60))
        self.toolButton_4.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/tool_about/datang.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(60, 50))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'苏新诗卵石体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">请在这里输入喊话内容。。。</span></p></body></html>", None))
        self.toolButton_5.setText(_translate("Form", "开始", None))
        self.label.setText(_translate("Form", "频道", None))
        self.comboBox.setItemText(0, _translate("Form", "世界", None))
        self.comboBox.setItemText(1, _translate("Form", "门派", None))
        self.comboBox.setItemText(2, _translate("Form", "当前", None))
        self.comboBox.setItemText(3, _translate("Form", "队伍", None))
        self.label_2.setText(_translate("Form", "间隔", None))
        self.toolButton_2.setText(_translate("Form", "收货", None))
        self.toolButton.setText(_translate("Form", "喊话", None))
        self.toolButton_3.setText(_translate("Form", "暗雷", None))
        self.toolButton_4.setText(_translate("Form", "关于", None))

import auto_qrc_rc
