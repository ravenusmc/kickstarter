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
        successful_by_category_data = []
        categories = ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
        'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance', 'Journalism']
        columns = ['Category', 'Count']
        successful_by_category_data.append(columns)
        # Getting dates and sorting data by them.
        first_time_stamp = pd.to_datetime(post_data['startDate'])
        last_time_stamp = pd.to_datetime(post_data['endDate'])
        # Sorting the data by the time frame that the user entered.
        data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
        for category in categories:
            #resetting the data set for each loop
            new_data_set = data
            rows = []
            dataset_length = len(new_data_set[(new_data_set.category == category) & (new_data_set.state == 'successful')])
            rows.append(category)
            rows.append(dataset_length)
            successful_by_category_data.append(rows)
        return(successful_by_category_data)

    # I will say this - I should have combined this method with the one above it which
    # would have been really easy - just including failures above! This is what
    # happens when I start to code but do not think through the code!!
    def failures_by_category(self, post_data):
        failures_by_category_data = []
        categories = ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
        'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance', 'Journalism']
        columns = ['Category', 'Count']
        failures_by_category_data.append(columns)
        # Getting dates and sorting data by them.
        first_time_stamp = pd.to_datetime(post_data['startDate'])
        last_time_stamp = pd.to_datetime(post_data['endDate'])
        # Sorting the data by the time frame that the user entered.
        data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
        for category in categories:
            #resetting the data set for each loop
            new_data_set = data
            rows = []
            dataset_length = len(new_data_set[(new_data_set.category == category) & (new_data_set.state == 'failed')])
            rows.append(category)
            rows.append(dataset_length)
            failures_by_category_data.append(rows)
        return(failures_by_category_data)

    def Success_And_Failures_chart(self, post_data):
        success_and_failures_data = []
        columns = ['State', 'Count']
        success_and_failures_data.append(columns)
        # Getting dates and sorting data by them.
        first_time_stamp = pd.to_datetime(post_data['startDate'])
        last_time_stamp = pd.to_datetime(post_data['endDate'])
        # Sorting the data by the time frame that the user entered.
        data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
        states = ['failed', 'successful', 'canceled']
        for state in states:
            #resetting the data set for each loop
            new_data_set = data
            rows = []
            dataset_length = len(new_data_set[(new_data_set.state == state)])
            rows.append(state)
            rows.append(dataset_length)
            success_and_failures_data.append(rows)
        return success_and_failures_data

    def All_States_By_Category(self, post_data):
        All_States_By_Category_data = []
        columns = ['Category', 'successful', 'failed', 'canceled']
        All_States_By_Category_data.append(columns)
        # Getting dates and sorting data by them.
        first_time_stamp = pd.to_datetime(post_data['startDate'])
        last_time_stamp = pd.to_datetime(post_data['endDate'])
        # Sorting the data by the time frame that the user entered.
        data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
        categories = ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
        'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance', 'Journalism']
        for category in categories:
            #resetting the data set for each loop
            new_data_set = data
            #This list will hold the data for a specific row
            rows = []
            rows.append(category)
            category_data_set = new_data_set[(new_data_set.category == category)]
            states = ['successful', 'failed', 'canceled']
            for state in states:
                #resetting the data set for each loop
                state_data_set = category_data_set
                dataset_length = len(state_data_set[(state_data_set.state == state)])
                rows.append(dataset_length)
            All_States_By_Category_data.append(rows)
        return All_States_By_Category_data

    # def All_States_By_Category(self, post_data):
    #     All_States_By_Category_data = []
    #     columns = ['Category', 'Count']
    #     All_States_By_Category_data.append(columns)
    #     # Getting dates and sorting data by them.
    #     first_time_stamp = pd.to_datetime(post_data['startDate'])
    #     last_time_stamp = pd.to_datetime(post_data['endDate'])
    #     print(first_time_stamp)
    #     print(last_time_stamp)
    #     # Sorting the data by the time frame that the user entered.
    #     data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
    #     categories = ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
    #     'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance', 'Journalism']
    #     for category in categories:
    #         #resetting the data set for each loop
    #         new_data_set = data
    #         category_data_set = new_data_set[(new_data_set.category == category)]
    #         states = ['failed', 'successful', 'canceled']
    #         total = 0
    #         for state in states:
    #             rows = []
    #             #resetting the data set for each loop
    #             state_data_set = category_data_set
    #             dataset_length = len(state_data_set[(state_data_set.state == state)])
    #             total = dataset_length + total
    #         rows.append(category)
    #         rows.append(total)
    #         All_States_By_Category_data.append(rows)
    #     return All_States_By_Category_data

    # def Success_And_Failures_chart(self, post_data):
    #     success_and_failures_data = []
    #     columns = ['Category', 'State', 'Count']
    #     success_and_failures_data.append(columns)
    #     # Getting dates and sorting data by them.
    #     first_time_stamp = pd.to_datetime(post_data['startDate'])
    #     last_time_stamp = pd.to_datetime(post_data['endDate'])
    #     # Sorting the data by the time frame that the user entered.
    #     data = self.data.loc[(self.data['deadline'] >= first_time_stamp) & (self.data['deadline'] <= last_time_stamp), :]
    #     categories = ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
    #     'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance', 'Journalism']
    #     states = ['failed', 'successful', 'canceled']
    #     for category in categories:
    #         #resetting the data set for each loop
    #         new_data_set = data
    #         category_data_set = new_data_set[(new_data_set.category == category)]
    #         for state in states:
    #             rows = []
    #             rows.append(category)
    #             #resetting the data set for each loop
    #             state_data_set = category_data_set
    #             dataset_length = len(state_data_set[(state_data_set.state == state)])
    #             rows.append(state)
    #             rows.append(dataset_length)
    #             success_and_failures_data.append(rows)
    #     return success_and_failures_data





# data = Data()
# data.unique_values()
