import pandas as pd

# Đọc file dataset-city
def read_dataset_city(path):
    data_table = pd.read_csv(path)
    return data_table

