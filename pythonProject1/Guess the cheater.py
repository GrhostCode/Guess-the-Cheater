import random

value = random.randint(0, 1)

coin = value
if coin == 1:
    coin = "Cheater"
else:
    coin = "Good"
if coin == "Cheater":
     chance = 75
else:
    chance = 50
again = input("You ready (Y) (N) ")
again = "Y" or "y"
while again == "Y":
 else:

 flip = random.randint(0, 100)
if flip >= chance:
        flip = "Heads"

else:
        flip = "Tails"

print(flip)

again = input("Do you want to do it again, (Y) or (N)? ")

if again.upper == "N":
    answer = input("Do you think it was a cheater or good (C) or (G)")
    if answer.upper == coin:
        print("Correct")
    else:
        print("Incorrect")
else:
    again = "Y"

