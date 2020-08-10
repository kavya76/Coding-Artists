import os

import pandas as pd

threshold = 4.0
pd.options.mode.chained_assignment = None  # default='warn'
def path_list():
    paths = []
    for file in os.listdir("SCEC_DC"):
        if file.endswith(".catalog"):
            paths.append(os.path.join("SCEC_DC", file))
    return paths


def read_data(path):
    df = pd.read_csv(path, skiprows=10, header=None,
                     sep=r"\s*",
                     engine='python')  

    df.drop(df.tail(3).index,
            inplace=True)  
    df = df.rename(columns={0: "Date"})
    df = df.rename(columns={1: "Time"})
    df = df.rename(columns={2: "ET"})
    df = df.rename(columns={3: "GT"})
    df = df.rename(columns={4: "Magnitude"})
    df = df.rename(columns={5: "M"})
    df = df.rename(columns={6: "Lat"})
    df = df.rename(columns={7: "Lon"})
    df = df.rename(columns={8: "Depth"})
    df = df.rename(columns={9: "Q"})
    df = df.rename(columns={10: "EVID"})
    df = df.rename(columns={11: "NPH"})
    df = df.rename(columns={12: "NGRM"})

    return df
