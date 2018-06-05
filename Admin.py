from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Admin import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymssql

#数据库服务器信息
server='DESKTOP-9J11AF2'
user="admin"
password="123"
database="SQLCD"

title=['业主号', '业主名']
dist={0:'owner_num',1:'owner_name'}
class AdminForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(AdminForm, self).__init__()
        self.setupUi(self)

        self.conn = pymssql.connect(server, user, password, database, charset="GBK")
        self.cur = self.conn.cursor()
        self.init()
        self.num=self.model.rowCount()


    def init(self):
        sql = "SELECT * FROM owner"
        self.cur.execute(sql)
        rows = self.cur.fetchall()

        self.model = QStandardItemModel(0, 2);
        self.model.setHorizontalHeaderLabels(title)
        self.addItem(rows)
        self.tableView.setModel(self.model)

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

        self.pushButton.clicked.connect(self.addRow)
        self.tableView.doubleClicked.connect(self.gettemp)
        self.tableView.doubleClicked.connect(self.tableView.edit)
        self.model.itemChanged.connect(self.addorcor)
        QtCore.QModelIndex



    def gettemp(self,item):
        self.temp=item.data()

    def addorcor(self,item):
        if item.row()>=self.num:
            self.num=self.num+1
            sql="INSERT INTO owner(owner_num) VALUES (%s)"
            self.cur.execute(sql,item.text())
        else:
            key=self.model.item(item.row(),0).text()
            if item.column()==0:
                sql="UPDATE owner SET owner_num=%s WHERE owner_num=%s"
                self.cur.execute(sql, (str(item.text()), self.temp))
            else:
                sql = "UPDATE owner SET owner_name=%s WHERE owner_num=%s"
                self.cur.execute(sql,(str(item.text()),str(key)))
        self.conn.commit()
        print(item.row(),item.column(),item.text())


    def addRow(self):
        self.model.appendRow([])

    def addItem(self,rows):
        row=len(rows)
        col=len(title)
        for i in range(row):
            date = []
            for j in range(col):
                item = QStandardItem(rows[i][j])
                date.append(item)
            self.model.appendRow(date)


