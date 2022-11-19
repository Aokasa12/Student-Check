from tkinter import *
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Decision(Toplevel):
    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.geometry('320x230')
        self.title('Toplevel Window')
        self.configure(bg = "#F4E8DA")
        self.mode = IntVar()
        self.mode.set(0)
        self.canvas = Canvas(
            self,
            bg = "#F4E8DA",
            height = 230,
            width = 320,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            320.0,
            45.0,
            fill="#DBC2AB",
            outline="")

        self.canvas.create_text(
            20.0,
            15.0,
            anchor="nw",
            text="Student Check",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(2),
            relief="flat"
        )
        self.button_1.place(
            x=52.0,
            y=166.0,
            width=216.0,
            height=39.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(1),
            relief="flat"
        )
        self.button_2.place(
            x=52.0,
            y=61.0,
            width=216.0,
            height=41.0
        )

        self.canvas.create_text(
            52.0,
            166.0,
            anchor="nw",
            text="Delete",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(0),
            relief="flat"
        )
        self.button_3.place(
            x=264.0,
            y=9.0,
            width=27.0,
            height=29.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(3),
            relief="flat"
        )
        self.button_4.place(
            x=52.0,
            y=115.0,
            width=216.0,
            height=39.0
        )
    def changeMode(self,mode):
        self.mode.set(mode)
        self.exit()

    def exit(self):
        self.destroy()