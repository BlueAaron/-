# -*- coding: utf-8 -*-
#!/usr/bin/python
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import time
import CMIMain_111
import CMIConfig
import CMINormalInject
import CMIPublic

class MainWidget(QDialog):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__()

        #初始化数据到内存
        CMIPublic.Config().ReadCsv()

        #显示主界面
        self.cmimain=CMIMain_111.Ui_Dialog()
        self.cmimain.setupUi(self)

        #注入
        self.cminormalinject=CMINormalInject.Ui_Dialog()
        #配置
        self.cmiconfig=CMIConfig.Ui_Dialog()

        #注入
        self.connect(self.cmimain.pushButton,SIGNAL("clicked()"),self.Inject)
        #配置
        self.connect(self.cmimain.pushButton_5,SIGNAL("clicked()"),self.slotChild)

    #注入
    def Inject(self):
        dlg=QDialog()
        self.cminormalinject.setupUi(dlg,self)
        dlg.exec_()

    #配置
    def slotChild(self):
        dlg=QDialog()
        self.cmiconfig.setupUi(dlg,self)
        dlg.exec_()

    #打印日志到界面
    def printLog(self,log):
        # print time.strftime("%Y-%m-%d %H:%M:%S")
        self.cmimain.textEdit.append("[%s]" % time.strftime("%Y-%m-%d %H:%M:%S")+log)
        self.cmimain.textEdit.update()

app=QApplication(sys.argv)
dialog=MainWidget()
dialog.show()
app.exec_()