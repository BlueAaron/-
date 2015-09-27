# -*- coding: cp936 -*-
import wx
import wx.html
class SketchHelp(wx.Dialog):
    text = '''
<html>
<body bgcolor="#E8E9ED">
<p><b>导入文件</b> win设备端口填写"None"，linux设备端口必须填写
</p>
<p><b>刷新周期</b> 刷新周期分钟为单位，1-1440分钟范围
</p>
<p><b>告警报错  </b> 设置范围为1-30天 
</p>
</body>
</html>
'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'Help DMS',
                          size=(420, 430) )
        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "Ok")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()
