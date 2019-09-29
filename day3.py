'''from ATM import ATM
a=ATM("kunja",1000)
cont = "y"
while cont.lower() == "y":
    print("Enter your choice:\n1.Withdraw\n2.Deposite\n3.Show Balance")
    choice=input("Your choice is:")
    if choice=='1':
        b=input("Enter withdrawal ammount:")
        print(a.Withdrawal(b))
    elif choice=='2':
        c=input("Enter deposits amount:")
        print(a.Deposits(c))

    elif choice=='3':
        print(a)
    else:
        print("invaild")

    cont = input("Continue?y/n:")
    if cont == "n":
        break'''


'''#from colorama import init
#init()
from colorama import  Fore
print(Fore.RED+"some black text")
print(Fore.GREEN+"some black text")'''
class Practice:
    def __init__(self,name):
        self.name=name


a=Practice("kunja")
print(a.name)