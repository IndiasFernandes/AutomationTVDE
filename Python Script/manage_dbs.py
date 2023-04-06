import os
import pandas as pd
import numpy as np
import math

path = 'downloads'

# Creates a list with all file names
filesInPath = os.listdir(path)

for file in filesInPath:
    df = pd.read_csv(file)

df = df.replace(np.nan, '', regex=True)

for index, row in df.iterrows():
    print(row['Motorista'])
    if row['Motorista'] == '':
        last_row = index
        break
print(df)
df = df.drop(df.index[index:], inplace=False)
print(df.to_string())
print(index)