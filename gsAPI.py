import os
import requests
import google_auth_oauthlib
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import re
from clint.textui import progress
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('sheets', 'v4', credentials=creds)
def download_map(url, path):
    input_string = url
    print("Processing...")
    print("Getting spreadsheet ID...")
    spreadsheet_id = input_string[39:83]
    pattern = re.compile(r'=(\d+)&')
    matches = pattern.findall(input_string)
    sheet_id = int(matches[0])
    print("Getting sheet ID...")
    sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = sheet_metadata.get('sheets', '')
    print("Getting sheet name...")
    for sheet in sheets:
        if sheet['properties']['sheetId'] == sheet_id:
            sheet_name = sheet['properties']['title']
            print('Sheet name:', sheet_name)
    
    link_range = input_string.split("range=")[1]
    range_name = sheet_name + f'!{link_range}'
    print("Your range is: ", link_range)
    
    download_confirm(spreadsheet_id, range_name, path)

def download_confirm(spreadsheet_id, range_name, path):
    name = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, 
                                        range=range_name).execute()
    print("You about to download:")
    for i in name.get('values'):
        print(i[0])
    confirm = input("Is this correct? y/n: ")
    if confirm == "y":
        print('Downloading...')
        download_start(spreadsheet_id, range_name, path)
        pass
    else:
        exit()
def download_start(spreadsheet_id, range_name, path):
    sheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id, 
                                        ranges=range_name, 
                                        fields="sheets/data/rowData/values/hyperlink").execute()

    values = sheets.get('sheets')[0].get('data')[0].get('rowData')
    for value in values:
        print(value.get('values')[0].get('hyperlink'))
        idpattern = re.compile(r'/(\d+)#osu')
        idmatches = idpattern.findall(value.get('values')[0].get('hyperlink'))
        map_id = int(idmatches[0])
        folderpath = path
        response = requests.get(f'https://beatconnect.io/b/{map_id}/', stream=True)
        header = response.headers.get('content-disposition')
        if header is None:
            filename = f'{map_id}.osz'
        else:
            filename = re.findall('filename=(.+)', header)[0]
            filename = filename.replace('"', '').replace(';', '').replace(':', '').replace(',', '')
        
        with open(folderpath + "/" + filename, 'wb') as f:
            total_length = int(response.headers.get('content-length'))
            for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()
        print(f"Downloaded map success: {filename}")
