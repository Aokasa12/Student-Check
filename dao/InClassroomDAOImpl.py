from helper.database.Database import Database
from model.InClassroom import InClassroom





class InClassroomDAOImpl():
    def __init__(self) -> None:
       self.cursor = Database().get_cursor()
       self.db = Database().get_database()

    def save(self,classroom : InClassroom) -> None:
        sql = "INSERT INTO InClassroom (StudentID,ClassID) VALUES (%s, %s)"
        val  = (classroom.StudentID,classroom.ClassID)
        self.cursor.execute(sql, val)
        self.db.commit()

    
    def findAll(self) -> list:
        self.cursor.execute("SELECT * FROM InClassroom")
        data = self.cursor.fetchall()
        inClassroomLst = []
        for inClassroom in data:
            inClassroomLst.append(InClassroom(StudentID=inClassroom[0],ClassID=inClassroom[1]))
        return inClassroomLst
    
    def delete(self,InClassroom : InClassroom) -> None:
        sql = f'DELETE FROM Classroom WHERE StudentID = {InClassroom.StudentID} ClassID = {InClassroom.ClassID}'
        self.cursor.execute(sql)
        self.db.commit()
    
    def find(self,studentId,classId)-> InClassroom:
        self.cursor.execute(f'SELECT * FROM Classroom where StudentID = {studentId} and classId = {classId}')
        inClassroom = self.cursor.fetchone()
        if inClassroom:
            return InClassroom(StudentID=inClassroom[0],ClassID=inClassroom[1])
        return None
    def findAllByClassId(self,classId) -> list:
        self.cursor.execute(f"SELECT * FROM InClassroom where ClassID = {classId}")
        data = self.cursor.fetchall()
        inClassroomLst = []
        for inClassroom in data:
            inClassroomLst.append(InClassroom(StudentID=inClassroom[0],ClassID=inClassroom[1]))
        return inClassroomLst
    def deleteFromClassId(self,classId):
        sql = f'DELETE FROM InClassroom WHERE ClassID = {classId}'
        self.cursor.execute(sql)
        self.db.commit()

    def findAllByClassIdJoinStudent(self,classId) -> list:
        self.cursor.execute(f"SELECT Student.Name FROM InClassroom inner join Student On InClassroom.StudentID = Student.StudentID where ClassID = {classId}")
        data = self.cursor.fetchall()
        inClassroomLst = []
        for inClassroom in data:
            inClassroomLst.append(inClassroom[0])
        return inClassroomLst


      