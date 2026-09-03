"""Randomisation and lists.

The live code picks who pays the bill. Commented examples show randint,
random(), uniform, heads/tails, and nested lists.
Rock-paper-scissors was started but not finished.
"""

import random

friends = ["alice ", "bob", "charlie", "david", "falana"]
# Option 1: random.choice picks one item from the list.
# print(random.choice(friends))
# Option 2 (same idea with an index):
# random_index = random.randint(0, 4)
# print(friends[random_index])

# --- earlier random practice ---
# random_integer = random.randint(1, 10)
# random_number = random.random() * 10
# random_float = random.uniform(1, 10)

# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("heads")
# else:
#     print("tails")

# Nested list (list inside a list):
# fruits = ["strawberry", "grapes", "apples", "peaches"]
# vegetable = ["tomatoes", "potatoes", "spinich"]
# dirty_dozen = [fruits, vegetable]
# print(dirty_dozen)

# rock paper scissors game — not implemented yet
