import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os



class SendEmail:

    def send_email(self,sender_address,sender_pass, subject,mail_content,recipient):
    
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls() #enable security
        session.login(sender_address, sender_pass) 
        message = MIMEMultipart()
        mail_contents = mail_content
        message['From'] =sender_address
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(mail_contents, 'plain'))
        text = message.as_string()
        session.sendmail(sender_address, recipient, text)
        session.quit()




