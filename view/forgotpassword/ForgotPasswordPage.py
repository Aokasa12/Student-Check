from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
#import path เพื่อเชื่อมไฟล์กับasset(ไฟล์รูป)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ForgotPasswordPage(BasePage):
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
            command=self.button_clicked,
             relief="flat"
        )
        self.button_1.place(
            x=187.0,
            y=351.0,
            width=151.0,
            height=47.0
        )   
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            200.0,
            190.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F4E8DA",
            highlightthickness=0
        )
        self.entry_1.place(
            x=72.0,
            y=167.0,
            width=256.0,
            height=44.0
        )
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            200.0,
            283.0,
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
            height=44.0
        )

        self.canvas.create_text(
            47.0,
            143.0,
            anchor="nw",
            text="Gmail",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )
        self.canvas.create_text(
            55.0,
            236.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.canvas.create_text(
            284.0,
            273.0,
            anchor="nw",
            text="Send",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )
        self.canvas.create_text(
            93.0,
            66.0,
            anchor="nw",
            text="Forgot Password",
            fill="#464543",
            font=("Inter Bold", 24 * -1)
        )

    def button_clicked(self):
        if self.controller:
            self.controller.buttonclick("Hello World")



        