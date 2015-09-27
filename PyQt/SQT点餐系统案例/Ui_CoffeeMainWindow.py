# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\SQT点餐系统案例.ui'
#
# Created: Sun May 10 02:02:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Ui_SysFrame import * 
from Ui_OpenDialog import *
from Ui_CheckOutDialog import *
from Ui_AddOrDelete import *
from Ui_Query import *
import CoffeeManage_rc
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Counter(QtGui.QListWidgetItem):
    def __init__(self, iCon, Text):
        super(Counter, self).__init__(iCon, Text)
        #初始化为空闲状态 0 忙碌状态为1
        self.Status = 0 
        self.No=-1
        self.MenuList = {}
        self.Consumption = 25
        self.ToolTipText = ''
        
    def RefreshToolTip(self):
        ToolTipText = ''
        if self.Status == 0 :
            ToolTipText = ToolTipText + '状态:空闲' + '\n\n'
        elif self.Status == 1:
            ToolTipText = ToolTipText + '状态:忙碌' + '\n\n'
        if self.MenuList:
            for Item in self.MenuList:
                ToolTipText = ToolTipText + self.MenuList[Item] + '\n\n'
        if self.Status == 1:
            ToolTipText = ToolTipText + '总消费:' + str(self.Consumption) +'\n'
        self.setToolTip("<html><head/><body><p>"+ToolTipText+"</p></body></html>")
            
    
