from tkinter import *
from tkinter.ttk import Labelframe
from PIL import ImageTk,Image

root = Tk()
root.title('Python')
root.geometry("1300x820")
root.configure(bg = "#F4E8DA")

frame = LabelFrame(root,width = 1024, height = 45,bg = "#DBC2AB").pack()
frame1 = LabelFrame(root,text = "Student Check",bg = "#DBC2AB")
frame1.place(x = 5,y =5)

b = Button(frame1, text = "Logout")
b.place(x = 100, y = 5)

frame2 = LabelFrame(root)
img = ImageTk.PhotoImage(Image.open("Rectangle 4.png"))

label = Label(frame2,image = img,anchor = 'center')
label.pack()

frame3 = Labelframe(root)
b2 = Button()

root.mainloop()