# Step 2: A Function with Options
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


print(generate(12))
print(generate(8, symbols=False))
print(generate(16, digits=False))
