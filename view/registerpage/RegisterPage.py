from pathlib import Path
from tkinter import  *

from view.BasePage import BasePage





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class RegisterPage(BasePage):
    def __init__(self,parent : Tk,request : dict):
        super().__init__(parent,request)
        self.parent.geometry("400x500")
        self.parent.configure(bg = "#F4E8DA")

        self.canvas = Canvas(
            self.parent,
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
            150.0,
            45.0,
            anchor="nw",
            text="Register",
            fill="#464543",
            font=("Inter Bold", 32 * -1)
        )
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.confirmClick,
            relief="flat"
        )
        self.button_1.place(
            x=114.0,
            y=381.0,
            width=170.0,
            height=63.0
        )
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            200.0,
            204.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0
        )
        self.entry_1.place(
            x=72.0,
            y=190.0,
            width=256.0,
            height=26.0
        )
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            200.0,
            274.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0,show="*"
        )
        self.entry_2.place(
            x=72.0,
            y=260.0,
            width=256.0,
            height=26.0
        )
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            200.0,
            335.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0,show="*"
        )
        self.entry_3.place(
            x=72.0,
            y=321.0,
            width=256.0,
            height=26.0
        )
        self.canvas.create_text(
            65.0,
            166.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.canvas.create_text(
            65.0,
            298.0,
            anchor="nw",
        text="Confirm Password",
        fill="#000000",
        font=("Inter Regular", 12 * -1)
        )
        self.canvas.create_text(
            65.0,
            236.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            199.0,
            145.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0
        )
        self.entry_4.place(
            x=71.0,
            y=131.0,
            width=256.0,
            height=26.0
        )
        self.canvas.create_text(
            65.0,
            107.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.backClick,
            relief="flat"
        )
        self.button_2.place(
            x=308.0,
            y=8.0,
            width=77.0,
            height=37.0
        )
        
    def confirmClick(self):
        if (self.controller):
            self.controller.register(self.entry_1.get(),self.entry_2.get(),self.entry_3.get(),self.entry_4.get())

    def backClick(self):
        if self.controller:
            self.controller.navLogin()


