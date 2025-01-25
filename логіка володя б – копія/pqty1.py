from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint 
def click():
    num_win = randint(0,100)
    txt1.setText("переможець")
    txt2.setText(str(num_win))

app = QApplication([])
win1 =QWidget()
win1.resize(100,100)
win1.move(200,100)
win1.setWindowTitle("vosad")
txt1 = QLabel("нажми ")
txt2 = QLabel("?")
btn = QPushButton("нажми на мене")
btn.clicked.connect(click)
line = QVBoxLayout()
line.addWidget(txt1,alignment=Qt.AlignCenter)
line.addWidget(txt2,alignment=Qt.AlignCenter)
line.addWidget(btn,alignment=Qt.AlignCenter)
win1.setLayout(line)
win1.show()
app.exec_()