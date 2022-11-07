from dataclasses import dataclass
import datetime

@dataclass
class CheckInStudent:

    ClassID : str
    StudentID : str
    Name : str
    Date : datetime.date
    ComeCheck : int
    AbsentCheck : int
    ComeReason : str
    AbsentReason : str



