# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'title.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import threading
import time

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

class Ui_Form(QtGui.QWidget):

    emit_python_list = QtCore.pyqtSignal(int)
    def __init__(self):

        super(Ui_Form, self).__init__()

    def setupUi(self, Form):
        self.processorThread=timer(self)
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(685, 199)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 48, 48))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setWhatsThis(_fromUtf8(""))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border:none\n"
""))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test)
        self.emit_python_list.connect(self.change)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def pp(self,flag):
        if flag%2==0:
            flag+=1
            print "ok"
        else:
            flag+=1
            print "ko"

    def test(self):
        thread = timer(self)
        thread.start()
        thread.stop()

    def change(self,flag):
        print "change",flag
        if flag%2==0:
            self.pushButton.setIcon(QtGui.QIcon("images/start2.png"))
        else:
            self.pushButton.setIcon(QtGui.QIcon("images/start.png"))

    def run(self,name):
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self, QtCore.SIGNAL("change()"))

class timer(threading.Thread):
    flag=1
    progressUpdated=QtCore.pyqtSignal(int)
    def __init__(self,title):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.title=title

    def run(self):
        # while not self.thread_stop:
        while self.flag<100:
        # while True:
            print self.flag
            if self.flag%2==0:
                self.title.pp(self.flag)

                self.title.emit_python_list.emit(self.flag)
                time.sleep(0.1)
                self.flag+=1
            else:
                self.title.pp(self.flag)
                self.title.emit_python_list.emit(self.flag)
                time.sleep(0.1)
                self.flag+=1
    def stop(self):
        self.thread_stop = True


