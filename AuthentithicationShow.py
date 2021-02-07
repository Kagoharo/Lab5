from PyQt5       import QtCore, QtGui, QtWidgets
import MySQLdb   as mysql
import ast

def convert(in_data):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)
    return tuple(map(cvt, in_data))


class ShowAuth(object):

    def loadconection(self):
        db = mysql.connect(host="127.0.0.1", user="root", passwd="qwasEXD85", db="mydb")
        with db:
            cur = db.cursor()
            rows = cur.execute("""select * from authentication""")
            data = cur.fetchall()

            for row in data:
                self.add_table(convert(row))

            cur.close()

    def add_table(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(35, 21, 731, 401))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Account_ID', 'login', 'password'])
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.btn_abrirbd2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrirbd2.setGeometry(QtCore.QRect(340, 460, 75, 23))
        self.btn_abrirbd2.setObjectName("btn_abrirbd2")
        self.btn_abrirbd2.clicked.connect(self.loadconection)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.btn_abrirbd2.setText(_translate("MainWindow", "Table"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ShowAuth()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())