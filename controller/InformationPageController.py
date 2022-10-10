from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation


class InformationPageController(BaseController):
    def __init__(self, view):
        self.view = view
    
    def buttonclick(self,command):
        print(command)
        from view.calculatorpage.CalculatorPage import CalculatorPage
        from controller.CalculatorPageController import CalculatorPageController
        Navigation().navigate(CalculatorPage,CalculatorPageController)