from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.BasePage import BasePage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class FrontPage(BasePage):
    def __init__(self,parent : Tk,request):
        super().__init__(parent,request)
        self.parent.geometry("1300x820")
        self.parent.configure(bg = "#F4E8DA")

        self.canvas = Canvas(
            self.parent,
            bg = "#F4E8DA",
            height = 820,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            694.0,
            1300.0,
            704.0,
            fill="#6E675D",
            outline="")
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1300.0,
            115.0,
            fill="#DBC2AB",
            outline="")
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            650.0,
            409.0,
            image=self.image_image_1
        )
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.login_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=1134.936767578125,
            y=37.0,
            width=122.063232421875,
            height=48.0
        )
        self.canvas.create_text(
            38.0,
            37.0,
            anchor="nw",
            text="Student Check",
            fill="#6E675D",
            font=("Inter ExtraBold", 24 * -1)
        )
        self.canvas.create_rectangle(
            260.0,
            230.0,
            1096.0,
            753.0,
            fill="#B9AA9C",
            outline="")
        self.canvas.create_rectangle(
            221.0,
            188.0,
            1079.0,
            732.0,
            fill="#E6CDB9",
            outline="")
        self.canvas.create_rectangle(
            603.0,
            264.0,
            874.0,
            550.0,
            fill="#F4E8DA",
            outline="")
        self.canvas.create_text(
            345.0,
            303.0,
            anchor="nw",
            text="Student Check",
            fill="#6E675D",
            font=("Inter Bold", 36 * -1)
        )
        self.canvas.create_text(
            691.0,
            345.0,
            anchor="nw",
            text="ถูกออกแบบมาเพื่อเพิ่มความสะดวกสบาย\nให้แด่คณะอาจารย์ที่ต้องการตรวจสอบ\nการเข้าเรียนของนักศึกษา",
            fill="#464543",
            font=("Inter Regular", 16 * -1)
        )
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.information_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=466.0,
            y=575.0,
            width=212.0,
            height=58.0
        )
        self.canvas.create_rectangle(
            0.0,
            115.0,
            1300.0,
            125.0,
            fill="#6E675D",
            outline="")
    
    def information_clicked(self):
        if self.controller:
            self.controller.informationclick()
    
    def login_clicked(self):
        if self.controller:
            self.controller.login()
        