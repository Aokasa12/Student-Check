from tkinter import *
from tkcalendar import Calendar
import datetime

class CalendarLevel(Toplevel):
    def __init__(self,parent,date):
        super().__init__(parent)
        self.title("Calendar")
        self.geometry("400x400")
        if (date):
            self.date_object = date
        else:
            self.date_object = datetime.date.today()



        self.cal = Calendar(self, selectmode = 'day',
               year = self.date_object.year, month = self.date_object.month,
               day = self.date_object.day)
 
        self.cal.pack(pady = 20)

        self.evar = StringVar()
 
        

        self.button = Button(self, text = "Get Date",
        command = self.grad_date).pack(pady = 20)
    def grad_date(self):
            self.evar.set(self.cal.get_date())
            self.destroy()
    def set_date(self,date):
        self.date_object = date
