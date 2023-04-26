import os
import google.auth
from googleapiclient.discovery import build

def write_to_gsheet(sheet_id, range_name, values):
    creds, _ = google.auth.load_credentials_from_file('google_application_credentials.json')
    service = build('sheets', 'v4', credentials=creds)
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id, range=range_name,
        valueInputOption='RAW', body=body).execute()
    print(f"{result.get('updatedCells')} cells updated.")

def main():
    sheet_id = os.environ['SPREADSHEET_ID']
    range_name = 'Sheet1!A1'
    values = [['Hello, World!']]
    write_to_gsheet(sheet_id, range_name, values)

if __name__ == '__main__':
    main()