class Ui_CoffeeMainWindow(QtGui.QMainWindow):
    MenuItem = ['美式咖啡 30RMB', '拿铁 30RMB','卡布奇诺 30RMB','香草奶昔 30RMB','草莓奶昔 30RMB','缤纷果汁 30RMB','伯爵红茶 30RMB'\
    ,'至尊奶茶 30RMB','炸薯条 20RMB','炸鸡块 20RMB']
    def keyPressEvent(self, event):
        if event.key()==QtCore.Qt.Key_Tab and event.modifers()==QtCore.Qt.AltModifier:
            pass
        if event.key() == QtCore.Qt.Key_Escape:
            reply=QtGui.QMessageBox.question(None,'温馨提示','请问是否退出如此高级的咖啡室管理系统!',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.close()
                exit()
            else:
                QtGui.QMessageBox.warning(None,'提示','你的选择会让你今生无憾!',QtGui.QMessageBox.Yes)
    
    def setupUi(self, MainWindow):
        #餐台对象字典
        self.CounterDict = {}
        #餐台对象列表
        self.CounterList =[]
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("#MainWindow{border-image: url(:/BroundBcak/背景.jpg);}"))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 141, 91))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{border-image: url(:/PushButton/开台-普通.jpg);}\n"
"QPushButton:hover{border-image: url(:/PushButton/开台-停留.jpg);}\n"
"QPushButton:pressed{border-image: url(:/PushButton/开台-点击.jpg);}"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 30, 141, 91))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{border-image: url(:/PushButton/添加或删除产品-普通.jpg);}\n"
"QPushButton:hover{border-image: url(:/PushButton/添加或删除产品-停留.jpg);}\n"
"QPushButton:pressed{border-image: url(:/PushButton/添加或删除产品-点击.jpg);}\n"
""))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 30, 141, 91))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{border-image: url(:/PushButton/查看状态-普通.jpg);}\n"
"QPushButton:hover{border-image: url(:/PushButton/查看状态-停留.jpg);}\n"
"QPushButton:pressed{border-image: url(:/PushButton/查看状态-点击.jpg);}\n"
""))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 30, 141, 91))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{border-image: url(:/PushButton/结账-普通.jpg);}\n"
"QPushButton:hover{border-image: url(:/PushButton/结账-停留.jpg);}\n"
"QPushButton:pressed{border-image: url(:/PushButton/结账-点击.jpg);}\n"
""))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 130, 141, 41))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(680, 60, 80, 50))
        self.toolButton.setStyleSheet('background-color: rgb(200, 115, 65, 100);')
        self.toolButton.setText('停止')
        self.toolButton.show()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("幼圆"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.ListView = QtGui.QListWidget(MainWindow)
        self.ListView.setGeometry(QtCore.QRect(200, 200, 530, 380))
        self.ListView.setObjectName(_fromUtf8("ListView"))
        self.ListView.setViewMode(QtGui.QListView.IconMode)
        self.ListView.setIconSize(QtCore.QSize(100, 100))
        self.ListView.setMovement(QtGui.QListView.Static)
        self.ListView.setSpacing(10)
        self.ListView.setStyleSheet(_fromUtf8("background-color: rgba(85, 0, 255, 30);"))
        listpixmap = QtGui.QPixmap(':/Status/状态空闲.jpg')
        ListCon = QtGui.QIcon(listpixmap.scaled(QtCore.QSize(200, 200)))
        ListItem  = Counter(ListCon, 'No 1')
        ListItem.No = 1
        self.CounterDict['1'] = ListItem
        self.CounterList.append(ListItem)
        ListItem1 = Counter(ListCon, 'No 2')
        ListItem1.No = 2
        self.CounterDict['2'] = ListItem1
        self.CounterList.append(ListItem1)
        ListItem2 = Counter(ListCon, 'No 3')
        ListItem2.No = 3
        self.CounterDict['3'] = ListItem2
        self.CounterList.append(ListItem2)
        ListItem3 = Counter(ListCon, 'No 4')        
        ListItem3.No = 4
        self.CounterDict['4'] = ListItem3
        self.CounterList.append(ListItem3)
        ListItem4 = Counter(ListCon, 'No 5')
        ListItem4.No = 5
        self.CounterDict['5'] = ListItem4
        self.CounterList.append(ListItem4)
        ListItem5 = Counter(ListCon, 'No 6')
        ListItem5.No = 6
        self.CounterDict['6'] = ListItem5
        self.CounterList.append(ListItem5)
        ListItem6 = Counter(ListCon, 'No 7')        
        ListItem6.No = 7
        self.CounterDict['7'] = ListItem6
        self.CounterList.append(ListItem6)
        ListItem7 = Counter(ListCon, 'No 8')
        ListItem7.No = 8
        self.CounterDict['8'] = ListItem7
        self.CounterList.append(ListItem7)
        ListItem8 = Counter(ListCon, 'No 9')
        ListItem8.No = 9
        self.CounterDict['9'] = ListItem8
        self.CounterList.append(ListItem8)
#        ListItem.setSizeHint(QtCore.QSize(200, 230))
#        ListItem1.setSizeHint(QtCore.QSize(200, 230))
        self.ListView.addItem(ListItem)
        self.ListView.addItem(ListItem1)
        self.ListView.addItem(ListItem2)
        self.ListView.addItem(ListItem3)
        self.ListView.addItem(ListItem4)
        self.ListView.addItem(ListItem5)
        self.ListView.addItem(ListItem6)
        self.ListView.addItem(ListItem7)
        self.ListView.addItem(ListItem8)
        
        self.CoffeeSound = QtGui.QSound('./安妮的仙境.wav')
        self.CoffeeSoundFlag = 1
        self.CoffeeSound.play()
        self.CoffeeSound.setLoops(-1)
        
        for Item in self.CounterList:
            Item.RefreshToolTip()
        #系统信息栏
        self.SysFrame = QtGui.QWidget(self)
        self.SysFrame.setGeometry(QtCore.QRect(20, 200, 150, 380))
        self.SysFrame.setStyleSheet(_fromUtf8("background-color: rgba(85, 0, 255, 30);"))
        self.SysFrameStyle = Ui_Form()
        self.SysFrameStyle.setupUi(self.SysFrame)
        #self.ListView.itemDoubleClicked.connect(self.DoubleClicked)
        
        self.pushButton.clicked.connect(self.Open)
        self.pushButton_2.clicked.connect(self.AddOrDelete)
        self.pushButton_3.clicked.connect(self.Query)
        self.pushButton_4.clicked.connect(self.CheckOut)
        self.toolButton.clicked.connect(self.PlayOrStop)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def DoubleClicked(self, Item):
        Text = Item.text() + '被你抓到了尽情的虐它吧'
        QtGui.QMessageBox.warning(None,'提示',Text,QtGui.QMessageBox.Yes)

    def PlayOrStop(self):
        if self.CoffeeSoundFlag  ==  1:
            self.CoffeeSound.stop()
            self.CoffeeSoundFlag = 0
            self.toolButton.setText('播放')
        elif self.CoffeeSoundFlag == 0:
            self.CoffeeSound.play()
            self.CoffeeSound.setLoops(-1)
            self.CoffeeSoundFlag = 1
            self.toolButton.setText('停止')
        
    def CheckOut(self):
        CheckOutDialog = Ui_CheckOutDialog(self)
        CheckOutDialog.setupUi(self)
        CheckOutDialog.show()
        
    def Open(self):
        OpenDialog = Ui_OpenDialog(self)
        OpenDialog.setupUi(self)
        OpenDialog.setWindowTitle('开台')
        OpenDialog.show()
        
    def AddOrDelete(self):
        AddOrDeleteDialog = Ui_AddOrDeleteDialog(self)
        AddOrDeleteDialog.setupUi(self)
        AddOrDeleteDialog.setWindowTitle('添加/删除餐饮')
        AddOrDeleteDialog.show()
        
    def Query(self):
        QueryDialog = Ui_QueryDialog(self)
        QueryDialog.setupUi(self)
        QueryDialog.show()
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "开台", None))
        self.label_2.setText(_translate("MainWindow", "添加/删除餐饮", None))
        self.label_3.setText(_translate("MainWindow", "查看状态", None))
        self.label_4.setText(_translate("MainWindow", "结账", None))





