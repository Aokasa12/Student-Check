from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
from dao.TeacherDAOImpl import TeacherDAOImpl
from helper.remember.RememberMe import RememberMe
from helper.context.Context import Context
from dao.ClassroomDAOImpl import ClassroomDAOImpl
import bcrypt
from tkinter import messagebox


class LoginPageController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.teacherDAO = TeacherDAOImpl()
        self.rememberMe = RememberMe()
    
    def forgotpassword(self):
        from view.forgotpassword.ForgotPasswordPage import ForgotPasswordPage
        from controller.ForgotPasswordPageController import ForgotPasswordPageController
        Navigation().navigate(ForgotPasswordPage,ForgotPasswordPageController)


    def register(self):
        from controller.RegisterPageController import RegisterPageController
        from view.registerpage.RegisterPage import RegisterPage
        Navigation().navigate(RegisterPage,RegisterPageController)
    
    def signin(self,email,password):
            teacher = self.teacherDAO.find(email=email)
            if (teacher is None):
                messagebox.showerror("Error", "ไม่มีผู้ใช้ Email นี้")
                return

            bytes = password.encode('utf-8')
            passwordBytes = teacher.Password.encode('utf-8')
        
            result = bcrypt.checkpw(bytes, passwordBytes)

            if (result is False):
                messagebox.showerror("Error","รหัสผ่านผิดพลาด")
                return
            
            self.rememberMe.save(email,password)

            globalContext = Context()
            globalContext.set_email(teacher.Email)
            globalContext.set_username(teacher.Username)

            messagebox.showinfo("Success", "ยืนยันตัวตนแล้ว")

            classroomDAO = ClassroomDAOImpl()
            data = classroomDAO.findAllFromTeacherEmail(teacher.Email)
            self.request.update({"classroom" : data})


            from view.listpage.ListPage import ListPage
            from controller.ListPageController import ListPageController

            Navigation().navigate(ListPage,ListPageController,self.request)


