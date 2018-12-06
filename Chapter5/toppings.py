request_toppings=["ushrooms","green peppers","extra cheess"]
for request_topping in request_toppings:
	print("Adding "+request_topping)
print("\nFinishd making your pizza!")
for request_topping in request_toppings:
	if request_topping=="green peppers":
		print("sorry,we are out of green peppers right now")
	else:
		print("Adding "+request_topping)
print("\nFinishd making your pizza!")
print(len(request_toppings))
cars=[]
#将列表放入条件表达式中，Python将在列表至少包含一个元素时返回true，列表为空返回false
if cars:
	print("pick one car")
else:
	print("Do you want a car?")