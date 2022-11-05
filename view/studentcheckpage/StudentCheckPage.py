from pathlib import Path
from cgitb import text
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class StudentCheckPage(BasePage):
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
            font=("Inter", 12 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            511.0,
            318.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            44.0,
            84.0,
            anchor="nw",
            text="Classroom",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=919.0,
            y=8.0,
            width=70.0,
            height=31.0
        )
        self.button_2 = Button(
            text = "+",
            font = 30,
            command=self.plus_clicked,
            background="#F4E8DA",
            width= 2
            ).pack(side = "left",padx=50,pady = 120,anchor= "nw")



    def plus_clicked(self):
        if self.controller:
            self.controller.plusclick()
        
    
    def logout_clicked(self):
        if self.controller:
            self.controller.logoutclick()