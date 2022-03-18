import pymysql
# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='60205nhd0014!', database='lab', charset='utf8')
cursor = db.cursor()

def cheat(cursor):
    cursor.execute("SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT;")
    cursor.execute("SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS;")
    cursor.execute("SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION;")
    cursor.execute("SET NAMES utf8;")
    cursor.execute("SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;")
    cursor.execute("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;")
    cursor.execute("SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';")
    cursor.execute("SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0;")
    cursor.execute("USE lab;")

#处理登录信息
sql_login = "SELECT t_id FROM user;"
Login_Accept_Manager = []
Login_Accept_Teacher = []
Login_Accept_Student = []
cursor.execute(sql_login)
logins = cursor.fetchall()
for i in logins:
    if i[0][0] == '0':
        Login_Accept_Manager.append(i[0])
    elif i[0][0] == 'T':
        Login_Accept_Teacher.append(i[0])
    else:
        Login_Accept_Student.append(i[0])
#获取实验室信息
sql_lab = "SELECT * FROM lab;"
cursor.execute(sql_lab)
labs = cursor.fetchall()

#获取课程信息
sql_course = "SELECT * FROM course;"
cursor.execute(sql_course)
courses = cursor.fetchall()

#获取教师信息
sql_teacher = "SELECT * FROM teacher;"
cursor.execute(sql_teacher)
teachers = cursor.fetchall()

#获取学生信息
sql_student = "SELECT * FROM student;"
cursor.execute(sql_student)
students = cursor.fetchall()

#获取软件信息
sql_software = "SELECT * FROM software;"
cursor.execute(sql_software)
softwares = cursor.fetchall()

db.close()