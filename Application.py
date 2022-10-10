
import tkinter as tk
from controller.LoginPageController import LoginPageController
from helper.navigation.Navigation import Navigation
from view.loginpage.LoginPage import LoginPage


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Python Classroom')
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', exit)
        Navigation().initialization(self)
        Navigation().navigate(LoginPage,LoginPageController)

    def exit(self):
        self.destroy()

