from PyQt5.QtGui import *
from sql import *

#实验室信息
lab_model = QStandardItemModel(len(labs), len(labs[0]))  # 存储任意结构数据
lab_model.setHorizontalHeaderLabels(['序号', '管理员序号', '实验室名称', '地址', '占地面积', '容纳人数', '电脑配置'])
for row in range(len(labs)):
    for column in range(len(labs[0])):
        i = QStandardItem(str(labs[row][column]))
        if (column == 0) | (column == 1):
            i.setEnabled(False)
        lab_model.setItem(row, column, i)

#课程信息
course_model = QStandardItemModel(len(courses), len(courses[0]))  # 存储任意结构数据
course_model.setHorizontalHeaderLabels(['课号', '实验室号', '课程名称', '授课教师', '实验学时', '学分', '人数'])
for row in range(len(courses)):
    for column in range(len(courses[0])):
        i = QStandardItem(str(courses[row][column]))
        if column == 0:
            i.setEnabled(False)
        course_model.setItem(row, column, i)

#教师信息
teacher_model = QStandardItemModel(len(teachers), len(teachers[0]))  # 存储任意结构数据
teacher_model.setHorizontalHeaderLabels(['教师号', '教师姓名'])
for row in range(len(teachers)):
    for column in range(len(teachers[0])):
        i = QStandardItem(str(teachers[row][column]))
        i.setEnabled(False)
        teacher_model.setItem(row, column, i)

#学生信息
student_model = QStandardItemModel(len(students), len(students[0]))  # 存储任意结构数据
student_model.setHorizontalHeaderLabels(['学号', '学生姓名'])
for row in range(len(students)):
    for column in range(len(students[0])):
        i = QStandardItem(str(students[row][column]))
        i.setEnabled(False)
        student_model.setItem(row, column, i)

#软件信息
software_model = QStandardItemModel(len(softwares), len(softwares[0]))  # 存储任意结构数据
software_model.setHorizontalHeaderLabels(['软件编号', '软件类别号', '软件名', '软件版本', '软件大小(MB)'])
for row in range(len(softwares)):
    for column in range(len(softwares[0])):
        i = QStandardItem(str(softwares[row][column]))
        software_model.setItem(row, column, i)

