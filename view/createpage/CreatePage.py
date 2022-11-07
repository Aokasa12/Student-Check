
from view.BasePage import BasePage
from pathlib import Path
from tkinter import *





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

            

class CreatePage(BasePage):
    
    def __init__(self,parent : Tk,request):
        super().__init__(request)
        self.width = 1024
        self.height = 795
        self.parent = parent
        parent.geometry(f"{self.width}x{self.height}")



        #top Panel
        self.topframe = Frame(parent,pady=3,bg="#DBC2AB",height=50)
        self.topframe.grid(row = 0,sticky = "ews")



        self.label = Label(self.topframe,text = "Student Check",background="#DBC2AB",font="Inter",padx=10,pady=10)
        self.label.grid( row = 0,column=0)



        self.image = PhotoImage(
            file=relative_to_assets("Vector.png"))

        self.back_button = Button(
            self.topframe,
            image=self.image,
            borderwidth=0,
            highlightthickness=0,
            command= self.nav_back,
            relief="flat",
            bg="#DBC2AB",
            width=80
        
        )
        self.topframe.grid_columnconfigure(1, weight=1)
        self.back_button.grid(row = 0, column=1,sticky= "e")

        #upper panel
        self.semi_topframe = Frame(parent,padx = 20,pady=20,bg = "#F4E8DA",height=80)
        self.semi_topframe.grid(row= 1,sticky="ewns")

        self.label = Label(self.semi_topframe,text = "Classroom Name :  ",background="#F4E8DA",font= "Inter 15 bold")
        self.label.grid(row = 0 , column=0)

        self.semi_topframe_extend = Frame(self.semi_topframe,highlightbackground="black",highlightthickness=1,width=500,height=35,bg= "#DBC2AB")
        self.semi_topframe_extend.grid(row = 0, column=1)

        self.classname = Entry(self.semi_topframe_extend, font= "Inter 15 bold",bg= "#DBC2AB",width=55)
        self.classname.pack(side=LEFT)

        #main panel

        self.mainframe = Frame(parent,bg = "#F4E8DA")
        self.mainframe.grid(row = 2 ,sticky="nsw")

        self.ctr_left = Frame(self.mainframe, bg='#F4E8DA', width=112, height=190)
        self.ctr_right = Frame(self.mainframe, bg='#F4E8DA', width=112, height=190)
        self.viewbar = Frame(self.mainframe,bg = "#DBC2AB" , width=800,height=350)
        self.viewbar.grid_propagate(False)
        


        self.ctr_right.grid(row=0, column=2, sticky="ns")
        self.ctr_left.grid(row=0, column=0, sticky="ns")
    


        self.upper_canvas = Frame(self.viewbar,width=780)

        #InitTable
        self.e = Entry(self.upper_canvas, width=20, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16))
                 
        self.e.pack(side=LEFT)
        self.e.insert(END, "รหัสนักศึกษา")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")
        self.e = Entry(self.upper_canvas, width=45, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16))
                 
        self.e.pack(side =LEFT)
        self.e.insert(END, "รายชื่อนักศึกษา")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")


        self.upper_canvas.pack(side=TOP,padx=(0,24))
        self.canvas = Canvas(self.viewbar,width=800,height=350)
        self.scrollbar = Scrollbar(self.viewbar, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.entryLst = []

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback())

        self.e1 = Entry(self.scrollable_frame, width=20, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16),textvariable=sv)

        self.e1.grid(row=0, column=0)
        self.e1.insert(END, "")

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback())


        self.e2 = Entry(self.scrollable_frame, width=45, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16),textvariable=sv)
                 
        self.e2.grid(row=0, column=1)
        self.e2.insert(END, "")

        self.entryLst.append([self.e1,self.e2])

        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.viewbar.grid(row = 0 , column= 1,sticky="nsew")

        #semibottom pane
        self.semi_bottom = Frame(parent,bg = "#F4E8DA",height=100)
        self.semi_bottom.pack_propagate(False)
        self.semi_bottom.grid(row = 3,sticky="new")


        self.image2 = PhotoImage(
            file=relative_to_assets("Group.png"))

        self.save_button = Button(self.semi_bottom,image=  self.image2 , bg="#F4E8DA",borderwidth=0,
            highlightthickness=0,
            relief="flat",command= self.create_classroom)
        self.save_button.pack(side=RIGHT,padx=(0,100))


        #bottom pane
        self.bottom = Frame(parent, bg = "#F4E8DA",height=100)
        self.bottom.grid(row=  4,sticky="nswe" )



        

    def updateTable(self):
        #for i in range(len(data)):
        #    for j in range(len(data[0])):
        #        if (j == 0) :
        #            self.e = Entry(self.scrollable_frame, width=20, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
        #                           font=('Arial',16))
        #         
        #            self.e.grid(row=i, column=j)
        #            self.e.insert(END, data[i][j])
        #            self.e.configure(state='readonly',readonlybackground="#DBC2AB")
        #        else:
        #            self.e = Entry(self.scrollable_frame, width=45, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
        #                           font=('Arial',16))
        #         
        #            self.e.grid(row=i, column=j)
        #            self.e.insert(END, data[i][j])
        #            self.e.configure(state='readonly',readonlybackground="#DBC2AB")
        
        
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback())

        self.e1 = Entry(self.scrollable_frame, width=20, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16),textvariable=sv)

        self.e1.grid(row=len(self.entryLst), column=0)
        self.e1.insert(END, "")

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback())


        self.e2 = Entry(self.scrollable_frame, width=45, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16),textvariable=sv)
                 
        self.e2.grid(row=len(self.entryLst), column=1)
        self.e2.insert(END, "")

        self.entryLst.append([self.e1,self.e2])



    def changePage(self):
        if (self.controller):
            self.controller.buttonclick("Hello")

    def callback(self):
        data = self.entryLst[len(self.entryLst) - 1]
        if data[0].get() != "" or data[1].get() != "":
            self.updateTable()
            return

    def create_classroom(self):
        if (self.controller):
            self.controller.createClass(self.classname,self.entryLst)
    
    def nav_back(self):
        if (self.controller):
            self.controller.navBack()