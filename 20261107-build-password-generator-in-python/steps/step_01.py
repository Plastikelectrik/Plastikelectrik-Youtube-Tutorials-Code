# Step 1: Random Letters
import random
import string

# a password of 12 random letters, small and capital
letters = string.ascii_letters
password = ""
for _ in range(12):
    password += random.choice(letters)
print("Your password:", password)
