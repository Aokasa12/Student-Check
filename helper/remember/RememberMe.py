import json

class RememberMe():
        
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
            self.file.close()
            return None

    
    

