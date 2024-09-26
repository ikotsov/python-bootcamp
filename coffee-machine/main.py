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


def report():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee {resources['coffee']}g"


def check_resources(coffee_type):
    if get_menu_water(coffee_type) > resources["water"]:
        print(f"Sorry there is not enough water.")

    if get_menu_milk(coffee_type) > resources["milk"]:
        print(f"Sorry there is not enough milk.")

    if get_menu_coffee(coffee_type) > resources["coffee"]:
        print(f"Sorry there is not enough coffee.")


def get_menu_water(coffee_type):
    return MENU[coffee_type]["ingredients"]["water"]


def get_menu_milk(coffee_type):
    return MENU[coffee_type]["ingredients"]["milk"]


def get_menu_coffee(coffee_type):
    return MENU[coffee_type]["ingredients"]["coffee"]


active = True

while active:
    type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if type_of_coffee == 'latte' or type_of_coffee == 'espresso' or type_of_coffee == 'cappuccino':
        check_resources(type_of_coffee)

    if type_of_coffee == 'report':
        print(report())

    if type_of_coffee == "off":
        active = False
