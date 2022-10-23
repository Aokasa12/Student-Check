from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class LoginPage(BasePage):
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
            125.0,
            66.0,
            anchor="nw",
            text="User Login",
            fill="#464543",
            font=("Inter Bold", 32 * -1)
)

        self.canvas.create_text(
            160.0,
            44.0,
            anchor="nw",
            text="Student Check",
            fill="#6E675D",
            font=("Inter SemiBold", 12 * -1)
)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.signinbuttonclicked,
            relief="flat"
)
        self.button_1.place(
            x=187.0,
            y=351.0,
            width=159.0,
            height=55.0
)
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.registerbuttonclicked,
            relief="flat"
)
        self.button_2.place(
            x=62.0,
            y=354.0,
            width=106.0,
            height=44.0
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
            65.0,
            143.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
)

        self.canvas.create_text(
            65.0,
            240.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter Regular", 12 * -1)
)
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command= self.forgotpasswordbuttonclicked,
            relief="flat"
)
        self.button_3.place(
            x=60.0,
            y=306.0,
            width=114.0,
            height=27.0 
)

    def registerbuttonclicked(self):
        if (self.controller):
            self.controller.registerclick()

    def signinbuttonclicked(self):
        if (self.controller):
            self.controller.signinclick("Hello World")
    
    def forgotpasswordbuttonclicked(self):
        if (self.controller):
            self.controller.forgotpasswordclick()