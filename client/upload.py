from config import *
import os
import requests
import sys

def upload(filename, key):
	files = { 
		"file": open(filename, "rb") 
	}
	data = {
		"key": key
	}
	response = requests.post(upload_url, files=files, data=data)
	if response.status_code == 200:
		return True, response.json()["url"]
	else:
		return False, response.json()["error"]

def notify(message):
	command = f"notify-send -a \"File Uploader\" \"{message}\""
	os.system(command)

def put_clipboard(content):
	command = f"qdbus org.kde.klipper /klipper setClipboardContents \"{content}\""
	os.system(command)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"No file specified.")
		sys.exit(1)

	success, message = upload(sys.argv[1], key)
	notify(f"{'File Uploaded!' if success else 'Unable to upload file:'}\n{message}")
	if success:
		put_clipboard(message)