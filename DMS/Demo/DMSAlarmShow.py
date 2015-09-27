# -*- coding: cp936 -*-
import wx
import wx.grid
import os
import csv


class AlarmShow(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Alarm Show',
                          size=(500, 400) )
        self.list = ['时间','IP','告警信息']
        self.grid = wx.grid.Grid(self,-1)
        self.grid.CreateGrid(16,len(self.list))
        #禁止编辑表格
        self.grid.EnableEditing(False)
        for date in range(len(self.list)):
                self.grid.SetColLabelValue(date, self.list[date])
        for cols in [0,1]:
            self.grid.SetColSize(cols, 100)
        for cols in [2]:
            self.grid.SetColSize(cols, 200)
        self.Grid = wx.FlexGridSizer(cols=6, hgap=10, vgap=5)
        self.Grid.Add(self.grid, 0,wx.EXPAND|wx.ALL, 0)
        
        self.OpenLog = wx.Button(self, wx.ID_OK, "OpenLog", pos=(15, 15))
        self.OpenLog.SetDefault()
        self.cancel = wx.Button(self, wx.ID_CANCEL, "Close", pos=(115, 15))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.Grid, 0, wx.EXPAND|wx.ALL, 5)
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(self.OpenLog)
        btns.AddButton(self.cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
        self.Bind(wx.EVT_BUTTON, self.OpenFile, self.OpenLog)
        
    def OpenFile(self,event): 
        wildcard = "IP List(*.csv)|*.csv|" \
            "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, "Select Ip List", os.getcwd(),
            "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            global csvpath
            csvpath=dialog.GetPath()
            self.Readcsv(csvpath)
            #删除初始化的16行，显示新导入的行，并且刷新
            self.grid.DeleteRows(pos=0, numRows=16)
            self.grid.AppendRows(len(self.timelist))
            #读取导入的IP信息
            for row in range(len(self.timelist)):
                self.grid.SetCellValue(row,0,self.timelist[row])
                self.grid.SetCellValue(row,1,self.iplist[row])
                self.grid.SetCellValue(row,2,self.alarmlist[row])
                
            #刷新表格
            self.grid.ForceRefresh()
        dialog.Destroy()
        
    def Readcsv(self,csvpath):
        with open(csvpath,'rb') as f:
            reader = csv.reader(f)
            self.timelist=[]
            self.iplist=[]
            self.alarmlist=[]
            for row in reader:
                self.timelist.append(row[0])
                self.iplist.append(row[1])
                self.alarmlist.append(row[2])