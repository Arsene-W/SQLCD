from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Owner import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymssql
import datetime

server='DESKTOP-9J11AF2'
user="owner"
password="123456"
database="SQLCD"

own_title=['业主号','业主名','房间号','电话']
serif_title=['月份','服务号','服务名','业主号','费用','服务人员','状态']
cha_title=['月份','业主号','水费','电费','物业费','物业维修费']
class OwnerForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, my_num,parent = None):
        super(OwnerForm, self).__init__()
        self.setupUi(self)

        self.my_num=my_num

        self.conn = pymssql.connect(server, user, password, database, charset="utf8")
        self.cur = self.conn.cursor()

        self.init()

        ser=self.getser()
        for i in range(len(ser)):
            self.comboBox.addItem(ser[i][0])
        self.pushButton.clicked.connect(self.showper)
        self.pushButton_2.clicked.connect(self.addSer)
        self.pushButton_3.clicked.connect(self.showserif)
        self.pushButton_4.clicked.connect(self.showcha)
        self.tableView.doubleClicked.connect(self.gettemp)
        self.tableView.doubleClicked.connect(self.tableView.edit)

        self.tablenum=0

    def init(self):
        self.model = QStandardItemModel(0, len(own_title));
        self.showper()



    def showper(self):
        self.model.clear()
        self.model = QStandardItemModel(0, len(own_title));
        self.model.setHorizontalHeaderLabels(own_title)
        sql="SELECT * FROM owner WHERE owner_num=%s"
        self.cur.execute(sql,self.my_num)
        rows = self.cur.fetchall()
        self.addItem(rows,own_title)
        self.tableView.setModel(self.model)
        #self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

        self.tablenum=0


    def showserif(self):
        self.model.clear()
        self.model = QStandardItemModel(0, len(serif_title));
        self.model.setHorizontalHeaderLabels(serif_title)
        sql="SELECT * FROM service_if"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.addItem(rows, serif_title)
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

        self.tablenum=1
        self.model.itemChanged.connect(self.cor)


    def showcha(self):
        self.model.clear()
        self.model = QStandardItemModel(0, len(cha_title))
        self.model.setHorizontalHeaderLabels(cha_title)
        sql = "SELECT month,owner_num,water_charges,electricity_charges,property_fee,repair_cost FROM charges WHERE owner_num=%s"
        self.cur.execute(sql,self.my_num)
        rows = self.cur.fetchall()
        self.addItem(rows, cha_title)
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

        self.tablenum=2
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

    def getser(self):
        sql="SELECT service_name FROM service"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        print(rows)
        return rows

    def addSer(self):
        try:
            sql="SELECT service_num FROM service WHERE service_name=%s"
            self.cur.execute(sql,self.comboBox.currentText())
            rows = self.cur.fetchall()
            sql = "INSERT INTO service_if(month,service_num,service_name,owner_num,situation) VALUES (%s,%s,%s,%s,%s)"

            self.cur.execute(sql, (datetime.datetime.now().month,rows[0][0],self.comboBox.currentText(),self.my_num,"未完成"))
            self.conn.commit()
            QMessageBox.information(self,"提示","服务添加成功")
        except:
            QMessageBox.critical(self,"错误","添加失败，可能您已添加过次服务")

    def gettemp(self,item):
        self.temp=item.data()

    def cor(self,item):
        key = [self.model.item(item.row(), 0).text(), self.model.item(item.row(), 1).text(),self.model.item(item.row(), 3).text()]
        if item.column()==6:
            sql = "UPDATE service_if SET situation=%s WHERE month=%s AND service_num=%s AND owner_num=%s"
            try:
                self.cur.execute(sql, (str(item.text()), key[0], key[1], key[2]))
                if item.text().replace(' ', '') == "完成":
                    print("!")
                    sql = "SELECT repair_cost FROM charges WHERE month=%s AND owner_num=%s"
                    self.cur.execute(sql, (key[0], key[2]))
                    rows = self.cur.fetchall()
                    print("$")

                    if rows[0][0] != None:
                        sql = "UPDATE charges SET repair_cost=%s WHERE month=%s AND owner_num=%s"
                        self.cur.execute(sql, (
                        float(rows[0][0]) + float(self.model.item(item.row(), 4).text()), key[0], key[2]))
                    else:
                        print("@")
                        sql = "UPDATE charges SET repair_cost=%s WHERE month=%s AND owner_num=%s"
                        print(self.model.item(item.row(), 4).text(), key[0], key[2])
                        self.cur.execute(sql, (self.model.item(item.row(), 4).text(), key[0], key[2]))
            except:
                QMessageBox.critical(self, '错误', '账单可能还未生成')
                self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                return
            self.conn.commit()




