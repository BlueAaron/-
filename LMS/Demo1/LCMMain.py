# -*- coding: utf-8 -*-
#!/usr/bin/python

#显示窗口图标
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import threading
import time

import title

class MainWidget(QWidget):
    closeWidget = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWidget, self).__init__()
        self.title=title.Ui_Form()
        self.closeWidget.connect(self.mytest)
        self.closeWidget.emit()
        self.title.setupUi(self)
        self.resize(980,600)
        self.setMinimumSize(900, 600)
        self.location = QRect()

        #初始化position
        self.m_DragPosition=self.pos()
        #取消窗口的标题框
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint )
        self.setMouseTracking(True)
        self.setStyleSheet("background-color:white;")

    def test(self):
        self.closeWidget.connect(self.mytest)
    def mytest(self):
        print "hehe "

    #支持窗口拖动,重写两个方法
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

app=QApplication(sys.argv)
MainWidget=MainWidget()
MainWidget.show()
sys.exit(app.exec_())
