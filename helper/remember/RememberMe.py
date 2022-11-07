from helper.singleton.singleton import singleton
from model.Teacher import Teacher

import json

class RememberMe():
    def __init__(self) -> None:
        self.email = None
        self.password = None
        

    def save(self,email,password):
        try:
            self.file = open("storage.json","w")
            user = {
            "Email" : email,
            "Password" : password
            }


            json.dump(user,self.file)
            self.file.close()
        except Exception as e:
            print(e)

    

    def read(self):
        try:
            self.file = open("storage.json","r")
            json_object = json.load(self.file)
            self.file.close()
            return json_object
        except Exception as e:
            print(e)
            return None

    
    

