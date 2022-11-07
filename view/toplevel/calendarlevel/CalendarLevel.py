from tkinter import *
from tkcalendar import Calendar
import datetime

class CalendarLevel(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Calendar")
        self.geometry("400x400")
        date_object = datetime.date.today()

        self.cal = Calendar(self, selectmode = 'day',
               year = date_object.year, month = date_object.month,
               day = date_object.day)
 
        self.cal.pack(pady = 20)

        self.evar = StringVar()
 
        

        self.button = Button(self, text = "Get Date",
        command = self.grad_date).pack(pady = 20)
    def grad_date(self):
            self.evar.set(self.cal.get_date())
            self.destroy()
