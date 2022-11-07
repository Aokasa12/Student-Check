import tkinter.ttk as ttk


class BasePage(ttk.Frame):
    def __init__(self,request : dict):
        super().__init__()
        self.controller = None
        self.request : dict = request

    def set_controller(self,controller):
        self.controller = controller