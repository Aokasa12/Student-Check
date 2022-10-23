from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


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

        self.canvas.create_text(
            115.0,
            66.0,
            anchor="nw",
            text="Forgot Password",
            fill="#464543",
            font=("Inter Bold", 24 * -1)
        )
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.login_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=179.0,
            y=344.0,
            width=167.0,
            height=61.0
        )
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            200.0,
            190.0,
            image= self.entry_image_1
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
        self.canvas.create_text(
            65.0,
            143.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.login_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=308.0,
            y=8.0,
            width=77.0,
            height=34.0
        )

    def login_clicked(self):
        if self.controller:
            self.controller.loginclick()