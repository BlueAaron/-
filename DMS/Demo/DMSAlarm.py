# -*- coding: utf-8 -*- 
import os 
import datetime

def alarm_calculate(alarm_Line,DMSDataDirc): #鍛婅璁＄畻骞跺悗杩斿洖鍛婅淇℃伅瀛楀吀锛屽苟鍐欏叆鏂囦欢
  alarm_txt=[]
  now=datetime.datetime.now()
  alarm_time=now.strftime("%Y-%m-%d %H:%M")

  for i in DMSDataDirc:
    alarm={}
    var_i=i+(16-len(i))*' '
    dev_mem=DMSDataDirc[i]['mem']
    if dev_mem!="none":
        dev_mem=int(DMSDataDirc[i]['mem'])
        alarm_mem=int(alarm_Line[0])
        if dev_mem <= alarm_mem:
           am='%s,%s,Memory alarm'%(alarm_time,var_i)
           alarm['mem']=am
           alarm_txt.append(am)
    dev_disk=DMSDataDirc[i]['disk']
    if dev_disk!="none":
        dev_disk=int(DMSDataDirc[i]['disk'])
        alarm_disk=int(alarm_Line[1])
        if dev_disk >= alarm_disk:
            ad='%s,%s,Disk alarm'%(alarm_time,var_i)
            alarm['disk']=ad
            alarm_txt.append(ad)
    dev_cpu=DMSDataDirc[i]['cpu']
    if dev_cpu!="none":
        dev_cpu=int(DMSDataDirc[i]['cpu'])
        alarm_cpu=int(alarm_Line[2])
        if dev_cpu >= alarm_cpu:
            ac='%s,%s,CPU alarm'%(alarm_time,var_i)
            alarm['cpu']=ac 
            alarm_txt.append(ac)
    DMSAlarmDirc[i]=alarm
  if os.path.exists('Alarm_log')==False:    
    os.makedirs('Alarm_log')
  today=datetime.date.today()
  txt_name='Alarm_log\\Alarm'+str(today)+'.csv'
  txt=''
  for i in alarm_txt:
    txt +=i+'\n'
  f=open(txt_name,'a')
  f.write(txt)
  f.close()

def clear_txt(var_date):  #娓呴櫎鏃ュ瓙鍑芥暟
  sav_names=[]
  today=datetime.date.today()
  for i in range(0,int(var_date)):
    sav_time=today-datetime.timedelta(days=i)
    sav_name='Alarm'+str(sav_time)+'.csv'
    sav_names.append(sav_name)
  for root,dirs,filenames in os.walk('Alarm_log'):
    for f in filenames:
      if f not in sav_names:
        fname=os.path.join(root,f)
        os.remove(fname)
		
		
DMSAlarmDirc={} #杩斿洖缁撴灉鍛婅淇℃伅瀛楀吀
# dir={'10.1.1.3': {'username': 'root', 'passwd': 'Huawei@123', 'port': '39200', 'platform': 'linux', 'online': 'offline', 'disk': '10000', 'mem': '2222', 'cpu': '222'}, '10.1.1.2': {'username': 'admin', 'passwd': 'admin123', 'port': '', 'platform': 'win', 'online': 'offline', 'disk': '222', 'mem': '222', 'cpu': '2222'}, '127.0.0.1': {'username': 'root', 'passwd': '', 'port': '', 'platform': 'win', 'online': 'online', 'disk': '111', 'mem': '11', 'cpu': '1'}}
# 
# alarm_calculate([1,1,1],dir)
# clear_txt('7')
#print DMSAlarmDirc  
