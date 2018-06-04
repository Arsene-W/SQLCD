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
class AdminForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(AdminForm, self).__init__()
        self.setupUi(self)

        self.conn = pymssql.connect(server, user, password, database, charset="GBK")
        self.cur = self.conn.cursor()
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
        self.addItem([('DSF','AFASD')])


    def addItem(self,rows):
        row=len(rows)
        col=len(title)
        for i in range(row):
            date = []
            for j in range(col):
                item = QStandardItem(rows[i][j])
                date.append(item)
            self.model.appendRow(date)


