#! /bin/bash

echo "Installing file-uploader..."

read -p "Enter upload host url (https://your.website.com/upload.php): " host_url

upload_key=$(echo $RANDOM | md5sum | head -c 32)

read -p "Do you want to set a custom upload key? (Y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
	read -p "Enter upload key: " upload_key
fi

echo "Host URL   : $host_url"
echo "Upload Key : $upload_key"

read -p "Is the above correct? (Y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
	echo "Quitting."
	exit 0
fi

server_default_config_file=server/config.def.php
server_config_file=server/config.php

client_config_path=~/.config/file-uploader
client_config_file=$client_config_path/config.ini

client_upload_script=client/upload.py
client_script_destination=/usr/bin/upload-file

context_menu_source=client/kde-plasma-context-menu/Upload.desktop
context_menu_destination=/usr/share/kservices5/ServiceMenus

echo "Generating $server_config_file"

cp $server_default_config_file $server_config_file
sed -i -e "s/UploadKey123/$upload_key/g" $server_config_file

echo "Generating $client_config_file"

mkdir -p $client_config_path

echo "[settings]" >> $client_config_file
echo "hosturl = $host_url" >> $client_config_file
echo "uploadkey = $upload_key" >> $client_config_file

echo "Copying $client_upload_script to $client_script_destination"

sudo cp $client_upload_script $client_script_destination

read -p "Do you want to install the context menu entry for Dolphin? (Y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
	sudo cp $context_menu_source $context_menu_destination/Upload.desktop
fi

echo "All done."