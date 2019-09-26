'''for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=",")'''


'''a=int(input())
fact =1
i=1
while i<=a:
    fact*=i
    i+=1
print(fact)'''''''''
'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"

)

mycursor=mydb.cursor()
mycursor.execute("use StudentGrading")
#mycursor.execute("create table students(st_no integer(10),st_name varchar(50),primary key(st_no))")

mycursor.execute("INSERT INTO student (st_no,st_name) VALUES ("5", "Highway 21")")

mydb.commit()

print(mycursor.rowcount, "record inserted.")'''
'''l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))'''
'''a=int(input())
b={i:i*i for i in range(1,a+1)}
print(b)'''
'''a=int(input())
for i in range(1,a+1):
  c=i*i
  print(f"{i}:{c}",end=", ")'''

count = "Y"
while count == "Y":

  a = int(input("Multiplie Table\nPlease enter the number that you want:"))
  print(f"You have select number:{a}")
  print("You have select number:", a)
  count = input("Are you sure:Y or N")
  if count == "N":
    break
  else:

    if count=="Y":
      break
    else:
      count = input("do you want to fix the number:Y or N").upper()
      a = int(input("Enter the number:"))
  for i in range(1, 11):
    print("{}*{}={}".format(a, i, a * i))
    # print(f"{a}*{i}={a*i}")
  count = input("Do you want to continue:Y or N").upper()
  if count == "":
    break

