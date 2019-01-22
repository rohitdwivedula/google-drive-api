# Setup

1. Go to the [Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python) page, enable the Drive API and download the credentials file. Save the credentials file in the working directory.
2. Run this in the command prompt: 
```shell
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
3. Run quickstart.py in the terminal. A browser window should open up - complete the authentication flow. (You will need to give complete Google Drive permission)
4. Run main.py to upload all files in /data folder
5. The script will prompt you whether to delete the 