#py_obj.py
import py_class

#making car1 object that has its own properties
car1 = py_class.Car("Car1")
car2 = py_class.Car("Car2")

car1.start()
car1.inc_speed(30)
car2.start()
car1.dec_speed(50)
car1.stop()


