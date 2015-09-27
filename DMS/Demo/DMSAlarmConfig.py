# -*- coding: cp936 -*-
import wx
import string

data={"mem":"1000","cpu":"90","disk":"90"}

class DataXferValidator(wx.PyValidator):# 声明验证器
     def __init__(self,data,key):
         wx.PyValidator.__init__(self)
         self.key = key
         self.data = data
         self.Bind(wx.EVT_CHAR, self.OnChar)

     def Clone(self):
         """
         Note that every validator must implement the Clone() method.
         """
         return DataXferValidator(self.data,self.key)

     def Validate(self, win):# 没有验证数据
         textCtrl = self.GetWindow()
         text = textCtrl.GetValue()

         if len(text) == 0:
             wx.MessageBox("This field must contain some text!", "Error")
             textCtrl.SetBackgroundColour("pink")
             textCtrl.SetFocus()
             textCtrl.Refresh()
             return False
         if  int(text) < 0:
             wx.MessageBox("This Value is not in right range!", "Error")
             textCtrl.SetBackgroundColour("pink")
             textCtrl.SetFocus()
             textCtrl.Refresh()
             return False
         else:
             textCtrl.SetBackgroundColour(
                 wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
             textCtrl.Refresh()
             return True
    

     def TransferToWindow(self):# 对话框打开时被调用
         textCtrl = self.GetWindow()
         textCtrl.SetValue(self.data.get(self.key, ""))
         return True

     def TransferFromWindow(self):# 对话框关闭时被调用
         textCtrl = self.GetWindow()
         self.data[self.key] = textCtrl.GetValue()
         return True
     
     def OnChar(self, evt):# 数据处理
         key = chr(evt.GetKeyCode())
#          if self.data == "no-alpha" and key in string.letters:
#               return
         if (self.key == "cpu" or self.key == "mem" or self.key == "disk") and key in string.letters:
              return
         evt.Skip()



class AlarmConfig(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Config Alarm',
                          size=(440, 400) )

        sizer = wx.BoxSizer(wx.VERTICAL)
        about = wx.StaticText(self, -1, "Alarm Config")
        cpu = wx.StaticText(self, -1, "CpuAlarm:")
        mem = wx.StaticText(self, -1, "MemAlarm:")
        disk = wx.StaticText(self, -1, "DiakAlarm:")
              
        self.cpu_t  = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"cpu"))
        self.mem_t = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"mem"))
        self.disk_t = wx.TextCtrl(self,-1,validator=DataXferValidator(data,"disk"))
        
        self.cpuValue=self.cpu_t.GetValue()
        self.memVaule=self.mem_t.GetValue()
        self.diskValue=self.disk_t.GetValue()

        self.Bind(wx.EVT_TEXT,self.GetCpu,self.cpu_t)
        self.Bind(wx.EVT_TEXT,self.GetMem,self.mem_t)
        self.Bind(wx.EVT_TEXT,self.GetDisk,self.disk_t)  
         
        okay = wx.Button(self, wx.ID_OK, "OK", pos=(15, 15))
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(115, 15))
        
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)

        fgs = wx.FlexGridSizer(4, 2, 5, 5)
        fgs.Add(cpu, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.cpu_t, 0, wx.EXPAND)
        fgs.Add(mem, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.mem_t, 0, wx.EXPAND)
        fgs.Add(disk, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.disk_t, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)
        
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
    def GetCpu(self,evt):
        self.cpuValue=self.cpu_t.GetValue()
    
    def GetMem(self,evt):
        self.memVaule=self.mem_t.GetValue()
        
    def GetDisk(self,evt):
        self.diskValue=self.disk_t.GetValue()

