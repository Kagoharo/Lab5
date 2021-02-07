from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mysql
from HumanShow import Showhuman

class Human(object):
    def show_Human(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Showhuman()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(25, 50, 31, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 160, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 301, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.dels)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 120, 161, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_Human)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Id_Human"))
        self.label_2.setText(_translate("MainWindow", "Full_Name"))
        self.pushButton.setText(_translate("MainWindow", "Change_Human"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_Human"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_Human"))
        self.pushButton_4.setText(_translate("MainWindow", "Show_Human"))


    def change(self):

        try:
            ID_Human = int(self.lineEdit.text())
            Full_Name = self.lineEdit_2.text()
        except:
            return

        try:
            db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
            cur = db.cursor()
            ch1 = """UPDATE human SET Full_Name = %s WHERE ID_Human = %s"""
            ch2 = (Full_Name, ID_Human)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            ID_Human = int(self.lineEdit.text())
            Full_Name = self.lineEdit_2.text()
        except:
            return
        db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
        cur = db.cursor()
        cur.execute('insert into human values(%s, %s)',
            (int(ID_Human), Full_Name))
        db.commit()
        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
        cur = db.cursor()
        try:
            ID = int(self.lineEdit.text())
        except:
            return
        cur.execute("DELETE FROM human WHERE ID_Human = %s",(int(ID),))
        db.commit()
        cur.close()
        db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Human()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())