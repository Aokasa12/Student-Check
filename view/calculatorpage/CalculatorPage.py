from cgitb import text
from tkinter import *
from view.BasePage import BasePage


class CalculatorPage(BasePage):
    
    def __init__(self,parent : Tk):
        super().__init__()
        parent.geometry()
        parent.configure(bg = "#F4E8DA")

        self.label1 = Label(text="รัศมี",font=30).grid(row = 0,sticky=W)
        radius = IntVar()
        et1 = Entry(width=30,textvariable=radius,font = 30)
        et1.grid(row=0,column=1)

        self.label2 = Label(text="พื้นที่วงกลม",font = 30).grid(row = 1,sticky=W)
        et2 = Entry(width=30,font=30)
        et2.grid(row = 1,column=1)

        self.btn1 = Button(text="คำนวณ",command = self.changePage).grid(row = 2,column = 1,sticky=W)

    def changePage(self):
        if (self.controller):
            self.controller.buttonclick("Hellot")




