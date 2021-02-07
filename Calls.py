from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mysql
from CallsShow import Showcalls

class Calls(object):
    def show_Calls(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Showcalls()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 30, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 50, 90, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 50, 90, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 50, 90, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 50, 90, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 50, 90, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(550, 50, 90, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 100, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 30, 100, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 30, 100, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 30, 100, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 30, 100, 20))
        self.label_7.setObjectName("label_7")
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 150, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_Calls)
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
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
        self.label.setText(_translate("MainWindow", "ID_Call"))
        self.label_2.setText(_translate("MainWindow", "Duration"))
        self.label_3.setText(_translate("MainWindow", "Date"))
        self.label_4.setText(_translate("MainWindow", "Outgoing_number"))
        self.label_5.setText(_translate("MainWindow", "Outgoing_city"))
        self.label_6.setText(_translate("MainWindow", "Incoming_city"))
        self.label_7.setText(_translate("MainWindow", "Incoming_number"))
        self.pushButton.setText(_translate("MainWindow", "Change call"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_Call"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_Call"))
        self.pushButton_4.setText(_translate("MainWindow", "Show_Calls"))


    def change(self):

        try:
            ID_Call = int(self.lineEdit.text())
            Duration = self.lineEdit_2.text()
            Date = self.lineEdit_3.text()
            Outgoing_number = self.lineEdit_4.text()
            Outgoing_city = self.lineEdit_5.text()
            Incoming_city = self.lineEdit_6.text()
            Incoming_number = self.lineEdit_7.text()
        except:
            return

        try:
            db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
            cur = db.cursor()
            ch1 = """UPDATE calls SET Duration = %s, Date = %s Outgoing_number = %s, Outgoing_city = %s Incoming_city = %s, Incoming_number = %s WHERE ID_Call = %s"""
            ch2 = (Duration, Date, Outgoing_number, Outgoing_city, Incoming_city, Incoming_number, ID_Call)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            ID_Call = int(self.lineEdit.text())
            Duration = self.lineEdit_2.text()
            Date = self.lineEdit_3.text()
            Outgoing_number = self.lineEdit_4.text()
            Outgoing_city = self.lineEdit_5.text()
            Incoming_city = self.lineEdit_6.text()
            Incoming_number = self.lineEdit_7.text()
        except:
            return
        db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
        cur = db.cursor()
        cur.execute('insert into calls values(%s, %s, %s, %s, %s, %s, %s)', \
            (int(ID_Call), Duration, Date, Outgoing_number, Outgoing_city, Incoming_city, Incoming_number,))
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
        cur.execute("DELETE FROM calls WHERE ID_Call = %s",(int(ID),))
        db.commit()
        cur.close()
        db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Calls()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
