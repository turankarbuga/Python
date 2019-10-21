import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.input = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.print = QtWidgets.QPushButton("Print")

        self.setGeometry(300,300,500,400)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.input)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.print)
        v_box.addStretch()

        self.setLayout(v_box)

        self.clear.clicked.connect(self.click)
        self.print.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Clear" :
            self.input.clear()
        else:
            print(self.input.text())





app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())