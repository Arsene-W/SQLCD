import pymssql
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Login import Ui_MainWindow
from Register import RegisterForm

#数据库服务器信息
server='DESKTOP-9J11AF2'
user="login"
password="321"
database="SQLCD"
class LoginForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(LoginForm, self).__init__()
        self.setupUi(self)

        self.re = RegisterForm()
        self.conn = pymssql.connect(server, user, password, database, charset="GBK")
        self.cur = self.conn.cursor()

        self.pushButton.clicked.connect(self.loclick)
        self.pushButton_2.clicked.connect(self.reclick)

    def loclick(self):
        account=self.lineEdit.text()
        password=self.lineEdit_2.text()
        sql = "SELECT * FROM accounts WHERE account=%s AND password=%s"
        self.cur.execute(sql,(account,password))
        rows = self.cur.fetchall()
        if len(rows):
            print ('yes')
            print (rows[0][2])
            self.conn.close()

        else:
            print ('no')

    def reclick(self):
        if self.cur:
            self.re.SetSql(self.conn,self.cur)
            self.re.exec_()

