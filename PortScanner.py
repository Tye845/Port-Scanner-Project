#!/bin/python3

import sys
import socket
from datetime import datetime

# End goal accepts 2 arguments: python3 scanner.py <ip>
# Define target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translates hostname to IPv4 address
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")

# Add banner
print("-" * 50)
print("Scanning target "+ target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
	for port in range(100,150):
	
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port)) #if port is open it throws a 0, otherwise 1

		print("Checking port {}".format(port))
		
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
	
	
