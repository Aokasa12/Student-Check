from view.BasePage import BasePage
class BaseController:
    def __init__(self,view):
        self.view = view
        self.request = dict()

