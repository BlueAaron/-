#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from frmmain_ui import Ui_frmMain
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import Qt





class MyForm(QtGui.QMainWindow):
   def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
     
        self.ui = Ui_frmMain()

        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.startAnimation()
      
   

        self.ui.closeToolButton.clicked.connect(self.on_closeToolButton_clicked)
        self.ui.minToolButton.clicked.connect(self.on_minToolButton_clicked)
        self.ui.killToolButton.clicked.connect(self.on_killToolButton_clicked)
        self.ui.checkToolButton_2.clicked.connect(self.on_checkToolButton_2_clicked)
        self.ui.fixToolButton.clicked.connect(self.on_fixToolButton_clicked)
        self.ui.rabToolButton.clicked.connect(self.on_rabToolButton_clicked)
        self.ui.opToolButton.clicked.connect(self.on_opToolButton_clicked)
        self.ui.exToolButton.clicked.connect(self.on_exToolButton_clicked)
        self.ui.mzToolButton.clicked.connect(self.on_mzToolButton_clicked)
        self.ui.gjToolButton.clicked.connect(self.on_gjToolButton_clicked)
        
       







   def mousePressEvent(self,event):

      if ( event.button() == Qt.LeftButton ):
        
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()
        
      elif ( event.button() == Qt.MiddleButton):
         self.closeWindowAnimation()
      elif(  event.button() == Qt.RightButton ):
         self.shakeWindow()


   def mouseMoveEvent(self,event):

      if ( event.buttons() == Qt.LeftButton ):
        
         self.endPos = event.globalPos() - self.startPos
         self.move(self.endPos)



   
   
   def on_closeToolButton_clicked(self):
      self.closeWindowAnimation()

   def on_minToolButton_clicked(self):
      self.showMinimized()




   def shakeWindow(self):

      animation = QPropertyAnimation(self,"geometry")
      animation.setDuration(500)
      animation.setKeyValueAt(0,QRect(QPoint(self.frameGeometry().x()-3,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.1,QRect(QPoint(self.frameGeometry().x()+6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.2,QRect(QPoint(self.frameGeometry().x()-6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.3,QRect(QPoint(self.frameGeometry().x()+6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.4,QRect(QPoint(self.frameGeometry().x()-6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.5,QRect(QPoint(self.frameGeometry().x()+6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.6,QRect(QPoint(self.frameGeometry().x()-6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.7,QRect(QPoint(self.frameGeometry().x()+6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.8,QRect(QPoint(self.frameGeometry().x()-6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(0.9,QRect(QPoint(self.frameGeometry().x()+6,self.frameGeometry().y()),self.size()))
      animation.setKeyValueAt(1,QRect(QPoint(self.frameGeometry().x()-3,self.frameGeometry().y()),self.size()))
      animation.start()


   def setStackCurrentPage(self,index):
      widget =QWidget()
      widget = self.ui.stackedWidget.widget(index)
      self.ui.stackedWidget.setCurrentWidget(widget)
     

   def closeWindowAnimation(self):

      self.animation = QPropertyAnimation(self,"windowOpacity")
      self.animation.setDuration(1000)
      self.animation.setStartValue(1)
      self.animation.setEndValue(0)
      self.animation.start()
      #self.animation.finished.connect(self.close)
     


   def startAnimation(self):

      self.animation = QPropertyAnimation(self,"windowOpacity")
      self.animation.setDuration(1000)
      self.animation.setStartValue(0)
      self.animation.setEndValue(1)
      self.animation.start()


 


   def on_killToolButton_clicked(self):
      self.setStackCurrentPage(1)



   def on_checkToolButton_2_clicked(self):

      self.setStackCurrentPage(0)


   def on_fixToolButton_clicked(self):

      self.setStackCurrentPage(2)


   def on_rabToolButton_clicked(self):

      self.setStackCurrentPage(3)


   def on_opToolButton_clicked(self):

      self.setStackCurrentPage(4)
     
   def on_exToolButton_clicked(self):

      self.setStackCurrentPage(5)


   def on_mzToolButton_clicked(self):

     self.setStackCurrentPage(6)


   def on_gjToolButton_clicked(self):

     self.setStackCurrentPage(7)

   


   


      
      

    
      
 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
