# -*- coding: utf-8 -*- 
import wmi 
import threading
import paramiko
import pythoncom
import DMSDircEqui
import os
class ssh_linux():  #linux信息获取基本函数类
  def __init__(self,ip,port,account,password):
    self.ip=ip
    self.port=int(port)
    self.account=account
    self.password=password
    self.op='linux'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(self.ip,self.port,self.account,self.password,timeout=5)
    self.p=ssh

  def disk_usage(self):
    ssh=self.p
    cmd="df -h|tr -s ' '|cut -d ' ' -f5|grep -o '[0-9]*'|sort -rn|head -n1"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out= stdout.readlines()
    err= stderr.readlines()
    if len(err)==0:
      for i in out:
        DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(self.ip,'disk',i[:-1])
 #       print '%s %s disk_usage: %s' %(self.os,self.ip,i[:-1])
    else:
      for j in err:
        print j[:-1]
  def memory_usage(self):
    ssh=self.p
    cmd='free -m|head -n2|tail -n1|tr -s " "|cut -d " " -f4'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out= stdout.readlines()
    err= stderr.readlines()
    if len(err)==0:
      for i in out:
        DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(self.ip,'mem',i[:-1])
#        print '%s %s memory_usage: %s' %(self.os,self.ip,i[:-1])
    else:
      for j in err:
        print j[:-1]
    ssh.close()
  def cpu_usage(self):
    ssh=self.p
    cmd='tempvm=` vmstat 1 3|head -n4|tail -n1`;expr `echo $tempvm|tr -s " "|cut -d " " -f13` + `echo $tempvm|tr -s " "|tail -n1|cut -d " " -f14`'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out= stdout.readlines()
    err= stderr.readlines()
    if len(err)==0:
      for i in out:
        DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(self.ip,'cpu',i[:-1])
#        print   '%s %s cpu_usage: %s' %(self.os,self.ip,i[:-1])
    else:
      for j in err:
        print j[:-1]
  def shutdown_linux(self):
    ssh=self.p
    cmd='shutdown'
    stdout, stderr = ssh.exec_command(cmd)
#    time.sleep(30)
#    ping='ping'+str(self.ip)
#    p=os.popen(ping)
#    r=p.read()
 #   print r
#    p.close()
  def disconnect_ssh(self):
    ssh=self.p
    ssh.close()
class ssh_win(): #windows信息获取基本函数类
  def __init__(self,ip,account,password):
    self.ip=ip
    self.account=account
    self.password=password
    self.op='windows'
    pythoncom.CoInitialize()
    self.c = wmi.WMI(computer=self.ip,user=self.account,password=self.password)
  def memory_use(self):
    c = self.c
    p=os.popen('systeminfo')
    m=p.readlines()
    #z=filter(lambda x:x.isdigit(),m[24]) 
    f=filter(lambda x:x.isdigit(),m[25]) 
   # use=str(100*(int(z)-int(f))/int(z))
#    print "%s %s Memory use: %s" %(self.os,self.ip,f) 
    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(self.ip,'mem',f)
  def  cpu_use(self):
    c = self.c  
    for cpu in c.Win32_Processor(): 
      cu=str(cpu.LoadPercentage)
#      print '%s %s Utilization: %s: %s%%' % (self.os,self.ip,cpu.DeviceID,cu)
    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(self.ip,'cpu',cu)   
  def disk_use(self):
    c = self.c
    ds=[]
    for disk in c.Win32_LogicalDisk (DriveType=3):
      d=int(100.0*(long(disk.Size)-long(disk.FreeSpace)) / long(disk.Size)) 
      ds.append(d)
#      print  "%s %s %s %.f use" % (self.os,self.ip,disk.Caption,d)
      
    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(self.ip,'disk',str(max(ds)))
  def shutdown_win(self):
    c = self.c
    os = c.Win32_OperatingSystem(Primary=1)[0]
    os.Shutdown()
def thread_linux(ip,port,account,password): #linux信息获取多线程方法
  try:
    s=ssh_linux(ip,port,account,password)
    s.disk_usage()
    s.memory_usage()
    s.cpu_usage()
    s.disconnect_ssh()
  except:
    pass
def thread_win(ip,account,password): #windows信息获取多线程方法
  try:
    w=ssh_win(ip,account,password)
    w.memory_use()
    w.cpu_use()
    w.disk_use() 
  except:
    pass
  
def shutdown_win(ip,account,password):  #windows关机操作多线程方法
  try:
    w=ssh_win(ip,account,password)
    w.shutdown_win()
  except:
    pass
 
def shutdown_linux(ip,port,account,password):  #linux关机操作多线程方法
  try:
    s=ssh_linux(ip,port,account,password)
    s.shutdown_linux()
    s.disconnect_ssh()
  except:
    pass
def get_info(info): #采集设备信息的函数
  theads=[]
  for m in info:
    ip=m[0]
    port=m[1]
    account=m[2]
    password=m[3] 
    if  port=='None':
      t=threading.Thread(target=thread_win,args=(ip,account,password))
      theads.append(t)
      t.start()
    else:
      a=threading.Thread(target=thread_linux,args=(ip,port,account,password)) 
      theads.append(a)
      a.start()  
  for j in theads:
    j.join()
def shut_down(info): #采集设备信息的函数
  theads=[]
  for m in info:
    ip=m[0]
    port=m[1]
    account=m[2]
    password=m[3] 
    if  port=='None':
      t=threading.Thread(target=shutdown_win,args=(ip,account,password))
      theads.append(t)
      t.start()
    else:
      a=threading.Thread(target=shutdown_linux,args=(ip,port,account,password)) 
      theads.append(a)
      a.start()  
  for j in theads:
    j.join()
