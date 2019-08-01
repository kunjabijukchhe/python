# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def deposite(x,y):
    return int(x)+int(y)
def withdraw(x,y):
    return int(x)-int(y)

cont = "y"
while cont== "y":
    print("Enter your choice:\n1.Withdraw\n2.Deposite\n3.Show Balance")
    choice=input("your choice is:")
    amount=50000
    name="kunja bijukchhe"
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

    cont = input("Continue?y/n:")
    if cont == " ":
        break
    
