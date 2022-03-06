MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def is_resouce_sufficient(order_ingredients):
    """Do we have enough ingredients for this order"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Collect money"""
    total = int(input("Enter Quarters ")) * 0.25
    total += int(input("Enter Dimes ")) * 0.1
    total += int(input("Enter Nickles ")) * 0.05
    total += int(input("Enter Pennies ")) * 0.01
    return total


def is_transaction_successful(payment, drink_cost):
    """Make sure there is enough money"""
    if payment >= drink_cost:
        change = round(payment - drink_cost,2)
        print(f"Here is your change: {change}")
        global profit
        profit += drink_cost
        return True
    print("Sorry that's not enough money. Money refunded")
    return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the require ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resouce_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])