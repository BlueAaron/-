#-*- coding: cp936 -*-

import win32gui
import win32con
import time

class TestTaskbarIcon:
    def __init__(self):
        
        # 注册一个窗口类
        self.wc = win32gui.WNDCLASS()
        self.hinst = self.wc.hInstance = win32gui.GetModuleHandle(None)
        self.wc.lpszClassName = "DMSTaskbar"
        self.wc.lpfnWndProc = self.wndProc
        self.classAtom = win32gui.RegisterClass(self.wc)
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow( self.classAtom, "DMSTaskbar", style,
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                0, 0, self.hinst, None)
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE  
        hicon = win32gui.LoadImage(self.hinst, 'logo.ico', win32con.IMAGE_ICON, 0, 0, icon_flags)  
        nid = (self.hwnd, 0, win32gui.NIF_ICON, win32con.WM_USER+20, hicon, "DMSTaskbar")
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        

    def showMsg(self, title, msg):
        nid = (self.hwnd, # 句柄
                0, # 托盘图标ID
                win32gui.NIF_INFO, # 标识
                0, # 回调消息ID
                0, # 托盘图标句柄
                "DMSTaskbar", # 图标字符串
                msg, # 气球提示字符串
                0, # 提示的显示时间
                title, # 提示标题
                win32gui.NIIF_INFO # 提示用到的图标
                )
        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, nid)

    def OnDestroy(self):
        win32gui.DestroyWindow(self.hwnd)   #毁掉托盘  
        win32gui.UnregisterClass(self.classAtom,self.hinst)#注销  
        
    def wndProc(self, hwnd, msg, wParam, lParam):
        if msg == win32con.WM_SIZE: pass
        if msg == win32con.WM_PAINT: pass
        if msg == win32con.WM_CLOSE: pass
        if msg == win32con.WM_DESTROY:
            nid = (self.hwnd, 0)
            win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
 
 
'''
函数名       : DMSShowAlarmMsg
功能描述     : 弹出消息气泡
输入参数     : DMSMsgContent(消息内容)
返回值       : 
调用函数     :
被调用函数   :
作者         : DMS
日期         : 2015-3-19
修改日期     :
修改内容     :
'''   
def DMSShowAlarmMsg(DMSMsgContent):
    t = TestTaskbarIcon()
    t.showMsg("DMS系统消息", str(DMSMsgContent))
    time.sleep(5)
    t.OnDestroy()