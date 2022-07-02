import datetime
import os
from sms import Sms
from send_email import SendEmail
from dataframe import Data
import random




messages = {
    'b_day_msg': [f'The Lord your God is in your midst, a mighty one who will save; He will rejoice over you with '
                  'gladness; he will quiet you by his love; he will exult over you with loud singing.” – Zephaniah 3:17 '
                  'Happiest of birthdays to you, ###. May God hold His comforting hand over your life in the coming '
                  'year',
                  'May Jesus Christ continue to bless you abundantly and keep you safe in his loving care. On your '
                  "birthday, enjoy His divine presence in your life. Have a happy and holy birthday, ###. You mean"
                  " the world to us! Araba Baptist Church",
                  "Life by itself is a gift, so never forget to thank God for it. Moreover, never forget to make the most"
                  "of it. May God bless you on your birthday with abundant peace and joy. Happy birthday, ###. we "
                  "love you more than words can say. Araba Baptist Church",
                  "On your birthday, we wish you every ounce of happiness ###. We hope you bring glory to Jesus’s "
                  "name every day of the coming year. Have fun and a blessed day. we love you. Araba Baptist Church",
                  "God is always there to guide you, protect you and comfort you. You are never alone.He is always near. "
                  "May you have a lovely day and an even more beautiful year ahead. Happy Birthday. May God bless you "
                  "abundantly, ###! Araba Baptist Church",
                  "Wishing you a day filled with happy memories and a year with numerous reasons to be thankful about. "
                  "Happy Birthday ###. May God bless you. Araba Baptist Church",
                  "Happy birthday, ###. On your birthday we pray to God for your health and well-being. May Jesus gift you "
                  "all the success, pride, and prosperity. Have a great year ahead. Araba Baptist Church"],
    'wed_msg': ["Love that grows through time is such an inspiring thing. Congratulations on your ### years together."
                "Araba Baptist Church",
                "Having each other’s backs and taking care of one another’s souls for ### years, that’s a beautiful faith walk."
                "Happy Anniversary Araba Baptist Church",
                "Sharing in your happiness as you celebrate ### years of marriage. Today is your day to be in the "
                "spotlight…to celebrate all you’ve accomplished together…and to bask in all the admiration. "
                "Araba Baptist Church",
                "### years of marriage! It couldn’t have been easy every day, but you two make it look that way "
                "Araba Baptist Church."

                ],
    'bday_months': [{1:'',
                2:"The month of February brings many gifts, one of those was you. A beautiful gift that "
                  "captivated our soul and changed our lives. A lovely gift that we are grateful for. Welcome to your "
                  "Birthday month. Araba Baptist Church",
                3:"The month of March brings many gifts, one of those was you. A beautiful gift that "
                  "captivated our soul and changed our lives. A lovely gift that we are grateful for. Welcome to your "
                  "Birthday month. Araba Baptist Church",
                4: "The month of April brings many gifts, one of those was you. A beautiful gift that "
                  "captivated our soul and changed our lives. A lovely gift that we are grateful for. Welcome to your "
                  "Birthday month. Araba Baptist Church"

    }],
    'General_month': [{1:'',
                2:"In this new month, may God give you new hope and a fresh start\
                as we start this month. May God arrange your steps on the right way, and may \
                your day, and all the week in this month be full of bliss.Happy \
                new Month to you and yours.",
                3:"You will shine like the sun and be precious as the diamonds. No matter what happens, you will always be at the top. We wish you a month that will shine as you shine. It is a month of possibilities. Enjoy the new month.",
                4: "In this new month, may you always testify as you live, and may you receive more than a downpour of rain of blessings? Happy new month.Araba Baptist Church"

    }

    ]
}


