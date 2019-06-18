def translate(pharse):
    transaltion = ""
    for letter in pharse:
        if letter.lower() in "AEIOUaeiou":
            if letter.upper():
                transaltion=transaltion+"G"
            else:
                transaltion = transaltion+"g"
        else:
            transaltion= transaltion+letter
    return transaltion
print(translate(input("enter a pharse:")))
