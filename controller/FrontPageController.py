from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
from helper.remember.RememberMe import RememberMe

class FrontPageController(BaseController):
    def __init__(self, view):
        super().__init__(view)
    
    def login(self):

        remember = RememberMe()
        data = remember.read() 

        if (data is not None):
            self.request.update({"Email" : data["Email"]})
            self.request.update({"Password" : data["Password"]})
            
        from view.loginpage.LoginPage import LoginPage
        from controller.LoginPageController import LoginPageController
        Navigation().navigate(LoginPage,LoginPageController,self.request)