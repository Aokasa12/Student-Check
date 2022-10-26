from tkinter import *

master = Tk()

master.configure(background='#F4E8DA')
master.columnconfigure(1, weight = 2)

nb_of_columns = 4 # to be replaced by the relevant number
titleframe = Frame(master, bg ="#DBC2AB")
titleframe.grid(row=0, column=0, columnspan=nb_of_columns, sticky='ew')
titlelabel = Label(titleframe, text="Student Check",font = 12,bg ="#DBC2AB")
titlelabel.grid(row = 1, column=1,padx = 10)
# other widgets on the same row:
space1 = Label(titleframe,text = "",bg = "#DBC2AB").grid(row = 2,column = 3)
Button(titleframe,font = 16, text='Logout', bg = "#DBC2AB").grid(row = 1,column = 4,padx = 1100)
master.geometry('1300x820')
master.mainloop() 