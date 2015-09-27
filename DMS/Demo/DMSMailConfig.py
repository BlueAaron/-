# -*- coding: cp936 -*-
import wx
import string

data={"smtp":"smtp.qq.com","from":"xxxx@qq.com","to":"xxxx@qq.com","user":"XXXX","passwd":"XXXX"}

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

#          if len(text) == 0:
#              wx.MessageBox("This field must contain some text!", "Error")
#              textCtrl.SetBackgroundColour("pink")
#              textCtrl.SetFocus()
#              textCtrl.Refresh()
#              return False
#          if  int(text) > 100 or int(text) < 0 or int(text) > 100:
#              wx.MessageBox("This Value is not in right range!", "Error")
#              textCtrl.SetBackgroundColour("pink")
#              textCtrl.SetFocus()
#              textCtrl.Refresh()
#              return False
#          else:
#              textCtrl.SetBackgroundColour(
#                  wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
#              textCtrl.Refresh()
         return True
    

     def TransferToWindow(self):# 对话框打开时被调用
         textCtrl = self.GetWindow()
         textCtrl.SetValue(self.data.get(self.key, ""))
         #SystemConfig().alarmlock.
         return True

     def TransferFromWindow(self):# 对话框关闭时被调用
         textCtrl = self.GetWindow()
         self.data[self.key] = textCtrl.GetValue()
         return True
     
     def OnChar(self, evt):# 数据处理
         key = chr(evt.GetKeyCode())
#          if self.data == "no-alpha" and key in string.letters:
#               return
#          if (self.key == "cpu" or self.key == "mem" or self.key == "disk") and key in string.letters:
#               return
         evt.Skip()



class MailConfig(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Config Mail',
                          size=(440, 400) )

        sizer = wx.BoxSizer(wx.VERTICAL)
        about = wx.StaticText(self, -1, "Mail Config")
        smtp = wx.StaticText(self, -1, "SMTP:")
        mail = wx.StaticText(self, -1, "From:")
        tomail = wx.StaticText(self, -1, "To:")
        user = wx.StaticText(self, -1, "User:")
        passwd = wx.StaticText(self, -1, "Passwd:")
          
        self.smtp_t  = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"smtp"))
        self.mail_t = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"from"))
        self.tomail_t = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"to"))
        self.user_t = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"user"))
        self.passwd_t = wx.TextCtrl(self, -1,validator=DataXferValidator(data,"passwd"),style=wx.TE_PASSWORD)
        
        self.smtpValue=self.smtp_t.GetValue()
        self.mailValue=self.mail_t.GetValue()
        self.tomailValue=self.tomail_t.GetValue()
        self.userValue=self.user_t.GetValue()
        self.passwdValue=self.passwd_t.GetValue()

        self.Bind(wx.EVT_TEXT,self.GetSmtp,self.smtp_t)
        self.Bind(wx.EVT_TEXT,self.GetMail,self.mail_t) 
        self.Bind(wx.EVT_TEXT,self.GetToMail,self.tomail_t)
        self.Bind(wx.EVT_TEXT,self.GetToMail,self.tomail_t)
        self.Bind(wx.EVT_TEXT,self.GetToMail,self.tomail_t)
         
        okay = wx.Button(self, wx.ID_OK, "OK", pos=(15, 15))
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(115, 15))
        
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)

        fgs = wx.FlexGridSizer(5, 2, 5, 5)
        fgs.Add(smtp, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.smtp_t, 0, wx.EXPAND)
        fgs.Add(mail, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.mail_t, 0, wx.EXPAND)
        fgs.Add(tomail, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.tomail_t, 0, wx.EXPAND)
        fgs.Add(user, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.user_t, 0, wx.EXPAND)
        fgs.Add(passwd, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.passwd_t, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)
        
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
    def GetSmtp(self,evt):
        self.smtpValue=self.smtp_t.GetValue()
    
    def GetMail(self,evt):
        self.mailValue=self.mail_t.GetValue()
        
    def GetToMail(self,evt):
        self.tomailValue=self.tomail_t.GetValue()

    def GetUser(self,evt):
        self.userValue=self.user_t.GetValue()

    def GetPasswd(self,evt):
        self.passwdValue=self.passwd_t.GetValue()
