"""Number manipulation: rounding, floor division, and f-strings.

Also estimates remaining weeks of life if you live to 90.
"""

# int() drops the decimal part (truncates toward zero).
print(int(8 / 3))
# Floor division // always rounds down.
print(8 // 3)

# Change a value based on its previous value.
score = 0
score += 1
print(score)

# Weeks left until age 90 (52 weeks per year).
age = input("Your age? ")
years_left = 90 - int(age)
weeks = years_left * 52
print(f"You have {weeks} left to live so live happily")
