from state import MENU, resources


def game():
    on = True

    while on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == 'latte' or user_input == 'espresso' or user_input == 'cappuccino':
            if not enough_water(user_input):
                print("Sorry there is not enough water.")
            if not enough_milk(user_input):
                print("Sorry there is not enough milk.")
            if not enough_coffee(user_input):
                print("Sorry there is not enough coffee.")

        if user_input == 'report':
            print(report())

        if user_input == "off":
            on = False


def enough_water(coffee_type):
    water_left = MENU[coffee_type]["ingredients"]["water"]
    return water_left < resources["water"]


def enough_milk(coffee_type):
    milk_left = MENU[coffee_type]["ingredients"]["milk"]
    return milk_left < resources["milk"]


def enough_coffee(coffee_type):
    coffee_left = MENU[coffee_type]["ingredients"]["coffee"]
    return coffee_left < resources["coffee"]


def report():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee {resources['coffee']}g"


game()
