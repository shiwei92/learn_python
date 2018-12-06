#从一个模块导入多个类
from Car import Car,ElectricCar
my_tesla=ElectricCar("tesla","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_car=Car("audi","a15",2020)
print(my_car.get_descriptive_name())