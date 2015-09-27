from PyQt4 import QtGui
from Ui_CoffeeMainWindow import *
from Ui_LoginDialog import *

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginDialog = Ui_LoginDialog()
    LoginDialog.setupUi()
    LoginDialog.show()
    if LoginDialog.exec_() == 0 and LoginDialog.LoginSuccess == 1:
        CoffeeMainWindow = Ui_CoffeeMainWindow()
        CoffeeMainWindow.setupUi(CoffeeMainWindow)
        CoffeeMainWindow.show()
        sys.exit(app.exec_())

