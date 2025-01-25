from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from notes import Ui_MainWindow
import json


import json
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_meke.clicked.connect(self.edd_note)

    def show_note(self):
        self.ui.list_1.clear()
        self.ui.list2.clear()
        print ( notes.keys())
        for note in notes.keys():
            self.ui.list_1.addItem(note)
            self.ui.list2.addItem(notes[note]["теги"])

def add_note(self):
    not_neme,ok = QInputDialog.getText(self,"додати замітку","назва замітки")
    if ok and not_neme != "":
        notes[not_neme] = {"теги":[],"тексе": ""} 

with open("notes.json","r",encoding="utf-8") as file:
    notes = json.load(file)

print(notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()