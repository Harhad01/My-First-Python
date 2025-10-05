MENU = {
    "espresso": {
        "ingredients": {"water": 500, "coffee": 300},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 500, "milk": 600, "coffee": 36},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 500, "milk": 600, "coffee": 36},
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 30000,
    "milk": 20000,
    "coffee": 1000,
}

def is_resource_sufficient(order_ingredients):
    """Returns True if there are enough resources."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, otherwise False."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def process_coins():
    """Returns the total amount of coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    print(f"Total inserted: ${total}")
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
        print("Coffee machine is turning off... Bye!")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








