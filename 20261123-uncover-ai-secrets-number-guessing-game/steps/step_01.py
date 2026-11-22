# Step 1: A Secret Number
import random

secret = random.randint(1, 100)      # a whole number from 1 to 100
print("I am thinking of a number from 1 to 100.")

guess = int(input("Your guess: "))
if guess == secret:
    print("Correct, well done!")
else:
    print("No, it was", secret)
