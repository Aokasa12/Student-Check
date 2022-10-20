
import tkinter as tk
from controller.FrontPageController import FrontPageController
from helper.navigation.Navigation import Navigation
from view.frontpage.FrontPage import FrontPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Python Classroom')
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', exit)
        Navigation().initialization(self)
        Navigation().navigate(FrontPage,FrontPageController)

    def exit(self):
        self.destroy()

