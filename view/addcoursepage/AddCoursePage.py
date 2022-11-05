# Python program to create a table
from pathlib import Path
from cgitb import text
from tkinter import *
from view.BasePage import BasePage


class AddCoursePage(BasePage):
	def __init__(self,parent : Tk):
		super().__init__()
		parent.title("Student Check")
		parent.geometry("1024x600")
		parent.configure(bg = "#F4E8DA")

		self.canvas = Canvas(
            parent,
            bg = "#F4E8DA",
            height = 600,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

		self.canvas.place(x = 0, y = 0)
		self.canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            45.0,
            fill="#DBC2AB",
            outline="")

		self.canvas.create_text(
            20.0,
            15.0,
            anchor="nw",
            text="Student Check",
            fill="#464543",
            font=("Inter", 12 * -1))

		self.Label1 = Label(text="Classroom Name : ",font = ("Inter",18 * 1),bg = "#F4E8DA",).pack(side = "left",padx=70,pady = 90,anchor= "n")
		txt = StringVar
		self.Subject = Entry(textvariable=txt,bg="#DBC2AB").place(x= 300,y = 92,width=600,height=30)
		
	
		scroll_bar = Scrollbar(self)
		scroll_bar.pack( side = RIGHT,fill = Y )
		mylist = Listbox(yscrollcommand = scroll_bar.set )
		mylist.pack( side = LEFT, fill = BOTH ,padx=70,pady=90,anchor="n")
		scroll_bar.config( command = mylist.yview )
   

   

		# code for creating table
		#for i in range(total_rows):
			#for j in range(total_columns):
				#self.e = Entry(self, width=20, fg='blue',
							#font=('Arial',16,'bold'))
				
				#self.e.grid(row=i, column=j)
				#self.e.insert(END, lst[i][j])
		# take the data
		#lst = [(1,'Raj','Mumbai',19),
		#(2,'Aaryan','Pune',18),
		#(3,'Vaishnavi','Mumbai',20),
		#(4,'Rachna','Mumbai',21),
		#(5,'Shubham','Delhi',21)]

		# find total number of rows and
		# columns in list
		#total_rows = len(lst)
		#total_columns = len(lst[0])

