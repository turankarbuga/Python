import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300,300,400,300)
        self.radioText = QLabel("What is the height of Mount Everest?")
        self.optionA = QRadioButton("8341 m")
        self.optionB = QRadioButton("8759 m")
        self.optionC = QRadioButton("8848 m")
        self.optionD = QRadioButton("9132 m")
        self.button = QPushButton("Choose")
        self.responseText = QLabel("")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radioText)
        v_box.addWidget(self.optionA)
        v_box.addWidget(self.optionB)
        v_box.addWidget(self.optionC)
        v_box.addWidget(self.optionD)
        v_box.addStretch()
        v_box.addWidget(self.responseText)
        v_box.addWidget(self.button)

        self.button.clicked.connect(lambda: self.click(self.optionA.isChecked(),self.optionB.isChecked(),self.optionC.isChecked(),self.optionD.isChecked()))

        self.setLayout(v_box)
        self.setWindowTitle("Radio Button.")
        self.show()

    def click(self,optionA,optionB,optionC,optionD):

        if optionA:
            self.responseText.setText("Wrong Answer!!")
        elif optionB:
            self.responseText.setText("Wrong Answer!!")
        elif optionC:
            self.responseText.setText("Correct Answer!!")
        elif optionD:
            self.responseText.setText("Wrong Answer!!")
        else:
            self.responseText.setText("Please choose one of them.")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())