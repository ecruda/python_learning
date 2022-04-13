#vehicle.py
class Vehicle():

	def __init__(self, name, started = False, speed = 0):
		self.started = started
		self.speed = speed
		self.name = name

	def start(self, name):
		self.started = True
		print(name + " started")

	def stop(self):
		self.speed = 0

	def inc_speed(self, delta):
		if self.started:
			self.speed = self.speed + delta
		else:
			print("Start " + name + " first")

	def dec_speed(self, delta): 
		if self.started:
			self.speed = self.speed - delta
		else:
			print("Start " + name + " first")

	def turn_off(self):
		self.started = False