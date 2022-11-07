from controller.BaseController import BaseController
from helper.context.Context import Context
from helper.navigation.Navigation import Navigation
from dao.ClassroomDAOImpl import ClassroomDAOImpl
from tkinter import *
from tkinter import messagebox
from dao.CheckInDAOImpl import CheckInDAOImpl
from dao.InClassroomDAOImpl import InClassroomDAOImpl
from dao.StudentDAOImpl import StudentDAOImpl
from model.CheckIn import CheckIn
from model.CheckInStudent import CheckInStudent
from view.toplevel.comecheck.ComeCheck import ComeCheck
from view.toplevel.calendarlevel.CalendarLevel import CalendarLevel
from model.CheckInBox import CheckInBox
from view.toplevel.absentcheck.AbsentCheck import AbsentCheck



class CheckPageController(BaseController):
    def __init__(self, view ):
        super().__init__(view)
    
    def back(self):

        globalContext = Context()
        tEmail = globalContext.get_email()

        classroomDAO = ClassroomDAOImpl()
        data = classroomDAO.findAllFromTeacherEmail(tEmail)
        self.request.update({"classroom" : data})


        from view.listpage.ListPage import ListPage
        from controller.ListPageController import ListPageController

        Navigation().navigate(ListPage,ListPageController,self.request)
    
    def logout(self):
        context = Context()
        del context

        from view.frontpage.FrontPage import FrontPage
        from controller.FrontPageController import FrontPageController

        Navigation().navigate(FrontPage,FrontPageController)

    def calendar(self):
        up = CalendarLevel(self.view.parent)
        up.grab_set()
        up.wait_window()
        return up.evar.get()

    def box_clicked(self,studentId,side,lst,classId,date):

        checkInDAO = CheckInDAOImpl()
        checkIn = checkInDAO.find(classId,studentId,date)

        for i in lst:
            checkInBox : CheckInBox = i
            if (checkInBox.StudentID == studentId):
                data = checkInBox
        
            


        if (side == "left"):
            if (data.ComeCheck == 0):
                if (data.AbsentCheck == 1):
                    messagebox.showerror("Error","โปรดกรอกข้อมูลให้ถูกต้อง")
                    return

                up = ComeCheck(self.view.parent)
                up.grab_set()
                up.wait_window()
                dict = {0:"",1:"เข้าเรียนตรงเวลา",2:"เข้าเรียนสาย",3:"เรียน Onsite",4:"เรียน Online"}
                choice = up.choice.get()
                if choice < 5:
                    reason = dict[choice]
                else:
                    reason = up.txt.get()
                
                data.ComeCheck = 1
                data.LeftButton.configure(image=self.view.checkbox)
                data.LeftLabel.config(text = reason)
            

            else:
                reason = ""
                data.ComeCheck = 0
                data.LeftButton.configure(image=self.view.emptybox)
                data.LeftLabel.config(text = reason)
            checkInDAO.update(CheckIn(ClassID=checkIn.ClassID,StudentID=checkIn.StudentID,Date=checkIn.Date,ComeCheck=data.ComeCheck,AbsentCheck=checkIn.AbsentCheck,ComeReason=reason,AbsentReason=checkIn.AbsentReason))
            
        

        
        if (side == "right"):
            if (data.AbsentCheck == 0):
                if (data.ComeCheck == 1):
                    messagebox.showerror("Error","โปรดกรอกข้อมูลให้ถูกต้อง")
                    return
                up = AbsentCheck(self.view.parent)
                up.grab_set()
                up.wait_window()
                dict = {0:"",1:"ขาดแบบไม่แจ้งล่วงหน้า",2:"ขาดแบบแจ้งล่วงหน้า",3:"ติดธุระ",4:"ลาป่วย",5:"Covid-19"}
                choice = up.choice.get()
                if choice < 6:
                    reason = dict[choice]
                else:
                    reason = up.txt.get()
                
                data.AbsentCheck = 1
                data.RightButton.configure(image=self.view.checkbox)
                data.RightLabel.config(text = reason)

            else:
                reason = ""
                data.AbsentCheck = 0
                data.RightButton.configure(image=self.view.emptybox)
                data.RightLabel.config(text = reason)
            checkInDAO.update(CheckIn(ClassID=checkIn.ClassID,StudentID=checkIn.StudentID,Date=checkIn.Date,ComeCheck=checkIn.ComeCheck,AbsentCheck=data.AbsentCheck,ComeReason=checkIn.ComeReason,AbsentReason=reason))
        



    def newData(self,date,classId):
        print(date)
        checkInDAO = CheckInDAOImpl()
        checkInLst = []
        data = checkInDAO.findAllByClassIdAndDateJoinStudent(classId,date)
        if (len(data) > 0):
            for i in range(len(data)):
                checkInLst.append(CheckInStudent(ClassID=classId,StudentID=data[i][1],Name=data[i][8],Date=data[i][2],ComeCheck=data[i][3],AbsentCheck=data[i][4],ComeReason=data[i][5],AbsentReason=data[i][6]))
            self.view.insertData(checkInLst,enable = True)
            return
        
        inClassroomDAO = InClassroomDAOImpl()
        inClassroom = inClassroomDAO.findAllByClassId(classId)


        studentDAOImpl = StudentDAOImpl()
        checkInLst = []
        for i in inClassroom:
            student = studentDAOImpl.find(studentID=i.StudentID)
            checkIn = CheckIn(ClassID=classId, StudentID=student.StudentID,Date=date,ComeCheck=0,AbsentCheck=0,ComeReason="",AbsentReason="")
            checkInStudent = CheckInStudent(ClassID=classId,StudentID=student.StudentID,Name=student.Name,Date=date,ComeCheck=0,AbsentCheck=0,ComeReason="",AbsentReason="")
            checkInLst.append(checkInStudent)
            checkInDAO.save(checkIn)

        self.view.insertData(checkInLst,enable = True)
        
        





