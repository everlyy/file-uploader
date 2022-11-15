# File Uploader

Small tool to upload files to a file hosting server. \
Currently only *properly* works on KDE Plasma, because things such as setting the clipboard and notifying are done through commands. \
The uploading works fine on other platforms, but you'll have to edit the code to set the clipboard and notify you.

# How to Use

 * Copy `server/config.def.php` to `server/config.php` and edit it for your needs.
 * Copy `client.config.def.py` to `client.config.py` and edit it for your needs.
 * Now upload `server/upload.php` and `config.php` to your host.

### The following is only if you're using KDE Plasma
 * Edit `client/kde-plasma-context-menu/Upload.desktop` so the `Exec` path is correct.
 * Copy `client/kde-plasma-context-menu/Upload.desktop` to `/usr/share/kservices5/ServiceMenus/`.
 * Now restart all instances of Dolphin and then you should have a "Upload to Host" action on files.