# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 360)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 190, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(210, 80, 89, 16))
        self.radioButton_3.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(120, 80, 89, 16))
        self.radioButton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.radioButton.setObjectName("radioButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 30, 51, 31))
        self.label.setStyleSheet("font: 18pt \"黑体\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 80, 89, 16))
        self.radioButton_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 300, 75, 23))
        self.pushButton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 51, 16))
        self.label_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 190, 51, 16))
        self.label_3.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 250, 51, 16))
        self.label_4.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 250, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(310, 80, 89, 16))
        self.radioButton_4.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.pushButton_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注   册"))
        self.radioButton_3.setText(_translate("Dialog", "水费代表"))
        self.radioButton.setText(_translate("Dialog", "管理员"))
        self.label.setText(_translate("Dialog", "注册"))
        self.radioButton_2.setText(_translate("Dialog", "业主"))
        self.pushButton.setText(_translate("Dialog", "注册"))
        self.label_2.setText(_translate("Dialog", "账号"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.label_4.setText(_translate("Dialog", "业主号"))
        self.radioButton_4.setText(_translate("Dialog", "电费代表"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

