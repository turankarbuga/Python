import sys
from PyQt5 import QtWidgets,QtGui
from time import sleep

def Window():

    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt5")
    window.setGeometry(250,300,600,400)
    window.show()

    def click():

        window.close()

    button = QtWidgets.QPushButton(window)
    button.setText("Click for Exit.")
    button.move(260,335)
    button.show()
    button.clicked.connect(click)

    label1 = QtWidgets.QLabel(window)
    label1.setText("PyQt5 Lectures. Lecture #1")
    label1.move(130,30)
    label1.setFont(QtGui.QFont("Times",18))
    label1.show()

    label2 = QtWidgets.QLabel(window)
    label2.setPixmap(QtGui.QPixmap("python22.png"))
    label2.move(50,75)
    label2.show()







    sys.exit(app.exec_())



Window()