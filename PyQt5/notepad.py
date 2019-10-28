import sys
import os
from PyQt5.QtWidgets import QWidget,QTextEdit,QPushButton,QVBoxLayout,QHBoxLayout,QApplication,QFileDialog
from PyQt5.QtWidgets import qApp,QAction,QMainWindow


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.textArea = QTextEdit()
        self.openButton = QPushButton("Open File")
        self.clearButton = QPushButton("Clear")
        self.saveButton = QPushButton("Save File")

        h_box = QHBoxLayout()
        h_box.addWidget(self.openButton)
        h_box.addWidget(self.clearButton)
        h_box.addWidget(self.saveButton)

        v_box = QVBoxLayout()
        v_box.addWidget(self.textArea)
        v_box.addLayout(h_box)

        self.clearButton.clicked.connect(self.clear)
        self.saveButton.clicked.connect(self.save_file)
        self.openButton.clicked.connect(self.open_file)

        self.setLayout(v_box)

    def clear(self):
        self.textArea.clear()

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))

        with open(file_name[0],"w") as file:
            file.write(self.textArea.toPlainText())

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))

        with open(file_name[0],"r") as file:
            self.textArea.setText(file.read())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = Window()
        self.setCentralWidget(self.window)
        self.setWindowTitle("Notepad App")
        self.show()

        self.create_menu()

    def create_menu(self):

        menubar = self.menuBar()
        file = menubar.addMenu("File")

        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clear = QAction("Clear",self)

        file_exit = QAction("Exit",self)
        file_exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear)
        file.addAction(file_exit)

        file.triggered.connect(self.response)

    def response(self,action):

        if action.text() == "Open File":
            self.window.open_file()
        elif action.text() == "Save File":
            self.window.save_file()
        elif action.text() == "Clear":
            self.window.clear()
        elif action.text() == "Exit":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
