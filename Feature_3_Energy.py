import numpy as np
import pandas as pd

from Feature_1_time import read_feature_1
from filter import read_data, path_list, threshold

paths = path_list()

def read_feature_3(path):
    df = read_data(path)

    df['Magnitude'] = df['Magnitude'].apply(pd.to_numeric)
    new_df = df.loc[df["Magnitude"] > threshold]
    x = new_df['Date']
    new_df["Date"] = pd.to_datetime(x, format='%Y/%m/%d')
    del new_df["Time"]
    groups = new_df.groupby(new_df.Date.dt.month) 
    T = read_feature_1(path)
    months_available = groups.groups.keys() 
    dE = []
    for month in months_available:
        dE.append(np.sum(groups.get_group(month)["Magnitude"].apply(lambda x: np.sqrt(10**(11.8+1.5*x)))))
    dE = np.array(dE)
    old = np.seterr('ignore')  # used to ignore divide by zero exception
    return np.array(dE / T)

def read_full_feature_3():
    Energy = []
    for path in paths:
        Energy.append(read_feature_3(path))
    return np.array(Energy)