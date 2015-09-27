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
        #设置logo
        self.SetIcon(wx.Icon('logo.ico',wx.BITMAP_TYPE_ICO))
        #设置鼠标指针格式
        self.SetCursor( wx.StockCursor( wx.CURSOR_HAND ) ) 
        self.panel=wx.Panel(self,-1)
        #设置panel背景颜色
        self.panel.SetBackgroundColour('White')
       
#         #创建定时器
#         self.timer=wx.Timer(self)

        #创建状态栏
        self.status = self.CreateStatusBar()
        menuBar = wx.MenuBar()# 创建菜单栏
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
        menuBar.Append(menu, "File ") # 在菜单栏上附上菜单
        menuBar.Append(menu2, "System ") 
        menuBar.Append(menu3, "Alarm ") 
        menuBar.Append(menu4, "Help ") 
        self.SetMenuBar(menuBar)  # 在框架上附上菜单栏
        
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

        #绑定事件
        self.Bind(wx.EVT_MENU, self.OpenFile, self.Import)
        self.Bind(wx.EVT_MENU, self.SaveFile, self.Export)
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, self.Exit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.About)
        self.Bind(wx.EVT_MENU, self.OnHelp, self.Help)
        self.Bind(wx.EVT_MENU, self.OnConfig, self.Config)
        self.Bind(wx.EVT_MENU, self.OnMailConfig, self.MailConfig)
        self.Bind(wx.EVT_MENU, self.OnSystemConfig, self.SystemConfig)
        self.Bind(wx.EVT_MENU, self.OnAlarm, self.Alarm)
        #最小化事件绑定
        self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)
        self.Bind(wx.EVT_CLOSE, self.OnClose) 
        
#         #绑定定时器
#         self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        #定时器时间
        mytime=int(DMSSytemConfig.data["checktime"])
        sleeptime=mytime*60
        self.thread = DownLoad_Video(self,sleeptime,whileflag)
        self.thread.setDaemon(True)
        self.thread.start() 
#         self.timer.Start(mytime*60000)
        #初始化表格
        self.list = ['在线状态','IP','设备类型','CPU使用率(%)','内存剩余(MB)','硬盘使用率(%)']
        self.grid = wx.grid.Grid(self.panel,-1)
        self.grid.CreateGrid(16,len(self.list))
        #禁止编辑表格
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
        self.mainSizer.Add(self.Grid, 1, wx.EXPAND , 0)#1代表不自动增长
        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.mainSizer.SetSizeHints(self)
        
    def OnCloseWindow(self, event):
                #退出对话框
        dlg = wx.MessageDialog(None, 'Sure to Exit?',
                      'DMS', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result==wx.ID_YES:
            self.thread.stop()
#             self.thread.join()
            dlg.Destroy()
            #关闭任务栏的图标
            self.taskBarIcon.Destroy()
            self.Destroy()
    #导入文件对话框       
    def OpenFile(self,event): 
        wildcard = "IP List(*.csv)|*.csv|" \
            "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, "Select Ip List", os.getcwd(),
            "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            global csvpath
            csvpath=dialog.GetPath()
            self.Readcsv(csvpath)
            #删除初始化的10行，显示新导入的行，并且刷新
            self.grid.DeleteRows(pos=0, numRows=16)
            self.grid.AppendRows(len(DMSDircEqui.DMSDataDirc))
            #读取导入的IP信息
            for row in range(len(DMSDircEqui.DMSDataDirc)):
                self.grid.SetCellValue(row,1,DMSDircEqui.DMSDataDirc.keys()[row])
                self.grid.SetCellValue(row,2,DMSDircEqui.DMSDataDirc[DMSDircEqui.DMSDataDirc.keys()[row]]["platform"])
            #刷新表格
            self.grid.ForceRefresh()
        dialog.Destroy()
     
    #导出csv文件   
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
                #生成IP，用户名，密码，系统类型列表
                self.iplist.append(row[0])
                self.oslist.append(row[1])
                self.usrlist.append(row[2])
                self.pwdlist.append(row[3])
                self.portlist.append(row[4])
            #初始化字典
            DMSDircEqui.DMSDircEquiClass().DMSDataDircInsert(self.iplist)
            #初始化系统类型、用户名、密码、端口
            for ip in self.iplist:
                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"platform", self.oslist[self.iplist.index(ip)])

                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"username", self.usrlist[self.iplist.index(ip)])

                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"passwd", self.pwdlist[self.iplist.index(ip)])
                    
                    DMSDircEqui.DMSDircEquiClass().DMSDataDircUpdate(ip,"port", self.portlist[self.iplist.index(ip)])   #
            #拷贝字典
            self.initdir=copy.deepcopy(DMSDircEqui.DMSDataDirc )          
    
    def Writecsv(self,csvpath):
        with open(csvpath, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile,dialect='excel')
            #读取字典
            dir=DMSDircEqui.DMSDataDirc
            iplist=DMSDircEqui.DMSDataDirc.keys()
            #初始化表头
            spamwriter.writerow(['IP','系统类型','在线状态','CPU使用率','内存剩余','硬盘占用'])
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
    #获取IP的行号                           
    def FindPos(self,ip):
        return DMSDircEqui.DMSDataDirc.keys().index(ip)
    
    #定时器
