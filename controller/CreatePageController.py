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
        self.classroomDAO  =ClassroomDAOImpl()
        self.studentDAO  = StudentDAOImpl()
        self.inClassroomDAO = InClassroomDAOImpl()
        self.context = Context()
    
    

    def createClass(self,classname,classLst):
        try:
            if self.validate(classname,classLst) is False:
                return
        
            studentLst = []
            for i in range(len(classLst)-1):
                studentLst.append(Student(StudentID=classLst[i][0].get() , Name=classLst[i][1].get()))


            teacher_email = self.context.get_email()


            classroom = Classroom(ClassID=None , Name= classname,TeacherEmail=teacher_email )
            self.classroomDAO.save(classroom)

            classroom = self.classroomDAO.findFromNameAndEmail(classroom)




            for i in studentLst:
                self.studentDAO.saveOrUpdate(i)


            
            for i in studentLst:
                self.inClassroomDAO.save(InClassroom(StudentID=i.StudentID,ClassID=classroom.ClassID))
            
            self.navBack()
        except Exception as e:
            print(e)
        


    def validate(self,classname,classLst) -> bool:
        if classname == "":
            messagebox.showerror("Error", "โปรดใส่ชื่อห้องเรียน")
            return False
        tEmail = self.context.get_email()
        classroom = self.classroomDAO.findFromNameAndEmail(Classroom(ClassID=None,Name=classname,TeacherEmail=tEmail))
        if (classroom):
            messagebox.showerror("Error", "มีห้องเรียนนี้อยู่แล้ว")
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
            email = self.context.get_email()

            data = self.classroomDAO.findAllFromTeacherEmail(email)
            self.request.update({"classroom" : data})

            from view.listpage.ListPage import ListPage
            from controller.ListPageController import ListPageController

            Navigation().navigate(ListPage,ListPageController,self.request)
        except Exception as e:
            print(e)
    def find_class(self,classname):

        if (classname == ""):
            return None
        data = self.classroomDAO.filterFromName(classname)
        return data