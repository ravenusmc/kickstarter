#importing supporting libraries
import numpy as np
import pandas as pd
import datetime

# This class will deal with a majority of the data processing that this project will
# handle.
class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/ks-projects-201801.csv')

    def unique_values(self):
        print(self.data['main_category'].unique())


data = Data()
data.unique_values()
