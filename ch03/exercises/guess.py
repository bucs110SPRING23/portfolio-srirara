import random

answer = random.randrange(1, 11)
print(answer)

for i in range (3):
    guess = int(input("Guess the number from 1-10:"))
    if (guess == answer):
        print("You got it!")
        break
    elif(guess < answer):
        print("Too low")
    else:
        print("Too high")