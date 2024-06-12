

class ArrayTransformer:
    def transform(self, df, column_name):
        return df[column_name].to_numpy()

