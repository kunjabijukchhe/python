def max_num(a,b,c):
 if a>=b and a>=c:
      return a
 elif b>=a and b>=c:
      return b
 else:
     return c

a=input()
b=input()
c=input()
print("the greatest number " + max_num(a,b,c))