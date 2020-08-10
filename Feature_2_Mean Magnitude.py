import numpy as np
import pandas as pd
from filter import read_data, path_list,threshold

paths = path_list()

def read_feature_2(path):
    df = read_data(path)

    df['Magnitude'] = df['Magnitude'].apply(pd.to_numeric)
    new_df = df.loc[df["Magnitude"] > threshold]
    # x = new_df['Date']+' '+new_df['Time']
    # new_df["Datetime"] = pd.to_datetime(x ,format='%Y/%m/%d %H:%M:%S.%f')
    x = new_df['Date']
    new_df["Date"] = pd.to_datetime(x, format='%Y/%m/%d')
    del new_df["Time"]
    groups = new_df.groupby(
        new_df.Date.dt.month) 

    #print(groups['Magnitude'].mean())
    return groups['Magnitude'].mean()

def read_full_feature_2():
    Mean_Magnitude = []
    for path in paths:
        Mean_Magnitude.append(read_feature_2(path))
    return np.array(Mean_Magnitude)
