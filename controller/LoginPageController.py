from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
import sys
#if "InformationPageController" not in sys.modules:
#    from controller.InformationPageController import InformationPageController
class LoginPageController(BaseController):
    def __init__(self, view):
        self.view = view


    def buttonclick(self,command):
        print(command)
        from controller.InformationPageController import InformationPageController
        from view.informationpage.InformationPage import InformationPage
        Navigation().navigate(InformationPage,InformationPageController)