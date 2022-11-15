#! /bin/bash

echo "Uninstalling file-uploader..."

read -p "Are you sure you want to uninstall? (Y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
	exit 0
fi

client_config_path=~/.config/file-uploader
client_script_path=/usr/bin/upload-file
context_menu_path=/usr/share/kservices5/ServiceMenus/Upload.desktop

echo "Removing $client_config_path..."
rm -r $client_config_path

echo "Removing $client_script_path..."
sudo rm $client_script_path

echo "Removing $context_menu_path..."
sudo rm $context_menu_path

echo "All done."