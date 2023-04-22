import os

import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from entities.manage_dbs import getUber
from google.oauth2.service_account import Credentials
credentials_path = 'credentials/tvde-382009-9532aa3c4aca.json'

if os.path.exists(credentials_path):
    try:
        # Connect to Google Sheets API
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path,
                                                                       ['https://www.googleapis.com/auth/spreadsheets',
                                                                        'https://www.googleapis.com/auth/drive'])
        client = gspread.authorize(credentials)

    except HttpError as e:
        print(e)
        exit()

sheet = client.open('TVDE_Dashboard')
sheet_id = sheet.id


df = getUber()

sheet = client.open('TVDE_Dashboard')

# Select the worksheet where you want to write the data
worksheet = sheet.worksheet("Sheet1")

# Convert the Pandas DataFrame into a list of lists
data = df.values.tolist()

# Clear any existing data from the worksheet
worksheet.clear()

# Write the data to the worksheet
worksheet.update('A1', data)


exit()










# Convert DataFrame to 2D array
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                   'age': [25, 30, 35],
                   'city': ['New York', 'San Francisco', 'Los Angeles']})
values = df.values.tolist()

# Write the data to the sheet
range_name = 'Sheet1!A1'
body = {
    'values': values
}
result = client.spreadsheets().values().update(
    spreadsheetId=sheet_id, range=range_name,
    valueInputOption='USER_ENTERED', body=body).execute()
print(f"{result.get('updatedCells')} cells updated.")
exit()
for index, row in df.iterrows():
    if row['Motorista'] != 'Todos os motoristas':
        list_data = [row['Motorista'], row['Telemóvel do motorista'], row['Tarifa bruta'], row['Taxa de cancelamento'],
                     row['Portagem'], row['Taxa Bolt'], row['Bónus do Motorista'], row['Gorjeta'], row['Horas online'],
                     row['Utilização']]
        print(list_data)

cell_range = sheet.range('A1:B{}'.format(df.iterrows()))

flat_data = [cell for row in data for cell in row]

df_list = df.values.tolist()

request_body = {
    'values': df_list
}