from calendar import c
from tkinter import *
from tkinter.ttk import Labelframe
from turtle import right
from PIL import ImageTk,Image

root = Tk()
root.title('Python')
root.geometry("1300x820")
root.configure(bg = "#F4E8DA")

def logoutclick():
    print("Hello")
def plusclick():
    print("GG")
    bp = Button(frame1,text = "เพิ่มรายวิชา",bg="#DBC2AB",command = plusclick,height=2,width=170)


frame = LabelFrame(root,width = 1310, height = 40,bg = "#DBC2AB")
frame.place(relx =.5, rely = .0,anchor= "n")
b = Button(frame, text = "Logout",bg = "#DBC2AB",command=logoutclick)
b.place(x = 1225,y=6)
a = Label(text = "StudentCheck",bg = "#DBC2AB",font=15).place(x = 10, y = 6)
frame1 = LabelFrame(root, width=1260,height=740,bg = "#B3947F").place(x = 20, y = 60)
bp = Button(frame1,text = "เพิ่มรายวิชา",bg="#DBC2AB",command = plusclick,height=2,width=170)
bp.place(x = 50, y = 100)


root.mainloop()