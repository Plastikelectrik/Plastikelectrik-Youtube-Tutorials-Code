import random


def ask_number():
    # ask again until the player types a whole number from 1 to 100
    while True:
        text = input("Your guess: ")
        if text.isdigit() and 1 <= int(text) <= 100:
            return int(text)
        print("Please type a whole number from 1 to 100.")



def play_round():
    # one full game; it returns the number of attempts
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
    return attempts


best = None                          # no game played yet
while True:
    attempts = play_round()
    if best is None or attempts < best:
        best = attempts
        print("New best score!")
    print("Best so far:", best, "attempts")
    again = input("Play again? (y/n) ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break
