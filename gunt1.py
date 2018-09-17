#<--*-- coding:utf-8 --*-->
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Main(object):       #主窗口
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 491, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuType_Here = QtWidgets.QMenu(self.menubar)
        self.menuType_Here.setObjectName("menuType_Here")
        MainWindow.setMenuBar(self.menubar)
        self.actionChushi = QtWidgets.QAction(MainWindow)
        self.actionChushi.setObjectName("actionChushi")
        self.actionXinjian = QtWidgets.QAction(MainWindow)
        self.actionXinjian.setObjectName("actionXinjian")
        self.menuType_Here.addAction(self.actionChushi)
        self.menuType_Here.addAction(self.actionXinjian)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuType_Here.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menuType_Here.setTitle(_translate("MainWindow", "Type Here"))
        self.actionChushi.setText(_translate("MainWindow", "chushi"))
        self.actionXinjian.setText(_translate("MainWindow", "xinjian"))
##########################################################
class Ui_Show(object):     #子窗口1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 190, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "第一个内嵌窗口"))    
###############################    
class Ui_New(object):           #子窗口2
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 180, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 230, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 250, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(190, 320, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 300, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 410, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "第二个内嵌窗口"))
        self.label_2.setText(_translate("MainWindow", "TXT_LABLE"))
        self.label_3.setText(_translate("MainWindow", "TXT_LABLE"))
        self.label_4.setText(_translate("MainWindow", "TXT_LABLE"))
        self.pushButton.setText(_translate("MainWindow", "PushButton")) 
#################################################    
    
    
class Main(QMainWindow,Ui_Main):      #控制程序
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.child1 = Show()
        self.child2 = New()
        self.actionChushi.triggered.connect(self.New)
        self.actionXinjian.triggered.connect(self.Show)
        
    def Show(self):
        self.gridLayout.addWidget(self.child1)#将窗口放入girdLayout中
        self.child2.hide()
        self.child1.show()#打开子窗口1
        
    def New(self):
        self.gridLayout_2.addWidget(self.child2)
        self.child1.hide()
        self.child2.show()
 
class New(QMainWindow,Ui_New):
    def __init__(self):
        super(New,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Close)
    def Close(self):
        self.close()
 
class Show(QMainWindow,Ui_Show):
    def __init__(self):
        super(Show,self).__init__()
        self.setupUi(self)
 
if __name__=='__main__':
    app = QApplication(sys.argv)
    Main = Main()
    Show = Show()
    New = New()
    Main.show()
    sys.exit(app.exec_())
