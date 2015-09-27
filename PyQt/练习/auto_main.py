from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import auto_speak

class Test(QWidget,auto_speak.Ui_Form):
    def __init__(self,parent=None):
        super(Test,self).__init__(parent)
        self.setupUi(self)

app=QApplication(sys.argv)
dialog=Test()
dialog.show()
app.exec_()