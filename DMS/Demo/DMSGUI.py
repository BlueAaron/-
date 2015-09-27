# -*- coding: cp936 -*-
import wx 
import wx.html
import wx.grid
import sys
import os
import csv
import time
from threading import Thread
from wx.lib.pubsub import pub
from wx import Panel
import threading
import copy

import DMSAbout
import DMSHelp
import DMSDircEqui
import DMSCheckEqui
import DMSMsgShow
import DMSSytemConfig
import DMSAlarmShow
import DMSHidewindow
import DMSAlarm
import DMSMailConfig
import DMSAlarmConfig
import DMSInfo
import DMSMailSend

whileflag=True
class MyFrame(wx.Frame):
    def __init__(self, parent):
        id=wx.NewId()
        wx.Frame.__init__(self, parent, id, title='DMS-Device Manager System',pos=(100,100),size=(800,600))
        #����logo
        self.SetIcon(wx.Icon('logo.ico',wx.BITMAP_TYPE_ICO))
        #�������ָ���ʽ
        self.SetCursor( wx.StockCursor( wx.CURSOR_HAND ) ) 
        self.panel=wx.Panel(self,-1)
        #����panel������ɫ
        self.panel.SetBackgroundColour('White')
       
#         #������ʱ��
#         self.timer=wx.Timer(self)

        #����״̬��
        self.status = self.CreateStatusBar()
        menuBar = wx.MenuBar()# �����˵���
        menu = wx.Menu()
        menu2 = wx.Menu()
        menu3 = wx.Menu()
        menu4 = wx.Menu()
        self.Import = menu.Append(wx.NewId(), "Import ", "Import your ip list")
        self.Export = menu.Append(wx.NewId(), "Export", "Export your device info")
#         self.Add = menu.Append(wx.NewId(), "AddDevice", "Add ip in list")
#         self.Add = menu.Append(wx.NewId(), "DelDevice", "Delete ip in list")
        menu.AppendSeparator()
        self.Exit = menu.Append(wx.NewId(), "Exit", "Exit DMS")
        self.Config = menu2.Append(wx.NewId(), "AlarmConfig", "Alarm Config")
        self.MailConfig = menu2.Append(wx.NewId(), "MailConfig", "Mail Config")
        self.SystemConfig = menu2.Append(wx.NewId(), "SystemConfig", "System Config")
        self.Alarm = menu3.Append(wx.NewId(), "Show", "Alarm Show")
        self.About = menu4.Append(wx.NewId(), "About", "About")
        self.Help = menu4.Append(wx.NewId(), "Help", "Help")
        menuBar.Append(menu, "File ") # �ڲ˵����ϸ��ϲ˵�
        menuBar.Append(menu2, "System ") 
        menuBar.Append(menu3, "Alarm ") 
        menuBar.Append(menu4, "Help ") 
        self.SetMenuBar(menuBar)  # �ڿ���ϸ��ϲ˵���
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.taskBarIcon=DMSHidewindow.TaskBarIcon(self)
        
#         MyIP = wx.StaticText(self.panel, -1, "   IP:")
#         IP_Value = wx.TextCtrl(self.panel, -1, value="1.1.1.1")
#         OsType = wx.StaticText(self.panel, -1, "   OsType:")
#         OsType_Value = wx.Choice(self.panel, -1,choices=['all','Linux','win'],name="win")
#         addrSizer = wx.FlexGridSizer(cols=5, hgap=20, vgap=5)
#         search = wx.Button(self.panel, label="Search",size=(50,25))

   
#         addrSizer.Add(MyIP, 0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_HORIZONTAL )
#         addrSizer.Add(IP_Value, 0, wx.FIXED_MINSIZE)
#         addrSizer.Add(OsType, 0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_HORIZONTAL )
#         addrSizer.Add(OsType_Value, 0, wx.FIXED_MINSIZE)
#         addrSizer.Add(search, 0, wx.FIXED_MINSIZE)
        self.mainSizer.SetSizeHints(self)

        #���¼�
        self.Bind(wx.EVT_MENU, self.OpenFile, self.Import)
        self.Bind(wx.EVT_MENU, self.SaveFile, self.Export)
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, self.Exit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.About)
        self.Bind(wx.EVT_MENU, self.OnHelp, self.Help)
        self.Bind(wx.EVT_MENU, self.OnConfig, self.Config)
        self.Bind(wx.EVT_MENU, self.OnMailConfig, self.MailConfig)
        self.Bind(wx.EVT_MENU, self.OnSystemConfig, self.SystemConfig)
        self.Bind(wx.EVT_MENU, self.OnAlarm, self.Alarm)
        #��С���¼���
        self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)
        self.Bind(wx.EVT_CLOSE, self.OnClose) 
        
