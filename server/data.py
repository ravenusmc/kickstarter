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
        #checking the datatypes of a column
        print(self.data.dtypes)
        #print(self.data['main_category'].unique())

    def first_chart(self, category, state, currency, country, start_date, end_date, money_goal, backers):
        # This list will hold the data that will be returned from this method.
        first_chart_data = []
        columns = ['State', 'Count']
        first_chart_data.append(columns)
        first_time_stamp = pd.to_datetime(start_date)
        last_time_stamp = pd.to_datetime(end_date)
        # Sorting the data by the time frame that the user entered.
        data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
        # Sorting the data by the other parameters that the user entered.
        data_set = data[(data.category == category) & (data.currency == currency) & (data.country == country) & (data.backers <= backers) & (data.goal <= money_goal)]
        states = ['failed', 'successful', 'canceled']
        for state in states:
            #resetting the data set for each loop
            new_data_set = data_set
            rows = []
            dataset_length = len(new_data_set[(new_data_set.state == state)])
            rows.append(state)
            rows.append(dataset_length)
            first_chart_data.append(rows)
        return first_chart_data

    def successful_by_category(self, post_data):
        print(post_data)
        return('Hi')



# data = Data()
# data.unique_values()
