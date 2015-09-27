# -*- coding: utf-8 -*-

from PyQt4.QtSql import *
from model.server import ServerModel
from PyQt4.QtCore import QStringList

class SolutionModel():
        
    def load(self, name):
        sql = "SELECT * FROM solution WHERE name='%s'" % name
        q = QSqlQueryModel()
        q.setQuery(sql)
        if(q.rowCount()):
            server_model = ServerModel()
            return server_model.findByIds(q.record(0).value("servers").toString())
        else:
            return []
        
    def add(self, name, servers):
        q = QSqlQuery()
        return q.exec_("INSERT INTO solution(name,servers)VALUES('%s','%s')" % (name, servers))
        
    def delete(self, name):
        q = QSqlQuery()
        return q.exec_("DELETE FROM solution WHERE name='%s'" % name)
        
    def check(self, name):
        q = QSqlQueryModel()
        q.setQuery("SELECT COUNT(1) FROM solution WHERE name='%s'" % name)
        return q.record(0).value(0).toInt()[0]
        
    def list(self):
        q = QSqlQueryModel()
        q.setQuery("SELECT name FROM solution")
        strlist = QStringList()
        strlist.append(u"请选择")
        for i in range(q.rowCount()):
            strlist.append(q.record(i).value(0).toString())
        return strlist
