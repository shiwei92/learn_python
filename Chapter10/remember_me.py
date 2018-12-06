import json
'''username=input("what is your name?")
filename="user_name.json"
with open(filename,"w") as f_obj:
	json.dump(username,f_obj)
	print("we will remeber you when you come back "+username)'''
filename="user_name.json"
with open(filename) as f_obj:
	username=json.load(f_obj)
	print("welcome back "+username)