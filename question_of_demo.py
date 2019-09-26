from random import randint
number={1:"a",2:"b",3:"c",4:"d"}

a=open("answer_of demo.txt","w")
for i in range(1,26):
    a.write(f"The question number {i} answer is {number[randint(1,4)]}\n")

