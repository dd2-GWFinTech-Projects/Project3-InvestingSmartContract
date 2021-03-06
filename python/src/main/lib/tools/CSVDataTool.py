import pandas as pd

class CSVDataTool:
    """
    CSV utility functions.
    """

    def load_csv_data_as_dataframe(self, csv_file_path):
        dataframe = pd.read_csv(csv_file_path)
        return dataframe

    def load_csv_data_as_dict(self, csv_file_path):
        dataframe = pd.read_csv(csv_file_path)
        return dataframe.to_dict()
