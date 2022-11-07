from dataclasses import dataclass
import datetime

@dataclass
class CheckIn:

    ClassID : str
    StudentID : str
    Date : datetime.date
    ComeCheck : int
    AbsentCheck : int
    ComeReason : str
    AbsentReason : str



