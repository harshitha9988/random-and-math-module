import random

while True:
    x=input("Choose one:  Rock  paper  scissors  :  ")
    y=["rock", "paper", "scissors"]

    z=random.choice(y)
    print(f"\nYou chose {x}, the computer chose {z}.\n")


    if x==z:
        print("TIE! You and the computer chose the same thing!")

    elif z== "scissors":
        
        if x=="rock":
          print("Rock smashes scissors! You win!")

        else:
            print("scissors cut paper! You lost!")

    elif x="paper"