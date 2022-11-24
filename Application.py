
import tkinter as tk
from controller.FrontPageController import FrontPageController
from helper.navigation.Navigation import Navigation
from helper.database.Database import Database
from view.frontpage.FrontPage import FrontPage


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Python Classroom')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', exit)
        Database()
        Navigation().initialization(self)
        Navigation().navigate(FrontPage,FrontPageController)


    def exit(self):
        Database().__del__()
        self.destroy()

