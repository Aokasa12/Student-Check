from helper.database.Database import Database
from model.Student import Student




class StudentDAOImpl():
    def __init__(self) -> None:
       self.cursor = Database().get_cursor()
       self.db = Database().get_database()

    def save(self,student : Student) -> None:
        sql = "INSERT INTO Student (StudentID, Name) VALUES (%s, %s)"
        val  = (student.StudentID,student.Name)
        self.cursor.execute(sql, val)
        self.db.commit()

    
    def saveOrUpdate(self,student : Student) -> None:

        data = self.find(student.StudentID)
        if (data):
            return
        sql = "INSERT INTO Student (StudentID, Name) VALUES (%s, %s)"
        val  = (student.StudentID,student.Name)
        self.cursor.execute(sql, val)
        self.db.commit()

    
    def findAll(self) -> list:
        self.cursor.execute("SELECT * FROM Student")
        data = self.cursor.fetchall()
        studentLst = []
        for student in data:
            studentLst.append(Student(StudentID=student[0],Name=student[1]))
        return studentLst

    def update(self,student : Student) -> None:
        sql = f'UPDATE Student SET Name = "{student.Name}"  WHERE StudentID = {student.StudentID}'
        self.cursor.execute(sql)
        self.db.commit()
    
    def delete(self,student : Student) -> None:
        sql = f'DELETE FROM Student WHERE StudentID = {student.StudentID}'
        self.cursor.execute(sql)
        self.db.commit()
        
    def find(self,studentID)-> Student:
        self.cursor.execute(f'SELECT * FROM Student where StudentID = {studentID}')
        student = self.cursor.fetchone()
        if student:
            return Student(StudentID=student[0],Name=student[1])
        return None


      