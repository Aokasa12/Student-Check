from controller.BaseController import BaseController
from helper.context.Context import Context
from helper.navigation.Navigation import Navigation
from dao.ClassroomDAOImpl import ClassroomDAOImpl
from dao.CheckInDAOImpl import CheckInDAOImpl
class FilterClassPageController(BaseController):
    def __init__(self, view ):
        super().__init__(view)
        self.context = Context()
        self.classroomDAO = ClassroomDAOImpl()
        self.checkInDAO = CheckInDAOImpl()
    
    def getHistory(self,classId,name):
        data = self.checkInDAO.findStudentByClassIdAndDateJoinStudent(classId,name)
        historyLst = []
        for i in data:
            if (i[1] == 0 and i[2] == 0):
                check = "ไม่มีข้อมูล"
            elif (i[1] == 1):
                check = "มาเรียน"+ f"({i[3]})"
            elif (i[2] == 1):
                check = "ขาดเรียน"+ f"({i[4]})"
            historyLst.append([i[0].strftime("%d/%m/%y"),check])
        self.view.insertData(historyLst)

    def logout(self):
        del self.context

        from view.frontpage.FrontPage import FrontPage
        from controller.FrontPageController import FrontPageController

        Navigation().navigate(FrontPage,FrontPageController)
    def back(self):

        tEmail = self.context.get_email()

        data = self.classroomDAO.findAllFromTeacherEmail(tEmail)
        self.request.update({"classroom" : data})


        from view.listpage.ListPage import ListPage
        from controller.ListPageController import ListPageController

        Navigation().navigate(ListPage,ListPageController,self.request)
