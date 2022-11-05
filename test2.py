from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()

# w = Frame ( master, option, ... )

  """frame1 = LabelFrame(root, width=1260,height=740,bg = "#B3947F").place(x = 20, y = 60)

        bp = Button(frame1,text = "เพิ่มรายวิชา",bg="#DBC2AB",command = plusclick,height=2,width=170)
        bp.place(x = 50, y = 100)

        photo = PhotoImage(file=relative_to_assets("Rectangle4.png"))
        photoimage = photo.subsample(1,1)
        ph = Label(root,image=photoimage).place(x = 20, y = 60) 

        frame = LabelFrame(root,width = 1310, height = 40,bg = "#DBC2AB")
        frame.place(relx =.5, rely = .0,anchor= "n")

        b = Button(frame, text = "Logout",bg = "#DBC2AB",command=logoutclick)
        b.place(x = 1225,y=6)
        a = Label(text = "Student Check",bg = "#DBC2AB",font=15).place(x = 10, y = 6)"""
