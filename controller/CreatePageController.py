from controller.BaseController import BaseController
from helper.navigation.Navigation import Navigation
from dao.ClassroomDAOImpl import ClassroomDAOImpl
from helper.context.Context import Context
from tkinter import messagebox
from model.Student import Student
from model.Classroom import Classroom
from helper.context.Context import Context
from model.InClassroom import InClassroom
from dao.InClassroomDAOImpl import InClassroomDAOImpl
from dao.StudentDAOImpl import StudentDAOImpl
class CreatePageController(BaseController):
    def __init__(self, view ):
        super().__init__(view)
    
    

    def createClass(self,classname,classLst):
        try:
            if self.validate(classname,classLst) is False:
                return
        
            studentLst = []
            for i in range(len(classLst)-1):
                studentLst.append(Student(StudentID=classLst[i][0].get() , Name=classLst[i][1].get()))


            context = Context()
            teacher_email = context.get_email()


            classroomDAO = ClassroomDAOImpl()
            classroom = Classroom(ClassID=None , Name= classname.get(),TeacherEmail=teacher_email )
            classroomDAO.save(classroom)

            classroom = classroomDAO.findFromNameAndEmail(classroom)



            studentDAO = StudentDAOImpl()

            for i in studentLst:
                studentDAO.saveOrUpdate(i)

            inClassroomDAO = InClassroomDAOImpl()

            
            for i in studentLst:
                inClassroomDAO.save(InClassroom(StudentID=i.StudentID,ClassID=classroom.ClassID))
            
            self.navBack()
        except Exception as e:
            print(e)
        


    def validate(self,classname,classLst) -> bool:
        if classname.get() == "":
            messagebox.showerror("Error", "โปรดใส่ชื่อห้องเรียน")
            return False
        if len(classLst) == 0:
            messagebox.showerror("Error", "โปรดกรอกข้อมูล")
            return False
        
        checkLst = []

        for i in range(len(classLst)-1):
            #print(classLst[i][0].get() , classLst[i][1].get() , "Time =",i)
            if classLst[i][0].get() == "" or (classLst[i][0].get().isnumeric() == False ) or classLst[i][1].get() == "":
                messagebox.showerror("Error", "โปรดใส่ข้อมูลให้ถูกต้อง")
                return False
            
            if classLst[i][0].get() in checkLst:
                messagebox.showerror("Error","มีรหัสประจำตัวซ้ำ")
                return False
            
            checkLst.append(classLst[i][0].get())
        
        return True
    
    def navBack(self):
        try:
            context = Context()
            email = context.get_email()

            classroomDAO = ClassroomDAOImpl()
            data = classroomDAO.findAllFromTeacherEmail(email)
            self.request.update({"classroom" : data})

            from view.listpage.ListPage import ListPage
            from controller.ListPageController import ListPageController

            Navigation().navigate(ListPage,ListPageController,self.request)
        except Exception as e:
            print(e)