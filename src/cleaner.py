import numpy as np


class DataCleaner:

    def __init__(self, df):
        self.df = df

    def clean(self, column_number_to_clean):
        self.df.replace('\xa0', np.nan, inplace=True)
        #\n, \xa01
        self.df.replace(['\n', '\xa0'], '', regex=True, inplace=True)
        return self.df.dropna(subset=[self.df.columns[column_number_to_clean]])

