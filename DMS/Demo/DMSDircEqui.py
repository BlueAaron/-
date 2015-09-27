#-*- coding:utf-8 -*-
'''
文件名       : DMSDircEqui.py
文件描述     : 定义DMS系统基础类库
作者         : DMS
日期         : 2015-3-19
修改日期     :
修改内容     :
'''
import copy

DMSDataDirc={} #DMS数据字典

#数据字典操作类
class DMSDircEquiClass:
    #定义数据字典初始值
    DMSDataDircMember={'online':'none','cpu':'none','mem':'none',
                       'disk':'none','platform':'none',
                       'username':'none','passwd':'none','port':'none'}
    
    #初始化数据字典
    def DMSDataDircInsert(self,IPList):
        for key in IPList:
            if key not in DMSDataDirc:
                DMSDataDirc[key]=copy.deepcopy(self.DMSDataDircMember)
                
    #更新数据字典
    def DMSDataDircUpdate(self,IP,UpObj,UpObjValue):
        if UpObj in self.DMSDataDircMember:
           DMSDataDirc[IP][UpObj]=UpObjValue
           
    #删除数据字典键
    def DMSDataDircDelete(self,IPList):
        for key in IPList:
            DMSDataDirc.pop(key) 
