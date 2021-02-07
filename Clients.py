from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mysql
from ClientsShow import Showclients
class Clients(object):
    def show_Clients(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Showclients()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 70, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 50, 80, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 50, 111, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 50, 90, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 30, 100, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 30, 120, 20))
        self.label_5.setObjectName("label_5")
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
        self.pushButton_4.setGeometry(QtCore.QRect(180, 150, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_Clients)
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
        self.label.setText(_translate("MainWindow", "ID_client"))
        self.label_2.setText(_translate("MainWindow", "Date_of_birth"))
        self.label_3.setText(_translate("MainWindow", "Number"))
        self.label_4.setText(_translate("MainWindow", "Connected_sevices"))
        self.label_5.setText(_translate("MainWindow", "Number_of_agreement"))
        self.pushButton.setText(_translate("MainWindow", "Change_client"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_client"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_client"))
        self.pushButton_4.setText(_translate("MainWindow", "Show_Clients"))


    def change(self):

        try:
            ID_client = int(self.lineEdit.text())
            Date_of_birth = self.lineEdit_2.text()
            Number = self.lineEdit_3.text()
            Connected_sevices = self.lineEdit_4.text()
            Number_of_agreement = self.lineEdit_5.text()
        except:
            return

        try:
            db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
            cur = db.cursor()
            ch1 = """UPDATE client SET Date_of_birth = %s, Number = %s, Connected_sevices = %s, Number_of_agreement = %s WHERE ID_client = %s"""
            ch2 = (Date_of_birth, Number, Connected_sevices, Number_of_agreement, ID_client)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            ID_client = int(self.lineEdit.text())
            Date_of_birth = self.lineEdit_2.text()
            Number = self.lineEdit_3.text()
            Connected_sevices = self.lineEdit_4.text()
            Number_of_agreement = self.lineEdit_5.text()
        except:
            return
        db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
        cur = db.cursor()
        cur.execute('insert into client values(%s, %s, %s, %s, %s)',
            (int(ID_client), Date_of_birth, Number, Connected_sevices, Number_of_agreement, ))
        db.commit()
        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
        cur = db.cursor()
        try:
            id = int(self.lineEdit.text())
        except:
            return
        cur.execute("DELETE FROM client WHERE ID_client = %s",(int(id),))
        db.commit()
        cur.close()
        db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Clients()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())