'''def length_of_stringe(name):
    print(len(name)*len(name)*len(name))

length_of_stringe("kunja")'''
'''a={"a":"b","c":"d"}
print(a["a"])'''

'''a={"a":"  *  ","b":" *** ","c":"*****"}
print(a["a"])
print(a["b"])
print(a["c"])'''
def patten(letter):
    ptte={1:"  *  ",2:" *** ",3:"*****"}
    a={"a":[1,2,3],"b":[3,2,1]}
    for i in a[letter]:
        print(ptte[i])


patten("b")

