# -*- coding: cp936 -*-
import wx
import wx.html
class SketchAbout(wx.Dialog):
    text = '''
<html>
<body bgcolor="#E8E9ED">
<center><table bgcolor="#00697F" width="100%" cellspacing="0"
cellpadding="0" border="1">
<tr>
<td align="center"><h1>I Love Python!</h1></td>
</tr>
</table>
</center>
<p><b>版本</b> V1.0
</p>
<p><b>开发</b> 王亭亭/吴曙光/叶飞
</p>
<p><b>团队  </b> No.1 <a href="#" color='black'>工具链接</a>
</p>
</p>
<p><img src="montain.gif" width="380" height="170" />
</p>
</body>
</html>
'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About DMS',
                          size=(420, 430) )
        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "Ok")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()
