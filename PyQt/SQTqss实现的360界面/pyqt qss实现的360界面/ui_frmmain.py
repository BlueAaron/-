# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmmain.ui'
#
# Created: Sat Jun 27 22:36:17 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName(_fromUtf8("frmMain"))
        frmMain.resize(900, 595)
        frmMain.setStyleSheet(_fromUtf8("* {\n"
"font-family:\'微软雅黑\';\n"
"color:white;\n"
"}\n"
"\n"
"/*设置背景图片*/\n"
"QMainWindow{\n"
"border-image:url(\":/images/background_mainwnd.png\");\n"
"}\n"
"\n"
"/*ToolButton扁平化*/\n"
"QToolButton[objectName=\"skinToolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"skinToolButton\"]:hover {\n"
"image:url(:/images/skin_hover.png);\n"
"}\n"
"QToolButton[objectName=\"skinToolButton\"]:pressed {\n"
"image:url(:/images/skin_pressed.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"feedToolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"feedToolButton\"]:hover {\n"
"image:url(:/images/feedback_hover.png);\n"
"}\n"
"QToolButton[objectName=\"feedToolButton\"]:pressed {\n"
"image:url(:/images/feedback_pressed.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"menuToolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"menuToolButton\"]:hover {\n"
"image:url(:/images/menu_hover.png);\n"
"}\n"
"QToolButton[objectName=\"menuToolButton\"]:pressed {\n"
"image:url(:/images/menu_pressed.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"minToolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"minToolButton\"]:hover {\n"
"image:url(:/images/min_hover.png);\n"
"}\n"
"QToolButton[objectName=\"minToolButton\"]:pressed {\n"
"image:url(:/images/min_pressed.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"closeToolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closeToolButton\"]:hover {\n"
"image:url(:/images/close_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closeToolButton\"]:pressed {\n"
"image:url(:/images/close_pressed.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"firewallToolButton\"] {\n"
"background-image:url(:/images/firewall_open_normal.png);\n"
"background-repeat:none;\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"firewallToolButton\"]:hover {\n"
"background-image:url(:/images/firewall_open_hover.png);\n"
"\n"
"}\n"
"QToolButton[objectName=\"firewallToolButton\"]:pressed {\n"
"background-image:url(:/images/firewall_open_press.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"guardToolButton\"] {\n"
"background-image:url(:/images/guard_open_normal.png);\n"
"background-repeat:none;\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"guardToolButton\"]:hover {\n"
"background-image:url(:/images/guard_open_hover.png);\n"
"\n"
"}\n"
"QToolButton[objectName=\"guardToolButton\"]:pressed {\n"
"background-image:url(:/images/guard_open_press.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"payinsureToolButton\"] {\n"
"background-image:url(:/images/payinsure_close_normal.png);\n"
"background-repeat:none;\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"payinsureToolButton\"]:hover {\n"
"background-image:url(:/images/payinsure_close_hover.png);\n"
"\n"
"}\n"
"QToolButton[objectName=\"payinsureToolButton\"]:pressed {\n"
"background-image:url(:/images/payinsure_close_press.png);\n"
"}\n"
"\n"
"/*三文本颜色*/\n"
"QToolButton[objectName=\"firewallToolButton\"],QToolButton[objectName=\"guardToolButton\"],QToolButton[objectName=\"payinsureToolButton\"] {\n"
"background-position:10px 10px;\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"\n"
"/*stackedWidget*/\n"
"QStackedWidget {\n"
"background-color:white;\n"
"}\n"
"\n"
"/*立即体检按钮*/\n"
"QToolButton[objectName=\"checkToolButton\"] {\n"
"border-radius:5px;\n"
"}\n"
"QToolButton[objectName=\"checkToolButton\"]:hover {\n"
"image:url(:/images/check_hover.png);\n"
"}\n"
"QToolButton[objectName=\"checkToolButton\"]:pressed {\n"
"image:url(:/images/check_pressed.png);\n"
"}\n"
"\n"
"/**/\n"
"QStackedWidget QToolButton {\n"
"color:black;\n"
"}\n"
"QToolButton::hover{\n"
"border:0px;\n"
"}  \n"
""))
        self.centralWidget = QtGui.QWidget(frmMain)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 110, 900, 485))
        self.stackedWidget.setStyleSheet(_fromUtf8(""))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.line_2 = QtGui.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(668, 120, 231, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.page)
        self.line_3.setGeometry(QtCore.QRect(668, 210, 231, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.page)
        self.line_4.setGeometry(QtCore.QRect(740, 130, 20, 88))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.page)
        self.line_5.setGeometry(QtCore.QRect(820, 130, 20, 88))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.layoutWidget = QtGui.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 110, 536, 120))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setSpacing(50)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/error.png")))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.checkToolButton = QtGui.QToolButton(self.page)
        self.checkToolButton.setGeometry(QtCore.QRect(230, 290, 169, 69))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/check_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkToolButton.setIcon(icon)
        self.checkToolButton.setIconSize(QtCore.QSize(166, 66))
        self.checkToolButton.setObjectName(_fromUtf8("checkToolButton"))
        self.line = QtGui.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(660, 1, 16, 495))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(675, 2, 220, 111))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/register_bg.png")))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.layoutWidget1 = QtGui.QWidget(self.page)
        self.layoutWidget1.setGeometry(QtCore.QRect(670, 230, 231, 261))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolButtonOne = QtGui.QToolButton(self.layoutWidget1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/net_pretext.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonOne.setIcon(icon1)
        self.toolButtonOne.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonOne.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonOne.setAutoRaise(True)
        self.toolButtonOne.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonOne.setObjectName(_fromUtf8("toolButtonOne"))
        self.gridLayout.addWidget(self.toolButtonOne, 0, 0, 1, 1)
        self.toolButtonTwo = QtGui.QToolButton(self.layoutWidget1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/mobile.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonTwo.setIcon(icon2)
        self.toolButtonTwo.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonTwo.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonTwo.setAutoRaise(True)
        self.toolButtonTwo.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonTwo.setObjectName(_fromUtf8("toolButtonTwo"))
        self.gridLayout.addWidget(self.toolButtonTwo, 0, 1, 1, 1)
        self.toolButtonThree = QtGui.QToolButton(self.layoutWidget1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/net_repair.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonThree.setIcon(icon3)
        self.toolButtonThree.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonThree.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonThree.setAutoRaise(True)
        self.toolButtonThree.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonThree.setObjectName(_fromUtf8("toolButtonThree"))
        self.gridLayout.addWidget(self.toolButtonThree, 0, 2, 1, 1)
        self.toolButtonFour = QtGui.QToolButton(self.layoutWidget1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/net_speed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonFour.setIcon(icon4)
        self.toolButtonFour.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonFour.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonFour.setAutoRaise(True)
        self.toolButtonFour.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonFour.setObjectName(_fromUtf8("toolButtonFour"))
        self.gridLayout.addWidget(self.toolButtonFour, 1, 0, 1, 1)
        self.toolButtonFive = QtGui.QToolButton(self.layoutWidget1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/recovery.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonFive.setIcon(icon5)
        self.toolButtonFive.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonFive.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonFive.setAutoRaise(True)
        self.toolButtonFive.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonFive.setObjectName(_fromUtf8("toolButtonFive"))
        self.gridLayout.addWidget(self.toolButtonFive, 1, 1, 1, 1)
        self.toolButtonSix = QtGui.QToolButton(self.layoutWidget1)
        self.toolButtonSix.setIcon(icon1)
        self.toolButtonSix.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonSix.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonSix.setAutoRaise(True)
        self.toolButtonSix.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonSix.setObjectName(_fromUtf8("toolButtonSix"))
        self.gridLayout.addWidget(self.toolButtonSix, 1, 2, 1, 1)
        self.toolButtonSeven = QtGui.QToolButton(self.layoutWidget1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/desktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonSeven.setIcon(icon6)
        self.toolButtonSeven.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonSeven.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonSeven.setAutoRaise(True)
        self.toolButtonSeven.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonSeven.setObjectName(_fromUtf8("toolButtonSeven"))
        self.gridLayout.addWidget(self.toolButtonSeven, 2, 0, 1, 1)
        self.toolButtonEight = QtGui.QToolButton(self.layoutWidget1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/game_box.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonEight.setIcon(icon7)
        self.toolButtonEight.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonEight.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonEight.setAutoRaise(True)
        self.toolButtonEight.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonEight.setObjectName(_fromUtf8("toolButtonEight"))
        self.gridLayout.addWidget(self.toolButtonEight, 2, 1, 1, 1)
        self.toolButtonNine = QtGui.QToolButton(self.layoutWidget1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/first_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonNine.setIcon(icon8)
        self.toolButtonNine.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonNine.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonNine.setAutoRaise(True)
        self.toolButtonNine.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonNine.setObjectName(_fromUtf8("toolButtonNine"))
        self.gridLayout.addWidget(self.toolButtonNine, 2, 2, 1, 1)
        self.firewallToolButton = QtGui.QToolButton(self.page)
        self.firewallToolButton.setGeometry(QtCore.QRect(680, 140, 59, 111))
        self.firewallToolButton.setMinimumSize(QtCore.QSize(59, 111))
        self.firewallToolButton.setMaximumSize(QtCore.QSize(59, 111))
        self.firewallToolButton.setIconSize(QtCore.QSize(50, 60))
        self.firewallToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.firewallToolButton.setAutoRaise(True)
        self.firewallToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.firewallToolButton.setObjectName(_fromUtf8("firewallToolButton"))
        self.guardToolButton = QtGui.QToolButton(self.page)
        self.guardToolButton.setGeometry(QtCore.QRect(760, 140, 59, 111))
        self.guardToolButton.setMinimumSize(QtCore.QSize(59, 111))
        self.guardToolButton.setMaximumSize(QtCore.QSize(59, 111))
        self.guardToolButton.setIconSize(QtCore.QSize(50, 60))
        self.guardToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.guardToolButton.setAutoRaise(True)
        self.guardToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.guardToolButton.setObjectName(_fromUtf8("guardToolButton"))
        self.payinsureToolButton = QtGui.QToolButton(self.page)
        self.payinsureToolButton.setGeometry(QtCore.QRect(840, 140, 59, 111))
        self.payinsureToolButton.setMinimumSize(QtCore.QSize(59, 111))
        self.payinsureToolButton.setMaximumSize(QtCore.QSize(59, 111))
        self.payinsureToolButton.setIconSize(QtCore.QSize(50, 60))
        self.payinsureToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.payinsureToolButton.setAutoRaise(True)
        self.payinsureToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.payinsureToolButton.setObjectName(_fromUtf8("payinsureToolButton"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_7 = QtGui.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 127);"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_8 = QtGui.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_8.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0)"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.label_9 = QtGui.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_9.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127)"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.label_10 = QtGui.QLabel(self.page_5)
        self.label_10.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 127)"))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.label_11 = QtGui.QLabel(self.page_6)
        self.label_11.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_11.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 127)"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.label_12 = QtGui.QLabel(self.page_7)
        self.label_12.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_12.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255)"))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.label_13 = QtGui.QLabel(self.page_8)
        self.label_13.setGeometry(QtCore.QRect(210, 60, 501, 361))
        self.label_13.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 255)"))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.stackedWidget.addWidget(self.page_8)
        self.layoutWidget2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(-8, 30, 911, 80))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(10, -1, 50, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkToolButton_2 = QtGui.QToolButton(self.layoutWidget2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_Examine.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkToolButton_2.setIcon(icon9)
        self.checkToolButton_2.setIconSize(QtCore.QSize(48, 48))
        self.checkToolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.checkToolButton_2.setAutoRaise(True)
        self.checkToolButton_2.setArrowType(QtCore.Qt.NoArrow)
        self.checkToolButton_2.setObjectName(_fromUtf8("checkToolButton_2"))
        self.horizontalLayout.addWidget(self.checkToolButton_2)
        self.killToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_dsmain.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.killToolButton.setIcon(icon10)
        self.killToolButton.setIconSize(QtCore.QSize(48, 48))
        self.killToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.killToolButton.setAutoRaise(True)
        self.killToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.killToolButton.setObjectName(_fromUtf8("killToolButton"))
        self.horizontalLayout.addWidget(self.killToolButton)
        self.fixToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_SysRepair.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fixToolButton.setIcon(icon11)
        self.fixToolButton.setIconSize(QtCore.QSize(48, 48))
        self.fixToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fixToolButton.setAutoRaise(True)
        self.fixToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.fixToolButton.setObjectName(_fromUtf8("fixToolButton"))
        self.horizontalLayout.addWidget(self.fixToolButton)
        self.rabToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_TraceCleaner.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rabToolButton.setIcon(icon12)
        self.rabToolButton.setIconSize(QtCore.QSize(48, 48))
        self.rabToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.rabToolButton.setAutoRaise(True)
        self.rabToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.rabToolButton.setObjectName(_fromUtf8("rabToolButton"))
        self.horizontalLayout.addWidget(self.rabToolButton)
        self.opToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_SpeedupOpt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opToolButton.setIcon(icon13)
        self.opToolButton.setIconSize(QtCore.QSize(48, 48))
        self.opToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.opToolButton.setAutoRaise(True)
        self.opToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.opToolButton.setObjectName(_fromUtf8("opToolButton"))
        self.horizontalLayout.addWidget(self.opToolButton)
        self.exToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_expert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exToolButton.setIcon(icon14)
        self.exToolButton.setIconSize(QtCore.QSize(48, 48))
        self.exToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.exToolButton.setAutoRaise(True)
        self.exToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.exToolButton.setObjectName(_fromUtf8("exToolButton"))
        self.horizontalLayout.addWidget(self.exToolButton)
        self.mzToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_diannaomenzhen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mzToolButton.setIcon(icon15)
        self.mzToolButton.setIconSize(QtCore.QSize(48, 48))
        self.mzToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mzToolButton.setAutoRaise(True)
        self.mzToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.mzToolButton.setObjectName(_fromUtf8("mzToolButton"))
        self.horizontalLayout.addWidget(self.mzToolButton)
        self.gjToolButton = QtGui.QToolButton(self.layoutWidget2)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ico_softmgr.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gjToolButton.setIcon(icon16)
        self.gjToolButton.setIconSize(QtCore.QSize(48, 48))
        self.gjToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.gjToolButton.setAutoRaise(True)
        self.gjToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.gjToolButton.setObjectName(_fromUtf8("gjToolButton"))
        self.horizontalLayout.addWidget(self.gjToolButton)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/logo.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 127, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(700, 2, 26, 30))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/medal.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.skinToolButton = QtGui.QToolButton(self.centralWidget)
        self.skinToolButton.setGeometry(QtCore.QRect(749, 0, 30, 28))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/skin_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skinToolButton.setIcon(icon17)
        self.skinToolButton.setIconSize(QtCore.QSize(27, 25))
        self.skinToolButton.setObjectName(_fromUtf8("skinToolButton"))
        self.feedToolButton = QtGui.QToolButton(self.centralWidget)
        self.feedToolButton.setGeometry(QtCore.QRect(779, 0, 30, 25))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/feedback_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.feedToolButton.setIcon(icon18)
        self.feedToolButton.setIconSize(QtCore.QSize(27, 22))
        self.feedToolButton.setObjectName(_fromUtf8("feedToolButton"))
        self.menuToolButton = QtGui.QToolButton(self.centralWidget)
        self.menuToolButton.setGeometry(QtCore.QRect(809, 0, 30, 25))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/menu_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuToolButton.setIcon(icon19)
        self.menuToolButton.setIconSize(QtCore.QSize(27, 22))
        self.menuToolButton.setObjectName(_fromUtf8("menuToolButton"))
        self.minToolButton = QtGui.QToolButton(self.centralWidget)
        self.minToolButton.setGeometry(QtCore.QRect(839, 0, 30, 25))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/min_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minToolButton.setIcon(icon20)
        self.minToolButton.setIconSize(QtCore.QSize(27, 22))
        self.minToolButton.setObjectName(_fromUtf8("minToolButton"))
        self.closeToolButton = QtGui.QToolButton(self.centralWidget)
        self.closeToolButton.setGeometry(QtCore.QRect(869, 0, 30, 25))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeToolButton.setIcon(icon21)
        self.closeToolButton.setIconSize(QtCore.QSize(27, 22))
        self.closeToolButton.setObjectName(_fromUtf8("closeToolButton"))
        frmMain.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmMain)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(_translate("frmMain", "MainWindow", None))
        self.label_5.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">您的电脑已经 </span><span style=\" font-size:14pt; color:#ff0000;\">24 </span><span style=\" font-size:12pt; color:#000000;\">天没有体检，建议立即体检！</span><br/></p><p><span style=\" font-size:10pt; color:#727272;\">系统可能已经存在大量风险，安全性和性能都在急速下降，</span><br/><span style=\" font-size:10pt; color:#727272;\">建议您每天坚持电脑体检，提高电脑的安全和性能</span></p></body></html>", None))
        self.checkToolButton.setText(_translate("frmMain", "...", None))
        self.toolButtonOne.setText(_translate("frmMain", "1", None))
        self.toolButtonTwo.setText(_translate("frmMain", "2", None))
        self.toolButtonThree.setText(_translate("frmMain", "3", None))
        self.toolButtonFour.setText(_translate("frmMain", "4", None))
        self.toolButtonFive.setText(_translate("frmMain", "5", None))
        self.toolButtonSix.setText(_translate("frmMain", "6", None))
        self.toolButtonSeven.setText(_translate("frmMain", "7", None))
        self.toolButtonEight.setText(_translate("frmMain", "8", None))
        self.toolButtonNine.setText(_translate("frmMain", "9", None))
        self.firewallToolButton.setText(_translate("frmMain", "木马防火墙", None))
        self.guardToolButton.setText(_translate("frmMain", "360保镖", None))
        self.payinsureToolButton.setText(_translate("frmMain", "网购先赔", None))
        self.label_7.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">木马查杀</span></p></body></html>", None))
        self.label_8.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">系统修复</span></p></body></html>", None))
        self.label_9.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">垃圾清理</span></p></body></html>", None))
        self.label_10.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">优化加速</span></p></body></html>", None))
        self.label_11.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">电脑专家</span></p></body></html>", None))
        self.label_12.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">电脑门诊</span></p></body></html>", None))
        self.label_13.setText(_translate("frmMain", "<html><head/><body><p><span style=\" font-size:36pt;\">软件管家</span></p></body></html>", None))
        self.checkToolButton_2.setText(_translate("frmMain", "电脑体检", None))
        self.killToolButton.setText(_translate("frmMain", "木马查杀", None))
        self.fixToolButton.setText(_translate("frmMain", "系统修复", None))
        self.rabToolButton.setText(_translate("frmMain", "垃圾清理", None))
        self.opToolButton.setText(_translate("frmMain", "优化加速", None))
        self.exToolButton.setText(_translate("frmMain", "电脑专家", None))
        self.mzToolButton.setText(_translate("frmMain", "电脑门诊", None))
        self.gjToolButton.setText(_translate("frmMain", "软件管家", None))
        self.label_2.setText(_translate("frmMain", "360安全卫士9.2 By Ysx", None))
        self.skinToolButton.setText(_translate("frmMain", "...", None))
        self.feedToolButton.setText(_translate("frmMain", "...", None))
        self.menuToolButton.setText(_translate("frmMain", "...", None))
        self.minToolButton.setText(_translate("frmMain", "...", None))
        self.closeToolButton.setText(_translate("frmMain", "...", None))

import res_rc
