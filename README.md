# About

This script will upload a file in a specific directory to your Google Drive Account. 

# Setup
1. Clone this repo. 
2. Go to the [Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python) page, enable the Drive API and download the credentials file. Save the credentials file in the working directory.
3. Run this in the command prompt: 
```shell
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
4. Run quickstart.py in the terminal. A browser window should open up - complete the authentication flow. (You will need to give complete Google Drive permission)
5. Create a folder /data inside the working directory. Place files you want to upload inside that.
5. Run main.py to upload all files in /data folder
6. The script will prompt you whether to delete the local copies of the file or not. 

# Future Improvements 

1. Add support to specify **which directory** in Google Drive to save the files in.
2. Add functionality to check if file with same name already exists on drive. Prompt user whether to overwrite or not. 
3. Support upload of folders and nested folders