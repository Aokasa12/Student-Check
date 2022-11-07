from controller.BaseController import BaseController
from tkinter import messagebox
from helper.navigation.Navigation import Navigation
import smtplib
import bcrypt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from model.Teacher import Teacher
from dao.TeacherDAOImpl import TeacherDAOImpl
import secrets
import smtplib, ssl
import string
class ForgotPasswordPageController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.teacherDAO = TeacherDAOImpl()
    def forgot_password(self,email):
        teacher = self.teacherDAO.find(email)
        if teacher == None:
            messagebox.showerror("Error", "ไม่มี Email นี้")
            return

        newPassword = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
        bytes = newPassword.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes,salt)

        teacher = Teacher(Email = teacher.Email,Username=teacher.Username,Password=hash.decode("utf-8"))
        self.teacherDAO.update(teacher)


        port = 587  # For starttls
        msg = MIMEMultipart()
        msg['From'] = 'ryuinw123.thang@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'ATrip Forgetpassword'
        smtp_server = "smtp.gmail.com"
        sender_email = "ryuinw123.thang@gmail.com"
        receiver_email = email
        password = "xgmuqytakzfussxe"
        message = "Your Username is " + teacher.Username + """
Your Password is """ + newPassword
        msg.attach(MIMEText(message,"plain"))
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        messagebox.showinfo(title="Success", message="ส่งรหัสไปที่ Email ของท่านแล้ว")

    def back(self):
        from controller.LoginPageController import LoginPageController
        from view.loginpage.LoginPage import LoginPage
        Navigation().navigate(LoginPage,LoginPageController)
        
    
    

