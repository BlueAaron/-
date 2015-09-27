# -*- coding: utf-8 -*-
#!/usr/bin/python
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import CMIMain
import CMIConfig
import CMINormalInject
import CMIPublic

class MainWidget(QDialog):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__()

        #初始化数据到内存
        CMIPublic.Config().ReadCsv()
        print CMIPublic.cmiconfig

        #显示主界面
        self.cmimain=CMIMain.Ui_Dialog()
        self.cmimain.setupUi(self)

        #注入
        self.cminormalinject=CMINormalInject.Ui_Dialog()
        #配置
        self.cmiconfig=CMIConfig.Ui_Dialog()

        #注入
        self.connect(self.cmimain.pushButton,SIGNAL("clicked()"),self.Inject)
        #配置
        self.connect(self.cmimain.pushButton_5,SIGNAL("clicked()"),self.slotChild)

        self.printLog("test")
        self.printLog("test")
        self.printLog("test")

    #注入
    def Inject(self):
        dlg=QDialog()
        self.cminormalinject.setupUi(dlg,self)
        dlg.exec_()

    #配置
    def slotChild(self):
        dlg=QDialog()
        self.cmiconfig.setupUi(dlg)
        dlg.exec_()

    def printLog(self,log):
        self.cmimain.plainTextEdit.appendPlainText(log)


app=QApplication(sys.argv)
dialog=MainWidget()
dialog.show()
app.exec_()