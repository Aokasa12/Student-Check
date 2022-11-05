from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
import sys
#if "InformationPageController" not in sys.modules:
#    from controller.InformationPageController import InformationPageController
class LoginPageController(BaseController):
    def __init__(self, view):
        self.view = view


    def registerclick(self):
        from controller.RegisterPageController import RegisterPageController
        from view.registerpage.RegisterPage import RegisterPage
        Navigation().navigate(RegisterPage,RegisterPageController)
    
    def signinclick(self,command):
        print(command)
        from controller.StudentCheckController import StudentCheckController
        from view.studentcheckpage.StudentCheckPage import StudentCheckPage
        Navigation().navigate(StudentCheckPage,StudentCheckController)
    
    def forgotpasswordclick(self):
        from controller.ForgotPasswordPageController import ForgotPasswordPageController
        from view.forgotpassword.ForgotPasswordPage import ForgotPasswordPage
        Navigation().navigate(ForgotPasswordPage,ForgotPasswordPageController)