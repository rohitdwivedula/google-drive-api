# About

This 

# Setup
1. Clone this repo. 
2. Go to the [Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python) page, enable the Drive API and download the credentials file. Save the credentials file in the working directory.
3. Run this in the command prompt: 
```shell
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
4. Run quickstart.py in the terminal. A browser window should open up - complete the authentication flow. (You will need to give complete Google Drive permission)
5. Run main.py to upload all files in /data folder
6. The script will prompt you whether to delete the local copies of the file or not. 