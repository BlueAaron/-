# -*- coding: utf-8 -*-

import os, time
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTableWidget, QTableWidgetItem
import func

class FileList(QTableWidget):
    def __init__(self,  parent):
        super(FileList,self).__init__(parent)
        self.setAcceptDrops(True)
        
        self.createContextMenu()
        self.itemSelectionChanged.connect(self.on_itemSelectionChanged)
     
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        pass
        #super().dragMoveEvent(event)
        
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file = url.toLocalFile()
                self._addItem(file)                 
            event.acceptProposedAction()
        else:
            super().dropEvent(event)  
     
    def _addItem(self, file):
        if(os.path.isfile(file)):                         
            row = self.rowCount()
            file_size = os.path.getsize(file)
            mtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(file).st_mtime))
            
            self.insertRow(row)
            self.setItem(row, 0, QTableWidgetItem(file))     
            self.setItem(row, 1, QTableWidgetItem(func.sizeof_fmt(file_size)))
            self.setItem(row, 2, QTableWidgetItem(mtime)) 
        
    def createContextMenu(self):  
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        QtCore.QObject.connect(self, QtCore.SIGNAL("customContextMenuRequested(const QPoint&)"), self.showContextMenu)
 
        self.contextMenu = QtGui.QMenu(self)  
        self.menu_add = self.contextMenu.addAction(QtGui.QIcon("icon/0949090.png"),u"添加文件")  
        self.menu_remove = self.contextMenu.addAction(QtGui.QIcon("icon/0949091.png"),u"移除文件")  
        self.menu_remove.setEnabled(False)

        self.menu_add.triggered.connect(self.onMenuAddClicked)  
        self.menu_remove.triggered.connect(self.onMenuRemoveClicked)   
  
  
    def showContextMenu(self, point):  
        # show context menu
        point.setY(point.y() + 25)
        if self.rowCount():
            point.setX(point.x() + 15)
            
        self.contextMenu.exec_(self.mapToGlobal(point))    
    
    def onMenuAddClicked(self):  
        files = QtGui.QFileDialog.getOpenFileNames(self, u"选择文件")
        for file in files:
            self._addItem(file)
        
    def onMenuRemoveClicked(self):
        self._removeSelected()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self._removeSelected()
        elif event.key() == Qt.Key_Escape:
            self.clearSelection()
    
    def _removeSelected(self):
        rows = list(set([index.row() for index in self.selectedIndexes()]))
        for i in range(len(rows)):
            self.removeRow(rows[i]-i)
     
    def on_itemSelectionChanged(self):
        rows = self.selectedIndexes()
        if(rows):
            self.menu_remove.setEnabled(True)
        else:
            self.menu_remove.setEnabled(False)
            
        
