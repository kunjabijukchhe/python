
from IPython.display import clear_output
def borad(b):
    print(b[7]+"|"+b[8]+"|"+b[9])
    print("-|-|-")
    print(b[4]+"|"+b[5]+"|"+b[6])
    print("-|-|-")
    print(b[1]+"|"+b[2]+"|"+b[3])

c=["#","X","O","X","O","X","O","X","O","X"]
borad(c)
def player():
    mark=""
    while mark!="X" and mark!="O":
        mark=input("Player1, choose X or O: ")

    if mark=="X":
        return ("X","O")
    else:
        return ("O","X")

player1,player2=player()

