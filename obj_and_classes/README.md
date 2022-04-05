Folder is chapter on objects and classes

Function is a section of a program that performs a specific task and returns a value... usually

To define a  function, use def, eg. 
	
	#function test has arument a and b and returns a + b
	def test(a, b):
		#blah
		return a + b


Method is when a function is a part of an object or Python class

	To call a method, input obj_name.method(arg), eg.

		car.readspeed()
		car.incspeed(40)

Object is a collection of data and methods that operate on that data. Objects are also defined by a class

	To create an object, input obj_name = obj_class(), eg.
		
		car1 = Car()
		car2 = Car()

A class is a blueprint for one or more objects

	To create a class, input class class_name:, and proceed to define variables and methods in the class, eg.
		
		class Car:
			speed = 0




