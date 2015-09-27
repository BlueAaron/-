from PyQt4 import uic
def slotChild(self):
    dlg=uic.loadUi("mytest.ui")
    dlg.exec_()
