#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_wRepresentative import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymssql
import datetime

import sys

server='DESKTOP-9J11AF2'
user="representative"
password="123456789"
database="SQLCD"

charges_title=['业主号','之前用水量','目前用水量','用水量','水费','物业费','维修费']
serviceif_title=['月份','服务号','服务名','业主号','费用','服务人员','状态']

class wRepresentativeForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self,parent = None):
        super(wRepresentativeForm, self).__init__()
        self.setupUi(self)

        self.conn = pymssql.connect(server, user, password, database, charset="utf8")
        self.cur = self.conn.cursor()

        self.comboBox.setCurrentIndex(datetime.datetime.now().month - 1)
        self.init()
        self.pushButton.clicked.connect(self.addRow)
        self.pushButton_2.clicked.connect(self.showserif)
        self.pushButton_3.clicked.connect(self.delete)
        self.tableView.doubleClicked.connect(self.gettemp)
        self.tableView.doubleClicked.connect(self.tableView.edit)


        self.comboBox.currentTextChanged.connect(self.showcha)


        self.tablenum=0


    def init(self):
        self.model = QStandardItemModel(0, len(charges_title))
        self.showcha()

#展示账单
    def showcha(self):
        self.model.clear()
        self.model = QStandardItemModel(0, len(charges_title));
        self.model.setHorizontalHeaderLabels(charges_title)
        sql = "SELECT owner_num,last_water,now_water,water_yield,water_charges,property_fee,repair_cost FROM charges WHERE month=%s"
        self.cur.execute(sql, self.comboBox.currentText())
        rows = self.cur.fetchall()
        self.addItem(rows, charges_title)
        self.tableView.setModel(self.model)
        #self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

        self.model.itemChanged.connect(self.addorcor)
        self.num = self.model.rowCount()
        self.tablenum=0
        self.pushButton_3.setEnabled(False)
        self.pushButton.setEnabled(True)



#添加表项
    def addItem(self, rows,title):
        row = len(rows)
        col = len(title)
        print(col)
        for i in range(row):
            date = []
            for j in range(col):
                item = QStandardItem(str(rows[i][j]))
                date.append(item)
            self.model.appendRow(date)

#添加行
    def addRow(self):
        self.model.appendRow([])

#添加或修改
    def addorcor(self,item):
        text = item.text()
        if self.tablenum==0:
            #print(self.num)
            if item.row()>=self.num:

                self.num = self.num + 1
                sql="INSERT INTO charges(month,owner_num) VALUES (%s,%s)"
                try:
                    self.cur.execute(sql, (self.comboBox.currentText(), "待填"))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，可能该业主号不存在')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    self.num = self.num - 1
                    return

            if self.model.item(item.row(), 0) != None:
                if item.column() != 0:
                    key = self.model.item(item.row(), 0).text()
                else:
                    if self.temp != None:
                        key = self.temp
                    else:
                        key = "待填"
            else:
                key = "待填"

            if item.column() == 0:

                sql = "UPDATE charges SET owner_num=%s WHERE owner_num=%s"
                try:

                    self.cur.execute(sql, (str(text), key))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复0')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return
            elif item.column()==3:
                sql = "UPDATE charges SET water_yield=%s ,water_charges=%s WHERE month=%s AND owner_num=%s"
                try:
                    print(str(item.text()),str(float(item.text())*float(self.doubleSpinBox.text())),str(self.comboBox.currentText()),str(key))
                    self.cur.execute(sql,(str(item.text()),str(float(item.text())*float(self.doubleSpinBox.text())),str(self.comboBox.currentText()),str(key)))
                    self.model.setItem(item.row(),4,QStandardItem(str(float(item.text())*float(self.doubleSpinBox.text()))))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return



            elif item.column()==5:
                sql = "UPDATE charges SET property_fee=%s WHERE owner_num=%s"
                try:
                    self.cur.execute(sql, (str(item.text()), key))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return

            elif item.column() == 2:
                sql = "UPDATE charges SET now_water=%s WHERE month=%s AND owner_num=%s"
                try:

                    self.cur.execute(sql, (str(item.text()),str(self.comboBox.currentText()), str(key)))
                    print(float(text)-float(self.model.item(item.row(), 1).text()))
                    self.model.setItem(item.row(), 3,QStandardItem(str(float(text)-float(self.model.item(item.row(), 1).text()))))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复#')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return
            elif item.column() == 1:
                sql = "UPDATE charges SET last_water=%s WHERE owner_num=%s"
                try:
                    self.cur.execute(sql, (str(item.text()), key))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return




            self.conn.commit()
            #print(item.row(),item.column(),item.text())
        elif self.tablenum==1:
            key=[self.model.item(item.row(),0).text(),self.model.item(item.row(),1).text(),self.model.item(item.row(),3).text()]
            if item.column() == 4:
                sql = "UPDATE service_if SET cost=%s WHERE month=%s AND service_num=%s AND owner_num=%s"
                try:
                    self.cur.execute(sql, (str(item.text()), key[0],key[1],key[2]))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return
            elif item.column() == 5:
                sql = "UPDATE service_if SET serviceman=%s WHERE month=%s AND service_num=%s AND owner_num=%s"
                try:
                    self.cur.execute(sql, (str(item.text()), key[0],key[1],key[2]))
                except:
                    QMessageBox.critical(self, '错误', '输入有误，主码可能重复')
                    self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                    return


            self.conn.commit()


#获取修改前值
    def gettemp(self,item):
        self.temp=item.data()

#展示服务信息
    def showserif(self):
        self.model.clear()
        self.model = QStandardItemModel(0, len(serviceif_title));
        self.model.setHorizontalHeaderLabels(serviceif_title)
        print("*")
        sql = "SELECT * FROM service_if"
        self.cur.execute(sql)
        rows = self.cur.fetchall()

        self.addItem(rows, serviceif_title)
        self.tableView.setModel(self.model)
        # self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

        self.model.itemChanged.connect(self.addorcor)
        self.num = self.model.rowCount()
        self.tablenum=1

        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(True)

#删除
    def delete(self):
        indexs = self.tableView.selectionModel().selection().indexes()
        if len(indexs) > 0:
            index = indexs[0]
            key = [self.model.item(index.row(), 0).text(), self.model.item(index.row(), 1).text(), self.model.item(index.row(), 3).text()]
            sql = "DELETE FROM service_if WHERE month=%s AND service_num=%s AND owner_num=%s"
            print(key[0],key[1],key[2])
            self.cur.execute(sql,(key[0],key[1],key[2]))
            self.conn.commit()
            self.model.removeRows(index.row(), 1)



