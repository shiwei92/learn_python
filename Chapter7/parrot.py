#input()向用户输出提示并获取用户输入，将输入存储在一个变量中
#message=input("Tell me something,and I will repeat it back to you:")
#print(message)
#使用int()获取数值输入
'''age=input("How old art you?")
if(int(age)>18):
	print("old enough")
else:
	print("no admission")'''
'''current_number=1
while current_number<5:
	print(current_number)
	current_number+=1
prompt="Do you know my name?"
message=""
while message!="quit":
	message=input(prompt)
	if message!="quit":
		print(message)'''
#使用while循环处理列表和字典
unconfirmed_users=["jack","stark","rogers"]
confirmed_users=[]
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print("Verify user: "+current_user.title())
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print (confirmed_user.title())
while 'rogers' in confirmed_users:
	confirmed_users.remove('rogers')
print(confirmed_users)

responses={}
polling_active=True
while polling_active:
	name=input("\nWhat is your name?")
	response=input("\nWhich mountain would you like to climb someday?")
	responses[name]=response
	repeat=input("Would you like to let another person respond?(yes/no)?")
	if repeat=="no":
		polling_active=False
print("--Poll Results--")
for name,mountain in responses.items():
	print(name+" want to climb "+mountain)
	


