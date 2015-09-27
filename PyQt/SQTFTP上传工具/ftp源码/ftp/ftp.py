# -*- coding: utf-8 -*-

import sys
import atexit
from PyQt4 import QtGui
from PyQt4.QtSql import QSqlDatabase
from main import MainWindow


@atexit.register
def appExit():
    pass

def createConnection(): 
    db=QSqlDatabase.addDatabase("QSQLITE") 
    db.setDatabaseName("sqlite.db3") 
    return db.open()

createConnection()

app = QtGui.QApplication(sys.argv)
app.addLibraryPath("qt4_plugins")
main_window = MainWindow()
main_window.showMaximized()
main_window.show()
sys.exit(app.exec_())
