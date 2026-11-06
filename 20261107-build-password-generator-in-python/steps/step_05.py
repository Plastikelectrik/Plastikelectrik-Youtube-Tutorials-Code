# Step 5: Safer Randomness
import secrets
import string

SYMBOLS = "!@#$%&*?-_"



def generate(length, digits=True, symbols=True):
    """a random password of the given length, made from the chosen kinds of characters"""
    kinds = [string.ascii_lowercase, string.ascii_uppercase]
    if digits:
        kinds.append(string.digits)
    if symbols:
        kinds.append(SYMBOLS)
    # one character of every kind, so none is missing, then the rest from all of them
    chars = [secrets.choice(kind) for kind in kinds]
    pool = "".join(kinds)
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def ask_length():
    # a whole number from 8 to 64
    while True:
        text = input("How many characters? (8-64) ").strip()
        if text.isdigit() and 8 <= int(text) <= 64:
            return int(text)
        print("Please type a number from 8 to 64.")


def ask_yes(question):
    # True for yes, False for no; anything else is asked again
    while True:
        answer = input(question + " (y/n) ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


length = ask_length()
digits = ask_yes("Include digits?")
symbols = ask_yes("Include symbols?")
print("Your password:", generate(length, digits, symbols))
