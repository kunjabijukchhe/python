class Calculator:
    def __init__(self,num):
        self.num=num
    def add(self,num1):
        self.num=int(self.num)+int(num1)
        return self.num
    def sub(self,num2):
        self.num = int(self.num) - int(num2)
        return self.num
    def mul(self,num3):
        self.num = int(self.num) * int(num3)
        return self.num
    def div(self,num4):
        self.num = int(self.num) / int(num4)
        return self.num
    def __str__(self):
        return f"{self.num}"
c=Calculator(0)
count="y"
while count.lower()=="y":


    print("+------------------+")
    print("|Enter your choice:|\n|1.ADD             |\n|2.SUBTRACT        |\n|3.MULTIPLY        |\n|4.DIVISION        |")
    print("+------------------+")
    print("\n")
    print("+------------------>")
    choice=input("| Your choice is: --> ")
    print("+------------------>")
    print(c)
    if choice=="1":

        print(c.add(input("Enter to add:")))
    if choice=="2":

        print(c.sub(input("Enter to subtract")))
    if choice=="3":

        print(c.mul(input("Enter to multiply")))
    if choice=="4":

        print(c.div(input("Enter to divided")))


    print("\n+---------------+")
    cont = input("Continue(y/n)?:")
    print("+---------------+")
    if cont == "n":
        break
