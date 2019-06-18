try:
    #value=10/0
    num=int(input("enter a number:"))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid")
