# Step 3: Count the Attempts
import random

secret = random.randint(1, 100)
print("I am thinking of a number from 1 to 100.")

guess = 0
attempts = 0
while guess != secret:
    guess = int(input("Your guess: "))
    attempts += 1                    # one more try
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")

print(f"Correct! You needed {attempts} attempts.")
