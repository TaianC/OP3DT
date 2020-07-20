// Offline Python3 Documentation Tool (OP3DT)
// Made by perpetualCreations (Taian Chen)
// Licensed under GPL

// https://dreamerslegacy.xyz/

OP3DT is a tool that automatically downloads the latest Python3 documentation, via Requests.
Currently it supports Windows and Linux, however hasn't been tested with all Linux distributions.
This requires Python3, and a web browser to view HTML files. If possible, occasionally a connection to the Internet for updates (this is not necessary at all however).
To start, install Python dependencies listed in requirements.txt, and run install.bat on Windows and install.sh on Linux.
Please note after installation you can safely delete this tool and on Windows its shortcut. It does not install itself into the operating system.

An update script checking for updates will run a few seconds after startup. If an update is available, a dialogue will appear. Otherwise, it will simply exit afterwards.
If an error occurs, an incident message will be written to the error-log folder.
You can force an update with force-update.bat and force-update.sh.

To access documentation, in Windows a shortcut should have been made in your Desktop folder, after installing.
In Linux, run view-docs.sh. You may want to create an alias.

See https://github.com/TaianC/OP3DT/ for additional information, or https://dreamerslegacy.xyz/.
