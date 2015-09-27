# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonAll\PythonPro\SQT点餐系统案例\AddOrDelete.ui'
#
# Created: Sat May 23 22:18:44 2015
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

class Ui_AddOrDeleteDialog(QtGui.QDialog):
    def setupUi(self, MainWindow):
        self.setObjectName(_fromUtf8("self"))
        self.resize(544, 445)
        self.MainWindow=MainWindow
        self.MenuItem = MainWindow.MenuItem
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(170, 90, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(240, 90, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 181, 20))
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(80, 210, 181, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        for Item in self.MenuItem:
            self.comboBox.addItem(Item)
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 210, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(280, 210, 54, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 330, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.Add)
        self.pushButton_2.clicked.connect(self.Delete)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "添加/删除餐饮", None))
        self.label.setText(_translate("Dialog", "台号", None))
        self.label_2.setText(_translate("Dialog", "产品", None))
        self.label_3.setText(_translate("Dialog", "数量", None))
        self.pushButton.setText(_translate("Dialog", "添加", None))
        self.pushButton_2.setText(_translate("Dialog", "删除", None))

    def Add(self):
        if self.lineEdit.text():
            if self.lineEdit_2.text() and int(self.lineEdit_2.text())>0:
                if self.MainWindow.CounterDict[self.lineEdit.text()].Status:
                    if self.comboBox.currentText().split(' ')[0] in self.MainWindow.CounterDict[self.lineEdit.text()].MenuList:
                        NewNum = int(self.lineEdit_2.text())+int(self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]].split('*')[1])
                        self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]]=self.comboBox.currentText()+'*'+str(NewNum)
                        QtGui.QMessageBox.warning(None,'提示','已经添加餐饮'+self.comboBox.currentText().split(' ')[0]+'*'+self.lineEdit_2.text(),QtGui.QMessageBox.Yes)
                        self.MainWindow.CounterDict[self.lineEdit.text()].Consumption = self.MainWindow.CounterDict[self.lineEdit.text()].Consumption + \
                        int(self.comboBox.currentText().split(' ')[1].split('R')[0])*int(self.lineEdit_2.text())
                        self.MainWindow.CounterDict[self.lineEdit.text()].RefreshToolTip()
                    else:
                        self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]]=self.comboBox.currentText()+'*'+self.lineEdit_2.text()
                        QtGui.QMessageBox.warning(None,'提示','已经添加新餐饮'+self.comboBox.currentText().split(' ')[0]+'*'+self.lineEdit_2.text(),QtGui.QMessageBox.Yes)
                        self.MainWindow.CounterDict[self.lineEdit.text()].Consumption = self.MainWindow.CounterDict[self.lineEdit.text()].Consumption + \
                        int(self.comboBox.currentText().split(' ')[1].split('R')[0])*int(self.lineEdit_2.text())
                        self.MainWindow.CounterDict[self.lineEdit.text()].RefreshToolTip()
                else:
                    QtGui.QMessageBox.warning(None,'提示','未开台无法添加删除餐饮',QtGui.QMessageBox.Yes)
            else:
                QtGui.QMessageBox.warning(None,'提示','数量异常无法添加',QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.warning(None,'提示','台号为空无法添加',QtGui.QMessageBox.Yes)
    
    def Delete(self):
        if self.lineEdit.text():
            if self.lineEdit_2.text() and int(self.lineEdit_2.text())>0:
                if self.MainWindow.CounterDict[self.lineEdit.text()].Status:
                    if self.comboBox.currentText().split(' ')[0] in self.MainWindow.CounterDict[self.lineEdit.text()].MenuList:
                        NewNum = int(self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]].split('*')[1])-int(self.lineEdit_2.text())
                        if NewNum > 0:
                            self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]]=self.comboBox.currentText()+'*'+str(NewNum)
                            QtGui.QMessageBox.warning(None,'提示','已经减少餐饮'+self.comboBox.currentText().split(' ')[0]+'*'+self.lineEdit_2.text(),QtGui.QMessageBox.Yes)
                            
                            self.MainWindow.CounterDict[self.lineEdit.text()].Consumption=self.MainWindow.CounterDict[self.lineEdit.text()].Consumption - \
                            int(self.comboBox.currentText().split(' ')[1].split('R')[0])*int(self.lineEdit_2.text())
                            self.MainWindow.CounterDict[self.lineEdit.text()].RefreshToolTip()
                            
                        else:
                            self.MainWindow.CounterDict[self.lineEdit.text()].Consumption=self.MainWindow.CounterDict[self.lineEdit.text()].Consumption - \
                            int(self.comboBox.currentText().split(' ')[1].split('R')[0]) * \
                            int(self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]].split(' ')[1].split('*')[1])
                            
                            del self.MainWindow.CounterDict[self.lineEdit.text()].MenuList[self.comboBox.currentText().split(' ')[0]]
                            QtGui.QMessageBox.warning(None,'提示','减少餐饮的数量已经让该餐饮总数低于或0故删除餐点',QtGui.QMessageBox.Yes)
                            self.MainWindow.CounterDict[self.lineEdit.text()].RefreshToolTip()
                    else:
                        QtGui.QMessageBox.warning(None,'提示','未点该类餐饮,无法删除'+self.comboBox.currentText().split(' ')[0]+'*'+self.lineEdit_2.text(),QtGui.QMessageBox.Yes)
                    print(self.MainWindow.CounterDict[self.lineEdit.text()].MenuList)
                else:
                    QtGui.QMessageBox.warning(None,'提示','未开台无法添加删除餐饮',QtGui.QMessageBox.Yes)
            else:
                QtGui.QMessageBox.warning(None,'提示','数量异常无法添加',QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.warning(None,'提示','台号为空无法添加',QtGui.QMessageBox.Yes)
        


