class User():
	def __init__(self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
	def describe_user(self):
		print("First_name is "+self.first_name.title()+" Last_name is "+self.last_name.title())
	def greet_user(self):
		print("Hello,"+self.first_name+" "+self.last_name)
user=User("jack","sparrow")
user.describe_user()
user.greet_user()