from dataclasses import dataclass
from tkinter import *
@dataclass
class CheckInBox:

    StudentID : str
    ComeCheck : int
    AbsentCheck : int
    LeftLabel : Label
    RightLabel : Label
    LeftButton : Button
    RightButton : Button
