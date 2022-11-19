from helper.database.Database import Database
from model.CheckIn import CheckIn


class CheckInDAOImpl():
    def __init__(self) -> None:
       self.cursor = Database().get_cursor()
       self.db = Database().get_database()

    def save(self,checkIn : CheckIn) -> None:
        sql = "INSERT INTO CheckIn (ClassID,StudentID,Date,ComeCheck,AbsentCheck,ComeReason,AbsentReason) VALUES (%s, %s, %s,%s,%s ,%s,%s)"
        val  = (checkIn.ClassID,checkIn.StudentID,checkIn.Date,checkIn.ComeCheck,checkIn.AbsentCheck,checkIn.ComeReason,checkIn.AbsentReason)
        self.cursor.execute(sql, val)
        self.db.commit()

    
    def findAll(self) -> list:
        self.cursor.execute("SELECT * FROM CheckIn")
        data = self.cursor.fetchall()
        checkInLst = []
        for checkIn in data:
            checkInLst.append(CheckIn(ClassID=checkIn[0],StudentID=checkIn[1],Date=checkIn[2],IsCheck=checkIn[3],Reason=checkIn[4]))
        return checkInLst

    def update(self,checkIn : CheckIn) -> None:
        sql = f'UPDATE CheckIn SET  ComeCheck = "{checkIn.ComeCheck}" , AbsentCheck = "{checkIn.AbsentCheck}" , ComeReason = "{checkIn.ComeReason}" , AbsentReason = "{checkIn.AbsentReason}"  WHERE ClassID = {checkIn.ClassID} and StudentID = {checkIn.StudentID} and  Date = "{checkIn.Date}"'
        self.cursor.execute(sql)
        self.db.commit()
    
    def delete(self,checkIn : CheckIn) -> None:
        sql = f'DELETE FROM CheckIn WHERE ClassID = {checkIn.ClassID} and StudentID = {checkIn.StudentID}'
        self.cursor.execute(sql)
        self.db.commit()

    def find(self,classId,studentId,date) -> CheckIn:
        self.cursor.execute(f'SELECT * FROM CheckIn where ClassID = "{classId}" and StudentID = "{studentId}" and Date = "{date}"')
        checkIn = self.cursor.fetchone()
        if checkIn:
            return CheckIn(ClassID=checkIn[0],StudentID=checkIn[1],Date=checkIn[2],ComeCheck=checkIn[3],AbsentCheck=checkIn[4],ComeReason=checkIn[5],AbsentReason=checkIn[6])
        return None
    def findAllByClassIdAndDateJoinStudent(self,classId,date):
        self.cursor.execute(f"SELECT * FROM CheckIn inner join Student ON Student.StudentID = CheckIn.StudentID where classId = '{classId}' and date = '{date}'")
        data = self.cursor.fetchall()
        checkInLst = []
        for checkIn in data:
            checkInLst.append(checkIn)
        return checkInLst
    
    def findAllByClassIdAndDateJoinStudentJoinClassroom(self,classId,date):
        self.cursor.execute(f"SELECT Classroom.Name,CheckIn.StudentID,Student.Name,CheckIn.Date,CheckIn.ComeCheck,CheckIn.AbsentCheck,CheckIn.ComeReason,CheckIn.AbsentReason FROM CheckIn inner join Student ON Student.StudentID = CheckIn.StudentID inner join Classroom on CheckIn.ClassID = Classroom.ClassID where CheckIn.classId = '{classId}' and CheckIn.date = '{date}'")
        data = self.cursor.fetchall()
        checkInLst = []
        for checkIn in data:
            checkInLst.append(checkIn)
        return checkInLst

    def deleteFromClassId(self,classId):
        sql = f'DELETE FROM CheckIn WHERE ClassID = {classId}'
        self.cursor.execute(sql)
        self.db.commit()
    
    def findStudentByClassIdAndDateJoinStudent(self,classId,name):
        self.cursor.execute(f"SELECT CheckIn.Date,CheckIn.ComeCheck,CheckIn.AbsentCheck,ComeReason,AbsentReason FROM CheckIn inner join Student ON Student.StudentID = CheckIn.StudentID where CheckIn.ClassID = '{classId}' and Student.Name = '{name}'")
        data = self.cursor.fetchall()
        checkInLst = []
        for checkIn in data:
            checkInLst.append(checkIn)
        return checkInLst

    
      
    
