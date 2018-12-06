file_name="invoice.txt"
'''try:
	with open(file_name) as f_obj:
		contents=f_obj.read()
except Exception as err:
	print(err)
else:
	print(contents.strip())'''
try:
	print(1/0)
except Exception as err:
	print("error: "+str(err))
else:
	print("ok")
	