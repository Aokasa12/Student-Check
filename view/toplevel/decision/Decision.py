from tkinter import *
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Decision(Toplevel):
    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.geometry('320x200')
        self.title('Toplevel Window')
        self.configure(bg = "#F4E8DA")
        self.mode = IntVar()
        self.mode.set(0)
        self.canvas = Canvas(
            self,
            bg = "#F4E8DA",
            height = 200,
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
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(0),
            relief="flat"
        )
        self.button_1.place(
            x=272.0,
            y=11.0,
            width=26.0,
            height=24.0
        )
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(1),
            relief="flat"
        )
        self.button_2.place(
            x=52.0,
            y=80.0,
            width=216.0,
            height=39.0
        )
        
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(2),
            relief="flat"
        )
        self.button_3.place(
            x=52.0,
            y=136.0,
            width=216.0,
            height=39.0
        )
    def changeMode(self,mode):
        self.mode.set(mode)
        self.exit()

    def exit(self):
        self.destroy()