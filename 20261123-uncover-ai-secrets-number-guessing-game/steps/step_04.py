# Step 4: Check the Input
import random


def ask_number():
    # ask again until the player types a whole number from 1 to 100
    while True:
        text = input("Your guess: ")
        if text.isdigit() and 1 <= int(text) <= 100:
            return int(text)
        print("Please type a whole number from 1 to 100.")


secret = random.randint(1, 100)
print("I am thinking of a number from 1 to 100.")

guess = 0
attempts = 0
while guess != secret:
    guess = ask_number()
    attempts += 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")

print(f"Correct! You needed {attempts} attempts.")
