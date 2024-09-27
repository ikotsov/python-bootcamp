import state


def game():
    on = True

    while on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == 'latte' or user_input == 'espresso' or user_input == 'cappuccino':
            handle_coffee_input(user_input)
        elif user_input == 'report':
            print(report())
        elif user_input == "off":
            on = False
        else:
            print("Wrong input")


def handle_coffee_input(coffee_type):
    enough_resources = enough_water(coffee_type) and enough_coffee(
        coffee_type) if coffee_type == "espresso" else enough_water(coffee_type) and enough_milk(
        coffee_type) and enough_coffee(coffee_type)

    if not enough_resources:
        if not enough_water(coffee_type):
            print("Sorry there is not enough water.")
            return
        if not enough_milk(coffee_type):
            print("Sorry there is not enough milk.")
            return
        if not enough_coffee(coffee_type):
            print("Sorry there is not enough coffee.")
            return

    coins_inserted = process_coins()
    coffee_costs = state.MENU[coffee_type]["cost"]
    if coins_inserted < coffee_costs:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = coins_inserted - coffee_costs
        if change > 0:
            print(f"Here is ${round(change, 2)} dollars in change.")

        state.profit += coffee_costs
        deduct_resources(coffee_type)
        print(f"Here is your {coffee_type} ☕️. Enjoy!")


def enough_water(coffee_type):
    water_left = state.MENU[coffee_type]["ingredients"]["water"]
    return water_left < state.resources["water"]


def enough_milk(coffee_type):
    milk_left = state.MENU[coffee_type]["ingredients"]["milk"]
    return milk_left < state.resources["milk"]


def enough_coffee(coffee_type):
    coffee_left = state.MENU[coffee_type]["ingredients"]["coffee"]
    return coffee_left < state.resources["coffee"]


QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01


def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    return (quarters * QUARTER) + (dimes * DIME) + (nickles * NICKLE) + (pennies * PENNY)


def deduct_resources(coffee_type):
    ingredients = state.MENU[coffee_type]["ingredients"]
    state.resources["water"] = state.resources["water"] - ingredients["water"]
    state.resources["coffee"] = state.resources["coffee"] - ingredients["coffee"]
    if coffee_type != "espresso":
        state.resources["milk"] = state.resources["milk"] - ingredients["milk"]


def report():
    return f"Water: {state.resources['water']}ml \nMilk: {state.resources['milk']}ml \nCoffee: {state.resources['coffee']}g \nMoney: ${state.profit}"


game()
