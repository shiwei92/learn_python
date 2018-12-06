file_name="programming.txt"
'''
如果文件不存在，open会自动创建(如果是r或r+，程序会报错找不到文件)
四种模式 r 读，w 写 ，a 追加  r+ 读取和写入
w 和 r+ 会清空文件中数据
'''
with open(file_name,"r+") as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

	
