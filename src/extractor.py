import pandas as pd

class DataExcelExtractor:

    def extract(self, path, sheet_name):
        df = pd.read_excel(path, sheet_name=sheet_name)
        return df

