#! /usr/bin/env python3

import configparser
import os
import requests
import sys

CONFIGPATH = os.path.expanduser("~/.config/file-uploader")
CONFIGFILE = f"{CONFIGPATH}/config.ini"
DEFAULTHOST = "https://your.website.com/upload.php"
DEFAULTKEY = "UploadKey123"

class Config:
	def __init__(self, host_url, upload_key):
		self.host_url = host_url
		self.upload_key = upload_key

def create_default_config():
	if os.path.exists(CONFIGFILE):
		return

	if not os.path.exists(CONFIGPATH):
		os.makedirs(CONFIGPATH)

	config = configparser.ConfigParser()
	config["settings"] = {
		"HostUrl": DEFAULTHOST,
		"UploadKey": DEFAULTKEY
	}

	with open(CONFIGFILE, "w") as file:
		config.write(file)

def get_config():
	create_default_config()

	config = configparser.ConfigParser()
	config.read(CONFIGFILE)
	
	if "settings" not in config:
		return None

	if config["settings"]["UploadKey"] == DEFAULTKEY:
		message = f"You are currently using the defauly upload key. Please set one in '{CONFIGFILE}'"
		print(message)
		notify(message)

	return Config(config["settings"]["HostUrl"], config["settings"]["UploadKey"])

def upload(host_url, filename, upload_key):
	files = { 
		"file": open(filename, "rb") 
	}
	data = {
		"key": upload_key
	}
	response = requests.post(host_url, files=files, data=data)
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

	config = get_config()
	success, message = upload(config.host_url, sys.argv[1], config.upload_key)
	notify(f"{'File Uploaded!' if success else 'Unable to upload file:'}\n{message}")
	if success:
		put_clipboard(message)