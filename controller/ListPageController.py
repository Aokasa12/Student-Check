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
    def change_password(self):
        from view.changepassword.ChangePasswordPage import ChangePasswordPage
        from controller.ChangePasswordPageController import ChangePasswordPageController
        Navigation().navigate(ChangePasswordPage,ChangePasswordPageController)
        

    def delete_classroom(self,classId):
        

        inClassroomDAO = InClassroomDAOImpl()
        inClassroomDAO.deleteFromClassId(classId)

        checkInDAO = CheckInDAOImpl()
        checkInDAO.deleteFromClassId(classId)

        classroomDAO = ClassroomDAOImpl()
        classroomDAO.delete(Classroom(ClassID=classId,Name=None,TeacherEmail=None))

        context = Context()
        tEmail = context.get_email()

        data = classroomDAO.findAllFromTeacherEmail(tEmail)
        self.request.update({"classroom" : data})


        from view.listpage.ListPage import ListPage
        from controller.ListPageController import ListPageController

        Navigation().navigate(ListPage,ListPageController,self.request)


    def enter_classroom(self,classId):
        self.request.update({"classId":classId})

        inClassroomDAO = InClassroomDAOImpl()
        inClassroom = inClassroomDAO.findAllByClassId(classId)

        studentDAOImpl = StudentDAOImpl()
        checkInLst = []
        for i in inClassroom:
            student = studentDAOImpl.find(studentID=i.StudentID)
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
    