class Celebrants:

    def __init__(self):
        self.df = Data().df
        




    def month_birthday_celebrants(self):
            today = datetime.datetime.today().date()
            # today = datetime.datetime(2020, 2, 1)
            month = today.month
            email = self.df[self.df.month == month].email
            phone_number = self.df[self.df.month == month].phone_number
            title = self.df[self.df.month == month].title
            first_name =  self.df[self.df.month == month].first_name.str.title() 
            surname =  self.df[self.df.month == month].surname.str.title()
            return [title,first_name,surname,phone_number,email]

    def today_birthday_celebrants(self):
        celebrant_details = {}
        # today = datetime.datetime.today().date()
        today = datetime.datetime(2020, 6, 30)
        month = today.month
        day = today.day
        phone_number = self.df[self.df.month_and_day == (month, day)].phone_number
        email = self.df[self.df.month_and_day == (month, day)].email
        first_name  = self.df[self.df.month_and_day == (month, day)].first_name
        title = self.df[self.df.month_and_day == (month, day)].title
        surname = self.df[self.df.month_and_day == (month, day)].surname

        return list(zip(title,first_name,surname,phone_number,email))

    def today_wedding(self):
        lst = []
        celebrants_info = {}
        today = datetime.datetime.today().date()
        # today = datetime.datetime(2020, 4, 9)
        month = today.month
        day = today.day
        email = self.df[self.df.wed_month_day == (month, day)].email
        phone_number = self.df[self.df.wed_month_day == (month, day)].phone_number
        first_name = self.df[self.df.wed_month_day == (month, day)].first_name
        surname  = self.df[self.df.wed_month_day == (month, day)].surname
        title = self.df[self.df.wed_month_day == (month, day)].title
        year_of_marriage = self.df[self.df.wed_month_day == (month, day)].wedding_age
        return list(zip(title,first_name,surname,phone_number,email,year_of_marriage))


    def eligible_monthly_msg(self):
        eligible = self.df[self.df['age'] > 12 ].phone_number
        return eligible

    def b_day_checker(self):
        if len(self.today_birthday_celebrants()) > 0 :
            return True
        else:
            return False

    def wedding_checker(self):
        if len(self.today_wedding()) > 0:
            return True
        else:
            return False

    def b_day_message_picker(self, member):
        message_picked = random.choice(list(messages['b_day_msg']))
        hash_replace = message_picked.replace('###', member)
        return hash_replace

    def wed_message_picker(self, age):
        message_picked = random.choice(list(messages['wed_msg']))
        hash_replace = message_picked.replace('###', str(age))
        return hash_replace

    def birthday_month_message_picker(self, month):
        messsage_picked = messages['bday_months'][0][month]
        return messsage_picked

    def messaging_test(self):
        # for the day birthday celebrants
        if self.b_day_checker():
            message_details = {'names': [],
                               'messages': [],
                               "fullname": []
                               }
            sms = self.sms
            sender_name = 'Araba B.C'
            for i in self.today_birthday_celebrants():
                first_name = i[1]
                surname = i[2]
                phone_numbers = i[3]
                email=i[4]
                phone_numbers = '2348080415982'
                name = i[0] + " " + i[1]
                full_name = name + " " + surname
                message = self.b_day_message_picker(name)
                message_details['names'].append(name)
                message_details['messages'].append(message)
                message_details['fullname'].append(full_name)
                subject = 'Happy Birthday'
                sms.sms_sender(sender=sender_name, phone_numbers=phone_numbers, message=message)
                try:
                    email.send_email(os.environ.get('secretariat_email'),os.environ.get('secretariat_password'),subject,message,i[4])
                except:
                    pass
            

            # send_email(messagess,subject)


    

    def messaging(self):
