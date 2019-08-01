
'''char_name="kunja"
age="19"
print("my name is "+char_name+",")
print( age +" years old")
print("i like my name "+char_name+"")
print("and i am really "+age+" years old")'''

'''a="kunja"
b=18
print("I'm name is",a+". And your age is ",b)
print("I'm name is %r" %"kunja")
print("I'm name is %s" %"kunja")
print("this number is called %.2f" %3.7)
print("this number is called %s" %3.7)
print("this number is called %d" %3.7)
a=22/7
print("the value of %.51f" %a)
kunja=[18,18.22,"kunja"]
b=kunja*2
print(b)'''
kunja1=[1,2,3]
kunja2=[4,5,6]
kunja3=[7,8,9]
kunja4=[kunja1,kunja2,kunja3]
print(kunja4)
a=kunja4[0][1]
b=kunja1[1]
print(a)
print(b)
c=[row[0] for row in kunja4]
d=[row[1] for row in kunja4]
e=[row[2] for row in kunja4]
print(c)
print(d)
print(e)