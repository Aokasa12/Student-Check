from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class StudentCheckPage(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1300x820")

        self.resizable(False,False)

    def Label(self):
        self.backGroundImage = PhotoImage(file=relative_to_assets("Picturebk.png"))
        self.backGroundImageLabel = self.Label(self,image = self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)

if __name__ == "__main___":
    Stu = StudentCheckPage()
    Stu.Label()
    Stu.mainloop()