workers={"stark":563235.12,"widow":2357123.23,"rogers":15.723,"hulk":1785.3,"fury":17856}
totalSalary=0
for salary in workers.values():
	totalSalary+=salary
print(totalSalary)
for worker,salary in workers.items():
	print("worker: "+worker+" salary: "+str(salary)+" rate: "+str(2000*(salary/totalSalary)))