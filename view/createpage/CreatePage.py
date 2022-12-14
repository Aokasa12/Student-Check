
from view.BasePage import BasePage
from pathlib import Path
from tkinter import *
from model.Classroom import Classroom




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

            

class CreatePage(BasePage):
    
    def __init__(self,parent : Tk,request):
        super().__init__(parent,request)
        self.width = 1024
        self.height = 795
        self.parent.geometry(f"{self.width}x{self.height}")



        #top Panel
        self.topframe = Frame(self.parent,pady=3,bg="#DBC2AB",height=50)
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
        self.semi_topframe = Frame(self.parent,bg = "#F4E8DA",height=80)
        self.semi_topframe.grid(row= 1,sticky="ewns",padx = 20,pady=(20,0))

        self.label = Label(self.semi_topframe,text = "Classroom Name :  ",background="#F4E8DA",font= "Inter 15 bold")
        self.label.grid(row = 0 , column=0)

        self.semi_topframe_extend = Frame(self.semi_topframe,highlightbackground="black",highlightthickness=1,width=500,height=35,bg= "#DBC2AB")
        self.semi_topframe_extend.grid(row = 0, column=1)

        self.classroom_name = StringVar()
        self.classroom_name.trace("w", lambda name, index, mode, sv=self.classroom_name: self.find_class())#ถ้ามีตัวอักษรพิมพ์ไปให้ใช้self.find_class

        self.classname = Entry(self.semi_topframe_extend, font= "Inter 15 bold",bg= "#DBC2AB",width=55,textvariable=self.classroom_name)

        self.classname.pack(side=LEFT)

        #main panel

        self.mainframe = Frame(self.parent,bg = "#F4E8DA")
        self.mainframe.grid(row = 3 ,sticky="swe")

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
        self.e.insert(END, "รหัสนักศึกษา")#ใส่ชื่อในช่องนั้น
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")#read only
        self.e = Entry(self.upper_canvas, width=45, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,
                                   font=('Arial',16))
                 
        self.e.pack(side =LEFT)
        self.e.insert(END, "รายชื่อนักศึกษา")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")


        self.upper_canvas.pack(side=TOP,padx=(0,24))
        self.canvas = Canvas(self.viewbar,width=800,height=350)
        self.scrollbar = Scrollbar(self.viewbar, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(#กำหนดความสามารถพิเศษ frameที่เลื่อนขึ้นเลื่อนลงได้
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.entryLst = []

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback())#เขียนค่า,callbackขึ้นบรรทัดใหม่

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
        self.semi_bottom = Frame(self.parent,bg = "#F4E8DA",height=100)
        self.semi_bottom.pack_propagate(False)
        self.semi_bottom.grid(row = 4,sticky="new")


        self.image2 = PhotoImage(
            file=relative_to_assets("Group.png"))

        self.save_button = Button(self.semi_bottom,image=  self.image2 , bg="#F4E8DA",borderwidth=0,
            highlightthickness=0,
            relief="flat",command= self.create_classroom)
        self.save_button.pack(side=RIGHT,padx=(0,100))


        #bottom pane
        self.bottom = Frame(self.parent, bg = "#F4E8DA",height=100)
        self.bottom.grid(row=  5,sticky="nswe" )





        #Outer Frame
        self.filter_frame = Frame(self.parent ,bg = "#F4E8DA" )
        self.filter_frame.grid(row = 2 , sticky = "n",padx=(0,12),pady=(0,20))
        



        

    def updateTable(self):
        
        
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



    def callback(self):
        data = self.entryLst[len(self.entryLst) - 1]
        if data[0].get() != "" or data[1].get() != "":
            self.updateTable()
            return

    def create_classroom(self):
        if (self.controller):
            self.controller.createClass(self.classroom_name.get(),self.entryLst)
    
    def nav_back(self):
        if (self.controller):
            self.controller.navBack()
    def find_class(self):
        if (self.controller):
            data = self.controller.find_class(self.classroom_name.get())
            self.insert_filter(data)
    def insert_filter(self,data):
        for widget in self.filter_frame.winfo_children():
            widget.destroy()
        if len(self.filter_frame.winfo_children()) == 0:
            tmp = Frame(self.filter_frame, width=1, height=1, borderwidth=0, highlightthickness=0)
            tmp.pack()
            self.parent.update_idletasks()
            tmp.destroy()

        
        if data:
            for i in data:
                classname = i[0]
                frame = Frame(self.filter_frame,width=600,height=30,bg="#FFFFFF")
                label = Label(frame,text = classname,bg = "#FFFFFF",font=('Arial',16))
                label.pack(side=LEFT,padx=(20,0))

                def click_frame(event,name = classname):
                    self.classroom_name.set(name)

                frame.bind("<Button-1>",click_frame)
                label.bind("<Button-1>",click_frame)

                frame.pack(side = TOP)
                frame.pack_propagate(False)
        
