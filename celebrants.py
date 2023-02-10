import datetime
import os
from sms import Sms
from send_email import SendEmail
from data import Data
import random
from dotenv import load_dotenv
from messages import messages


email_from = 'secretariat@abc.org.ng'
password = 'ABCilasamaja1953'
# email_to = ['justmeontop@gmail.com',"benjamin20130874@gmail.com",
# 'oye93@aol.com',"Oluwatidamilare19@gmail.com","oshinojo.adedeji@gmail.Com",
# "Kennykolaru@gmail.com"]
email_to = ['oye93@aol.com']

class Celebrants:

    def __init__(self):
        self.df = Data().df
        load_dotenv()

    def month_birthday_celebrants(self):
        today = datetime.datetime.today().date()
        # today = datetime.datetime(2020, 2, 1)
        month = today.month
        email = self.df[self.df.month == month].email
        phone_number = self.df[self.df.month == month].phone_number
        title = self.df[self.df.month == month].title
        first_name = self.df[self.df.month == month].first_name.str.title()
        surname = self.df[self.df.month == month].surname.str.title()
        return [title, first_name, surname, phone_number, email]

    def today_birthday_celebrants(self):
        celebrant_details = {}
        today = datetime.datetime.today().date()
        # today = datetime.datetime(1993, 3, 9)
        month = today.month
        day = today.day
        phone_number = self.df[self.df.month_and_day ==
                               (month, day)].phone_number
        email = self.df[self.df.month_and_day == (month, day)].email
        first_name = self.df[self.df.month_and_day == (month, day)].first_name
        title = self.df[self.df.month_and_day == (month, day)].title
        surname = self.df[self.df.month_and_day == (month, day)].surname

        return list(zip(title, first_name, surname, phone_number, email))

    def today_wedding(self):
        lst = []
        celebrants_info = {}
        today = datetime.datetime.today().date()
        # today = datetime.datetime(2020, 4, 9)
        month = today.month
        day = today.day
        email = self.df[self.df.wed_month_day == (month, day)].email
        phone_number = self.df[self.df.wed_month_day ==
                               (month, day)].phone_number
        first_name = self.df[self.df.wed_month_day == (month, day)].first_name
        surname = self.df[self.df.wed_month_day == (month, day)].surname
        title = self.df[self.df.wed_month_day == (month, day)].title
        year_of_marriage = self.df[self.df.wed_month_day == (
            month, day)].wedding_age
        return list(zip(title, first_name, surname, phone_number, email, year_of_marriage))

    def eligible_monthly_msg(self):
        eligible = self.df[self.df['age'] > 12].phone_number
        return eligible

    def b_day_checker(self):
        if len(self.today_birthday_celebrants()) > 0:
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

    def messaging(self):
        # for the day birthday celebrants
        if self.b_day_checker():
            
            sms = Sms()
            email = SendEmail()
            sender_name = 'Araba B.C'
            for i in self.today_birthday_celebrants():
                phone_numbers = i[3]
                # phone_numbers = '08080415982'
                name = f'{i[0]} {i[1]}'
                message = self.b_day_message_picker(name)
                subject = 'Happy Birthday'

                sms.sms_sender(sender=sender_name,
                               phone_numbers=phone_numbers, message=message)
            

        if self.wedding_checker():
           
            sms = Sms()
            sender_name = 'Araba B.C'
            for i in self.today_wedding():
                # phone_numbers = i[3]
                phone_numbers = '2348080415982'
                name = f'{i[0]} {i[1]}'
                age = i[5]
                message = self.wed_message_picker(age)
               
                sms.sms_sender(sender=sender_name,
                               phone_numbers=phone_numbers, message=message)
            

# for the month birthday celebrant
        if datetime.datetime.today().date().day == 1 and len(self.month_birthday()) > 0:
            sms = Sms()
            sender_name = 'Araba B.C'
            phone_numbers = [i[1] for i in self.month_birthday()]
            name = [i[0] for i in self.month_birthday()]
            phone_numberss = ','.join(
                [str(elem) for elem in phone_numbers if len(elem) > 9])
            message = self.birthday_month_message_picker(
                datetime.datetime.today().date().month)
            # sms.sms_sender(sender=sender_name,
            #                phone_numbers=phone_numberss, message=message)
            messagess = f"monthly b_day message was sent to  {name}"
            subject = 'bday sent'

# A new month message to everyone
        if datetime.datetime.today().date().day == 1:
            sms = Sms()
            sender_name = 'Araba B.C'
            phone_numbers = self.monthly_msg()

            phone_numberss = ','.join(
                [str(elem) for elem in phone_numbers if len(elem) > 9])
            message = self.general_month_message_picker(
                datetime.datetime.today().date().month)
            sms.sms_sender(sender=sender_name,
                           phone_numbers=phone_numberss, message=message)
            print('sms sent')
            messagess = f"monthly message was sent to  everybody, {message}"
            subject = 'New Month'

        try:
            email.send_email(email_from,password,email_to,b_details= self.today_birthday_celebrants(), w_details=self.today_wedding())
        except Exception as e :
            print(f'bday {e}')


print(Celebrants().today_birthday_celebrants())

