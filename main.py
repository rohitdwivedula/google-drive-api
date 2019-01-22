import pickle
import os.path
import os
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build

if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

drive_service = build('drive', 'v3', credentials=creds)
files = os.listdir('./data')

# if directory empty, do nothing
if not files:
	print("Nothing to upload")
	quit()

for file in files:
	path = "./data/" + file
	file_metadata = {'name': file}
	media = MediaFileUpload(path, resumable=True)
	file = drive_service.files().create(body=file_metadata, media_body = media, fields='id').execute()
	print("File ID is " + file.get('id'));

a = input("Delete local copies? (Y/N)    ")
if a == 'y' or a == 'Y':
	for file in files:
		print("Deleting data/" + file)
		os.remove("./data/" + file)