
from helper.singleton.singleton import singleton
from model.Teacher import Teacher
@singleton
class Context():
    def __init__(self):
        self.email = None
        self.username = None


    def set_email(self,email):
        self.email = email
    def get_email(self):
        return self.email
    def del_email(self):
        del self.email
    

    def set_username(self,username):
        self.username = username
    def get_username(self):
        return self.username
    def del_username(self):
        del self.username
