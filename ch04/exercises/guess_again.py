import random

answer = random.randrange(1, 1001)
#print(answer)

correct = False
numGuesses = 0
while correct == False:
    numGuesses += 1
    guess = int(input("Guess the number from 1-1000:"))
    if (guess == answer):
        print("You got it!")
        print("It took you", numGuesses, "guesses to get it right. The correct answer is:", answer)
        correct = True
    elif(guess < answer):
          print("Too low")
    else:
        print("Too high")

#my guess is that the max number of guesses using a binary search would be 10 because log base 2 of 1000 is 9.9