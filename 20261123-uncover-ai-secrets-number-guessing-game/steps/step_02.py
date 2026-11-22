# Step 2: Keep Guessing with Hints
import random

secret = random.randint(1, 100)
print("I am thinking of a number from 1 to 100.")

guess = 0
while guess != secret:               # repeat until the player finds it
    guess = int(input("Your guess: "))
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")

print("Correct, well done!")
