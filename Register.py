from PyQt5 import QtCore, QtGui, QtWidgets

from ui_Register import Ui_Dialog

class RegisterForm(Ui_Dialog,QtWidgets.QDialog):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(RegisterForm, self).__init__()
        self.setupUi(self)

        self.conn=None
        self.cur=None

        self.pushButton.clicked.connect(self.register)

    def register(self):
        if self.radioButton.isChecked():
            type=1
        elif self.radioButton_3.isChecked():
            type=3
        else:
            type=2
        sql="INSERT INTO accounts VALUES(%s,%s,%s) "
        self.cur.execute(sql,(self.lineEdit.text(),self.lineEdit_2.text(),type))
        self.conn.commit()
        self.close()

    def SetSql(self,conn,cur):
        self.conn=conn
        self.cur=cur
