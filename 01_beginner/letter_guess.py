"""Letter-by-letter guess (if/else practice).

The secret word is "pasta". You guess the first letter, then the second.
Each check is a separate if/else — this is an early hangman-style idea.
"""

chosen_word = "pasta"
ask_user = input("Guess the first letter: ")
if ask_user == chosen_word[0]:
    print("Choose the next letter")
else:
    print("Incorrect, try again")

ask_user2 = input("Guess your second letter: ")
if ask_user2 == chosen_word[1]:
    print("Choose the next letter")
else:
    print("Incorrect, try again")
