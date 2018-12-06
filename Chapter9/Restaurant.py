class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
	def describe_restaurant(self):
		print("The restaurant's name is "+self.restaurant_name)
		print("The restaurant type is "+self.cuisine_type)
	def open_restaurant(self):
		print("The restaurant is working!")
	def get_number_served(self):
		print("The server-number is "+str(self.number_served))
	def increment_number_served(self,number):
		self.number_served+=number
restaurant=Restaurant("floor","Henan")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.get_number_served()
restaurant.increment_number_served(12)
restaurant.get_number_served()