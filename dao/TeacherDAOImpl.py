from helper.database.Database import Database
from model.Teacher import Teacher





class TeacherDAOImpl():
    def __init__(self) -> None:
       self.cursor = Database().get_cursor()
       self.db = Database().get_database()

    def save(self,teacher : Teacher) -> None:
        sql = "INSERT INTO Teacher (Email, Username,Password) VALUES (%s, %s, %s)"
        val  = (teacher.Email,teacher.Username,teacher.Password)
        self.cursor.execute(sql, val) #เอาsqlกับvalมาเชื่อมกันผ่าน%s
        self.db.commit() #insert,delete,updateต้องมีการcommitเพื่อยืนยันการเปลี่ยนแปลงข้อมูล

    
    def findAll(self) -> list:
        self.cursor.execute("SELECT * FROM Teacher")
        data = self.cursor.fetchall()
        teacherLst = []
        for teacher in data:
            teacherLst.append(Teacher(Email=teacher[0],Username=teacher[1],Password=teacher[2]))
        return teacherLst

    def update(self,teacher : Teacher) -> None:
        sql = f'UPDATE Teacher SET Username = "{teacher.Username}" , Password = "{teacher.Password}"  WHERE Email = "{teacher.Email}"'
        self.cursor.execute(sql)
        self.db.commit()
    
    def delete(self,teacher : Teacher) -> None:
        sql = f'DELETE FROM Teacher WHERE Email = "{teacher.Email}"'
        self.cursor.execute(sql)
        self.db.commit()
    def find(self,email)-> Teacher:
        self.cursor.execute(f'SELECT * FROM Teacher where Email = "{email}"')
        teacher = self.cursor.fetchone() #เอาข้อมูลมาตัวเดียว
        if teacher:
            return Teacher(Email=teacher[0],Username=teacher[1],Password= teacher[2])
        return None


      