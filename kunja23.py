

employee=open("employee.txt","r")
for a in employee.readlines():
    print(a)
#print(employee.readlines()[1])
employee.close()


