from tkinter import *
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AbsentCheck(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry('690x600')
        self.title('Toplevel Window')
        self.configure(bg = "#F4E8DA")

        self.topFrame = Frame(self,width=690,height=50,background="#DBC2AB")
        self.topFrame.pack(side= TOP)
        self.topFrame.pack_propagate(False)

        self.label = Label(self.topFrame,text = "Student  Check",font="Inter 15 bold",background="#DBC2AB")
        self.label.pack(side = LEFT,padx=(10,0))

        self.mainFrame = Frame(self,width=690,height=450,background="#F4E8DA")
        self.mainFrame.pack(side = TOP)
        self.mainFrame.pack_propagate(False)
        
        self.label1 = Label(self.mainFrame,text="รายละเอียดเพิ่มเติม",font="Inter 15 bold",background="#F4E8DA")
        self.label1.pack(side = TOP , padx=(0,350) , pady=15)

        self.label2 = Label(self.mainFrame,text="มาเรียน(ตัวเลือกเพิ่มเติม)",font="Inter 15",background="#F4E8DA")
        self.label2.pack(side = TOP , padx=(0,400),pady=5)

        self.choice = IntVar()
        self.choice.set(0)

        self.radio = Radiobutton(self.mainFrame,text = "ขาดแบบไม่แจ้งล่วงหน้า" , variable=self.choice,bg="#F4E8DA",value=1)
        self.radio.pack(side=TOP, padx=(0,310),pady=10)

        self.radio2 = Radiobutton(self.mainFrame,text = "ขาดแบบแจ้งล่วงหน้า" , variable=self.choice,bg="#F4E8DA",value=2)
        self.radio2.pack(side=TOP, padx=(0,320),pady=10)

        self.radio3 = Radiobutton(self.mainFrame,text = "ติดธุระ" , variable=self.choice,bg="#F4E8DA",value=3)
        self.radio3.pack(side=TOP, padx=(0,395),pady=10)

        self.radio4 = Radiobutton(self.mainFrame,text = "ลาป่วย" , variable=self.choice,bg="#F4E8DA",value=4)
        self.radio4.pack(side=TOP, padx=(0,395),pady=5)

        self.radio5 = Radiobutton(self.mainFrame,text = "Covid-19" , variable=self.choice,bg="#F4E8DA",value=5)
        self.radio5.pack(side=TOP, padx=(0,375),pady=5)

        self.tinyFrame = Frame(self.mainFrame,width=690,height=100,background="#F4E8DA")
        self.tinyFrame.pack_propagate(False)
        self.tinyFrame.pack(side = TOP ,pady=5)
        self.radio6 = Radiobutton(self.tinyFrame,text = "อื่นๆ (ไม่ควรเกิน 30 ตัวอักษร)" , variable=self.choice,bg="#F4E8DA",value=6)
        self.radio6.pack(side=TOP, padx=(0,295),pady=5)
        self.txt = StringVar()
        self.entry = Entry(self.tinyFrame,textvariable=self.txt,width=40 ,bg="#DBC2AB")
        self.entry.pack(side = TOP,padx=(0,200))


        self.bottomFrame = Frame(self.mainFrame,width=690 ,height=150,background="#F4E8DA")
        self.bottomFrame.pack_propagate(False)
        self.bottomFrame.pack(side = TOP)

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.bottomFrame,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.reset,
            relief="flat"
        )

        self.button_2.pack(side = LEFT , padx=(50,0))

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.bottomFrame,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.confirm,
            relief="flat"
        )

        self.button_3.pack(side = LEFT, padx=(50,0))
        
    def reset(self):
        self.choice.set(0)


    def confirm(self):
        self.destroy()
    
        
        
        