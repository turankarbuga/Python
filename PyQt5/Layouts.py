import sys
from PyQt5 import QtWidgets,QtGui


def Window():

    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setGeometry(300,300,600,500)
    window.show()

    okay = QtWidgets.QPushButton("Tamam")
    okay.show()
    cancel = QtWidgets.QPushButton("İptal")
    cancel.show()

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    window.setLayout(v_box)




    sys.exit(app.exec_())

Window()