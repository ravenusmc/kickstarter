#importing supporting libraries
import numpy as np
import pandas as pd
import datetime

# This class will deal with a majority of the data processing that this project will
# handle.
class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/ks-projects-201801.csv')
        self.data['deadline'] = pd.to_datetime(self.data['deadline'], infer_datetime_format=True)

    def unique_values(self):
        print(self.data['main_category'].unique())

    def first_chart(self, category, state, currency, country, start_date, end_date, money_goal, backers):
        first_time_stamp = pd.to_datetime(start_date)
        last_time_stamp = pd.to_datetime(end_date)
        data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
        print(len(data))


data = Data()
data.unique_values()
