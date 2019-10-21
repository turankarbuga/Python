import sys
from PyQt5 import QtWidgets,QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.label1 = QtWidgets.QLabel("Haven't clicked yet.")
        self.label1.setFont(QtGui.QFont("Times",24))
        self.label2 = QtWidgets.QLabel("0")
        self.label2.setFont(QtGui.QFont("Arial",50))
        self.click_button = QtWidgets.QPushButton("Click")
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.count = 0

        self.setGeometry(300,300,600,500)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label1)
        v_box.addWidget(self.click_button)
        v_box.addWidget(self.clear_button)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        def click():
            self.count += 1
            if self.count == 1:
                self.label1.setText("Clicked 1 time.")
                self.label2.setText("{}".format(self.count))
            else:
                self.label1.setText("Clicked {} times.".format(self.count))
                self.label2.setText("{}".format(self.count))

        def clear():
            self.label1.setText("Haven't clicked yet.")
            self.count = 0

        self.click_button.clicked.connect(click)
        self.clear_button.clicked.connect(clear)

        self.setLayout(h_box)

        self.show()



app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
