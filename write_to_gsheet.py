import os
import google.auth
from googleapiclient.discovery import build

def write_to_gsheet(sheet_id, range_name, platform, device, action_number, action_link, action_duration):
    creds, _ = google.auth.load_credentials_from_file('google_application_credentials.json')
    service = build('sheets', 'v4', credentials=creds)

    values = [[platform, device, action_number, action_link, action_duration]]
    body = {
        'values': values
    }

    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id, range=range_name,
        valueInputOption='RAW', body=body).execute()

    print(f"{result.get('updatedCells')} cells updated.")

def main():
    sheet_id = os.environ['SPREADSHEET_ID']
    range_name = 'Sheet1!A1'  # Update this to the desired cell range

    platform = os.environ['PLATFORM']
    device = os.environ['DEVICE']
    action_number = os.environ['ACTION_NUMBER']
    action_link = os.environ['ACTION_LINK']
    action_duration = os.environ['ACTION_DURATION']

    write_to_gsheet(sheet_id, range_name, platform, device, action_number, action_link, action_duration)

    if __name__ == '__main__':
    main()

