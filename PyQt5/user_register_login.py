import sys
import sqlite3
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.set_connect()

        self.init_ui()
    def set_connect(self):

        con = sqlite3.connect("database.db")
        self.cursor = con.cursor()
        self.cursor.execute("Create Table If not exists users (userName TEXT,password TEXT)")

    def init_ui(self):

        self.userName = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel("")
        self.button_login = QtWidgets.QPushButton("Login")
        self.button_register = QtWidgets.QPushButton("Register")

        self.setGeometry(300,300,400,300)
        self.setWindowTitle("Log in")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.userName)
        v_box.addWidget(self.password)
        v_box.addWidget(self.label)
        v_box.addStretch()
        v_box.addWidget(self.button_login)
        v_box.addWidget(self.button_register)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.button_register.clicked.connect(self.register_clicked)
        self.button_login.clicked.connect(self.login)

        self.setLayout(h_box)
        self.show()

    def register_clicked(self):

        self.register_window = Register_window()

    def login(self):
        self.cursor.execute("Select * from users where userName = ? and password = ?",(self.userName.text(),self.password.text()))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.label.setText("Incorrect username or \npassword")
        else:
            self.label.setText("successful login")


class Register_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()

    def connect_db(self):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()

    def init_ui(self):

        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Register")

        self.regUserName = QtWidgets.QLineEdit()
        self.regPassword = QtWidgets.QLineEdit()
        self.regPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.regButton = QtWidgets.QPushButton("Register")
        self.regLabel = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.regUserName)
        v_box.addWidget(self.regPassword)
        v_box.addWidget(self.regLabel)
        v_box.addStretch()
        v_box.addWidget(self.regButton)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.regButton.clicked.connect(self.regButton_clicked)

        self.setLayout(h_box)
        self.show()

    def regButton_clicked(self):
        self.cursor.execute("Insert Into users VALUES(?,?)",(self.regUserName.text(),self.regPassword.text()))
        self.con.commit()
        self.regLabel.setText("Succeed")


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
