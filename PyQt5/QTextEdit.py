import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QTextEdit,QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.textArea = QTextEdit()
        self.button = QPushButton("Clear")

        v_box = QVBoxLayout()
        v_box.addWidget(self.textArea)
        v_box.addWidget(self.button)

        self.setWindowTitle("Text Edit")
        self.setLayout(v_box)

        self.button.clicked.connect(self.click)

        self.show()

    def click(self):
        self.textArea.clear()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
