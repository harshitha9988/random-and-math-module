import random
x=True
y=str(random.randint(10,20))

print("I will pick a number from 0 to 15, can you guess it?")
print("The game ends when you get 1 hero!")

while x:
    z=input("Your guess:  \n")
    if y==z:
        print("Great job! You guessed it right!")
        print("the number was",y)
        break

    else:
        print("Sorry,",z, "was the wrong number")
        print("The correct answer was", y)
        print("Try again by rerunning the program!\n")