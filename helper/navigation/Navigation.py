from tkinter import Tk
from controller.BaseController import BaseController
from helper.singleton.singleton import singleton
from view.BasePage import BasePage


@singleton
class Navigation():
    def __init__(self : Tk):
        self.window : Tk = None
    
    def initialization(self,window):
        if (self.window == None):
            self.window = window
    
    def navigate(self,Page : BasePage,Controller  : BaseController , request : dict = dict()):

        self.clear()

        view = Page(self.window ,request)

        controller = Controller(view)

        view.set_controller(controller)
    
    def clear(self):
        for widget in self.window.winfo_children(): #เข้าไปในทุกwidgetที่เป็นไปได้
            widget.destroy()
