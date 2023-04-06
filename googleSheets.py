import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

credentials = service_account.Credentials.from_service_account_file('credentials/tvde-382009-ed897c28e484.json')

service = build('sheets', 'v4', credentials=credentials)

spreadsheet_id = 'your-spreadsheet-id'
range_name = 'Sheet1!A1'

df = pd.read_csv('Python Script/downloads/Bolt Weekly Report - 2023W09 - Lisbon Fleet Vogais do Coração Unipessoal lda.csv')

df_list = df.values.tolist()

request_body = {
    'values': df_list
}