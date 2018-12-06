import json
def get_stored_username():
	file_name="username_example.json"
	try:
		with open(file_name) as f_obj:
			username=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	username=input("what is your name?")
	file_name="username_example.json"
	with open(file_name,"w") as f_obj:
		json.dump(username,f_obj)
	return username
def greet_user():
	username=get_stored_username()
	if username:
		print("Welcome back,"+username+"!")
	else:
		username=get_new_username()
		print("We will remember you when you come back,"+username+"!")
greet_user()