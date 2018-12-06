while True:
	user_name=input("please enter your name!(enter q to quit) ")
	if user_name.lower()=="q":
		break
	else:
		print("welcome "+user_name)
		with open("user.txt","a") as file_obj:
			file_obj.write(user_name+"\n")