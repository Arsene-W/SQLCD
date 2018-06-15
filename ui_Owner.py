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
        MainWindow.resize(1057, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("font: 18pt \"黑体\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tableView = QtWidgets.QTableView(self.splitter_2)
        self.tableView.setMinimumSize(QtCore.QSize(756, 731))
        self.tableView.setStyleSheet("font: 14pt \"黑体\";")
        self.tableView.setObjectName("tableView")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setMinimumSize(QtCore.QSize(230, 159))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 60, 111, 51))
        self.pushButton.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(230, 381))
        self.groupBox.setStyleSheet("font: 14pt \"Agency FB\";")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 181, 31))
        self.comboBox.setStyleSheet("font: 15pt \"黑体\";")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 40, 91, 31))
        self.pushButton_2.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 160, 111, 51))
        self.pushButton_3.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 250, 111, 51))
        self.pushButton_5.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setMinimumSize(QtCore.QSize(230, 181))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 40, 111, 51))
        self.pushButton_4.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "物业管理系统-普通业主"))
        self.label.setText(_translate("MainWindow", "   普通业主"))
        self.pushButton.setText(_translate("MainWindow", "个人信息"))
        self.groupBox.setTitle(_translate("MainWindow", "业务"))
        self.pushButton_2.setText(_translate("MainWindow", "添加业务"))
        self.pushButton_3.setText(_translate("MainWindow", "查看业务"))
        self.pushButton_5.setText(_translate("MainWindow", "删除业务"))
        self.pushButton_4.setText(_translate("MainWindow", "查看账单"))

