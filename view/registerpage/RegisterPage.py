from pathlib import Path
from tkinter import  Canvas, Entry, Button, PhotoImage, Tk

from view.BasePage import BasePage





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class RegisterPage(BasePage):
    def __init__(self,parent : Tk):
        super().__init__()
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
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.confirmclicked,
            relief="flat"
        )
        self.button_1.place(
            x=125.0,
            y=389.0,
            width=157.0,
            height=53.0
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
            highlightthickness=0
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
            highlightthickness=0
        )
        self.entry_3.place(
            x=72.0,
            y=321.0,
            width=256.0,
            height=26.0
        )
        self.canvas.create_text(
            19.0,
            166.0,
            anchor="nw",
            text="Gmail",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.canvas.create_text(
            45.0,
            298.0,
            anchor="nw",
            text="Confirm Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )
        self.canvas.create_text(
            46.0,
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
            46.0,
            107.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.canvas.create_text(
            93.0,
            45.0,
            anchor="nw",
            text="Register",
            fill="#464543",
            font=("Inter Bold", 32 * -1)
        )
        
    def confirmclicked(self):
        if (self.controller):
            self.controller.confirmclick()