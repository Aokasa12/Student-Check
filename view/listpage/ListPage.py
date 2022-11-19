from email.mime import image
from tkinter import *
from pathlib import Path
from view.BasePage import BasePage





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ListPage(BasePage):
    def __init__(self,parent : Tk,request):
        super().__init__(parent,request)


        self.width = 1024
        self.height = 795
        self.parent.geometry(f"{self.width}x{self.height}")
        self.topframe = Frame(self.parent,pady=3,bg="#DBC2AB",height=50,width=1024)
        self.topframe.pack_propagate(False)
        self.label = Label(self.topframe,text = "Student Check",background="#DBC2AB",font="Inter",padx=10,pady=10)
        self.label.pack(side=LEFT)

        self.image = PhotoImage(
            file=relative_to_assets("Vector.png"))

        self.change_button = Button(
            self.topframe,
            image=self.image,
            borderwidth=0,
            highlightthickness=0,
            command= self.change_password,
            relief="flat",
            bg="#DBC2AB",
            width=100
        
        )

        self.image2 = PhotoImage(
            file=relative_to_assets("Logout.png"))

        self.logout_button = Button(
            self.topframe,
            image=self.image2,
            borderwidth=0,
            highlightthickness=0,
            command= self.logout,
            relief="flat",
            bg="#DBC2AB",
            width=100
        
        )

        self.change_button.pack(side=RIGHT)
        self.logout_button.pack(side = RIGHT)


        self.topframe.pack(side=TOP)

        self.bottom_frame = Frame(self.parent,bg ="#F4E8DA",height=745 ,width=1024)
        self.bottom_frame.pack_propagate(False)

        self.image3 = PhotoImage(
            file=relative_to_assets("Rectangle4.png"))

        self.backgroud = Label(self.bottom_frame,image = self.image3)
        self.backgroud.place(x = 18,y = 90)
        self.bottom_frame.pack()

        self.image4 = PhotoImage(
            file = relative_to_assets("Group9.png"))

        self.label1 = Label(self.bottom_frame,text="Classroom",font="Inter 15 bold",bg="#c4b09c")
        self.label1.pack(pady=(100,0),side=TOP)

        self.generate_classroom()

        self.image5 = PhotoImage(
            file = relative_to_assets("Group10.png"))

        self.add_button =  Button(
            self.bottom_frame,
            image=self.image5,
            borderwidth=0,
            highlightthickness=0,
            command= self.add_classroom,
            relief="flat",
            bg="#DBC2AB",
        
        )
        self.add_button.pack(side = TOP,padx=(0,900))
    def generate_classroom(self):
        data = self.request["classroom"]

        x = 60
        y = 145

        self.classLst = []
        for classroom in data:
            
            def classroom_pressed(classId = classroom.ClassID):
                self.classroom_pressed(classId)
            
            self.class_frame = Button(self.bottom_frame,image=self.image4,bg = "#b2917e",borderwidth=0,
            highlightthickness=0,
            relief="flat",)
            self.class_frame.config(command= classroom_pressed)#เพิ่มหรือเปลี่ยนแปลงคุณสมบัติทีหลัง
            self.class_frame.pack(side=TOP,pady=5)

            self.class_label = Label(self.bottom_frame,text=classroom.Name,bg = "#e0c4ac")
            self.class_label.place(x = x , y = y)
            self.class_label.bind("<Button-1>",classroom_pressed)#Button1คลิกซ้าย ให้Labelรับการคลิกด้วย
            y = y + 48
    
    def classroom_pressed(self,classId):
        if (self.controller):
            self.controller.choose_decision(classId)
    
    def add_classroom(self):
        if (self.controller):
            self.controller.add_classroom()
    def change_password(self):
        if (self.controller):
            self.controller.change_password()
    def logout(self):
        if (self.controller):
            self.controller.logout()



    

        



