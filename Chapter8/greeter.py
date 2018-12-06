#定义函数
def greet_user():
	print("Hello")
greet_user()
#向函数传递参数
def greet_user(username):
	print("Hello,"+username.title())
greet_user("stark")
def describe_pet(animal_type,pet_name):
	print("\nI have a "+animal_type)
	print("My " +animal_type+"'s name is "+pet_name)
describe_pet("dog","harry")
#关键字实参
describe_pet(pet_name="jan",animal_type="cat")
#默认值
def describe_pet_2(animal_type,pet_name="happy"):
	print("\nI have a "+animal_type)
	print("My " +animal_type+"'s name is "+pet_name)
describe_pet_2("fish")
def get_name(first_name,last_name):
	full_name=first_name+" "+last_name
	return full_name.title()
name=get_name("jim","green")
print(name)
def get_formatted_name(first_name,last_name):
	full_name=first_name+" "+last_name
	return full_name.title()
'''while True:
	print("\nTell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name=input("First name:")
	if f_name=="q":
		break
	l_name=input("Last name:")
	if l_name=="q":
		break
	full_name=get_formatted_name(f_name,l_name)
	print("\nHello "+full_name+"!")'''
def make_album(singer,album_name,sing_count=0):
	album={}
	album[singer]=album_name
	if sing_count:
		album["sing_count"]=sing_count
	return album

'''while True:
	print("\nenter some singer and songs:")
	print("(press 'q' to quit)")
	singer=input("singer:")
	if singer=='q':
		break
	song=input("song:")
	if song=="q":
		break
	album=make_album(singer,song)
	for key,value in album.items():
		print(key+" "+value)'''
def greet_users(names):
	for name in names:
		print("\nHello "+name.title()+"!")
greet_users(["stark","bucky","rogers"])
#传递任意数量的实参
def making_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
making_pizza("pepper")
making_pizza("mushroom","green peppers","extra cheese")
#位置实参和任意数量的实参
def making_pizza_2(size,*toppings):
	print("\nMaking a "+str(size)+"-inch pizza with the following topping:")
	for topping in toppings:
		print("_"+topping)
making_pizza_2(16,"pepper")
making_pizza_2(12,"mushroom","green peppers","extra cheese")
#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
	profile={}
	profile["first_name"]=first
	profile["last_name"]=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
user_info=build_profile("albert","einstein",location="princetion",field="physics")
print(user_info)
