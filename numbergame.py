import random

gamenumber = random.randint(1, 10)

while True:
    x=int(input("guess a number between 1 and 10: "))

    if x == gamenumber:
        print("you got it!")

    if x < gamenumber:
        print("Too low!")

    if x > gamenumber:
        print("Too high!")