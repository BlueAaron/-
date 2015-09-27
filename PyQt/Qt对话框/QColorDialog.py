# -*- coding: utf-8 -*-
#!/usr/bin/python
#QColorDialog对话框
import sys
from PyQt4 import QtGui, QtCore
class ColorDialog(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        color = QtGui.QColor(0, 0, 0)
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('ColorDialog')
        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.setFocus()
        self.widget = QtGui.QWidget(self)
        self.widget.setStyleSheet('QWidget {background-color: %SQT正则校验工具案例}' %color.name())
        self.widget.setGeometry(130, 22, 100, 100)
    def showDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.widget.setStyleSheet('QWidget {background-color: %SQT正则校验工具案例}' %col.name())
app = QtGui.QApplication(sys.argv)
qb = ColorDialog()
qb.show()
sys.exit(app.exec_())