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


def strength(password):
    """a score from 0 to 5 and a word for it"""
    score = 0
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    words = ["very weak", "weak", "weak", "medium", "strong", "very strong"]
    return score, words[score]


while True:
    choice = input("1 new password  2 check a password  3 quit: ").strip()
    if choice == "1":
        length = ask_length()
        digits = ask_yes("Include digits?")
        symbols = ask_yes("Include symbols?")
        password = generate(length, digits, symbols)
        score, word = strength(password)
        print("Your password:", password)
        print(f"Strength: {score} of 5, {word}")
    elif choice == "2":
        score, word = strength(input("Type the password to check: "))
        print(f"Strength: {score} of 5, {word}")
        if score < 4:
            print("Tip: use at least 12 characters, with digits, symbols and capital letters.")
    elif choice == "3":
        break
    else:
        print("Choose 1, 2 or 3.")
