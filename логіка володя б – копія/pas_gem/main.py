import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generation)

    def generation(self):
        singns = ""
        if self.ui.checkBox.isChecked():
            signs += "sdrekvzxbcvfsvjfhhtrnfbfbjtajtt"
        if self.ui.checkBox_2.isChecked():
            singns += "123456789"
        if self.ui.checkBox_3.isChecked():
            singns += "!@#$%^&*()"
        res = ""
        num = random.randint(8,12)
        for _ in range(num):
            res += random.choice(signs)
        self.ui.lineEdit.setText(res)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()