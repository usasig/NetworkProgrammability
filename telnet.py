import getpass
import sys
import telnetlib

HOST = "192.168.0.10"
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("rname: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("en\n")
if password:
	tn.read_until("assword: ")
	tn.write(password + "\n")
	
tn.write("show ver\n")

print tn.read_all()


### Modified ###
