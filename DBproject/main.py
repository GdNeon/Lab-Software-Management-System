#import sql
import sys
from login import Login_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #分辨率匹配

if __name__ == "__main__":
	#启动界面
	app = QApplication(sys.argv)
	form = QWidget()
	Login = Login_Dialog()
	Login.setupUi(form)
	form.show()
	sys.exit(app.exec_())