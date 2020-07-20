"""
Offline Python3 Documentation Tool
Made by perpetualCreations (Taian Chen), Licensed under GPL.

backend.py, contains backend functions meant to be imported
"""

# Init Phase
try:
	print("[INFO]: Importing packages for backend.py.")
	import requests
	from sys import exit as shutdown
	import pickle
	import os.path as path
	import zipfile
	from bs4 import BeautifulSoup
	from time import strftime, gmtime
except ImportError:
	requests = None
	shutdown = None
	pickle = None
	path = None
	zipfile = None
	BeautifulSoup = None
	strftime = None
	gmtime = None
	print("[FAIL]: Imports failed for backend.py. Closing...")
	exit(1)
pass

# Class

def logError(logData):
	"""
	Appends a file to error-log directory.
	:param logData: Exception output to be recorded.
	:return: None
	"""
	print("[INFO]: Logging error...")
	logFile = open("error-" + str((strftime("%b%d%Y%H%M%S"), gmtime())[0]) + ".txt", "w+")
	logFile.write(logData)
	logFile.close()
	print("[INFO]: Error logged.")
pass

def updateCheck():
	"""
	Checks for software and documentation updates.
	:return:
	"""
	try:
		updateDocumentationPage = BeautifulSoup(requests.get("https://docs.python.org/3/download.html").text, "html.parser")
		updateDocumentationTargetTag = updateDocumentationPage.findAll("a")
		updateDocumentationCycle = 0
		while updateDocumentationCycle <= len(updateDocumentationTargetTag):
			print(updateDocumentationCycle)
			print(updateDocumentationTargetTag[updateDocumentationCycle])
			if "archives/python" in updateDocumentationTargetTag[updateDocumentationCycle]:
				if "docs-html.zip" in updateDocumentationTargetTag[updateDocumentationCycle]:
					open("documentation.zip", "wb").write(requests.get("https://docs.python.org/3/" + updateDocumentationTargetTag[updateDocumentationCycle].get("href")).content)
				else:
					updateDocumentationCycle += 1
				pass
			else:
				updateDocumentationCycle += 1
			pass
		pass
		if updateDocumentationCycle > len(updateDocumentationTargetTag):
			logError("updateDocumentationCycle is greater than length of updateDocumentationTargetTag. This means no valid download link was found for documentation updates! \nPlease make an issue on the Github repository.")
		pass

	# TODO thin the sheer number of error case scenarios
	except requests.exceptions.ContentDecodingError as updateDocumentationContentDecodingError:
		logError(updateDocumentationContentDecodingError)
		return None
	except requests.exceptions.BaseHTTPError as updateDocumentationBaseHTTPError:
		logError(updateDocumentationBaseHTTPError)
		return None
	except requests.exceptions.ChunkedEncodingError as updateDocumentationChunkedEncodingError:
		logError(updateDocumentationChunkedEncodingError)
		return None
	except requests.exceptions.ConnectTimeout as updateDocumentationConnectTimeout:
		logError(updateDocumentationConnectTimeout)
		return None
	except requests.exceptions.ProxyError as updateDocumentationProxyError:
		logError(updateDocumentationProxyError)
		return None
	except requests.exceptions.SSLError as updateDocumentationSSLError:
		logError(updateDocumentationSSLError)
		return None
	except requests.exceptions.ConnectionError as updateDocumentationConnectionError:
		logError(updateDocumentationConnectionError)
		return None
	except requests.exceptions.HTTPError as updateDocumentationHTTPError:
		logError(updateDocumentationHTTPError)
		return None
	except requests.exceptions.InvalidSchema as updateDocumentationInvalidSchema:
		logError(updateDocumentationInvalidSchema)
		return None
	except requests.exceptions.InvalidURL as updateDocumentationInvalidURL:
		logError(updateDocumentationInvalidURL)
		return None
	except requests.exceptions.MissingSchema as updateDocumentationMissingSchema:
		logError(updateDocumentationMissingSchema)
		return None
	except requests.exceptions.ReadTimeout as updateDocumentationReadTimeout:
		logError(updateDocumentationReadTimeout)
		return None
	except requests.exceptions.RetryError as updateDocumentationRetryError:
		logError(updateDocumentationRetryError)
		return None
	except requests.exceptions.StreamConsumedError as updateDocumentationStreamConsumedError:
		logError(updateDocumentationStreamConsumedError)
		return None
	except requests.exceptions.Timeout as updateDocumentationTimeout:
		logError(updateDocumentationTimeout)
		return None
	except requests.exceptions.TooManyRedirects as updateDocumentationTooManyRedirects:
		logError(updateDocumentationTooManyRedirects)
		return None
	except requests.exceptions.URLRequired as updateDocumentationURLRequired:
		logError(updateDocumentationURLRequired)
		return None
	except requests.exceptions.RequestException as updateDocumentationRequestException:
		logError(updateDocumentationRequestException)
		return None
	pass
pass

updateCheck()