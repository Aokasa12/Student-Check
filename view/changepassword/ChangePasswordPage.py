from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ChangePasswordPage(BasePage):
    def __init__(self,parent : Tk,request):
        super().__init__(request)
                
        
        parent.geometry("400x500")
        parent.configure(bg = "#F4E8DA")
        
        
        self.canvas = Canvas(
            parent,
            bg = "#F4E8DA",
            height = 500,
            width = 400,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            200.0,
            250.0,
            image=self.image_image_1
        )
        
        self.canvas.create_text(
            93.0,
            66.0,
            anchor="nw",
            text="Change Password",
            fill="#464543",
            font=("Inter Bold", 24 * -1)
        )
        
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.change_password,
            relief="flat"
        )
        self.button_1.place(
            x=181.0,
            y=344.0,
            width=167.0,
            height=60.0
        )
        
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            200.0,
            180.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0,show="*"
        )
        self.entry_1.place(
            x=72.0,
            y=167.0,
            width=256.0,
            height=25.0
        )
        
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            200.0,
            306.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0,show="*"
        )
        self.entry_2.place(
            x=72.0,
            y=293.0,
            width=256.0,
            height=25.0
        )
        
        self.canvas.create_text(
            53.0,
            143.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            61.0,
            207.0,
            anchor="nw",
            text="New Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_click,
            relief="flat"
        )
        self.button_2.place(
            x=302.0,
            y=8.0,
            width=88.0,
            height=36.0
        )
        
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            199.0,
            242.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0,show="*"
        )
        self.entry_3.place(
            x=71.0,
            y=229.0,
            width=256.0,
            height=25.0
        )
        
        self.canvas.create_text(
            53.0,
            269.0,
            anchor="nw",
            text="Confirm Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )
    def back_click(self):
        if (self.controller):
            self.controller.goToListPage()
    def change_password(self):
        if (self.controller):
            self.controller.change_password(self.entry_1.get(),self.entry_3.get(),self.entry_2.get())
        