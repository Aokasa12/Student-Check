from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
import sys

class StudentCheckController(BaseController):
    def __init__(self, view):
        self.view = view


    def logoutclick(self):
        from controller.FrontPageController import FrontPageController
        from view.frontpage.FrontPage import FrontPage
        Navigation().navigate(FrontPage,FrontPageController)
    
    def plusclick(self):
        from controller.AddCourseController import AddCourseController
        from view.addcoursepage.AddCoursePage import AddCoursePage
        Navigation().navigate(AddCoursePage,AddCourseController)
 
