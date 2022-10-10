from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
class CalculatorPageController(BaseController):
    def __init__(self, view):
        self.view = view
    
    def buttonclick(self,command):
        print(command)
        from controller.ForgotPasswordPageController import ForgotPasswordPageController
        from view.forgotpassword.ForgotPasswordPage import ForgotPasswordPage
        Navigation().navigate(ForgotPasswordPage,ForgotPasswordPageController)