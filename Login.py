import pymssql
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Login import Ui_MainWindow
from Register import RegisterForm
from Admin import AdminForm

#数据库服务器信息
server='DESKTOP-9J11AF2'
user="login"
password="321"
database="SQLCD"
class LoginForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(LoginForm, self).__init__()
        self.setupUi(self)


        self.conn = pymssql.connect(server, user, password, database, charset="GBK")
        self.cur = self.conn.cursor()

        self.pushButton.clicked.connect(self.loclick)
        self.pushButton_2.clicked.connect(self.reclick)


    def loclick(self):
        account=self.lineEdit.text()
        password=self.lineEdit_2.text()
        sql = "SELECT type FROM accounts WHERE account=%s AND password=%s"
        self.cur.execute(sql,(account,password))
        ty = self.cur.fetchall()
        if len(ty)>0:
            if ty[0][0][0]=='1':
                print("yes")
                print(ty[0][0])
                self.close()
                self.ad=AdminForm()
                self.ad.show()
                self.conn.close()
        else:
            QtWidgets.QMessageBox.warning(self, '错误', '用户名或密码有误，请重新输入')

    def reclick(self):
        self.re = RegisterForm()
        if self.cur:
            self.re.SetSql(self.conn,self.cur)
            self.re.exec_()

