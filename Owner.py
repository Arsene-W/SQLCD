from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Owner import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymssql

server='DESKTOP-9J11AF2'
user="owner"
password="123456"
database="SQLCD"

own_title=['业主号','业主名']
class OwnerForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, my_num,parent = None):
        super(OwnerForm, self).__init__()
        self.setupUi(self)

        self.my_num=my_num

        self.conn = pymssql.connect(server, user, password, database, charset="GBK")
        self.cur = self.conn.cursor()

        self.init()

    def init(self):
        self.model = QStandardItemModel(0, 2);
        self.model.setHorizontalHeaderLabels(own_title)
        self.showper()
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)


    def showper(self):

        sql="SELECT * FROM owner WHERE owner_num=%s"
        self.cur.execute(sql,self.my_num)
        rows = self.cur.fetchall()
        print(rows)
        self.addItem(rows,own_title)
        print("*")


    def showserif(self):
        pass

    def showcha(self):
        pass

    def addItem(self, rows,title):
        row = len(rows)
        col = len(title)
        for i in range(row):
            date = []
            for j in range(col):
                item = QStandardItem(rows[i][j])
                date.append(item)
            self.model.appendRow(date)


