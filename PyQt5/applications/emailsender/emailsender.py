"""
Firstly, you should activate less secure apps in this link https://myaccount.google.com/lesssecureapps

Secondly, you can log in with your email address and password. (Don't forget only gmail)

Thirdly, just write subject ,message and add an address to the database and select it in combobox. Now you are ready to send message.

The Addresses which are added to database will save. If you start the application again addresses will come to the combobox.
However, you have to log in every time because your e-mail address and password are not saved by application.
"""

from PyQt5 import QtCore,QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3


def sendMessage():
    message = MIMEMultipart()
    message["From"] = loginwindow.returnUserEmail()
    message["To"] = ui.returnSelectedItem()
    message["Subject"] = ui.returnSubject()

    text = ui.returnMessage()

    message_body = MIMEText(text,"plain")
    message.attach(message_body)

    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(loginwindow.returnUserEmail(),loginwindow.returnUserPassword())
    mail.sendmail(message["From"],message["To"],message.as_string())

    ui.responseLabel.setText("Mail has been sent successfully.")


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 363)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.subjectLine = QtWidgets.QLineEdit(Form)
        self.subjectLine.setObjectName("subjectLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subjectLine)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.messageLine = QtWidgets.QTextEdit(Form)
        self.messageLine.setObjectName("messageLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.messageLine)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.newAddressLine = QtWidgets.QLineEdit(Form)
        self.newAddressLine.setObjectName("newAddressLine")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.newAddressLine)
        self.addressBox = QtWidgets.QComboBox(Form)
        self.addressBox.setObjectName("addressBox")
        self.addressBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.addressBox)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.addNewAddressButton = QtWidgets.QPushButton(Form)
        self.addNewAddressButton.setObjectName("addNewAddressButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.addNewAddressButton)
        self.deleteAddressButton = QtWidgets.QPushButton(Form)
        self.deleteAddressButton.setObjectName("deleteAddressButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.deleteAddressButton)
        self.sendMessageButton = QtWidgets.QPushButton(Form)
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sendMessageButton)
        self.responseLabel = QtWidgets.QLabel(Form)
        self.responseLabel.setText("")
        self.responseLabel.setObjectName("responseLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.responseLabel)

        self.addNewAddressButton.clicked.connect(self.addNewAddress)
        self.deleteAddressButton.clicked.connect(self.deleteAddress)
        self.sendMessageButton.clicked.connect(sendMessage)

        con = sqlite3.connect("database.db")
        self.cursor = con.cursor()
        self.cursor.execute("Create Table If Not Exists addresses(address TEXT)")
        self.cursor.execute("Select * From addresses")
        data = self.cursor.fetchall()

        for address in data:
            self.addressBox.addItem(address[0])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mail Sender"))
        self.label.setText(_translate("Form", "Subject"))
        self.label_2.setText(_translate("Form", "Message"))
        self.label_3.setText(_translate("Form", "Select Address"))
        self.label_4.setText(_translate("Form", "New Address"))
        self.addNewAddressButton.setText(_translate("Form", "Add New Address"))
        self.deleteAddressButton.setText(_translate("Form", "Delete Selected Address"))
        self.sendMessageButton.setText(_translate("Form", "Send Message"))

    def addNewAddress(self):
        address = self.newAddressLine.text()

        if len(address) > 0:
            if "@" not in address:
                self.responseLabel.setText("Please enter valid address.")
            elif (self.newAddressLine.text().count("@")) > 1:
                self.responseLabel.setText("Please enter valid address.")
            else:
                self.addressBox.addItem(address)
                self.responseLabel.setText("Address has been added successfully")

                con = sqlite3.connect("database.db")
                self.cursor = con.cursor()
                self.cursor.execute("Create Table If Not Exists addresses(address TEXT)")
                self.cursor.execute("insert into addresses values(?)",(address,))
                con.commit()
        else:
            self.responseLabel.setText("Please enter an address.")

    def deleteAddress(self):
        selectedItemIndex = self.addressBox.currentIndex()
        selectedItemText = self.addressBox.currentText()

        con = sqlite3.connect("database.db")
        self.cursor = con.cursor()
        self.cursor.execute("Delete from addresses where address = ?", (selectedItemText,))
        con.commit()

        self.addressBox.removeItem(selectedItemIndex)
        self.responseLabel.setText("Selected address has been deleted successfully")

    def returnSubject(self):
        subject = self.subjectLine.text()
        return subject

    def returnSelectedItem(self):
        selectedItem = self.addressBox.currentText()
        return selectedItem

    def returnMessage(self):
        message = self.messageLine.toPlainText()
        return message


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.email = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton("Login")
        self.email_label = QtWidgets.QLabel(self)
        self.email_label.setText("your e-mail:")
        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setText("your password:")

        self.setWindowTitle("Login")

        self.email_label.move(58,10)
        self.password_label.move(40,37)

        self.setGeometry(300, 300, 400, 200)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.email)
        v_box.addWidget(self.password)
        v_box.addStretch()
        v_box.addWidget(self.login_button)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.login_button.clicked.connect(self.login)

        self.setLayout(h_box)
        self.show()

    def login(self):

        Form.show()
        self.hide()

    def returnUserEmail(self):
        user_email = self.email.text()
        return user_email

    def returnUserPassword(self):
        user_password = self.password.text()
        return user_password


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    loginwindow = LoginWindow()
    ui.setupUi(Form)
    sys.exit(app.exec_())

