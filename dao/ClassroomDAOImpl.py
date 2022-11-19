from helper.database.Database import Database
from model.Classroom import Classroom





class ClassroomDAOImpl():
    def __init__(self) -> None:
       self.cursor = Database().get_cursor()
       self.db = Database().get_database()

    def save(self,classroom : Classroom) -> None:
        sql = "INSERT INTO Classroom (Name,TeacherEmail) VALUES (%s, %s)"
        val  = (classroom.Name,classroom.TeacherEmail)
        self.cursor.execute(sql, val)
        self.db.commit()

    
    def findAll(self) -> list:
        self.cursor.execute("SELECT * FROM Classroom")
        data = self.cursor.fetchall()
        classroomLst = []
        for classroom in data:
            classroomLst.append(Classroom(ClassID=classroom[0],Name=classroom[1],TeacherEmail=classroom[2]))
        return classroomLst

    def update(self,classroom : Classroom) -> None:
        sql = f'UPDATE Classroom SET Name = "{classroom.Name}"  WHERE ClassID = {classroom.ClassID}'
        self.cursor.execute(sql)
        self.db.commit()
    
    def delete(self,classroom : Classroom) -> None:
        sql = f'DELETE FROM Classroom WHERE ClassID = "{classroom.ClassID}"'
        self.cursor.execute(sql)
        self.db.commit()
    
    def find(self,classId)-> Classroom:
        self.cursor.execute(f'SELECT * FROM Classroom where ClassID = {classId}')
        classroom = self.cursor.fetchone()
        if classroom:
            return Classroom(ClassID=classroom[0],Name=classroom[1],TeacherEmail=classroom[2])
        return None
    
    def findFromNameAndEmail(self,classroom : Classroom)-> Classroom:
        self.cursor.execute(f'SELECT * FROM Classroom where Name = "{classroom.Name}" and TeacherEmail = "{classroom.TeacherEmail}" ORDER BY ClassID DESC')
        classroom = self.cursor.fetchone()
        if classroom:
            return Classroom(ClassID=classroom[0],Name=classroom[1],TeacherEmail=classroom[2])
        return None

    def findAllFromTeacherEmail(self,tEmail)  -> list:
        self.cursor.execute(f'SELECT * FROM Classroom where TeacherEmail = "{tEmail}"')#ใช้คำสั่งSQL
        data = self.cursor.fetchall()#เลือกทั้งหมด
        classroomLst = []
        for classroom in data:
            classroomLst.append(Classroom(ClassID=classroom[0],Name=classroom[1],TeacherEmail=classroom[2]))
        return classroomLst
    
    def filterFromName(self,name) -> list:
        self.cursor.execute(f'SELECT DISTINCT Name FROM Classroom where Name LIKE "{name}%" and NOT (Name = "{name}")   LIMIT 3')
        data = self.cursor.fetchall()
        classroomLst = []
        for classroom in data:
            classroomLst.append(classroom)
        return classroomLst


      