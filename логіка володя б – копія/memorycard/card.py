from app import App
from PyQt5.QtWidgets import QRadioButton,QLabel,QSpinBox,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout,QButtonGroup
from PyQt5.QtCore import Qt

btn_ans = QPushButton("відпочити")

btn_sleep = QPushButton("відпочити")
lb_min =QLabel("хвилин")
lb_ans = QLabel("запитаня")

btn_menu = QPushButton("меню")
box_min =   QSpinBox()
box_min.setValue(5)

btn_start = QPushButton("меню")
btn_ans1 = QRadioButton("1")
btn_ans2 = QRadioButton("2")
btn_ans3 = QRadioButton("3")
btn_ans4 = QRadioButton("4")

AnswersGroupBox = QGroupBox("варіант відовіді")
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)
line1 = QHBoxLayout()
line2 = QVBoxLayout()

line1.addWidget(btn_menu)
line1.addStretch(1)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)
line1.addWidget(lb_min)


line_btn_ans2 = QVBoxLayout()
line_btn_ans1 = QVBoxLayout()

line_btn_ans1.addWidget(btn_ans1)
line_btn_ans1.addWidget(btn_ans2)
line_btn_ans2.addWidget(btn_ans3)
line_btn_ans2.addWidget(btn_ans4)


mainline_btn_ans=QHBoxLayout()
mainline_btn_ans.addLayout(line_btn_ans1)
mainline_btn_ans.addLayout(line_btn_ans2)

AnswersGroupBox.setLayout(mainline_btn_ans)

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addStretch(1)
main_line.addWidget(lb_ans, stretch= 1,alignment=Qt.AlignCenter)
main_line.addStretch(1)

main_line.addWidget(AnswersGroupBox, stretch= 8)
main_line.addWidget(btn_ans)

ResGroupBox = QGroupBox("результат")
Lb_res = QLabel("правильність")
Lb_correct = QLabel("правельна відповідь")
line_res = QVBoxLayout()
line_res.addWidget(Lb_res)
line_res.addWidget(Lb_correct)
ResGroupBox.setLayout(line_res)

line_res = QVBoxLayout()
line_res.addWidget(Lb_res)
line_res.addWidget(Lb_correct)


ResGroupBox.setLayout(line_res)
main_line.addWidget(ResGroupBox)
ResGroupBox.hide()
main_line.addWidget(btn_ans)

def show_res():
    if btn_ans.text() == "відповісти":
        AnswersGroupBox.hide()
        ResGroupBox.show()
        btn_ans.setText("наступне питання")
