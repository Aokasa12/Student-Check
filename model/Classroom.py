from dataclasses import dataclass

@dataclass
class Classroom:

    
    ClassID : str #auto increment
    Name : str
    TeacherEmail : str #foreign key from supervisor



