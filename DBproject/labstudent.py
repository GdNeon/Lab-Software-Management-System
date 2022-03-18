# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labstudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from information import *
from sql import *

class Student_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 510)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 111, 23))
        self.pushButton.clicked.connect(self.lab_info)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 70, 111, 23))
        self.pushButton_2.clicked.connect(self.course_info)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 120, 111, 23))
        self.pushButton_5.clicked.connect(self.software_info)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(150, 20, 481, 411))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 340, 131, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 131, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "学生专用页面"))
        self.pushButton.setText(_translate("Dialog", "查看实验室信息"))
        self.pushButton_2.setText(_translate("Dialog", "查看课程信息"))
        self.pushButton_5.setText(_translate("Dialog", "查看软件信息"))
        self.label.setText(_translate("Dialog", "  欢迎回来！"))
        self.label_2.setText(_translate("Dialog", "    同学"))
        self.label_3.setText(_translate("Dialog", "   亲爱的"))

    def lab_info(self):
        self.model = lab_model
        self.tableView.setModel(self.model)

    def course_info(self):
        self.model = self.course_sel()
        self.tableView.setModel(self.model)

    def software_info(self):
        self.model = software_model
        self.tableView.setModel(self.model)

    def course_sel(self):
        #学生只能查看自己选的课
        csql = "SELECT * FROM course WHERE c_id IN (SELECT c_id FROM student_course WHERE t_id = " + self.line + ");"
        db.ping(reconnect=True)
        cursor.execute(csql)
        courses = cursor.fetchall()
        self.cmodel = QStandardItemModel(len(courses), len(courses[0]))  # 存储任意结构数据
        self.cmodel.setHorizontalHeaderLabels(['课号', '实验室号', '课程名称', '授课教师', '实验学时', '学分', '人数'])
        for row in range(len(courses)):
            for column in range(len(courses[0])):
                i = QStandardItem(str(courses[row][column]))
                self.cmodel.setItem(row, column, i)
        return self.cmodel

