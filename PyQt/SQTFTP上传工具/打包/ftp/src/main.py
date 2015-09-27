# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, Qt, QPoint, QTime
from PyQt4.QtGui import QMainWindow, QTableWidgetItem

from Ui_main import Ui_MainWindow
from server import Server
from model.platform import PlatformModel
from model.server import ServerModel
from model.solution import SolutionModel

from uploadthread import UploadThread

class MainWindow(QMainWindow, Ui_MainWindow):
    
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.server_model = ServerModel()
        self.platform_model = PlatformModel()
        self.solution_model = SolutionModel()
        
        self.upload_thread = UploadThread()
        self.upload_thread.finished.connect(self.on_upload_thread_finished)
        self.upload_thread.information.connect(self.on_upload_thread_information)
        
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)      
        self.initUi()
        self.initData()
        self.createContextMenu()
        
        
    def initUi(self):        
        self.file_list.setColumnWidth(0, 400)
        self.file_list.setColumnWidth(2, 150)
        
        self.selected_servers.setColumnWidth(2, 80)
        self.server_list.setColumnWidth(2, 80)
        
        self.server_list.hideColumn(0)        
        self.selected_servers.hideColumn(0)
        
        self.server_list.keyPressEvent = self.on_server_list_keyPressEvent
        self.selected_servers.keyPressEvent = self.on_selected_servers_keyPressEvent
        
        self.statusBar.showMessage(u"状态")
        
    def initData(self):
        self.platform.addItems(self.platform_model.list())        
        self.upload_solution.addItems(self.solution_model.list())   
                
    def createContextMenu(self):        
        self.server_list_contextmenu = QtGui.QMenu(self)  
        self.server_list_contextmenu.addAction(self.action_move2left) 
        self.server_list_contextmenu.addSeparator()
        self.server_list_contextmenu.addAction(self.action_add_server)  
        self.server_list_contextmenu.addAction(self.action_edit_server)  
        self.server_list_contextmenu.addAction(self.action_copy_server)  
        self.server_list_contextmenu.addSeparator()
        self.server_list_contextmenu.addAction(self.action_delete_server)  
       
    @pyqtSlot(QPoint)
    def on_server_list_customContextMenuRequested(self, point):
        """
        Slot documentation goes here.
        """
        point.setY(point.y() + 25)
        if self.server_list.rowCount():
            point.setX(point.x() + 15)
        self.server_list_contextmenu.exec_(self.server_list.mapToGlobal(point))    
        
    @pyqtSlot()
    def on_start_upload_clicked(self):
        """
        Slot documentation goes here.
        """               
        if self.file_list.rowCount() < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请先添加要上传的文件！")
            return
            
        if self.selected_servers.rowCount() < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请先添加服务器到上传列表中！")
            return
            
        answer = QtGui.QMessageBox.warning(self, u"提示", u"上传将覆盖服务器设置路径下的同名文件，确定上传吗？", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.No:
            return
            
        if self.upload_thread.isRunning() == False:
            files = [self.file_list.item(i, 0).text() for i in range(self.file_list.rowCount())]
            server_ids = [str(self.selected_servers.item(i, 0).text()) for i in range(self.selected_servers.rowCount())]
            servers = self.server_model.findByIds(",".join(server_ids))
            self.upload_thread.setData(files, servers)            
            self.upload_thread.start();
            
            self.stop_upload.setEnabled(True)
            self.start_upload.setEnabled(False)
              
    @pyqtSlot()
    def on_stop_upload_clicked(self):
        """
        Slot documentation goes here.
        """
                    
        if self.upload_thread.isRunning() == True:
            answer = QtGui.QMessageBox.warning(self, u"提示", u"确定终止当前上传任务？", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if answer == QtGui.QMessageBox.No:
                return
        
            self.start_upload.setEnabled(True)
            self.stop_upload.setEnabled(False)
            self.upload_thread.terminate();
    
    def on_upload_thread_finished(self):
        self.start_upload.setEnabled(True)
        self.stop_upload.setEnabled(False)
    
    @pyqtSlot(str)
    def on_upload_thread_information(self, info):
        time = QTime(QTime.currentTime())
        self.textBrowser.append(u"[%s] %s" % (time.toString(), info))
    
    @pyqtSlot(str)
    def on_upload_solution_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        if self.upload_solution.currentIndex() >  0:
            self.setSelectedServersData(self.solution_model.load(p0))
            self.remove_solution.setEnabled(True)
            self.refresh_server_list.clicked.emit(True)
        else:
            self.setSelectedServersData([])
            self.remove_solution.setEnabled(False)
        
    @pyqtSlot(str)
    def on_platform_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        self.setServerListData(self.server_model.findByPlatform(p0))
    
    @pyqtSlot()
    def on_move2left_clicked(self):
        """
        Slot documentation goes here.
        """        
        rows = list(set([index.row() for index in self.server_list.selectedIndexes()]))
        for i in range(len(rows)):
            row = rows[i]-i
            index = self.selected_servers.rowCount()
            self.selected_servers.insertRow(index)
            self.selected_servers.setItem(index, 0, self.server_list.item(row, 0).clone())
            self.selected_servers.setItem(index, 1, self.server_list.item(row, 1).clone())
            self.selected_servers.setItem(index, 2, self.server_list.item(row, 2).clone())
            self.selected_servers.setItem(index, 3, self.server_list.item(row, 3).clone())
            self.server_list.removeRow(row)
    
    @pyqtSlot()
    def on_move2right_clicked(self):
        """
        Slot documentation goes here.
        """
        rows = list(set([index.row() for index in self.selected_servers.selectedIndexes()]))
        for i in range(len(rows)):
            row = rows[i]-i
            self.selected_servers.removeRow(row)
        self.refresh_server_list.clicked.emit(True)
             
    @pyqtSlot()
    def on_menu_about_triggered(self):
        """
        Slot documentation goes here.
        """
        QtGui.QMessageBox.about(self, u"FTP Client", u"Powered by ZLH！")
    
    @pyqtSlot()
    def on_menu_clear_log_triggered(self):
        self.textBrowser.clear()
        
    @pyqtSlot()
    def on_add_solution_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.selected_servers.rowCount() < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请先添加服务器到上传列表中！")
            return
        
        text, ok = QtGui.QInputDialog.getText(self, u"添加", u"上传方案名称:")
        if ok == True:
            if self.solution_model.check(text) > 0:
                QtGui.QMessageBox.critical(self, u"提示", u"上传方案名称已存在！")
                return
            servers = [str(self.selected_servers.item(i, 0).text()) for i in range(self.selected_servers.rowCount())]
            if self.solution_model.add(text, ",".join(servers)):
                self.upload_solution.addItem(text)
                self.upload_solution.setCurrentIndex(self.upload_solution.count()-1)
                QtGui.QMessageBox.information(self, u"提示", u"操作成功！")
            else:
                QtGui.QMessageBox.critical(self, u"提示", u"操作失败！")
    
    @pyqtSlot()
    def on_remove_solution_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.upload_solution.currentIndex() ==  0:
            QtGui.QMessageBox.information(self, u"FTP Client", u"请选择要删除的上传方案！")
            return
            
        answer = QtGui.QMessageBox.question(self, u"提示", u"确定删除当前选中上传方案？", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.Yes:
            name = self.upload_solution.currentText()
            if self.solution_model.delete(name):
                self.upload_solution.removeItem(self.upload_solution.currentIndex())
                self.selected_servers.setRowCount(0)
                self.refresh_server_list.clicked.emit(True)
                QtGui.QMessageBox.information(self, u"提示", u"操作成功！")
        
    @pyqtSlot()
    def on_refresh_server_list_clicked(self):
        """
        Slot documentation goes here.
        """
        platform = self.platform.currentText()
        self.setServerListData(self.server_model.findByPlatform(platform))
         
    @pyqtSlot()
    def on_server_list_itemSelectionChanged(self):
        rows = self.server_list.selectedIndexes()
        if(rows):
            self.move2left.setEnabled(True)
            self.action_move2left.setEnabled(True)
            self.action_edit_server.setEnabled(True)
            self.action_copy_server.setEnabled(True)
            self.action_delete_server.setEnabled(True)
        else:
            self.move2left.setEnabled(False)
            self.action_move2left.setEnabled(False)
            self.action_edit_server.setEnabled(False)
            self.action_copy_server.setEnabled(False)
            self.action_delete_server.setEnabled(False)
   
    @pyqtSlot()
    def on_selected_servers_itemSelectionChanged(self):
        rows = self.selected_servers.selectedIndexes()
        if rows:
            self.move2right.setEnabled(True)
        else:
            self.move2right.setEnabled(False)
        
    def on_server_list_keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.server_list.clearSelection()
        elif event.key() == Qt.Key_Left:
            self.move2left.clicked.emit(True)
            
    def on_selected_servers_keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.selected_servers.clearSelection()
        elif event.key() == Qt.Key_Delete or event.key() == Qt.Key_Right:
            self.move2right.clicked.emit(True)        
            
    @pyqtSlot()
    def on_action_add_server_triggered(self):
        """
        Slot documentation goes here.
        """
        self.server = Server()
        self.server.saved.connect(self.on_server_saved)
        self.server.show()
    
    @pyqtSlot()
    def on_action_edit_server_triggered(self):
        """
        Slot documentation goes here.
        """
        server_id = self.server_list.item(self.server_list.currentRow(), 0).text()     
        
        self.server = Server()   
        self.server.saved.connect(self.on_server_saved)
        self.server.setData(self.server_model.item(server_id))     
        self.server.show() 
    
    @pyqtSlot()
    def on_action_copy_server_triggered(self):
        """
        Slot documentation goes here.
        """
        server_id = self.server_list.item(self.server_list.currentRow(), 0).text()  
        server_data = self.server_model.item(server_id)      
        server_data["id"] = None
        
        self.server = Server()   
        self.server.saved.connect(self.on_server_saved)
        self.server.setData(server_data)     
        self.server.show() 
    
    @pyqtSlot()
    def on_action_delete_server_triggered(self):
        """
        Slot documentation goes here.
        """
        index = self.server_list.currentRow()
        platform = self.server_list.item(index, 1).text()
        server = self.server_list.item(index, 2).text()
        answer = QtGui.QMessageBox.question(self, u"提示", u"确定删除 %s %s？" % (platform, server), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.Yes:            
            server_id = self.server_list.item(index, 0).text()      
            if self.server_model.delete(server_id):
                self.server_list.removeRow(index)
                QtGui.QMessageBox.information(self, u"提示", u"操作成功！")                
            else:
                QtGui.QMessageBox.critical(self, u"提示", u"操作失败！")
      
    def on_server_saved(self):
        self.refresh_server_list.clicked.emit(True)
        
    @pyqtSlot()
    def on_action_move2left_triggered(self):
        self.move2left.clicked.emit(True)
        
    def setServerListData(self, data):
        self.server_list.setRowCount(0)
        for row in data:
            if self.inSelectedServers(row["id"]) == False:
                index = self.server_list.rowCount()
                self.server_list.insertRow(index)
                self.server_list.setItem(index, 0, QTableWidgetItem(row["id"]))
                self.server_list.setItem(index, 1, QTableWidgetItem(row["platform"]))
                self.server_list.setItem(index, 2, QTableWidgetItem(row["server_name"]))
                self.server_list.setItem(index, 3, QTableWidgetItem(row["path"]))
            
    def setSelectedServersData(self, data):    
        self.selected_servers.setRowCount(0)
        for row in data:
            index = self.selected_servers.rowCount()
            self.selected_servers.insertRow(index)
            self.selected_servers.setItem(index, 0, QTableWidgetItem(row["id"]))
            self.selected_servers.setItem(index, 1, QTableWidgetItem(row["platform"]))
            self.selected_servers.setItem(index, 2, QTableWidgetItem(row["server_name"]))
            self.selected_servers.setItem(index, 3, QTableWidgetItem(row["path"]))
             
        self.refresh_server_list.clicked.emit(True)
                
    def inSelectedServers(self, server_id):
        for i in range(self.selected_servers.rowCount()):
            if self.selected_servers.item(i, 0).text() == server_id:
                return True
        return False
    
            
