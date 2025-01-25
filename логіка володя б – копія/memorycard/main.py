
from PyQt5.QtWidgets import QWidget , QMessageBox
from card import *
from app import App
from data import *
from random import *
from menu import *
radio_list = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]
frm_card = 0 
form_list =[]
# Тестові данні
def testlist():

    frm = Question('Максимальна висота атмосфери', '11000м', '1100м', '5000м', '25000м')
    form_list.append(frm)
    frm = Question('Дім', 'house', 'horse', 'hurry', 'hour')
    form_list.append(frm)
    frm = Question('Найпопулярніша гра в світі', 'Minecraft', 'GTA V', 'Roblox', 'Cs:Go')
    form_list.append(frm)



win_card = QWidget()
win_menu = QWidget()

def set_card():
    win_card.resize(600,500)
    win_card.setWindowTitle("Memory Card")
    win_card.move(0,0)
    win_card.setLayout(main_line)

def set_menu():
    win_menu.resize(1000,600)
    win_menu.setWindowTitle("Memory Card")
    win_menu.move(0,0)
    win_menu.setLayout(main_menu_line)
    
def back_to_menu():
    win_card.hide()
    win_menu.show()

def back_to_test():
    win_card.hide()
    win_card.show()
btn_back.clicked.connect(back_to_test)
btn_menu.clicked.connect(back_to_menu)

def show_q():
    list_q.clear()
    for q in form_list:
        list_q.addItem(q.name)
testlist()
show_q()

def clear_q():
    line_ans.clear()
    line_correct.clear()
    line_false1.clear()
    line_false2.clear()
    line_false3.clear()
btn_clear.clicked.connect(clear_q)

def add():
    q_text = line_ans.text()
    q_correct = line_correct.text()
    q_text2 = line_false1.text()
    q_text2 = line_false2.text()
    q_text3 = line_false3.text()

    if q_text and q_correct and q_text2 and q_text3 and q_text3:
        new_q = Question(q_text, q_correct, q_text3, q_text2, q_text3)
        form_list.append(new_q)
        show_q()
        list_q.addItem(new_q.name)

    else:
        msg_box = QMessageBox()
        msg_box.setWindowTitle("помилка")
        msg_box.setText("Заповніть всі поля")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec_()

btn_add.clicked.connect(add)

def show_q():
    q = choice(form_list)
    lb_ans.setText(q.neme)
    answer = [q.corect,q.wrong2,q.wrong3]
    shuffle(answer)

    btn_ans1.setText(answer[0])     
    btn_ans1.setText(answer[1])     
    btn_ans1.setText(answer[2])     
    btn_ans1.setText(answer[3]) 
    return q 
def show_ans():
    show_q()
    AnswersGroupBox.hide()
    ResGroupBox.hide()
    btn_ans.setText("відповісти")
    RadioGroup.setExclusive(0)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(1)

    # if selected_button:
    #     if q.check(selected_button.text):
    #         lb_res.setText("Ви правельно ")
    #         if

btn_ans.clicked.connect(show_res)


   



set_card()
set_menu()
win_card.show()
App.exec_()