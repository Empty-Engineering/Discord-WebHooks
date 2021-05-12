#Lukas Robin 12/5/2021
import sys
import os
import platform
import subprocess
import pkg_resources
def osDetect():
	required = {'requests'}
	installed = {pkg.key for pkg in pkg_resources.working_set}
	missing = required - installed
	if missing:
		os.system("python3 -m pip install requests")
	
webHook = 'https://discordapp.com/api/webhooks/842058306364768327/-CDTIr60FGQOVdD-i1KBan6RTWA8nnITk79Jl72kPNhZi7Uv-jFXAxqA795FVhOrDa-5'
def accept():
	eula = input("Would you like to send a message? ")
	if eula.lower() == "yes" or eula.lower() == "y":
		return True
	else:
		return False
	
def post(accept):
	if accept == True:
		import requests
		messageContent = input("Enter message here: ")
		jsonObj = {"type": 1, "id": "842058306364768327", "name": "Anouncements", "avatar": "null", "channel_id": "842057469052190785", "guild_id": "842057469052190781", "application_id": "null", "token": "-CDTIr60FGQOVdD-i1KBan6RTWA8nnITk79Jl72kPNhZi7UvjFXAxqA795FVhOrDa-5", "content" : messageContent}
		message = requests.post(webHook, data = jsonObj)
		print(message.text)
	
	else:
		exit()
		
def restart():
	os.execv(sys.executable, ['python'] + sys.argv)

osDetect()
post(accept())
restart()
