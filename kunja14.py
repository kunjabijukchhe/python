'''a= float(input("enter a first number:"))

b= float(input("enter a second number:"))

op=input("enter a operator:")



if op=="+":
    print(a+b)
elif op =="-":
     print(a - b)
elif op =="*":
      print(a * b)
elif op =="/":
      print(a / b)
else:
    print("invalid")'''
def deposite(x,y):
    return int(x)+int(y)
def withdraw(x,y):
    return int(x)-int(y)
def kunja():
    return kunja()
    kunja()
amount=50000
name="kunja bijukchhe"
print("Enter your choice:\n1.Withdraw\n2.Deposite\n3.Show Balance")
choice=input("your choice is:")
if choice=='1':
    a=input("Enter a withdraw amount:")
    if int(a) <= int(amount):
            print(withdraw(amount,a))
    else:
            print("invalid")
elif choice=='2':
    b=input("Enter your deposit amount:")
    print(deposite(amount,b))

elif choice=='3':
    print("Your name is "+name+".")
    print("your current balance is Rs."+str(amount))
else:
    print("invaild")

c=input("Do you want to continues y/n")
if c=="y":
    print(kunja())
else:
    print("good bye")






