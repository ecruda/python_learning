#example on how to create a python class

class Car:
	speed = 0
	started = False

	#start the car
	def start(self):
		self.started = True
		print("Car started")

	#increase speed, cannot be increased unless car is started
	def inc_speed(self, delta):
		if self.started
			self.speed = self.speed + delta
			print("Speed is now" + self.speed)

		else:
			print("Must start car first")

	#decrease speed, cannot be dec until car started
	def dec_speed(self, delta):
		if self.started
			self.speed = self.speed - delta
			print("Speed is now" + self.speed)

		else:
			print("Must start car first")

	#stops car
	def stop(self):
		self.speed = 0
		print("Stopped")
