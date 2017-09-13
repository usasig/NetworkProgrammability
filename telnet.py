import getpass
import sys
import telnetlib

HOST = raw_input("Enter Hostname/IP: " )
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write("en\n")
tn.write(b"cisco\n")
if password:
	tn.read_until("assword: ")
	tn.write(password + "\n")
	
tn.write(b"show ver\n")

print tn.read_all().decode('ascii')


### Modified ###
