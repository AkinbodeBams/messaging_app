
import math
import pandas as pd
import random
import requests
import datetime
import numpy as np
import os
from dotenv import load_dotenv


class Data:

    def __init__(self):
        load_dotenv()
        self.engine = 'postgresql://postgres:1855@localhost/araba-django'
        # self.engine = os.getenv(('db')
        self.df = pd.read_sql('select * from app_members', con=self.engine)
        self.df['wedding_date'] = pd.to_datetime(
            self.df['wedding_date'], errors='coerce')
        self.df['gender'] = self.df["gender"].str.strip()
        self.df['age'] = self.df['date_of_birth'].apply(self.age)
        self.df['wedding_age'] = self.df['wedding_date'].apply(self.age)
        self.df["gender"] = self.df["gender"].str.lower()
        self.df["marital_status"] = self.df["marital_status"].str.lower()
        self.df['title'] = self.df.apply(self.title_adder, axis=1)
        self.df['full_name'] = self.df.title + " " + \
            self.df.first_name + " " + self.df.surname
        self.df['month_and_day'] = self.df['date_of_birth'].apply(
            self.month_day)
        self.df['wed_month_day'] = self.df['wedding_date'].apply(
            self.wed_month_day)
        self.df['month'] = self.df['date_of_birth'].apply(self.month)
        self.df['wedding_date'] = pd.to_datetime(
            self.df['wedding_date'], errors='coerce')
        self.df['full_name'] = self.df.title + " " + \
            self.df.first_name + " " + self.df.surname
        self.df.drop_duplicates(subset='full_name', keep=False, inplace=True)

    def age(self, new):
        this_year = datetime.datetime.today().year
        age = this_year - new.year
        return age

    def month_day(self, new):
        return new.month, new.day

    def wed_month_day(self, new):
        if new == pd.isnull(np.datetime64('NaT')):
            month_and_day = (0, 0)
        else:
            current_month = new.month
            day = new.day
            month_and_day = (current_month, day)
        return month_and_day

    def month(self, new):
        current_month = new.month

        return current_month

    def title_adder(self, new):
        #     new['date_of_birth'] = pd.to_datetime(new['date_of_birth'], infer_datetime_format=True)
        new["gender"] = new["gender"]
        new["marital_status"] = new["marital_status"]
        if new.first_name.lower() == 'oluwagbenga' and new.surname.lower() == 'ojo':
            return 'Rev'
        elif new.gender.lower() == 'male' and self.age(new.date_of_birth) >= 70:
            return 'Pa'
        elif new.gender.lower() == 'female' and self.age(new.date_of_birth) >= 70:
            return 'Ma'
        elif new.gender.lower() == 'female' and self.age(new.date_of_birth) >= 40 and new.marital_status == 'single':
            return 'Ms'
        elif new.gender.lower() == 'male' and self.age(new.date_of_birth) >= 40 and new.marital_status == 'single':
            return 'Mr'
        elif new.gender.lower() == 'female' and new.marital_status == 'married':
            return 'Mrs'
        elif new.gender.lower() == 'female' and new.marital_status == 'single':
            return 'Miss'
        elif new.gender.lower() == 'male' and new.marital_status == 'married':
            return 'Mr'
        elif new.gender.lower() == 'male' and new.marital_status == 'single':
            return 'Bro'

        else:
            pass
