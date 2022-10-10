from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
class ForgotPasswordPageController(BaseController):
    def __init__(self, view):
        self.view = view

    def buttonclick(self,command):
        print(command)
        from controller.LoginPageController import LoginPageController
        from view.loginpage.LoginPage import LoginPage
        Navigation().navigate(LoginPage,LoginPageController) #เปลี่ยนหน้าUI