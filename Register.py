#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_Register import Ui_Dialog
import sys

class RegisterForm(Ui_Dialog,QtWidgets.QDialog):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(RegisterForm, self).__init__()
        self.setupUi(self)

        self.conn=None
        self.cur=None

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.close)
        self.radioButton_2.clicked.connect(self.enlineEdit_3)
        self.radioButton.clicked.connect(self.unlineEdit_3)
        self.radioButton_3.clicked.connect(self.unlineEdit_3)
        self.radioButton_4.clicked.connect(self.unlineEdit_3)



#控制业主框是否可编辑
    def enlineEdit_3(self,check):
        self.lineEdit_3.setEnabled(check)

    def unlineEdit_3(self,check):
        check= not check
        self.lineEdit_3.setEnabled(check)

#注册
    def register(self):
        if len(self.lineEdit_2.text())<6:
                QtWidgets.QMessageBox.warning(self,'错误','密码过短')
                return
        if self.radioButton.isChecked():
            type=1
        elif self.radioButton_3.isChecked():
            type=3
        elif self.radioButton_4.isChecked():
            type=4
        else:
            type=2
        if type==2 :
            sql="SELECT * FROM owner WHERE owner_num=%s"
            self.cur.execute(sql,self.lineEdit_3.text())
            tf = self.cur.fetchall()
            # if len(tf)>0:


            sql="INSERT INTO accounts VALUES(%s,%s,%s,%s) "
            try:
                self.cur.execute(sql,(self.lineEdit.text(),self.lineEdit_2.text(),type,self.lineEdit_3.text()))
                self.conn.commit()
                self.close()
            except:
                QtWidgets.QMessageBox.critical(self,'错误','注册失败，用户名可能重复或业主号输入错误')
            # else:
            #     QtWidgets.QMessageBox.warning(self, '错误', '未找到该业主号，请向管理员询问')
        else:
            sql = "INSERT INTO accounts(account,password,type) VALUES(%s,%s,%s) "
            try:
                self.cur.execute(sql, (self.lineEdit.text(), self.lineEdit_2.text(), type))
                self.conn.commit()
                self.close()
            except:
                QtWidgets.QMessageBox.critical(self, '错误', '注册失败，用户名可能重复')


#载入数据库
    def SetSql(self,conn,cur):
        self.conn=conn
        self.cur=cur
