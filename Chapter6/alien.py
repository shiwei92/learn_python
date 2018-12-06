#定义字典
alien_0={"color":"green","points":5}
#访问字典
print(alien_0["color"])
print(alien_0["points"])
newpoints=alien_0["points"]
print("you just earned "+str(newpoints)+" points")
#添加一对键值对
alien_0["x_position"]=0
alien_0["y_position"]=25
print(alien_0)
#修改字典
alien_0["color"]="red"
print(alien_0)
alien_0={"x_position":0,"y_position":25,"speed":"medium"}
print("Original x_position: "+str(alien_0["x_position"]))
#向右移动外星人
#根据外星人的当前速度决定将其移动多远
if alien_0["speed"]=="slow":
	x_increment=1
elif alien_0["speed"]=="medium":
	x_increment=2
else:
	x_increment=3
alien_0["x_position"]=alien_0["x_position"]+x_increment
print("New x_position: "+str(alien_0["x_position"]))
#删除键值对
alien_0={"color":"red","speed":"slow"}
del alien_0["color"]
print(alien_0)
#遍历所有的键值对,for循环将每个键值对存储到指定额两个变量中
user_0={"username":"efermi","first":"enrico","last":"fermi"}
for key,value in user_0.items():
	print("\nKey: "+key)
	print("\nValue: "+value)
favorite_languages={"jen":"python","sarah":"c","edward":"ruby","phil":"python"}
for name,language in favorite_languages.items():
	print(name+"'s favourite language is "+language)
#遍历字典中所有键
for name in favorite_languages.keys():
	print(name.title())
if "jen" in favorite_languages.keys():
	print("jen in")
if "stark" not in favorite_languages.keys():
	print("stark not in")
#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(name.title()+",thank you for taking the poll.")
#遍历字典中的所有值
for language in favorite_languages.values():
	print (language.title())
if "CSharp" in favorite_languages.values():
	print("find CSharp")
else:
	print("not found")
for language in sorted(favorite_languages.values()):
	print (language.title())
#嵌套列表，字典里嵌套列表，列表里面嵌套字典
alien_0={"color":"green","points":"5"}
aline_1={"color":"yellow","points":"10"}
aline_2={"color":"red","points":"15"}
#列表中嵌套字典
alines=[alien_0,aline_1,aline_2]
print(alines)
alines=[]
for alien_number in range(30):
	alines.append({"color":"green","points":"5","speed":alien_number})
print(alines)
for alien in alines[:5]:
	print(alien)
#字典中嵌套列表
pizza={"crust":"thick","toppings":["mushrooms","extra cheese"]}
print("You ordered a "+pizza["crust"]+"-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
	print("\t"+topping)
favorite_languages={
"jen":["python","ruby"],
"sarah":["c"],
"edward":["ruby","go"],
"phil":["python","haskell"],
}
for name,languages in favorite_languages.items():
	print(name.title()+"'s favorite language is ")
	for language in languages:
		print("\t"+language)
#字典中嵌套字典
users={
"aeinstein":{"first":"albert","last":"einstein","location":"princeton"},
"mcurie":{"first":"marie","last":"curie","location":"pkaris"}
}
for user_name,user_info in users.items():
	print("\nUsername:"+user_name)
	full_name=user_info["first"]+" "+user_info["last"]
	location=user_info["location"]
	print("\tFullName: "+full_name)
	print("\tLocation: "+location)
del users["mcurie"]
print(users)