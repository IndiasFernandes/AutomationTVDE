import os
import pandas as pd
import numpy as np
import math

def getUber():

    path = 'downloads'

    # Creates a list with all file names
    filesInPath = os.listdir(path)


    print('Files not available, but checking:')
    print(filesInPath)
    filesInPath == ['2023W09(0207-1307)UBER.csv']

    for file in filesInPath:
        df = pd.read_csv('downloads/'+file)

    df = df.replace(np.nan, '', regex=True)

    column_name = 'Motorista'  # the name of the specific column you want to check

    idx = (df[column_name].index[df[column_name].apply(lambda x: not x)].tolist() or [None])[0]
    if idx is not None:
        print(f"Deleting all rows starting on {idx}")
        index_to_drop = range(idx, len(df))
        df = df.drop(index_to_drop)
        print(f"Deleted {len(index_to_drop)} rows")
    else:
        print(f"No empty rows found in column '{column_name}'")
    print(f"Uber Dataset found from {file}")


    # df = df.drop(df.index[index:], inplace=False)
    # print(df.to_string())
    # print(index)

    return df