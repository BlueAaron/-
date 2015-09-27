# -*- coding: utf-8 -*-

from PyQt4.QtCore import  QThread, QFile, QFileInfo, QByteArray, QIODevice, pyqtSignal
from PyQt4.QtNetwork import QFtp
from string import Template  

class UploadThread(QThread):
    information = pyqtSignal(str)
    
    def __init__(self):
        super(UploadThread,self).__init__()
        self.ftp = QFtp(self)   
        self.ftp.stateChanged.connect(self.on_ftp_stateChanged)
        self.ftp.commandFinished.connect(self.on_ftp_commandFinished)
        self.ftp.dataTransferProgress.connect(self.on_ftp_dataTransferProgress)
        self.uploading = False    
        
    def setData(self, files, servers):
        self.files = files
        self.servers = servers
        self.servers_index = 0
        self.succeed = 0
        
    def run(self):
        num = len(self.servers)
        for self.servers_index in range(num):        
            self.files_index = 0
            self.ftp.connectToHost(self.servers[self.servers_index]["host"], int(self.servers[self.servers_index]["port"]))
            self.uploading = True
            while self.uploading:
                QThread.sleep(1)
        
        self.information.emit(u"<font color=green>所有服务器上传完成。成功：%s 失败：%s</font><br />" % (self.succeed, num - self.succeed))
    
    def terminate(self):
        self.ftp.abort()
        super(UploadThread, self).terminate()
        self.information.emit(u"<font color=red>上传任务被终止！</font><br />")
        
    def on_ftp_stateChanged(self, state):
        if self.ftp.error():
            self.information.emit(u"<font color=red>错误：%s</font>" % self.ftp.errorString())
            if self.ftp.error() == 1:
                self.ftp.close()
            else:
                self.do_ftp_close()
        
        if state == QFtp.HostLookup:
            s = Template(
            u"""创建连接：${platform}-${server_name} 主机：${host} 端口：${port}"""
            )
            self.information.emit(s.substitute(self.servers[self.servers_index]))    
        elif state == QFtp.Connecting:
            pass
        elif state == QFtp.Connected:
            self.information.emit(u"登陆账号：%s" % self.servers[self.servers_index]["account"])
            self.do_ftp_login()
        elif state == QFtp.LoggedIn:
            self.information.emit(u"进入目录：%s" % self.servers[self.servers_index]["path"])
            self.do_ftp_cd()
        elif state == QFtp.Closing:                      
            self.do_ftp_close()
        
    def on_ftp_commandFinished(self):     
        if self.ftp.error():
            self.information.emit(u"<font color=red>错误：%s</font>" % self.ftp.errorString())
            if self.ftp.error() == 1:
                self.ftp.close()
            else:
                self.do_ftp_close()
            
        if self.ftp.currentCommand() == QFtp.Login:
            pass
        elif self.ftp.currentCommand() == QFtp.Cd:            
            self.do_ftp_put()          
        elif self.ftp.currentCommand() == QFtp.Put:            
            self.information.emit(u"上传成功：%s" % self.files[self.files_index])
            
            self.files_index += 1
            if self.files_index == len(self.files):
                self.information.emit(u"上传完成")                
                self.succeed += 1
    
    def do_ftp_login(self):
        self.ftp.login(self.servers[self.servers_index]["account"], self.servers[self.servers_index]["password"])
        
    def do_ftp_cd(self):
        self.ftp.cd(self.servers[self.servers_index]["path"])
        
    def do_ftp_put(self):
        num = len(self.files)
        for i in range(num):
            file = self.files[i]
            fhandle = QFile(file)
            fhandle.open(QIODevice.ReadOnly)
            byte_array = QByteArray()
            byte_array.append(fhandle.readData(fhandle.size()))
            
            fileinfo = QFileInfo(file)
            filename = fileinfo.fileName()
            self.ftp.put(byte_array, filename)  
                   
        self.ftp.close()
        
    def on_ftp_dataTransferProgress(self, done,total):
        pass
        
    def do_ftp_close(self):
        self.ftp.abort()
        self.information.emit(u"断开连接<br />")
        self.uploading = False
