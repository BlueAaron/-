# -*- coding: utf-8 -*-
import csv
cmiconfig={'cmiip':'127.0.0.1','oracleurl':'','oracleuser':'','oraclepwd':''}
class Config:
    def ReadCsv(self):
        for line in open("CMIConfig/config.csv"):
            cmiip, oracleurl, oracleuser,oraclepwd = line.split(",")
            cmiconfig['cmiip']=cmiip
            cmiconfig['oracleurl']=oracleurl
            cmiconfig['oracleuser']=oracleuser
            oraclepwd = oraclepwd.replace('\n','')
            cmiconfig['oraclepwd']=oraclepwd

