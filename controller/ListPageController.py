from controller.BaseController import BaseController
from helper.context.Context import Context
from helper.navigation.Navigation import Navigation
from dao.InClassroomDAOImpl import InClassroomDAOImpl
from model.CheckInStudent import CheckInStudent
from dao.StudentDAOImpl import StudentDAOImpl
from view.toplevel.decision.Decision import Decision
from dao.ClassroomDAOImpl import ClassroomDAOImpl
from dao.CheckInDAOImpl import CheckInDAOImpl
from model.Classroom import Classroom
class ListPageController(BaseController):
    def __init__(self, view ):
        super().__init__(view)
        self.inClassroomDAO = InClassroomDAOImpl()
        self.checkInDAO = CheckInDAOImpl()
        self.classroomDAO = ClassroomDAOImpl()
        self.studentDAOImpl = StudentDAOImpl()

    def choose_decision(self,classId):
        up = Decision(self.view.parent)
        up.grab_set()
        up.wait_window()

        if (up.mode.get() == 0):
            return
        elif (up.mode.get() == 1):
            self.enter_classroom(classId)
        elif (up.mode.get() == 2):
            self.delete_classroom(classId)
        elif(up.mode.get() ==  3):
            self.filter_classroom(classId)
            return
    def change_password(self):

        from view.changepassword.ChangePasswordPage import ChangePasswordPage
        from controller.ChangePasswordPageController import ChangePasswordPageController
        Navigation().navigate(ChangePasswordPage,ChangePasswordPageController)
    
    def filter_classroom(self,classId):

        self.request.update({"classId":classId})

        data = self.inClassroomDAO.findAllByClassIdJoinStudent(classId)
        
        self.request.update({"studentLst" : data})
        
        from view.filterclass.FilterClassPage import FilterClassPage
        from controller.FilterClassPageController import FilterClassPageController
        Navigation().navigate(FilterClassPage,FilterClassPageController,self.request)
        

    def delete_classroom(self,classId):
        

        self.inClassroomDAO.deleteFromClassId(classId)

        self.checkInDAO.deleteFromClassId(classId)

        self.classroomDAO.delete(Classroom(ClassID=classId,Name=None,TeacherEmail=None))

        context = Context()
        tEmail = context.get_email()

        data = self.classroomDAO.findAllFromTeacherEmail(tEmail)
        self.request.update({"classroom" : data})


        from view.listpage.ListPage import ListPage
        from controller.ListPageController import ListPageController

        Navigation().navigate(ListPage,ListPageController,self.request)


    def enter_classroom(self,classId):
        self.request.update({"classId":classId})

        inClassroom = self.inClassroomDAO.findAllByClassId(classId)

        checkInLst = []
        for i in inClassroom:
            student = self.studentDAOImpl.find(studentID=i.StudentID)
            checkIn = CheckInStudent(ClassID=classId, StudentID=student.StudentID,Name=student.Name,Date=None,ComeCheck=0,AbsentCheck=0,ComeReason="",AbsentReason="")
            checkInLst.append(checkIn)
        



        self.request.update({"checkInLst":checkInLst})


        print(self.request)
        from view.checkpage.CheckPage import CheckPage
        from controller.CheckPageController import CheckPageController
        Navigation().navigate(CheckPage,CheckPageController,self.request)
    
    def add_classroom(self):
        from view.createpage.CreatePage import CreatePage
        from controller.CreatePageController import CreatePageController
        Navigation().navigate(CreatePage,CreatePageController)
    
    def logout(self):
        context = Context()
        del context

        from view.frontpage.FrontPage import FrontPage
        from controller.FrontPageController import FrontPageController

        Navigation().navigate(FrontPage,FrontPageController)
    