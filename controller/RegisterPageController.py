from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
import sys
class RegisterPageController(BaseController):
    def __init__(self, view):
        self.view = view


    def confirmclick(self):
        from controller.LoginPageController import LoginPageController
        from view.loginpage.LoginPage import LoginPage
        Navigation().navigate(LoginPage,LoginPageController)
