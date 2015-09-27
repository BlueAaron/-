# -*- coding: cp936 -*-
import wx
import wx.html
class SketchHelp(wx.Dialog):
    text = '''
<html>
<body bgcolor="#E8E9ED">
<p><b>�����ļ�</b> win�豸�˿���д"None"��linux�豸�˿ڱ�����д
</p>
<p><b>ˢ������</b> ˢ�����ڷ���Ϊ��λ��1-1440���ӷ�Χ
</p>
<p><b>�澯����  </b> ���÷�ΧΪ1-30�� 
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
