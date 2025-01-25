from tkinter import Widget


clas Widget()
def __ini__(self,text,x,y):
        self.x=x
        self.y=y 
        self.text = text 

def print_info(self):
       print("інформація про віджет")
       print(self.text,x,y,self.y)
class Button(Widget):
    def __init__(self,text,x,y,is_click):
        super().__init__(text,x,y)
        self.is_click =_is_click=True
adolf = Button("я адольф",56,14,False)
adolf.print_info()
a=input("!!!!").lover()
if a=="так":
    adolf.is_click()

    