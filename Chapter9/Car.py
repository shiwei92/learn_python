class Car():
	'''一次模拟汽车的简单尝试'''
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_descriptive_name(self):
		long_name=str(self.year)+" "+self.make+" "+self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
	def update_odometer(self,mileage):
		if mileage>self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("you cannot roll back an odmeter")
	def increment_odometer(self,miles):
		self.odometer_reading+=miles

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()
	def describe_battery(self):
		print("This car has a "+str(self.battery.battery_size)+"-kwh battery.")
class Battery():
	def __init__(self,battery_size=70):
		self.battery_size=battery_size
	def get_range(self):
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		message="This car can go approximately "+str(range)+" miles on a full charge."
		print(message)
'''my_new_car=Car("audi","a4",2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#直接修改属性的值
my_new_car.odometer_reading=23
my_new_car.read_odometer()
#通过方法修改属性的值
my_new_car.update_odometer(50)
my_new_car.read_odometer()
my_new_car.update_odometer(40)
#通过方法对属性值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_tesla=ElectricCar("tesla","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.get_range()'''
