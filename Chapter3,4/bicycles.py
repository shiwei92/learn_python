bicycles = ['trek', 'cannondate', 'redline', 'specialized']
print(bicycles)
# 访问列表
print(bicycles[0])
# 添加列表元素
bicycles.append("first")
print(bicycles)
bicycles.insert(0, "zero")
print(bicycles)
# 修改列表元素
bicycles[1] = "second"
print(bicycles)
# 删除列表元素
del bicycles[-1]
print(bicycles)
# 使用pop()获取被删除的末尾元素
poped_bicycles = bicycles.pop()
print(poped_bicycles)
print(bicycles)
# 使用索引可以弹出任何位置处的元素
first_owned = bicycles.pop(0)
print(first_owned)
# 使用remove删除元素
print(bicycles)
bicycles.remove("redline")
print(bicycles)
name = "123"
#使用sort永久性排序
cars=['bmw','audi','toyoto','subaru']
#cars.sort()
print(cars)
#sorted进行临时排序
print(sorted(cars))
print(cars)
#reverse对列表元素反转
cars.reverse()
print(cars)
print("*****************操作列表***********************")
#for循环列表
print("*******for循环列表*******")
magicians=["alice","devid","caroline"]
for magician in magicians:
    print(magician)
for magician in magicians:
	print(magician.title()+", that was a great trick")
	print("I cannot wait to see your next trick,"+magician.title()+".\n")
print("Thank you,everyone.That was a great magic show")
print(magician)
print("*******range生成列表*******")
for value in range(1,5):
	print (value)
	#1,2,3,4
numbers=list(range(1,6))
print(numbers)
#从2开始数，每次加2，直到达到或超过11
even_numbers=list(range(2,11,2))
print(even_numbers)
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)
#列表解析
squares_list=[value**2 for value in range(1,11)]
print(squares_list)
values=[v for v in range(1,21)]
print (values)
#数到数字20
for value in range(1,20):
	print (value)
#计算1到1000000的总和
values=list(range(1,1000001))
print(min(values))
print(max(values))
print(sum(values))
for value in range(1,21,2):
	print (value)
values=[value for value in range(3,30,3)]
print (values)
values=[value**3 for value in range(1,11)]
print (values)
print("************列表切片***************")
player=["jack","stark","bucky","rogers","lion"]
#切片里的都是索引，从索引为1到索引为3，不包括索引为3
print(player[1:3])
print(player[1:4])
#输出从第二个索引一直到最后，都是从左到右
print(player[2:])
print(player[-3:])
print(player[-3:-2])
#遍历切片
for p in player[:3]:
	print(p.title())
#利用切片复制列表
player_copy=player[:]
print("player_copy:")
print(player_copy)
#字符串也能用切片
str_title="the first three items in the list are"
print(str_title[1:3])
print("*******元组*********")
dimensions=(200,50)
print (dimensions[0])
for dimension in dimensions:
	print (dimension)
