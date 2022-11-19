from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from view.BasePage import BasePage




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class InformationPage(BasePage):
    def __init__(self,parent : Tk,request):
        super().__init__(parent,request)
        self.parent.geometry("1024x600")
        self.parent.configure(bg = "#F4E8DA")
        self.canvas = Canvas(
            self.parent,
            bg = "#F4E8DA",
            height = 600,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
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
        self.canvas.create_text(
            44.0,
            84.0,
            anchor="nw",
            text="ต้องการเพิ่มรายละเอียด",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            61.0,
            117.0,
            anchor="nw",
            text="มาเรียน(ตัวเลือกเพิ่มเติม)\n\n   เข้าเรียนตรงเวลา\n\n   เข้าเรียนสาย\n\n   เรียนOnsite\n\n   เรียนOnline",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
        self.canvas.create_rectangle(
            56.0,
            258.0,
            66.0,
            268.0,
            fill="#000000",
            outline="")
        self.canvas.create_rectangle(
            56.0,
            343.0,
            66.0,
            353.0,
            fill="#000000",
            outline="")
        self.canvas.create_rectangle(
            56.0,
            373.0,
            66.0,
            383.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            403.0,
            66.0,
            413.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            433.0,
            66.0,
            443.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            463.0,
            66.0,
            473.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            493.0,
            66.0,
            503.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            198.0,
            66.0,
            208.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            63.0,
            288.0,
            anchor="nw",
            text="ขาดเรียน(ตัวเลือกเพิ่มเติม)\n\n   ขาดแบบไม่แจ้งล่วงหน้า\n\n   ขาดแบบแจ้งล่วงหน้า\n\n   ติดธุระ\n\n   ลาป่วย\n\n   Covid-19\n\n   อื่นๆ",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            978.0,
            10.0,
            1002.0,
            34.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            168.0,
            66.0,
            178.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            56.0,
            228.0,
            66.0,
            238.0,
            fill="#000000",
            outline="")

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
            x=56.0,
            y=528.0,
            width=151.0,
            height=32.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=234.0,
            y=528.0,
            width=151.0,
            height=32.0
        )

    def button_clicked(self):
        if self.controller:
            self.controller.buttonclick("Hello World")






