from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
from helper.context.Context import Context
from dao.ClassroomDAOImpl import ClassroomDAOImpl
from dao.TeacherDAOImpl import TeacherDAOImpl
from helper.context.Context import Context
from model.Teacher import Teacher
from tkinter import messagebox
import bcrypt
class ChangePasswordPageController(BaseController):
    def __init__(self, view ):
        super().__init__(view)
    
    def goToListPage(self):
        context = Context()
        email = context.get_email()

        classroomDAO = ClassroomDAOImpl()
        data = classroomDAO.findAllFromTeacherEmail(email)
        self.request.update({"classroom" : data})

        from view.listpage.ListPage import ListPage
        from controller.ListPageController import ListPageController

        Navigation().navigate(ListPage,ListPageController,self.request)
    def change_password(self,password,newPassword,cNewPassword):
        if (newPassword != cNewPassword):
            messagebox.showerror("Error","รหัสผ่านใหม่ไม่ถูกต้อง")
            return

        context = Context()
        tEmail = context.get_email()
        tUsername = context.get_username()
        teacherDAO = TeacherDAOImpl()
        teacher = teacherDAO.find(tEmail)
        bytes = password.encode('utf-8')
        passwordBytes = teacher.Password.encode('utf-8')


        result = bcrypt.checkpw(bytes,passwordBytes)
        if (result is False):
            messagebox.showerror("Error","รหัสผ่านผิดพลาด")
            return

        print(password,newPassword,cNewPassword)
        
        bytes = newPassword.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes,salt)

        teacher = Teacher(Email = tEmail,Username=tUsername,Password=hash.decode("utf-8"))
        teacherDAO.update(teacher)

        messagebox.showinfo("Success","เปลี่ยนรหัสผ่านเสร็จสิ้น")
        self.goToListPage()

        





