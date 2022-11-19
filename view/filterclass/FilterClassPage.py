from view.BasePage import BasePage
from pathlib import Path
from tkinter import *
from tkinter import ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class FilterClassPage(BasePage):
    def __init__(self,parent : Tk,request):
        super().__init__(parent,request)
        self.width = 1024
        self.height = 795
        self.parent.geometry(f"{self.width}x{self.height}")
        self.parent.configure(bg = "#F4E8DA")

        self.topframe = Frame(self.parent,pady=3,bg="#DBC2AB",height=50,width=1024)
        self.topframe.pack_propagate(False)
        self.label = Label(self.topframe,text = "Student Check",background="#DBC2AB",font="Inter",padx=10,pady=10)
        self.label.pack(side=LEFT)


        self.image = PhotoImage(
            file=relative_to_assets("Vector.png"))

        self.back_button = Button(
            self.topframe,
            image=self.image,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat",
            bg="#DBC2AB",
            width=50
        
        )


        self.image3 = PhotoImage(
            file=relative_to_assets("Logout.png"))

        self.logout_button = Button(
            self.topframe,
            image=self.image3,
            borderwidth=0,
            highlightthickness=0,relief="flat",
            command=self.logout,
            bg="#DBC2AB",
            width=75
        
        )

        self.back_button.pack(side=RIGHT)
        self.logout_button.pack(side = RIGHT)


        self.topframe.pack(side=TOP)

        self.mainframe = Frame(self.parent,pady=3,bg="#F4E8DA",height=785,width=1024)
        self.mainframe.pack(side = TOP)
        self.mainframe.pack_propagate(False)

        self.label1 = Label(self.mainframe,text="Search",font=('Arial',12,"bold"),bg = '#F4E8DA')
        self.label1.pack(side = TOP,padx=(0,800),pady=10)

        self.filter_frame = Frame(self.mainframe,bg = "#F4E8DA",height=40,width=1024)
        self.filter_frame.pack_propagate(False)
        self.label2 = Label(self.filter_frame , text= "เลือกรหัสนักศึกษา",bg = "#F4E8DA",font=('Arial',12))



        self.label2.pack(side = LEFT,padx = (80,20))

        self.filter_frame_frame_input = Frame(self.filter_frame,width=200 ,height=30)
        self.filter_frame_frame_input.pack(side = LEFT)
        self.filter_frame.pack(side = TOP,pady = 10)

        self.choice = StringVar(value = "เลือกรายชื่อนักศึกษา")
        self.choice.trace("w", lambda name, index, mode, sv=self.choice: self.updateTable(self.choice))

        self.filter = ttk.Combobox(self.filter_frame_frame_input,font="Inter 12 bold",textvariable=self.choice,state="readonly")
        self.filter["values"] = tuple(request["studentLst"])
        self.filter.pack(side = LEFT)

        self.mainapplication = Frame(self.mainframe,bg = "#F4E8DA",height=800 , width=900)
        self.mainapplication.pack(side = TOP)
        self.mainapplication.pack_propagate(False)

        self.topTable = Frame(self.mainapplication,bg = "#DBC2AB",height=100 , width=900 )
        self.initTable()
        self.topTable.pack(side = TOP)


        self.maintable = Frame(self.mainapplication,bg = "black")
        self.canvas = Canvas(self.maintable,width=439,height=700,bg="#DBC2AB")
        self.scrollbar = Scrollbar(self.maintable, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)


        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        ))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)


        self.maintable.pack(side = TOP)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def initTable(self):
        self.e = Entry(self.topTable, width=12, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
        self.e.grid(row=0, column=0)
        self.e.insert(END, "วันที่")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")

        self.e = Entry(self.topTable, width=37, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
        self.e.grid(row=0, column=1)
        self.e.insert(END, "ประวัติ")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")

        self.e = Entry(self.topTable, width=24, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
    
    def insertData(self , historyLst):

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for i in range(len(historyLst)):
            self.e = Entry(self.scrollable_frame, width=12, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
            self.e.grid(row=i, column=0)
            self.e.insert(END, historyLst[i][0])
            self.e.configure(state='readonly',readonlybackground="#DBC2AB")

            self.e = Entry(self.scrollable_frame, width=35, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
            self.e.grid(row=i, column=1)
            self.e.insert(END, historyLst[i][1])
            self.e.configure(state='readonly',readonlybackground="#DBC2AB")

        

    def updateTable(self,choice):
        if (self.controller):
            self.controller.getHistory(self.request["classId"],choice.get())
        
        




    def logout(self):
        if (self.controller):
            self.controller.logout()
    def back(self):
        if (self.controller):
            self.controller.back()


        
