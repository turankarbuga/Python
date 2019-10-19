import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.label1 = QtWidgets.QLabel("Bana Henüz Tıklanmadı.")
        self.button1 = QtWidgets.QPushButton("Tıkla")
        self.button2 = QtWidgets.QPushButton("Sıfırla")
        self.count = 0

        self.setGeometry(300,300,600,500)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label1)
        v_box.addWidget(self.button1)
        v_box.addWidget(self.button2)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        def increase():
            self.count += 1
            self.label1.setText("Bana {} kere tıklandı".format(self.count))
        def clear():
            self.count = 0
            self.label1.setText("Bana Henüz Tıklanmadı.")

        self.button1.clicked.connect(increase)
        self.button2.clicked.connect(clear)

        self.setLayout(h_box)

        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