#     def OnTimer(self,event):
        #self.StatusBar = customStatusBar(self)

#         self.status.SetFieldsCount(2)
#         self.status.SetStatusWidths([-1,-2])
#         self.status.SetStatusText(u'正在检查设备是否在线。。。',0)
#         self.count=0
#         self.status.gauge=wx.Gauge(self.status,1001,100,pos=(138,2),size=(265,20),style = wx.GA_HORIZONTAL)
#         self.status.gauge.SetBezelFace(3)
#         self.status.gauge.SetShadowWidth(3)
#         self.status.gauge.SetValue(self.count)
#         self.SetStatusBar(self.status)




    #设置单元格颜色     
    def SetCellColor(self,row,col,color):
        self.grid.SetCellBackgroundColour(row, col, color)
        self.grid.ForceRefresh()
        
    def SetCellTextColor(self,row,col,color):
        self.grid.SetCellTextColour(row, col, color)
        self.grid.ForceRefresh()        
    #最小化事件
    def OnIconfiy(self, event):  
        #wx.MessageBox('Frame has been iconized!', 'Prompt')
        self.Hide()    
        event.Skip()
    
    #取消关闭功能     
    def OnClose(self, event):  
        pass 
    
class DownLoad_Video(threading.Thread): #下载函数
    def __init__(self,window,sleeptime,whileflag):
        threading.Thread.__init__(self)
        self.window = window
        self.sleeptime=sleeptime
        self.whileflag=whileflag
        self.ifdo=True 
        
    def run(self):
#         print self.ifdo
        while self.ifdo:
            #初始化告警标记
            alarmflag=0
            #告警开关
            print "hello"
            alarmlock=int(DMSSytemConfig.data["isalarm"])
            #邮件开关
            maillock=int(DMSSytemConfig.data["ismail"])
            #初始化字典
            try:
                DMSDircEqui.DMSDataDirc=self.initdir
            except Exception , e:
                pass
            #检查是否在线
            DMSCheckEqui.DMSCheckStatusEquiMuitl(DMSDircEqui.DMSDataDirc.keys())
            
#             self.window.status.gauge.SetValue(30)
            #初始设备信息列表
            infolist=[]
            iplist=DMSDircEqui.DMSDataDirc.keys()
            for ip in DMSDircEqui.DMSDataDirc:
                myinfo=[ip,DMSDircEqui.DMSDataDirc[ip]["port"],DMSDircEqui.DMSDataDirc[ip]["username"],DMSDircEqui.DMSDataDirc[ip]["passwd"]]
                infolist.append(myinfo)
            #获取设备属性
#             self.window.status.SetStatusText(u'正在获取设备信息。。。',0)
#             self.window.status.gauge.SetValue(50)
            DMSInfo.get_info(infolist)
            
#             self.window.status.gauge.SetValue(80)
            
            for ip in DMSDircEqui.DMSDataDirc:
                #获取IP所在的行
                row=self.FindPos(ip)
                self.window.grid.SetCellValue(row,0,DMSDircEqui.DMSDataDirc[ip]["online"])
                self.window.grid.SetCellValue(row,1,ip)
                self.window.grid.SetCellValue(row,2,DMSDircEqui.DMSDataDirc[ip]["platform"])
                self.window.grid.SetCellValue(row,3,DMSDircEqui.DMSDataDirc[ip]["cpu"])
                self.window.grid.SetCellValue(row,4,DMSDircEqui.DMSDataDirc[ip]["mem"])
                self.window.grid.SetCellValue(row,5,DMSDircEqui.DMSDataDirc[ip]["disk"])
                #刷新表格
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
            #生成消息框，然后让他自生自灭，不影响主界面
            if alarmflag!=0 and alarmlock==0:
                t=threading.Thread(target=DMSMsgShow.DMSShowAlarmMsg,args=(str('您有告警'),))
                t.start()
            #判断告警，并且写告警文件
            DMSAlarm.alarm_calculate([DMSAlarmConfig.data["mem"],DMSAlarmConfig.data["disk"],DMSAlarmConfig.data["cpu"]], DMSDircEqui.DMSDataDirc)
            #发送邮件
            if maillock==0 and alarmflag!=0:
                DMSMailSend.DMSMailSendInfo(mail_host=DMSMailConfig.data["smtp"], frommail=DMSMailConfig.data["from"], to_list= DMSMailConfig.data["to"].split(','), sub="DMS邮件消息", content="you have warnning,please check", mail_user=DMSMailConfig.data["user"], mail_pass=DMSMailConfig.data["passwd"])
            #清理告警文件
            DMSAlarm.clear_txt(int(DMSSytemConfig.data["savealarm"]))
            time.sleep(self.sleeptime)
            
#             self.status.gauge.SetValue(100)
#             self.status.gauge.Destroy()
#             self.status.SetStatusText(u'获取信息成功',0)  
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
        #启动画面时间
        time.sleep(2)
        
        self.frame = MyFrame(None) 
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def OnExit(self):
        pass
        
    
app = App()
app.MainLoop() 