#for the day birthday celebrants
        if self.b_day_checker():
            message_details = {'names': [],
                               'messages': [],
                               'full_name': []}
            sms = Sms()
            email = SendEmail()
            sender_name = 'Araba B.C'
            for i in self.today_birthday_celebrants():
                # first_name =
                # phone_numbers = i[2]
                phone_numbers = '2348080415982'
                name = i[0]

                message = self.b_day_message_picker(name)
                message_details['names'].append(name)
                message_details['messages'].append(message)
                subject = 'Happy Birthday'
                sms.sms_sender(sender=sender_name, phone_numbers=phone_numbers, message=message)
                try:
                    email.send_email(os.environ.get('secretariat_email'),os.environ.get('secretariat_password'),subject,message,i[4])
                except:
                    pass

                 # self.secretariat_email = os.environ.get('secretariat_email')
        # self.secretariat_password= os.environ.get('secretariat_password')
        # self.youth_email = os.environ.get('youth_email')
        # self.youth_password = os.environ.get('youth_password')
            

                
            # send_email(messagess,subject)



        else:
            messagess = 'No Birthday Sms was sent today'
            subject = 'no bday'

            send_email(messagess, subject)
#for the day wedding celebrant
        if self.wedding_checker():
            message_details = {'names': [],
                               'messages': [],
                               'wed_names': []}
            sms = Sms()
            sender_name = 'Araba B.C'
            for i in self.today_wedding():
                phone_numbers = i[1]
                # phone_numbers = '2348080415982'
                name = i[0]
                age = i[2]
                message = self.wed_message_picker(age)
                message_details['wed_names'].append(name)
                message_details['messages'].append(message)
                sms.sms_sender(sender=sender_name, phone_numbers=phone_numbers, message=message)

            messagess = f"wedding message was sent to {message_details['wed_names']}"
            subject = 'wedding sent'
            send_email(messagess, subject)
        else:
            messagess = "No Wedding Sms was sent today"
            subject = 'wedding not sent'
            send_email(messagess, subject)
# for the month birthday celebrant
        if datetime.datetime.today().date().day == 1 and len(self.month_birthday()) > 0:
            sms = Sms()
            sender_name = 'Araba B.C'
            phone_numbers = [i[1] for i in self.month_birthday()]
            name = [i[0] for i in self.month_birthday()]
            phone_numberss = ','.join([str(elem) for elem in phone_numbers if len(elem) > 9])
            message = self.birthday_month_message_picker(datetime.datetime.today().date().month)
            sms.sms_sender(sender=sender_name, phone_numbers=phone_numberss, message=message)
            messagess = f"monthly b_day message was sent to  {name}"
            subject = 'bday sent'
            send_email(messagess, subject)
#A new month message to everyone
        if datetime.datetime.today().date().day == 1:
            sms = Sms()
            sender_name = 'Araba B.C'
            phone_numbers = self.monthly_msg()

            phone_numberss = ','.join([str(elem) for elem in phone_numbers if len(elem) > 9])
            message = self.general_month_message_picker(datetime.datetime.today().date().month)
            sms.sms_sender(sender=sender_name, phone_numbers=phone_numberss, message=message)
            messagess = f"monthly message was sent to  everybody, {message}"
            subject = 'New Month'
            send_email(messagess, subject)


print(Celebrants().messaging_test())





# # os.environ.get

# user = 'arababaptistchurch@ymail.com'
# password = 'chhxqcqaewdofmmy'
# recipient= 'akinbodebamigboye@gmail.com'
# smtp_detail = 'smtp.mail.yahoo.com'
# SMTP_PORT = 587
# sms_username = 'secretariat@abc.org.ng'
# sms_password = 'Kimgo9-kejhim-bahwew'



# def send_email(msg,EMAIL_SUBJECT):
#     msg = MIMEText(msg)
#     msg['Subject'] = EMAIL_SUBJECT
#     msg['From'] = user
#     msg['To'] = recipient
#     debuglevel = True
#     mail = smtplib.SMTP(smtp_detail, SMTP_PORT)
#     mail.set_debuglevel(debuglevel)
#     mail.starttls()
#     mail.login(user, password)
#     mail.sendmail(user, recipient, msg.as_string())
#     mail.quit()







# # def wedding_age(new):
# #     this_year = datetime.datetime.today().year
# #     age = this_year - new.year
# #     return age





