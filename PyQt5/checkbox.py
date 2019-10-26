import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QCheckBox,QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Checkbox")
        self.textLabel = QLabel("")
        self.button = QPushButton("Click")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.textLabel)
        v_box.addStretch()
        v_box.addWidget(self.button)


        self.setLayout(v_box)
        self.setWindowTitle("Checkbox")
        self.setGeometry(300,300,200,250)

        self.button.clicked.connect(lambda: self.click(self.checkbox.isChecked()))
        self.show()

    def click(self, checkbox):
        if checkbox:
            self.textLabel.setText("Checkbox is checked")
        else:
            self.textLabel.setText("Checkbox is not checked")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())