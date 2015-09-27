# -*- coding: utf-8 -*-
#!/usr/bin/python
# this is the first test for pyqt4
import sys
from PyQt4 import QtGui
#创建APP对象
app=QtGui.QApplication(sys.argv)
#QWidget 部件是PyQt4 中所有用户界面类的父类
widget=QtGui.QWidget()
#resize()方法可以改变窗口部件的大小
widget.resize(250,150)
#设置窗口部件的标题
widget.setWindowTitle("Aaron")
#显示窗口
widget.show()
#循环监听事件，使用sys.exit()方法退出可以确保程序可以完整的结束，这种情况下系统的环境变量会记录程序是如何退出的
sys.exit(app.exec_())
