import tkinter.ttk as ttk
from tkinter import Tk


class BasePage(ttk.Frame):
    def __init__(self,parent : Tk,request : dict):
        super().__init__()
        self.controller = None
        self.parent = parent
        self.request : dict = request

    def set_controller(self,controller):
        self.controller = controller