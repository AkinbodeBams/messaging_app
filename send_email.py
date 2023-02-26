import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd






class SendEmail:

    def anniversary_items(self, lst, yrs= None):
        string = ''
       
        for item in lst:
            string+= f'<li>{item[0]} {item[1]} {item[2]}<br>Phone Number:{item[3]}<br>Email:{item[4]}<br></li>'

       
        return string


    def send_email(self,sender_address,sender_pass,recipient,b_details=None,w_details=None):
        date_str = pd.Timestamp.today().strftime('%Y-%m-%d')
        B = self.anniversary_items(b_details) if len(b_details) > 0 else '<li>No Birthday For today</li>'
        w = self.anniversary_items(w_details) if len(w_details) > 0 else '<li>No Wedding For today</li>'
        html = f'''
    <html>
        <body>
            <h1>Daily Anniversary report</h1>
            <p>Today's Birthday</p>
            <ul>
            B##
            </ul>
            <p>Today's Wedding</p>
             <ul>
            W##
            </ul>
        </body>
    </html>
    ''' 

        test1 = html.replace('B##',B)
        test2 = test1.replace('W##',w)
        email_message = MIMEMultipart()
        email_message['From'] = sender_address
        email_message['To'] = ','.join(recipient)
        email_message['Subject'] = f'Anniversary Reports For - {date_str}'
        email_message.attach(MIMEText(test2, "html"))
        email_string = email_message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_address, sender_pass)
            server.sendmail(sender_address, recipient, email_string)
