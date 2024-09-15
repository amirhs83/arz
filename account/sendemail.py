
import smtplib


def ssendemail(email,code):

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login("sharokhiamir0@gmail.com", "efuf irwz ndnv kyqi")

        

    s.sendmail("sharokhiamir0@gmail.com",email,str(code))
       
