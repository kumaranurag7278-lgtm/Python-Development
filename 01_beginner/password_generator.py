"""Password generator.

Asks how many letters, digits, and symbols you want, builds a list of
random characters, shuffles them, then joins them into one string.
"""

import random
import string

# list(...) turns the string of all letters into a real list of characters.
# (list[string.ascii_letters] is a type hint, not a list of letters.)
letters = list(string.ascii_letters)
digits = list(string.digits)
# Symbols: ASCII 33–126 that are not letters or digits (!, @, #, ...).
symbols = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]

print("Hey there! Welcome to password generator")
num_letters = int(input("Please input how many letters you would like in your password\n"))
num_digits = int(input("Please input how many digits you would like in your password\n"))
num_symbols = int(input("Please input how many symbols you would like in your password\n"))

# Build a list first so we can shuffle the order (harder-to-guess password).
password_list = []
for char in range(0, num_letters):
    password_list += random.choice(letters)
for char in range(0, num_digits):
    password_list += random.choice(digits)
for char in range(0, num_symbols):
    password_list += random.choice(symbols)

# shuffle() rearranges the list in place and returns None — do not print it.
random.shuffle(password_list)

password = " "
for char in password_list:
    password += char
print(password)

# --- easier version (no shuffle): add characters in letter-digit-symbol order ---
# password = " "
# for char in range(0, num_letters):
#     password += random.choice(letters)
# for char in range(0, num_digits):
#     password += random.choice(digits)
# for char in range(0, num_symbols):
#     password += random.choice(symbols)
# print(password)

# --- FizzBuzz / loop practice from this lesson ---
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
