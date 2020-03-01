#This file will deal with getting the data for the project.

#importing supporting libraries
import numpy as np
import pandas as pd
import datetime

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/ks-projects-201801.csv')

    def first_chart(self):
        pass


# data = Data()
# data.test()
