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

	To create an object, input obj_name = obj_class(), , this is also called a constructor eg.
		
		car1 = Car()
		car2 = Car()

A class is a blueprint for one or more objects.  

	To create a class, input class class_name:, and proceed to define variables and methods in the class, eg.
		
		class Car:
			speed = 0
			#other variables initialized

			def method1:
				#method1 actions


To make a class pass arguments through it, use the __init__() function:

		class Car:
			speed = 0
			#other variables initialized

			def __init__(self, var1, var2):
    			self.var1 = var1
    			self.var2 = var2

    		#to use init variables in methods, use self.var, eg.	
			def method1:
				print(self.var1 + "blah")
				#method1 actions

To include other files, use import "
filename" at the top, depends on file path




