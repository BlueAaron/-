# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\pyqt\ftp\main.ui'
#
# Created: Sun Dec 16 17:14:34 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 585)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/qtdemo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.start_upload = QtGui.QPushButton(self.centralWidget)
        self.start_upload.setObjectName(_fromUtf8("start_upload"))
        self.horizontalLayout_2.addWidget(self.start_upload)
        self.stop_upload = QtGui.QPushButton(self.centralWidget)
        self.stop_upload.setEnabled(False)
        self.stop_upload.setObjectName(_fromUtf8("stop_upload"))
        self.horizontalLayout_2.addWidget(self.stop_upload)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.file_list = FileList(self.centralWidget)
        self.file_list.setMinimumSize(QtCore.QSize(232, 0))
        self.file_list.setMaximumSize(QtCore.QSize(16777215, 300))
        self.file_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.file_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.file_list.setDragEnabled(False)
        self.file_list.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.file_list.setAlternatingRowColors(True)
        self.file_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.file_list.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.file_list.setObjectName(_fromUtf8("file_list"))
        self.file_list.setColumnCount(3)
        self.file_list.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(2, item)
        self.file_list.verticalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.file_list)
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.upload_solution = QtGui.QComboBox(self.centralWidget)
        self.upload_solution.setObjectName(_fromUtf8("upload_solution"))
        self.horizontalLayout_4.addWidget(self.upload_solution)
        self.add_solution = QtGui.QToolButton(self.centralWidget)
        self.add_solution.setMinimumSize(QtCore.QSize(22, 22))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icon/0949090.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_solution.setIcon(icon1)
        self.add_solution.setObjectName(_fromUtf8("add_solution"))
        self.horizontalLayout_4.addWidget(self.add_solution)
        self.remove_solution = QtGui.QToolButton(self.centralWidget)
        self.remove_solution.setEnabled(False)
        self.remove_solution.setMinimumSize(QtCore.QSize(22, 22))
        self.remove_solution.setMaximumSize(QtCore.QSize(22, 22))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icon/0949091.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_solution.setIcon(icon2)
        self.remove_solution.setObjectName(_fromUtf8("remove_solution"))
        self.horizontalLayout_4.addWidget(self.remove_solution)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.selected_servers = QtGui.QTableWidget(self.centralWidget)
        self.selected_servers.setMaximumSize(QtCore.QSize(300, 16777215))
        self.selected_servers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.selected_servers.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.selected_servers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.selected_servers.setObjectName(_fromUtf8("selected_servers"))
        self.selected_servers.setColumnCount(4)
        self.selected_servers.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.selected_servers.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.selected_servers.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.selected_servers.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.selected_servers.setHorizontalHeaderItem(3, item)
        self.verticalLayout_5.addWidget(self.selected_servers)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.move2left = QtGui.QPushButton(self.centralWidget)
        self.move2left.setEnabled(False)
        self.move2left.setMaximumSize(QtCore.QSize(60, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icon/09490922.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move2left.setIcon(icon3)
        self.move2left.setObjectName(_fromUtf8("move2left"))
        self.verticalLayout_3.addWidget(self.move2left)
        self.move2right = QtGui.QPushButton(self.centralWidget)
        self.move2right.setEnabled(False)
        self.move2right.setMaximumSize(QtCore.QSize(60, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icon/09490920.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move2right.setIcon(icon4)
        self.move2right.setObjectName(_fromUtf8("move2right"))
        self.verticalLayout_3.addWidget(self.move2right)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.platform = QtGui.QComboBox(self.centralWidget)
        self.platform.setObjectName(_fromUtf8("platform"))
        self.horizontalLayout_3.addWidget(self.platform)
        self.refresh_server_list = QtGui.QPushButton(self.centralWidget)
        self.refresh_server_list.setMaximumSize(QtCore.QSize(60, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icon/09490938.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_server_list.setIcon(icon5)
        self.refresh_server_list.setObjectName(_fromUtf8("refresh_server_list"))
        self.horizontalLayout_3.addWidget(self.refresh_server_list)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.server_list = QtGui.QTableWidget(self.centralWidget)
        self.server_list.setMaximumSize(QtCore.QSize(300, 16777215))
        self.server_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.server_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.server_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.server_list.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.server_list.setObjectName(_fromUtf8("server_list"))
        self.server_list.setColumnCount(4)
        self.server_list.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.server_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.server_list.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.server_list.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.server_list.setHorizontalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.server_list)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_operation = QtGui.QMenu(self.menuBar)
        self.menu_operation.setObjectName(_fromUtf8("menu_operation"))
        self.menu_help = QtGui.QMenu(self.menuBar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menu_server_manage = QtGui.QAction(MainWindow)
        self.menu_server_manage.setObjectName(_fromUtf8("menu_server_manage"))
        self.menu_exit = QtGui.QAction(MainWindow)
        self.menu_exit.setObjectName(_fromUtf8("menu_exit"))
        self.menu_about = QtGui.QAction(MainWindow)
        self.menu_about.setObjectName(_fromUtf8("menu_about"))
        self.action_add_server = QtGui.QAction(MainWindow)
        self.action_add_server.setIcon(icon1)
        self.action_add_server.setObjectName(_fromUtf8("action_add_server"))
        self.action_edit_server = QtGui.QAction(MainWindow)
        self.action_edit_server.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icon/09490944.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_server.setIcon(icon6)
        self.action_edit_server.setObjectName(_fromUtf8("action_edit_server"))
        self.action_copy_server = QtGui.QAction(MainWindow)
        self.action_copy_server.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icon/0949092.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_copy_server.setIcon(icon7)
        self.action_copy_server.setObjectName(_fromUtf8("action_copy_server"))
        self.action_delete_server = QtGui.QAction(MainWindow)
        self.action_delete_server.setEnabled(False)
        self.action_delete_server.setIcon(icon2)
        self.action_delete_server.setObjectName(_fromUtf8("action_delete_server"))
        self.action_move2left = QtGui.QAction(MainWindow)
        self.action_move2left.setEnabled(False)
        self.action_move2left.setIcon(icon3)
        self.action_move2left.setObjectName(_fromUtf8("action_move2left"))
        self.menu_clear_log = QtGui.QAction(MainWindow)
        self.menu_clear_log.setObjectName(_fromUtf8("menu_clear_log"))
        self.menu_operation.addAction(self.menu_clear_log)
        self.menu_operation.addSeparator()
        self.menu_operation.addAction(self.menu_exit)
        self.menu_help.addAction(self.menu_about)
        self.menuBar.addAction(self.menu_operation.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.menu_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FTP批量上传工具", None, QtGui.QApplication.UnicodeUTF8))
        self.start_upload.setText(QtGui.QApplication.translate("MainWindow", "上传", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_upload.setText(QtGui.QApplication.translate("MainWindow", "停止", None, QtGui.QApplication.UnicodeUTF8))
        item = self.file_list.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "文件", None, QtGui.QApplication.UnicodeUTF8))
        item = self.file_list.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "大小", None, QtGui.QApplication.UnicodeUTF8))
        item = self.file_list.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "修改日期", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">欢迎使用FTP批量上传工具。</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "上传方案：", None, QtGui.QApplication.UnicodeUTF8))
        self.add_solution.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>把当前上传服务器列表添加到上传方案中</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.add_solution.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_solution.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>删除当前选择的上传方案</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_solution.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        item = self.selected_servers.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        item = self.selected_servers.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "平台", None, QtGui.QApplication.UnicodeUTF8))
        item = self.selected_servers.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "服务器", None, QtGui.QApplication.UnicodeUTF8))
        item = self.selected_servers.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "路径", None, QtGui.QApplication.UnicodeUTF8))
        self.move2left.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>添加到上传服务器列表中</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.move2left.setText(QtGui.QApplication.translate("MainWindow", "左移", None, QtGui.QApplication.UnicodeUTF8))
        self.move2right.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>从上传服务器列表中删除</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.move2right.setText(QtGui.QApplication.translate("MainWindow", "右移", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "平台：", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_server_list.setText(QtGui.QApplication.translate("MainWindow", "刷 新", None, QtGui.QApplication.UnicodeUTF8))
        item = self.server_list.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        item = self.server_list.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "平台", None, QtGui.QApplication.UnicodeUTF8))
        item = self.server_list.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "服务器", None, QtGui.QApplication.UnicodeUTF8))
        item = self.server_list.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "路径", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_operation.setTitle(QtGui.QApplication.translate("MainWindow", "操作(&O)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_help.setTitle(QtGui.QApplication.translate("MainWindow", "帮助(&H)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_server_manage.setText(QtGui.QApplication.translate("MainWindow", "管理服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_exit.setText(QtGui.QApplication.translate("MainWindow", "退出(&X)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_about.setText(QtGui.QApplication.translate("MainWindow", "关于(&A)", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add_server.setText(QtGui.QApplication.translate("MainWindow", "添加", None, QtGui.QApplication.UnicodeUTF8))
        self.action_edit_server.setText(QtGui.QApplication.translate("MainWindow", "编辑", None, QtGui.QApplication.UnicodeUTF8))
        self.action_copy_server.setText(QtGui.QApplication.translate("MainWindow", "复制", None, QtGui.QApplication.UnicodeUTF8))
        self.action_delete_server.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.action_move2left.setText(QtGui.QApplication.translate("MainWindow", "左移", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_clear_log.setText(QtGui.QApplication.translate("MainWindow", "清空日志(&C)", None, QtGui.QApplication.UnicodeUTF8))

from control.filelist import FileList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

