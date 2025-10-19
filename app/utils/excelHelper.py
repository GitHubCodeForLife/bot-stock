import pandas as pd

class ExcelHelper:
    @staticmethod
    def read_excel(file_path, sheet_name):
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    
    @staticmethod
    def write_excel(file_path, sheet_name="Sheet1",  data_frame=None):
        # convert column time to str 
        if 'time' in data_frame.columns:
            data_frame['time'] = data_frame['time'].astype(str)
        # allow to create a new excel file or append to existing one
        # allow to write existing sheet or create new sheet
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a' if pd.io.common.file_exists(file_path) else 'w') as writer:
            data_frame.to_excel(writer, sheet_name=sheet_name, index=False)