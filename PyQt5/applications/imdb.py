#This application brings movies and rates in which are imdb top 250 list.

import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtWidgets

url = "https://www.imdb.com/chart/top"
response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

titles = soup.find_all("td",{"class":"titleColumn"})
rates = soup.find_all("td",{"class":"ratingColumn imdbRating"})


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 440)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton.clicked.connect(self.bring_movies)
        self.pushButton_2.clicked.connect(self.bring_moviesandrates)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IMDB Top 250"))
        self.pushButton.setText(_translate("Form", "Only Movies"))
        self.pushButton_2.setText(_translate("Form", "Movies with Rates"))

    def bring_movies(self):
        self.plainTextEdit.clear()
        for title in titles:
            title = title.text
            title = title.strip()
            title = title.replace("\n", "")
            self.plainTextEdit.appendPlainText(title)

    def bring_moviesandrates(self):
        self.plainTextEdit.clear()
        for title, rate in zip(titles, rates):
            rate = rate.text
            rate = rate.strip()
            rate = rate.replace("\n", "")

            title = title.text
            title = title.strip()
            title = title.replace("\n", "")
            title = title.strip()

            self.plainTextEdit.appendPlainText(title + " " + rate)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

