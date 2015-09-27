#-*- coding:utf-8 -*-
import DMSDircEqui
import threading  
import os

'''
函数名       : DMSCheckStatusEqui
功能描述     : 设置单个设备的在线状态
输入参数     : IP(参数合法性由调用者保证)
返回值       : 1 在线，0 不在线
调用函数     :
被调用函数   :
作者         : DMS
日期         : 2015-3-19
修改日期     :
修改内容     :
'''
def DMSCheckStatusEqui(IP):
    StrCmdExec='ping '+str(IP)+' -n 1 -w 1000'                          #命令字符串
    fd=os.popen(str(StrCmdExec))
    OutputC=fd.readlines()[5]  #ping获取结果 
    fd.close()   
    OutputR=OutputC.decode('gbk').encode('utf-8')  #处理结果乱码 
    if '100%' in OutputR:                          #判断在线状态
        DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(IP, 'online', 'offline')  #更新状态为offline
    else:
        DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(IP, 'online', 'online')  #更新状态为online


'''
函数名       ：DMSCheckStatusEquiMuitl
功能描述     : 检查多个设备的在线状态
输入参数     : EquiIPList(参数合法性由调用者保证)IP列表
返回值       : {IP:在线状态}，1 在线，0 不在线
调用函数     : CheckStatusEqui
被调用函数   :
作者         : DMS
日期         : 2015-3-19
修改日期     :
修改内容     :
'''

def DMSCheckStatusEquiMuitl(EquiIPList):
    EquiIPListT=[]
    threads=[]
    for x in range(0,len(EquiIPList),40):
        EquiIPListT=EquiIPList[x:x+40]
        for IP in EquiIPListT:
            threads.append(threading.Thread(target=DMSCheckStatusEqui,args=(str(IP),)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()  
        threads=[]  