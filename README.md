# File Uploader

Small tool to upload files to a file hosting server. \
Currently only *properly* works on KDE Plasma, because setting the clipboard is done through a KDE Plasma service. \
If you want to make it work on different distributions, edit the upload file to set the clipboard correctly.

# How to Use

You can use the `install.sh` script to install automatically, or do it yourself with the steps below.

 * Copy `server/config.def.php` to `server/config.php` and edit it for your needs.
 * Copy `client/config.def.py` to `client/config.py` and edit it for your needs.
 * Now upload `server/upload.php` and `config.php` to your host.

### The following is only if you're using KDE Plasma
 * Edit `client/kde-plasma-context-menu/Upload.desktop` so the `Exec` path is correct.
 * Copy `client/kde-plasma-context-menu/Upload.desktop` to `/usr/share/kservices5/ServiceMenus/`.
 * Now restart all instances of Dolphin and then you should have a "Upload to Host" action on files.
