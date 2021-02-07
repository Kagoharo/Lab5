from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from Backups import Backup
from User import User
from Calls import Calls
from Payment import Payment
from Human import Human
from Services import Services
from Authentithication import authentication
from Clients import Clients
class Ui_MainWindow(object):
    def User(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = User()
        self.ui.setupUi(self.window)
        self.window.show()
    def Calls(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Calls()
        self.ui.setupUi(self.window)
        self.window.show()
    def Payment(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Payment()
        self.ui.setupUi(self.window)
        self.window.show()
    def Human(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Human()
        self.ui.setupUi(self.window)
        self.window.show()
    def Services(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Services()
        self.ui.setupUi(self.window)
        self.window.show()
    def Backups(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Backup()
        self.ui.setupUi(self.window)
        self.window.show()
    def authentication(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = authentication()
        self.ui.setupUi(self.window)
        self.window.show()
    def Clients(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Clients()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(228, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closeEvent)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 61, 21))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 40, 131, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.User)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.authentication)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Human)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Payment)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.Services)
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.Calls)
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.Backups)
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_7")
        self.pushButton_9.clicked.connect(self.Clients)
        self.verticalLayout.addWidget(self.pushButton_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Chose:"))
        self.pushButton_2.setText(_translate("MainWindow", "User"))
        self.pushButton_3.setText(_translate("MainWindow", "authentication"))
        self.pushButton_4.setText(_translate("MainWindow", "Human"))
        self.pushButton_5.setText(_translate("MainWindow", "Payment"))
        self.pushButton_6.setText(_translate("MainWindow", "Services"))
        self.pushButton_7.setText(_translate("MainWindow", "Calls"))
        self.pushButton_8.setText(_translate("MainWindow", "Backups"))
        self.pushButton_9.setText(_translate("MainWindow", "Clients"))

    def closeEvent(self, event):
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())