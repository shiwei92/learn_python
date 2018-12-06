with open('pi_digits.txt') as file_object:
	contents=file_object.read()
	print(contents.rstrip())
#写路径的时候注意使用反斜杠
file_path="D:\\python_work\\text_files\\example.txt"
with open(file_path) as file_object2:
	contents2=file_object2.read()
	print(contents2.rstrip())
print("逐行读取")
with open(file_path) as file_object3:
	for line in file_object3:
		print("- "+line.rstrip())
