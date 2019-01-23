import pickle
import os.path
import os
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from shutil import rmtree

# Global variable to store drive service
drive_service = None

def main():	
	# if directory empty, do nothing
	files = os.listdir('./data')
	if not files:
		print("Nothing to upload")
		quit()

	# creating a drive service connection 
	global drive_service
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
		drive_service = build('drive', 'v3', credentials=creds)
	else:
		print("Credentials not found.\nPossible error with authentication flow. Exiting...")
		quit()

	# upload local files
	for file in files:
		path = "./data/" + file
		if os.path.isfile(path):
			file_metadata = {'name': file}
			media = MediaFileUpload(path, resumable=False)
			drive_file = drive_service.files().create(body=file_metadata, media_body = media, fields='id').execute()
			print("\n" + file + " Uploaded." + "\nFile ID is " + drive_file.get('id') + "\n")
		elif os.path.isdir(path):
			upload_folder(folder_name = file, folder_abs_path = os.path.abspath(path))
		elif os.path.islink(path):
			print("Warning: Symlinks are not followed.")
			print("Instance: " + os.path.abspath(file))
		else:
			print("FATAL ERROR")

	# delete local files
	a = input("Delete ALL local copies? (Y/N)\t")
	if a == 'y' or a == 'Y':
		for file in files:
			if os.path.isdir("./data/" + file):
				print("Deleting tree: data/" + file)
				rmtree("./data/" + file)
			elif os.path.isfile("./data/" + file):
				print("Deleting data/" + file)
				os.remove("./data/" + file)

def upload_folder(folder_name, folder_abs_path, parent=None):
	# create empty folder and place it under proper folder in GDrive
	folder_metadata = {
		'name' : folder_name,
		'mimeType' : 'application/vnd.google-apps.folder'
	}
	if parent != None: 
		folder_metadata.update({'parents': [parent]})
	file = drive_service.files().create(body=folder_metadata, fields='id').execute()
	folder_id = file.get('id')
	print("\nFolder: " + folder_name + " Created. Folder ID: " + folder_id + "\n")

	files = os.listdir(folder_abs_path)
	for file in files:
		path = folder_abs_path + '/' + file
		if os.path.isdir(path): 
			upload_folder(file, path, folder_id)
		elif os.path.islink(path):
			print("Warning: Symlinks are not followed.")
			print("Instance: " + path)
		else:
			file_metadata = {'name': file}
			file_metadata.update({'parents': [folder_id]})
			media = MediaFileUpload(path)
			drive_file = drive_service.files().create(body=file_metadata, 
					media_body = media, fields='id').execute()
			print("\n" + path + " Uploaded." + "\nFile ID is " + drive_file.get('id') + "\n")

if __name__ == '__main__':
	main()			