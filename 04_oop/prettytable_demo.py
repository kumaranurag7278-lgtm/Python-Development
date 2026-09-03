"""PrettyTable: a third-party class you can import and use like your own.

Install once: pip install prettytable
This is the same idea as Turtle — you create an object and call methods on it.
"""

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
table.add_row(["Anurag", 18, "Patna"])
table.add_row(["Riya", 20, "Delhi"])
# align is an attribute; 'l' means left-align columns.
table.align = "l"

print(table)
