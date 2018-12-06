file_name="pi_digits.txt"
with open(file_name) as file_object:
	lines=file_object.readlines()
#readlines 是读取文件中的内容，一行一行组成一个列表
for line in lines:
	print(line.rstrip())
with open(file_name) as file_object:
	lines=file_object.read()
#read 是读取文件中全部的内容，是一个str
print(lines)
with open(file_name) as file_object:
	lines_list=file_object.readlines()
lines=""
for line_list in lines_list:
	lines+=line_list.strip()
print(lines)
