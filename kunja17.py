'''secret="kunja"
guess=""

while guess!=secret:
    guess=input("enter a guess: ")
print("you win")'''
secret="kunja"
guess=""
guess_count=0
guess_limit=3
out_of_guesses =False

while guess!=secret and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("enter a guess: ")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("out of guesses,You lose")
else:
    print("you win")