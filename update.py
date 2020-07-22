"""
Offline Python3 Documentation Tool
Made by perpetualCreations (Taian Chen), Licensed under GPL.

update.py, update script based off of elements in backend.py
"""

try:
	print("[INFO]: Importing packages for update.py...")
	import backend
	from tkinter import messagebox
	import webbrowser
except ImportError as ie:
	backend = None
	messagebox = None
	webbrowser = None
	print("[FAIL]: Imports failed for backend.py. See below for details.")
	print(ie)
pass

updateCheckResults = backend.updateCheck()
updateLastUpdateCheckData = backend.updateLastUpdateCheckDataRead()

if messagebox.askyesno("OP3DT: Documentation Update", "The latest version of Python documentation is for " + updateCheckResults[2] + ".\n" + "The last known version checked was " + updateLastUpdateCheckData + ".\n" + "Would you like to re-download documentation?") is True:
	backend.updateDownload()
	backend.updateUnpack()
	if updateCheckResults[0] is True:
		if messagebox.askyesno("OP3DT: New Release Available", "New release for OP3DT is available on Github. \n Would you like to be sent to the releases page?") is True:
			webbrowser.open(updateCheckResults[1])
		else:
			messagebox.showinfo("OP3DT: Update Finished", "Application will now finish and close.")
		pass
	else:
		messagebox.showinfo("OP3DT: Update Finished", "Application will now finish and close.")
	pass
else:
	if updateCheckResults[0] is True:
		if messagebox.askyesno("OP3DT: New Release Available", "New release for OP3DT is available on Github. \n Would you like to be sent to the releases page?") is True:
			webbrowser.open(updateCheckResults[1])
		else:
			messagebox.showinfo("OP3DT: Update Finished", "Application will now finish and close.")
		pass
	else:
		messagebox.showinfo("OP3DT: Update Finished", "Application will now finish and close.")
	pass
pass

backend.updateLastUpdateCheckDataWrite(updateCheckResults[2])
backend.shutdown(0)
