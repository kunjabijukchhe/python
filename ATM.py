from colorama import  Fore
class ATM:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def Deposits(self,num1):
        self.balance=int(self.balance)+int(num1)
        return f"${num1} has been deposited in your account.\nYour new balance is ${self.balance}."

    def Withdrawal(self,num2):
        if self.balance>=int(num2):
            self.balance=int(self.balance)-int(num2)
            return f"${num2} has been withdraw from your account.\nYour new balance is ${self.balance}."
        else:
            return "FUNDS UNAVAIABLE"
    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"


a=ATM("kunja",1000)
cont = "y"
while cont.lower() == "y":
    print(Fore.LIGHTRED_EX+"+------------------+")
    print("|Enter your choice:|\n|1.Withdraw        |\n|2.Deposite        |\n|3.Show Balance    |")
    print("+------------------+")
    print("\n")
    print("+------------------+")
    choice=input("| Your choice is: --> ")
    print("+------------------+")
    if choice=='1':
        b=input("\nEnter withdrawal ammount:")
        print(a.Withdrawal(b))
    elif choice=='2':
        c=input("\nEnter deposits amount:")
        print(a.Deposits(c))

    elif choice=='3':
        print("\n")
        print(a)
    else:
        print("invaild")
    print("\n+---------------+")
    cont = input("Continue(y/n)?:")
    print("+---------------+")
    if cont == "n":
        break