#         #�󶨶�ʱ��
#         self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        #��ʱ��ʱ��
        mytime=int(DMSSytemConfig.data["checktime"])
        sleeptime=mytime*60
        self.thread = DownLoad_Video(self,sleeptime,whileflag)
        self.thread.setDaemon(True)
        self.thread.start() 
#         self.timer.Start(mytime*60000)
        #��ʼ�����
        self.list = ['����״̬','IP','�豸����','CPUʹ����(%)','�ڴ�ʣ��(MB)','Ӳ��ʹ����(%)']
        self.grid = wx.grid.Grid(self.panel,-1)
        self.grid.CreateGrid(16,len(self.list))
        #��ֹ�༭���
        self.grid.EnableEditing(False)
        for date in range(len(self.list)):
                self.grid.SetColLabelValue(date, self.list[date])
        for cols in [0,2,3,4,5]:
            self.grid.SetColSize(cols, 100)
        for cols in [1]:
            self.grid.SetColSize(cols, 150)
        self.Grid = wx.FlexGridSizer(cols=6, hgap=10, vgap=5)
        self.Grid.Add(self.grid, 0,wx.EXPAND|wx.ALL, 0)

        
        self.mainSizer.Add(wx.StaticLine(self.panel), 0,wx.EXPAND|wx.TOP|wx.BOTTOM, 5) 
        #sself.mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)     
        self.mainSizer.Add(wx.StaticLine(self.panel), 0,wx.EXPAND|wx.TOP|wx.BOTTOM, 5) 
        self.mainSizer.Add(self.Grid, 1, wx.EXPAND , 0)#1�����Զ�����
        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.mainSizer.SetSizeHints(self)
        
    def OnCloseWindow(self, event):
                #�˳��Ի���
        dlg = wx.MessageDialog(None, 'Sure to Exit?',
                      'DMS', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result==wx.ID_YES:
            self.thread.stop()
#             self.thread.join()
            dlg.Destroy()
            #�ر���������ͼ��
            self.taskBarIcon.Destroy()
            self.Destroy()
    #�����ļ��Ի���       
    def OpenFile(self,event): 
        wildcard = "IP List(*.csv)|*.csv|" \
            "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, "Select Ip List", os.getcwd(),
            "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            global csvpath
            csvpath=dialog.GetPath()
            self.Readcsv(csvpath)
            #ɾ����ʼ����10�У���ʾ�µ�����У�����ˢ��
            self.grid.DeleteRows(pos=0, numRows=16)
            self.grid.AppendRows(len(DMSDircEqui.DMSDataDirc))
            #��ȡ�����IP��Ϣ
            for row in range(len(DMSDircEqui.DMSDataDirc)):
                self.grid.SetCellValue(row,1,DMSDircEqui.DMSDataDirc.keys()[row])
                self.grid.SetCellValue(row,2,DMSDircEqui.DMSDataDirc[DMSDircEqui.DMSDataDirc.keys()[row]]["platform"])
            #ˢ�±��
            self.grid.ForceRefresh()
        dialog.Destroy()
     
    #����csv�ļ�   
    def SaveFile(self,event):
        wildcard = "Device Info(*.csv)|*.csv|" \
            "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, "Select Ip List", os.getcwd(),
            "", wildcard, wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            global csvpath
            csvpath=dialog.GetPath()
            self.Writecsv(csvpath)
        dialog.Destroy()
        
    def Readcsv(self,csvpath):
        with open(csvpath,'rb') as f:
            reader = csv.reader(f)
            self.iplist=[]
            self.oslist=[]
            self.usrlist=[]
            self.pwdlist=[]
            self.portlist=[]
            for row in reader:
                #����IP���û��������룬ϵͳ�����б�
                self.iplist.append(row[0])
                self.oslist.append(row[1])
                self.usrlist.append(row[2])
                self.pwdlist.append(row[3])
                self.portlist.append(row[4])
            #��ʼ���ֵ�
            DMSDircEqui.DMSDircEquiClass().DMSDataDircInsert(self.iplist)
            #��ʼ��ϵͳ���͡��û��������롢�˿�
            for ip in self.iplist:
                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"platform", self.oslist[self.iplist.index(ip)])

                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"username", self.usrlist[self.iplist.index(ip)])

                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"passwd", self.pwdlist[self.iplist.index(ip)])
                    
                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"port", self.portlist[self.iplist.index(ip)])   #
            #�����ֵ�
            self.initdir=copy.deepcopy(DMSDircEqui.DMSDataDirc )          
    
    def Writecsv(self,csvpath):
        with open(csvpath, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile,dialect='excel')
            #��ȡ�ֵ�
            dir=DMSDircEqui.DMSDataDirc
            iplist=DMSDircEqui.DMSDataDirc.keys()
            #��ʼ����ͷ
            spamwriter.writerow(['IP','ϵͳ����','����״̬','CPUʹ����','�ڴ�ʣ��','Ӳ��ռ��'])
            for ip in iplist:
                spamwriter.writerow([ip, dir[ip]['platform'],dir[ip]['online'],dir[ip]['cpu'],dir[ip]['mem'],dir[ip]['disk']]) 
                     
    def OnAbout(self, event):
        dlg = DMSAbout.SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnHelp(self, event):
        dlg = DMSHelp.SketchHelp(self)
        dlg.ShowModal()
        dlg.Destroy()   
        
    def OnConfig(self,event):
        dlg=DMSAlarmConfig.AlarmConfig()
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnMailConfig(self,event):
        dlg=DMSMailConfig.MailConfig()
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnSystemConfig(self,event):
        dlg=DMSSytemConfig.SystemConfig()
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnAlarm(self,event):
        dlg=DMSAlarmShow.AlarmShow()
        dlg.ShowModal()
        dlg.Destroy()
    #��ȡIP���к�                           
    def FindPos(self,ip):
        return DMSDircEqui.DMSDataDirc.keys().index(ip)
    
    #��ʱ��
#     def OnTimer(self,event):
        #self.StatusBar = customStatusBar(self)

#         self.status.SetFieldsCount(2)
#         self.status.SetStatusWidths([-1,-2])
#         self.status.SetStatusText(u'���ڼ���豸�Ƿ����ߡ�����',0)
#         self.count=0
#         self.status.gauge=wx.Gauge(self.status,1001,100,pos=(138,2),size=(265,20),style = wx.GA_HORIZONTAL)
#         self.status.gauge.SetBezelFace(3)
#         self.status.gauge.SetShadowWidth(3)
#         self.status.gauge.SetValue(self.count)
#         self.SetStatusBar(self.status)




    #���õ�Ԫ����ɫ     
    def SetCellColor(self,row,col,color):
        self.grid.SetCellBackgroundColour(row, col, color)
        self.grid.ForceRefresh()
        
    def SetCellTextColor(self,row,col,color):
        self.grid.SetCellTextColour(row, col, color)
        self.grid.ForceRefresh()        
    #��С���¼�
    def OnIconfiy(self, event):  
        #wx.MessageBox('Frame has been iconized!', 'Prompt')
        self.Hide()    
        event.Skip()
    
    #ȡ���رչ���     
    def OnClose(self, event):  
        pass 
    
class DownLoad_Video(threading.Thread): #���غ���
    def __init__(self,window,sleeptime,whileflag):
        threading.Thread.__init__(self)
        self.window = window
        self.sleeptime=sleeptime
        self.whileflag=whileflag
        self.ifdo=True 
        
    def run(self):
#         print self.ifdo
        while self.ifdo:
            #��ʼ���澯���
            alarmflag=0
            #�澯����
            print "hello"
            alarmlock=int(DMSSytemConfig.data["isalarm"])
            #�ʼ�����
            maillock=int(DMSSytemConfig.data["ismail"])
            #��ʼ���ֵ�
            try:
                DMSDircEqui.DMSDataDirc=self.initdir
            except Exception , e:
                pass
            #����Ƿ�����
            DMSCheckEqui.DMSCheckStatusEquiMuitl(DMSDircEqui.DMSDataDirc.keys())
            
#             self.window.status.gauge.SetValue(30)
            #��ʼ�豸��Ϣ�б�
            infolist=[]
            iplist=DMSDircEqui.DMSDataDirc.keys()
            for ip in DMSDircEqui.DMSDataDirc:
                myinfo=[ip,DMSDircEqui.DMSDataDirc[ip]["port"],DMSDircEqui.DMSDataDirc[ip]["username"],DMSDircEqui.DMSDataDirc[ip]["passwd"]]
                infolist.append(myinfo)
            #��ȡ�豸����
