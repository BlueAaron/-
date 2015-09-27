# -*- coding: utf-8 -*-

from PyQt4.QtSql import *
from string import Template  

class ServerModel():
        
    def countByPlatform(self, platform):
        q = QSqlQueryModel()
        q.setQuery("SELECT COUNT(1) FROM server WHERE platform='%s'" % platform)
        return q.record(0).value(0).toInt()[0]
    
    def findByPlatform(self, platform):
        if platform == u"全部":
            sql = "SELECT * FROM server"
        else:
            sql = "SELECT * FROM server WHERE platform='%s'" % platform
        q = QSqlQueryModel()
        q.setQuery(sql)
        result = []
        for i in range(q.rowCount()):
            record = q.record(i)
            row = {
                   "id":record.value("id").toString(), 
                   "platform":record.value("platform").toString(), 
                   "server_name":record.value("server_name").toString(), 
                   "path":record.value("path").toString()
                   }
            result.append(row)
        return result
        
    def findByIds(self, servers):
        sql = "SELECT * FROM server WHERE id IN(%s)" % servers
        q = QSqlQueryModel()
        q.setQuery(sql)
        result = []
        
        for i in range(q.rowCount()):
            record = q.record(i)
            row = {
                   "id":record.value("id").toString(), 
                   "platform":record.value("platform").toString(), 
                   "server_name":record.value("server_name").toString(), 
                   "path":record.value("path").toString(), 
                   "host":record.value("host").toString(), 
                   "port":record.value("port").toString(), 
                   "account":record.value("account").toString(), 
                   "password":record.value("password").toString()
                   }
            result.append(row)
        return result
        
    def item(self, server_id):
        q = QSqlQueryModel()
        q.setQuery("SELECT * FROM server WHERE id='%s'" % server_id)
        
        if q.rowCount():
            record = q.record(0)
            row = {
                   "id":record.value("id").toString(), 
                   "platform":record.value("platform").toString(), 
                   "server_name":record.value("server_name").toString(), 
                   "account":record.value("account").toString(), 
                   "password":record.value("password").toString(), 
                   "host":record.value("host").toString(), 
                   "port":record.value("port").toString(), 
                   "path":record.value("path").toString(),
                   "path":record.value("path").toString(),
                   }
            return row
        else:
            return False
        
    def add(self, fields):
        s = Template(
        u"""
        INSERT INTO server(platform,server_name,account,password,host,port,path)
        VALUES('${platform}','${server_name}','${account}','${password}','${host}','${port}','${path}')
        """
        )
        sql = s.substitute(fields)
        q = QSqlQuery()
        return q.exec_(sql)
    
    def update(self, server_id, fields):
        s = Template(
        u"""
        UPDATE 
            server 
        SET 
            platform='${platform}',
            server_name='${server_name}',
            account='${account}',
            password='${password}',
            host='${host}',
            port='${port}',
            path='${path}'
        WHERE
            id=${server_id}
        """
        )
        sql = s.substitute(fields)
        q = QSqlQuery()
        return q.exec_(sql)
        
    def delete(self, server_id):
        q = QSqlQuery()
        return q.exec_("DELETE FROM server WHERE id='%s'" % server_id)
