"""Coffee machine simulator.

Uses a MENU dictionary, resource checks, coin input, and a loop until
the user types "off". Type "report" to see remaining water/coffee/milk.
"""

resources = {
    "water": 1000,
    "coffee": 500,
    "milk": 800,
}
profit = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}


def check_resources(order_ingredient):
    """Return False if any ingredient is short, else True."""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print("Sorry, we don't have enough resources")
            return False
    return True


def process_coins():
    """Ask for coin counts and return the total in dollars."""
    print("Put your coins into the machine")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many pennies? ")) * 0.01
    total += int(input("How many nickles? ")) * 0.05
    return total


def is_transaction_successful(money_received, drink_cost):
    """Accept payment if it covers the drink cost; add to profit."""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}")
        profit += money_received
        return True
    else:
        print("Transaction failed")
        return False


def coffee_make(drink_name, order_ingredient):
    """Subtract ingredients and serve the drink."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
        print(f"Here's your {drink_name}")


is_on = True
while is_on:
    user_choice = input("What would you like? espresso / latte / cappuccino? or report? ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"water: {resources['water']}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                coffee_make(user_choice, drink["ingredients"])
