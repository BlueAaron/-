# -*- coding: cp936 -*-
import wx
import string

data={"checktime":"1","isalarm":"0","ismail":"0","savealarm":"7"}

class SystemConfig(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Config System',
                          size=(440, 400) )

        sizer = wx.BoxSizer(wx.VERTICAL)
        about = wx.StaticText(self, -1, "System Config")
        self.checktime = wx.StaticText(self, -1, "CheckTime（Min）:")
        self.checktime_t  = wx.TextCtrl(self, -1,data["checktime"])
        self.savealarm = wx.StaticText(self, -1, "SaveAlarm（Day）:")
        self.savealarm_t  = wx.TextCtrl(self, -1,data["savealarm"])        
        self.alarm = wx.StaticText(self, -1, "IsAlarm:")
        self.alarmlock = wx.RadioBox(self, -1, "", wx.DefaultPosition,wx.DefaultSize,['On','Off'])       
        self.alarmlock.SetSelection(int(data["isalarm"]))
        self.mail = wx.StaticText(self, -1, "IsMail:")
        self.mail_t = wx.RadioBox(self, -1, "", wx.DefaultPosition,wx.DefaultSize,['On','Off'])       
        self.mail_t.SetSelection(int(data["ismail"]))
                 
        okay = wx.Button(self, wx.ID_OK, "Save", pos=(15, 15))
        #okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(115, 15))
        
        self.Bind(wx.EVT_BUTTON,self.OnSave, okay)
        
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)

        fgs = wx.FlexGridSizer(4, 2, 5, 5)
        fgs.Add(self.checktime, 0, wx.ALIGN_CENTER)
        fgs.Add(self.checktime_t, 0, wx.EXPAND)
        fgs.Add(self.savealarm, 0, wx.ALIGN_CENTER)
        fgs.Add(self.savealarm_t, 0, wx.EXPAND)
        fgs.Add(self.alarm, 0, wx.ALIGN_CENTER)
        fgs.Add(self.alarmlock, 0, wx.EXPAND)
        fgs.Add(self.mail, 0, wx.ALIGN_CENTER)
        fgs.Add(self.mail_t, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)
        
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
    def OnSave(self,event):
        if int(self.checktime_t.GetValue())<1 or int(self.checktime_t.GetValue())>1440:
            dlg = wx.MessageDialog(None, 'Num Range:1~1440','DMS',wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            
        if int(self.savealarm_t.GetValue())<1 or int(self.savealarm_t.GetValue())>30:
            dlg = wx.MessageDialog(None, 'Num Range:1~1440','DMS',wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()        
        else:            
            data["checktime"]=self.checktime_t.GetValue()
            data["savealarm"]=self.savealarm_t.GetValue()
            data["isalarm"]=self.alarmlock.GetSelection()
            data["ismail"]=self.alarmlock.GetSelection()
            self.Destroy()
          
