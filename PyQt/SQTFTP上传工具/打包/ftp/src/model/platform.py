# -*- coding: utf-8 -*-

from PyQt4.QtSql import *
from PyQt4.QtCore import QStringList

class PlatformModel():       
        
    def add(self, name):
        q = QSqlQuery()
        return q.exec_("INSERT INTO platform(name)VALUES('%s')" % name)
    
    def update(self, new_name, old_name):
        q = QSqlQuery()
        return q.exec_("UPDATE platform SET name='%s' WHERE name='%s'" % (new_name, old_name))
        
    def delete(self, name):
        q = QSqlQuery()
        return q.exec_("DELETE FROM platform WHERE name='%s'" % name)
    
    def check(self, name):
        q = QSqlQueryModel()
        q.setQuery("SELECT COUNT(1) FROM platform WHERE name='%s'" % name)
        return q.record(0).value(0).toInt()[0]
        
    def list(self):
        q = QSqlQueryModel()
        q.setQuery("SELECT name FROM platform")
        strlist = QStringList()
        strlist.append(u"全部")
        for i in range(q.rowCount()):
            strlist.append(q.record(i).value(0).toString())
        return strlist
    
