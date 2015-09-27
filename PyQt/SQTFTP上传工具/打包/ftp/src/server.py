# -*- coding: utf-8 -*-

"""
Module implementing Server.
"""
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QDialog

from Ui_server import Ui_Server
from model.platform import PlatformModel
from model.server import ServerModel

class Server(QDialog, Ui_Server):
    saved = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(Server, self).__init__(parent)
        self.setupUi(self)
        
        self.server_id = None
        self.platform_model = PlatformModel()
        self.server_model = ServerModel()       
            
        self.initData()
        
    def initData(self):            
        self.platform.addItems(self.platform_model.list())
            
    @pyqtSlot()
    def on_add_platform_clicked(self):
        """
        Slot documentation goes here.
        """
        text, ok = QtGui.QInputDialog.getText(self, u"添加", u"平台名称:")
        if ok == True:
            if self.platform_model.check(text) > 0:
                QtGui.QMessageBox.critical(self, u"提示", u"平台名称已存在！")
            elif self.platform_model.add(text):
                self.platform.addItem(text) 
                self.platform.setCurrentIndex(self.platform.count()-1)
            else:
                QtGui.QMessageBox.critical(self, u"提示", u"添加平台失败")
    
    @pyqtSlot()
    def on_edit_platform_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.platform.count() == 0:
            QtGui.QMessageBox.information(self, u"提示", u"没有平台可以编辑！")
        else:
            old_text = self.platform.currentText()
            new_text, ok = QtGui.QInputDialog.getText(self, u"添加", u"平台名称:", 0, old_text)
            if ok == True:
                if self.platform_model.check(new_text) > 0:
                    QtGui.QMessageBox.critical(self, u"提示", u"平台名称已存在！")
                elif self.platform_model.update(new_text, old_text):
                    index = self.platform.currentIndex()
                    self.platform.setItemText(index, new_text)
                else:
                    QtGui.QMessageBox.critical(self, u"提示", u"修改平台失败")
            
    
    @pyqtSlot()
    def on_delete_platform_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.platform.count() == 0:
            QtGui.QMessageBox.information(self, u"提示", u"没有平台可以删除！")
            return
            
        answer = QtGui.QMessageBox.question(self, u"提示", u"确定删除当前选中平台？", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.Yes:
            text = self.platform.currentText()
            if self.server_model.countByPlatform(text) > 0:
                QtGui.QMessageBox.warning(self, u"提示", u"删除平台之前请先删除该平台下面的服务器！")
            else:
                if self.platform_model.delete(text):
                    self.platform.removeItem(self.platform.currentIndex())
                else:
                    QtGui.QMessageBox.critical(self, u"提示", u"删除平台失败")
    
    @pyqtSlot()
    def on_save_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.validator() == True:
            #platform,server_name,account,password,host,port,path
            fields = {
                      "server_id":self.server_id, 
                      "platform":self.platform.currentText(), 
                      "server_name":self.server_name.text(), 
                      "account":self.account.text(), 
                      "password":self.password.text(), 
                      "host":self.host.text(), 
                      "port":self.port.text(), 
                      "path":self.path.text()
                      }
            if self.server_id == None:          
                if self.server_model.add(fields):
                    QtGui.QMessageBox.information(self, u"提示", u"添加服务器成功！")
                    self.saved.emit()
                    self.close()
                else:
                    QtGui.QMessageBox.information(self, u"提示", u"添加服务器失败！")
            else:
                if self.server_model.update(self.server_id, fields):
                    QtGui.QMessageBox.information(self, u"提示", u"修改服务器成功！")
                    self.saved.emit()
                    self.close()
                else:
                    QtGui.QMessageBox.information(self, u"提示", u"修改服务器失败！")
        
    def validator(self):
        if len(self.server_name.text().trimmed()) < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请输入名称！")
            self.server_name.setFocus()
            return False
            
        if self.platform.count() < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请添加平台！")
            self.add_platform.clicked.emit(True)            
            return False
            
        if len(self.host.text().trimmed()) < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请输入主机！")
            self.host.setFocus()
            return False
            
        if len(self.port.text().trimmed()) < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请输入端口！")
            self.port.setFocus()
            return False
            
        if len(self.path.text().trimmed()) < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请输入路径！")
            self.path.setFocus()
            return False
            
        if len(self.account.text().trimmed()) < 1:
            QtGui.QMessageBox.information(self, "提示", "请输入账号！")
            self.account.setFocus()
            return False
        
        if len(self.password.text().trimmed()) < 1:
            QtGui.QMessageBox.information(self, u"提示", u"请输入密码！")
            self.password.setFocus()
            return False
            
        return True
        
    def setData(self, data):
        if data != False:
            if data["id"] != None:
                self.server_id = data["id"]
                self.groupBox.setTitle(u"修改")
            else:
                self.groupBox.setTitle(u"复制")
                
            index = self.platform.findText(data["platform"])
            self.platform.setCurrentIndex(index)
            self.server_name.setText(data["server_name"])
            self.account.setText(data["account"])
            self.password.setText(data["password"])
            self.host.setText(data["host"])
            self.port.setText(data["port"])
            self.path.setText(data["path"])
        
        
