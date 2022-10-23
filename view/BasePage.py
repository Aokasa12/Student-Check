from abc import abstractmethod
import tkinter.ttk as ttk


class BasePage(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.controller = None

    def set_controller(self,controller):
        self.controller = controller
#setไว้ว่าทุกตัวที่มีBasePageต้องมีController