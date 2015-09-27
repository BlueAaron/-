# -*- coding: utf-8 -*-
#!/usr/bin/python

#显示窗口图标
import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('SQT点餐系统案例')
        self.setWindowIcon(QtGui.QIcon('../images/32.png'))

app=QtGui.QApplication(sys.argv)
icon=Icon()
icon.show()
sys.exit(app.exec_())