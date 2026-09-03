"""Treasure Island: nested if/else adventure game.

The live program is the treasure hunt. Commented blocks below are earlier
if/else practice: rollercoaster, odd/even, BMI, leap year, and pizza order.
"""

print("Welcome to Treasure Island\nYour mission is to find the treasure!")
route_01 = input("Where do you want to go? left or right: ")
if route_01 == "left":
    route_02 = input(
        "You are now at the shore of a lake.\n"
        "Do you want to wait for the boat or swim to the next shore? "
    )
    if route_02 == "wait":
        route_03 = input(
            "A boat has arrived. Now you can go to Treasure Island.\n"
            "Choose one door among red, blue, yellow: "
        )
        if route_03 == "yellow":
            print("Finally you found the one piece. Great!")
        elif route_03 == "red":
            print("You are burnt to death.")
        else:
            print("You were eaten by a lion alive.")
    else:
        print("You were eaten by a crocodile alive.")
else:
    print("You fell into a hole! Game over for you.")

# --- earlier if/else practice ---
# height = int(input("what is your height in CM?"))
# if height >= 120:
#     print("you can ride the rollercoaster.")
# else:
#     print("too short to exist! so sorry you can not ride this rollercoaster.")

# number = int(input("input your number!  "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
