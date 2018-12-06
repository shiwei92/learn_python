#import module_name
#from module_name import function_name or Class_name
'''import Car
my_new_car=Car.Car("audi","a4",2016)
print(my_new_car.get_descriptive_name())'''
from Car import Car
my_new_car=Car("audi","a8",2018)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()