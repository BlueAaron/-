# -*- coding: utf-8 -*-
#!/usr/bin/python
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import cmiMain
import CMIConfig
class MainWidget(QDialog):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__()

        cmimain=cmiMain.Ui_Dialog()
        self.cmiconfig=CMIConfig.Ui_Dialog()


        # main_layout = QVBoxLayout(self)
        # main_layout.addWidget(cmimain)
        #
        # self.setLayout(main_layout)

        tabWidget=QTabWidget(self)
        w1=QDialog()
        cmimain.setupUi(w1)
        # cmiconfig.setupUi(w2)
        tabWidget.addTab(w1,"First")
        # tabWidget.addTab(w2,"Second")
        tabWidget.resize(800,700)

        self.connect(cmimain.pushButton_5,SIGNAL("clicked()"),self.slotChild)
        # self.connect(cmiconfig.pushButton,SIGNAL("clicked()"),self,SLOT("reject()"))

    def slotChild(self):
        dlg=QDialog()
        self.cmiconfig.setupUi(dlg)
        dlg.exec_()

app=QApplication(sys.argv)
dialog=MainWidget()
dialog.show()
app.exec_()