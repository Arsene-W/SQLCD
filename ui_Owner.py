# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Owner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 91, 31))
        self.label.setStyleSheet("font: 14pt \"黑体\";")
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 70, 761, 701))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 110, 111, 51))
        self.pushButton.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(890, 600, 111, 51))
        self.pushButton_4.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(820, 210, 231, 361))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 81, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 60, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 160, 111, 51))
        self.pushButton_3.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 250, 111, 51))
        self.pushButton_5.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "物业管理系统-普通业主"))
        self.label.setText(_translate("MainWindow", "普通业主"))
        self.pushButton.setText(_translate("MainWindow", "个人信息"))
        self.pushButton_4.setText(_translate("MainWindow", "查看账单"))
        self.groupBox.setTitle(_translate("MainWindow", "业务"))
        self.pushButton_2.setText(_translate("MainWindow", "添加业务"))
        self.pushButton_3.setText(_translate("MainWindow", "查看业务"))
        self.pushButton_5.setText(_translate("MainWindow", "删除业务"))

