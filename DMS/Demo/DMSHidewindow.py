import wx
class TaskBarIcon(wx.TaskBarIcon):  
    ID_Hello = wx.NewId()  
    def __init__(self, frame):  
        wx.TaskBarIcon.__init__(self)  
        self.frame = frame  
        self.SetIcon(wx.Icon(name='logo.ico', type=wx.BITMAP_TYPE_ICO), 'DMS!')  
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  
        self.Bind(wx.EVT_MENU, self.OnHello, id=self.ID_Hello)  

    def OnTaskBarLeftDClick(self, event):  
        if self.frame.IsIconized():  
           self.frame.Iconize(False)  
        if not self.frame.IsShown():  
           self.frame.Show(True)  
        self.frame.Raise()  

    def OnHello(self, event):  
        print 'handle'  

    def CreatePopupMenu(self):  
        pass