import random
number=random.randint(1,9)
chance=0
while chance<=5:
    guess=int(input("enter a number"))
    if guess > number:
        print("guess is greater than number")
    elif guess < number:
        print("guess is less than number")
    else:
        print("you won")
        break
    chance=chance+1
if chance > 5:
    print("you loose")


