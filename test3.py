from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Python')
root.geometry("1300x820")

frame = LabelFrame(root, text = "Student Check",bg = "#F4E8DA")
frame.pack()

b = Button(frame, text = "Logout")
b.pack()

root.mainloop()