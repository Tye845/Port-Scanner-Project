#!/bin/python3

# The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter
import sys

# A socket module is a module that implements sockets so that you can use them in your program for Internet communication. This is what allows us to make a node-to-node connenction
import socket

# The datetime module will allow us to create a banner and show the date and time of when we ran the Python scanner
from datetime import datetime

# End goal accepts 2 arguments: python3 scanner.py <ip>
# Define our target

if len(sys.argv) == 2:
	# We are going to create a variable called "target" and set it equal to the 1st argument
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4 address
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")


# After you finish the above statememts save it and run it


# Add a pretty banner
print("-" * 50)
print("Scanning target "+ target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)


# We will now implement a try catch statement, so the program will do something and if it can't we will have exceptions

try:
	# Full on port scanner consists of ports (1, 65535)
	for port in range(100,150):
	
		# AF_INET is our IPv4 address
		# SOCK_STREAM is our port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# This is going to attempt to connect to a port and if that port is not connectable then it will wait 1 second and then it will move onto the next port
		socket.setdefaulttimeout(1)
		
		# We will also store a result
		result = s.connect_ex((target,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
		
		# Enable the below statement after it is built out
		print("Checking port {}".format(port))
		
	
		if result == 0:
			print("Port {} is open".format(port))
		s.close()



# We will also need to throw in a few expections to make the code work and it is also helpful when you stop and think logically about the program
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
	
	
