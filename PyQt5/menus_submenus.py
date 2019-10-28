import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")

        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        exit_file = QAction("Exit",self)
        exit_file.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(exit_file)

        clear = QAction("Clear",self)
        edit.addAction(clear)

        find = edit.addMenu("Find")
        find_in_path = QAction("Find in Path..",self)
        replace_in_path = QAction("Replace in Path..",self)

        find.addAction(find_in_path)
        find.addAction(replace_in_path)

        exit_file.triggered.connect(self.do_exit)
        file.triggered.connect(self.response)

        self.setWindowTitle("Menu")
        self.setGeometry(300,300,300,200)
        self.show()

    def do_exit(self):
        qApp.quit()

    def response(self,action):

        if action.text() == "Open File":
            print("triggered open file")
        elif action.text() == "Save File":
            print("triggered save file")
        elif action.text() == "Exit":
            print("triggered exit")


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
