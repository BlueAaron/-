#-*- coding: cp936 -*-

import win32gui
import win32con
import time

class TestTaskbarIcon:
    def __init__(self):
        
        # ע��һ��������
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
        nid = (self.hwnd, # ���
                0, # ����ͼ��ID
                win32gui.NIF_INFO, # ��ʶ
                0, # �ص���ϢID
                0, # ����ͼ����
                "DMSTaskbar", # ͼ���ַ���
                msg, # ������ʾ�ַ���
                0, # ��ʾ����ʾʱ��
                title, # ��ʾ����
                win32gui.NIIF_INFO # ��ʾ�õ���ͼ��
                )
        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, nid)

    def OnDestroy(self):
        win32gui.DestroyWindow(self.hwnd)   #�ٵ�����  
        win32gui.UnregisterClass(self.classAtom,self.hinst)#ע��  
        
    def wndProc(self, hwnd, msg, wParam, lParam):
        if msg == win32con.WM_SIZE: pass
        if msg == win32con.WM_PAINT: pass
        if msg == win32con.WM_CLOSE: pass
        if msg == win32con.WM_DESTROY:
            nid = (self.hwnd, 0)
            win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
 
 
'''
������       : DMSShowAlarmMsg
��������     : ������Ϣ����
�������     : DMSMsgContent(��Ϣ����)
����ֵ       : 
���ú���     :
�����ú���   :
����         : DMS
����         : 2015-3-19
�޸�����     :
�޸�����     :
'''   
def DMSShowAlarmMsg(DMSMsgContent):
    t = TestTaskbarIcon()
    t.showMsg("DMSϵͳ��Ϣ", str(DMSMsgContent))
    time.sleep(5)
    t.OnDestroy()