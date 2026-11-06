# Step 3: Ask the User
import random
import string



def generate(length, digits=True, symbols=True):
    """a random password of the given length, made from the chosen kinds of characters"""
    pool = string.ascii_letters
    if digits:
        pool += string.digits
    if symbols:
        pool += "!@#$%&*?-_"
    return "".join(random.choice(pool) for _ in range(length))


length = int(input("How many characters? "))
digits = input("Include digits? (y/n) ").strip().lower() == "y"
symbols = input("Include symbols? (y/n) ").strip().lower() == "y"
print("Your password:", generate(length, digits, symbols))
