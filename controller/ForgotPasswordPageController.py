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

        newPassword = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))#เอาstrมารวมกัน สร้างPasswordมา8ตัวมั่วๆ
        bytes = newPassword.encode('utf-8')
        salt = bcrypt.gensalt()#เช็ครหัส.สร้างstrมั่วๆขึ้นมา
        hash = bcrypt.hashpw(bytes,salt)#เอาpasswordไปhashให้เป็นค่าstr60ตัว

        teacher = Teacher(Email = teacher.Email,Username=teacher.Username,Password=hash.decode("utf-8"))
        self.teacherDAO.update(teacher)


        port = 587  # For starttls พอร์ทนึงของการส่งEmail
        msg = MIMEMultipart() #Emailมีสามส่วนจากใครถึงใครข้อมูลคืออะไร
        msg['From'] = 'ryuinw123.thang@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'ATrip Forgetpassword'
        smtp_server = "smtp.gmail.com"#severของemail
        sender_email = "ryuinw123.thang@gmail.com"
        receiver_email = email #emailผู้รับ
        password = "xgmuqytakzfussxe" #passwordที่Google genให้
        message = "Your Username is " + teacher.Username + """
Your Password is """ + newPassword
        msg.attach(MIMEText(message,"plain")) #libaryกำหนดว่าจะส่งฟอร์มmessageที่ส่งให้ไปต้องเอาเข้าattach
        context = ssl.create_default_context()#protocol encrypt เชื่อมต่อข้อมูลที่ถูกเข้ารหัสไว้
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted ถ้าไม่ใช้ส่งเมลไม่ได้
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        messagebox.showinfo(title="Success", message="ส่งรหัสไปที่ Email ของท่านแล้ว")

    def back(self):
        from controller.LoginPageController import LoginPageController
        from view.loginpage.LoginPage import LoginPage
        Navigation().navigate(LoginPage,LoginPageController)
        
    
    

