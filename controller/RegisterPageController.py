from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
from model.Teacher import Teacher
from dao.TeacherDAOImpl import TeacherDAOImpl
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError #Library for check email
import bcrypt


class RegisterPageController(BaseController):
    def __init__(self, view ):
        super().__init__(view)
        self.teacherDAO = TeacherDAOImpl()


    def register(self,email,password,cPassword,username):
        try:
            if password != cPassword:
                messagebox.showerror("Error", "Password ไม่ถูกต้อง")
                return

            if (self.email_validate(email) is False):
                messagebox.showerror("Error", "ได้โปรดใส่ Email ที่ถูกต้อง")
                return

            teacher = self.teacherDAO.find(email)

            if teacher is not None:
                messagebox.showerror("Error", "Email นี้มีผู้ใช้อยู่แล้ว")
                return
            

            bytes = password.encode('utf-8')#bcryptต้องใช้utf-8

            salt = bcrypt.gensalt()

            hash = bcrypt.hashpw(bytes,salt)

            teacher = Teacher(Email=email,Username=username,Password=hash.decode('utf-8'))

            self.teacherDAO.save(teacher)

            messagebox.showinfo("Success" , "สมัครสมาชิกเสร็จสิ้น")

            from view.loginpage.LoginPage import LoginPage
            from controller.LoginPageController import LoginPageController
            Navigation().navigate(LoginPage,LoginPageController)

        except Exception as e:
            print(e)
        



    def navLogin(self):
        from controller.LoginPageController import LoginPageController
        from view.loginpage.LoginPage import LoginPage
        Navigation().navigate(LoginPage,LoginPageController)

    def email_validate(self,email) -> bool:
        try:
        # validate and get info
            v = validate_email(email)

            return True
        except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
            return False