#             self.window.status.SetStatusText(u'���ڻ�ȡ�豸��Ϣ������',0)
#             self.window.status.gauge.SetValue(50)
            DMSInfo.get_info(infolist)
            
#             self.window.status.gauge.SetValue(80)
            
            for ip in DMSDircEqui.DMSDataDirc:
                #��ȡIP���ڵ���
                row=self.FindPos(ip)
                self.window.grid.SetCellValue(row,0,DMSDircEqui.DMSDataDirc[ip]["online"])
                self.window.grid.SetCellValue(row,1,ip)
                self.window.grid.SetCellValue(row,2,DMSDircEqui.DMSDataDirc[ip]["platform"])
                self.window.grid.SetCellValue(row,3,DMSDircEqui.DMSDataDirc[ip]["cpu"])
                self.window.grid.SetCellValue(row,4,DMSDircEqui.DMSDataDirc[ip]["mem"])
                self.window.grid.SetCellValue(row,5,DMSDircEqui.DMSDataDirc[ip]["disk"])
                #ˢ�±��
                self.window.grid.ForceRefresh()
                
                if DMSDircEqui.DMSDataDirc[ip]["online"]=='offline':
                    for col in range(6):
                        self.window.SetCellColor(row, col, 'gray')
                else:
                    for col in range(6):
                        self.window.SetCellColor(row, col, 'white')
                if DMSDircEqui.DMSDataDirc[ip]["cpu"]!="none":      
                    if int(DMSDircEqui.DMSDataDirc[ip]["cpu"])>int(DMSAlarmConfig.data["cpu"]):
                        self.window.SetCellTextColour(row, 3, 'red')
                        alarmflag=alarmflag+1
                    else:
                        self.window.SetCellTextColour(row, 3, 'black')
                if DMSDircEqui.DMSDataDirc[ip]["mem"]!="none": 
                    if int(DMSDircEqui.DMSDataDirc[ip]["mem"])<int(DMSAlarmConfig.data["mem"]):
                        self.window.SetCellTextColour(row, 4, 'red') 
                        alarmflag=alarmflag+1
                    else:
                        self.window.SetCellTextColour(row, 4, 'black')
                if DMSDircEqui.DMSDataDirc[ip]["disk"]!="none":       
                    if int(DMSDircEqui.DMSDataDirc[ip]["disk"])>int(DMSAlarmConfig.data["disk"]):
                        self.window.SetCellTextColour(row, 5, 'red')
                        alarmflag=alarmflag+1
                    else:
                        self.window.SetCellTextColour(row, 5, 'black')
            #������Ϣ��Ȼ�������������𣬲�Ӱ��������
            if alarmflag!=0 and alarmlock==0:
                t=threading.Thread(target=DMSMsgShow.DMSShowAlarmMsg,args=(str('���и澯'),))
                t.start()
            #�жϸ澯������д�澯�ļ�
            DMSAlarm.alarm_calculate([DMSAlarmConfig.data["mem"],DMSAlarmConfig.data["disk"],DMSAlarmConfig.data["cpu"]], DMSDircEqui.DMSDataDirc)
            #�����ʼ�
            if maillock==0 and alarmflag!=0:
                DMSMailSend.DMSMailSendInfo(mail_host=DMSMailConfig.data["smtp"], frommail=DMSMailConfig.data["from"], to_list= DMSMailConfig.data["to"].split(','), sub="DMS�ʼ���Ϣ", content="you have warnning,please check", mail_user=DMSMailConfig.data["user"], mail_pass=DMSMailConfig.data["passwd"])
            #����澯�ļ�
            DMSAlarm.clear_txt(int(DMSSytemConfig.data["savealarm"]))
            time.sleep(self.sleeptime)
            
#             self.status.gauge.SetValue(100)
#             self.status.gauge.Destroy()
#             self.status.SetStatusText(u'��ȡ��Ϣ�ɹ�',0)  
    def stop (self):
#             print 'I am stopping it...'
            self.ifdo = False;      
            
class App(wx.App):

    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        
        bmp = wx.Image("welcome.jpg").ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                1000, None, -1)
        wx.Yield()
        #��������ʱ��
        time.sleep(2)
        
        self.frame = MyFrame(None) 
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def OnExit(self):
        pass
        
    
app = App()
app.MainLoop() 
