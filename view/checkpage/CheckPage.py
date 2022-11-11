from view.BasePage import BasePage
from pathlib import Path
from tkinter import *
import datetime
from model.CheckInBox import CheckInBox
from model.CheckIn import CheckIn

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

            

class CheckPage(BasePage):
    
    def __init__(self,parent : Tk , request):
        super().__init__(parent,request)


        self.date = None
        self.width = 1024
        self.height = 795
        self.parent.geometry(f"{self.width}x{self.height}")
        self.parent.configure(bg = "#F4E8DA")
        self.topframe = Frame(self.parent,pady=3,bg="#DBC2AB",height=50,width=1024)
        self.topframe.pack_propagate(False)
        self.label = Label(self.topframe,text = "Student Check",background="#DBC2AB",font="Inter",padx=10,pady=10)
        self.label.pack(side=LEFT)

        self.รูปวันที่ = PhotoImage(
            file = relative_to_assets("Group13.png")
        )

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

        self.image2 = PhotoImage(
            file=relative_to_assets("Vector2.png"))

        self.home_button = Button(
            self.topframe,
            image=self.image2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
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
        self.home_button.pack(side = RIGHT)
        self.logout_button.pack(side = RIGHT)


        self.topframe.pack(side=TOP)


        self.mainframe = Frame(self.parent,pady=3,bg="#F4E8DA",height=785,width=1024)
        self.mainframe.pack(side = TOP)
        self.mainframe.pack_propagate(False)

        self.label1 = Label(self.mainframe,text="Check",font=('Arial',12,"bold"),bg = '#F4E8DA')
        self.label1.pack(side = TOP,padx=(0,800),pady=10)

        self.date_frame = Frame(self.mainframe,bg = "#F4E8DA",height=40,width=1024)
        self.date_frame.pack_propagate(False)
        self.label2 = Label(self.date_frame , text= "กรอก วัน/เดือน/ปี(ค.ศ.) ที่ต้องการเช็คชื่อ ",bg = "#F4E8DA",font=('Arial',12))



        self.label2.pack(side = LEFT,padx = (0,0))

        self.date_frame_input = Frame(self.date_frame , bg = "#DBC2AB",width=200 ,height=30)
        self.date_frame_input.pack(side = LEFT)
        self.date_frame.pack(side = TOP,pady = 10)
        self.date_frame_input.pack_propagate(False)

        self.date_time = Button(self.date_frame_input,image = self.รูปวันที่,bg = "#F4E8DA",
            borderwidth=0,
            highlightthickness=0,relief="flat", command=self.calendar)
        self.date_time.pack(side = LEFT)

        self.date_label = Label(self.date_frame_input,text="กรุณากรอกวันที่",bg = "#DBC2AB",font="Inter 12 bold")
        self.date_label.pack(side = LEFT,padx=(20,0))

        self.exportButton = PhotoImage(
            file=relative_to_assets("Group5.png"))
        self.export_button = Button(self.date_frame,image=self.exportButton,bg = "#F4E8DA",borderwidth=0,highlightthickness=0,relief="flat",command=self.export)
        self.export_button.pack(side = RIGHT , padx = (0,30))

        




        self.mainapplication = Frame(self.mainframe,bg = "#DBC2AB",height=800 , width=900)
        self.mainapplication.pack(side = TOP)
        self.mainapplication.pack_propagate(False)

        self.topTable = Frame(self.mainapplication,bg = "#DBC2AB",height=100 , width=900 )
        self.initTable()
        self.topTable.pack(side = TOP)


        

        self.emptybox = PhotoImage(
            file=relative_to_assets("Rectangle.png"))

        self.checkbox = PhotoImage(
            file=relative_to_assets("Group.png"))


        self.maintable = Frame(self.mainapplication,bg = "black")
        self.canvas = Canvas(self.maintable,width=880,height=700,bg="#F4E8DA")
        self.scrollbar = Scrollbar(self.maintable, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        ))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.datalst = []

        self.insertData(self.request["checkInLst"])





        self.maintable.pack(side = TOP)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")




    


    def initTable(self):
        self.e = Entry(self.topTable, width=12, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
        self.e.grid(row=0, column=0)
        self.e.insert(END, "รหัสนักศึกษา")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")

        self.e = Entry(self.topTable, width=37, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
        self.e.grid(row=0, column=1)
        self.e.insert(END, "รายชื่อนักศึกษา")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")

        self.e = Entry(self.topTable, width=24, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
        self.e.grid(row=0, column=2)
        self.e.insert(END, "มาเรียน")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")

        self.e = Entry(self.topTable, width=24, fg='black',bg="#DBC2AB",highlightbackground="black",highlightthickness=1,justify=CENTER,
                                   font=('Arial',12))
                 
        self.e.grid(row=0, column=3)
        self.e.insert(END, "ขาดเรียน")
        self.e.configure(state='readonly',readonlybackground="#DBC2AB")


    def insertData(self , checkInLst,enable = False):

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.datalst.clear()
        for i in  range(len(checkInLst)):

            data: CheckIn = checkInLst[i]

            self.e = Frame(self.scrollable_frame, width=115,height= 30, bg="#DBC2AB",highlightbackground="black",highlightthickness=1,)
            self.l = Label(self.e, width=114,fg='black',bg="#DBC2AB",text=data.StudentID,font=('Arial',12))
            self.e.pack_propagate(False)
            self.e.grid(row = i,column=0)
            self.l.pack(side=LEFT)

            self.e = Frame(self.scrollable_frame, width=339,height= 30, bg="#DBC2AB",highlightbackground="black",highlightthickness=1,)
            self.l = Label(self.e, width=546,fg='black',bg="#DBC2AB",text=data.Name,font=('Arial',12))
            self.e.pack_propagate(False)
            self.e.grid(row = i,column=1)
            self.l.pack(side=LEFT)



            self.leftFrame = Frame(self.scrollable_frame, width=222,height= 30, bg="#DBC2AB",highlightbackground="black",highlightthickness=1,)

            if (enable):
                def func(studentId = data.StudentID):
                    if (self.controller):
                        self.controller.box_clicked(studentId,"left",self.datalst,self.request["classId"],self.date)
                if (data.ComeCheck == 0):
                    self.leftbox = Button(self.leftFrame , image=self.emptybox,borderwidth=0,
                        highlightthickness=0,relief="flat",command=func)
                else:
                    self.leftbox = Button(self.leftFrame , image=self.checkbox,borderwidth=0,
                        highlightthickness=0,relief="flat",command=func)
            else:
                self.leftbox = Button(self.leftFrame , image=self.emptybox,borderwidth=0,
                    highlightthickness=0,relief="flat")

            self.leftFrame.pack_propagate(False)
            self.leftFrame.grid(row = i,column=2)
            self.label1 = Label(self.leftFrame, text=data.ComeReason , bg="#DBC2AB")
            self.label1.pack(side = RIGHT , padx=(0,15) , pady=(0,4))
            self.leftbox.pack(side=TOP)

    
            self.rightFrame = Frame(self.scrollable_frame, width=222,height= 30, bg="#DBC2AB",highlightbackground="black",highlightthickness=1,)
            if (enable):
                def func(studentId = data.StudentID):
                    if (self.controller):
                        self.controller.box_clicked(studentId,"right",self.datalst,self.request["classId"],self.date)
                if (data.AbsentCheck == 0):
                    self.rightbox = Button( self.rightFrame, image=self.emptybox,borderwidth=0,
                    highlightthickness=0,relief="flat",command=func)
                else:
                    self.rightbox = Button( self.rightFrame, image=self.checkbox,borderwidth=0,
                    highlightthickness=0,relief="flat",command=func)
            else:
                self.rightbox = Button( self.rightFrame, image=self.emptybox,borderwidth=0,
                    highlightthickness=0,relief="flat")
            self.rightFrame.pack_propagate(False)
            self.label2 = Label(self.rightFrame, text=data.AbsentReason , bg="#DBC2AB")
            self.rightFrame.grid(row = i,column=3)
            self.label2.pack(side = RIGHT , padx=(0,15) , pady=(0,4))
            self.rightbox.pack(side=TOP)

            self.datalst.append(CheckInBox(data.StudentID,data.ComeCheck,data.AbsentCheck,self.label1,self.label2,self.leftbox,self.rightbox))


                

            




        

    def logout(self):
        if (self.controller):
            self.controller.logout()
    def back(self):
        if (self.controller):
            self.controller.back()
    
    def calendar(self):
        if (self.controller):
            date = self.controller.calendar()
            if (date == ""):
                return
            date = date.split("/")
            date = datetime.date(int("20" + date[2]),int(date[0]),int(date[1]))
            self.date = date
            self.date_label.config(text = date.strftime("%d/%m/%y"))
            self.controller.newData(date,self.request["classId"])

    def export(self):
        if (self.controller):
            self.controller.export(self.request["classId"],self.date)

