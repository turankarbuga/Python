from bs4 import BeautifulSoup
import requests
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QComboBox,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5 import QtGui

url = "https://www.doviz.com/"
response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")

gold_value = soup.find_all("span",{"class" : "value"})[0].text
dollar_value = soup.find_all("span",{"class" : "value"})[1].text
euro_value = soup.find_all("span",{"class" : "value"})[2].text
bist100 = soup.find_all("span",{"class" : "value"})[3].text
interest = soup.find_all("span",{"class" : "value"})[4].text


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.currencybox = QComboBox()
        self.button = QPushButton("Bring")
        self.currency_label = QLabel("")
        self.currency_label.setFont(QtGui.QFont("Times", 24))
        self.info_label = QLabel("")
        self.info_label.setFont(QtGui.QFont("Times",24))

        self.setGeometry(300,300,390,100)

        self.currencybox.addItems(["Gold","Dollar","Euro","Bist 100","Interest"])

        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.currencybox)

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.currency_label)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.button)

        h_box4 = QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.info_label)
        h_box4.addStretch()

        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)

        self.button.clicked.connect(self.click)

        self.setLayout(v_box)
        self.show()

    def click(self):

        if self.currencybox.currentText() == "Gold":
            self.info_label.setText("Current Gold Rate:")
            self.currency_label.setText(gold_value+"₺")

        elif self.currencybox.currentText() == "Dollar":
            self.info_label.setText("Current Dollar Rate:")
            self.currency_label.setText(dollar_value+"₺")

        elif self.currencybox.currentText() == "Euro":
            self.info_label.setText("Current Euro Rate:")
            self.currency_label.setText(euro_value+"₺")

        elif self.currencybox.currentText() == "Bist 100":
            self.info_label.setText("Current Bist 100:")
            self.currency_label.setText(bist100)

        elif self.currencybox.currentText() == "Interest":
            self.info_label.setText("Current Interest")
            self.currency_label.setText(interest)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
