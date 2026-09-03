"""Tip calculator.

Asks for the bill, a tip percent, and how many people are splitting,
then prints how much each person should pay.
"""

total_bill = float(input("What was the total bill, sir? $"))
tip = int(input("How much percent tip would you like to give? 10, 12, 20? "))
split = int(input("How many people would you like to split the bill with? "))

# Original formula: tip percent applied to the tip value itself (not the bill).
total_amount = tip / 100 * tip

total_amount_per_person = (total_amount + total_bill) / split
final_amount = round(total_amount_per_person, 2)
print(f"Each person should pay {final_amount}")
