operator={
    "add":"+",
    "sub":"-",
    "mul":"*",
    "div":"/"
}
print(operator["add"])
a=input()
b=input()
print(operator.get("+",int(a)+int(b)))