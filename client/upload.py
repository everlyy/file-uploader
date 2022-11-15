#! /usr/bin/env python3

import configparser
import os
import requests
import sys
import argparse

CONFIGPATH = os.path.expanduser("~/.config/file-uploader")
CONFIGFILE = f"{CONFIGPATH}/config.ini"
DEFAULTHOST = "https://your.website.com/upload.php"
DEFAULTKEY = "UploadKey123"

gui_mode = False

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
	if gui_mode:
		command = f"notify-send -a \"File Uploader\" \"{message}\""
		os.system(command)
	else:
		print(message)

def put_clipboard(content):
	command = f"qdbus org.kde.klipper /klipper setClipboardContents \"{content}\""
	os.system(command)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="The file to upload.")
	parser.add_argument("-g", "--gui-mode", help="Uses GUI notifications to tell you what's happening", action="store_true", dest="gui_mode")
	parser.add_argument("-c", "--clipboard", help="Put resulting link in clipboard", action="store_true", dest="clipboard")
	args = parser.parse_args()

	gui_mode = args.gui_mode

	config = get_config()
	success, message = upload(config.host_url, args.file, config.upload_key)
	notify(f"{'File Uploaded!' if success else 'Unable to upload file:'}\n{message}")
	if success and args.clipboard:
		put_clipboard(message)