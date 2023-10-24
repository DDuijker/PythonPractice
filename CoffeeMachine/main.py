from information import MENU
from information import resources

money = 0
is_on = True
QUARTER_VALUE = 0.25
DIME_VALUE = 0.1
NICKLE_VALUE = 0.05
PENNY_VALUE = 0.01


def current_resources():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


def sufficient_resources(coffee):
    """Checks if there are enough resources to make the drink, returns boolean"""
    menu_ingredients = MENU[coffee]['ingredients']
    for ingredient in menu_ingredients:
        if resources[ingredient] >= menu_ingredients[ingredient]:
            return True
        else:
            print(f"Sorry there is not enough {ingredient}")
            return False


def calculate_total(amount_of_quarters, amount_of_dimes, amount_of_nickles, amount_of_pennies):
    """Calculates the total value based on the amount of quarters, dimes, nickles and pennies.
    Returns total rounded to 2 decimals"""
    money_input = 0
    money_input += amount_of_quarters * QUARTER_VALUE
    money_input += amount_of_dimes * DIME_VALUE
    money_input += amount_of_nickles * NICKLE_VALUE
    money_input += amount_of_pennies * PENNY_VALUE
    return round(money_input, 2)


def add_money(coffee_cost):
    global money
    money += coffee_cost


def check_transaction_successful(money_inserted, coffee):
    """Checks if the user has enough money to purchase the drink. Returns boolean"""
    cost = MENU[coffee]['cost']
    # Compare amount given to necessary amount
    if money_inserted >= cost:
        # Enough? Cost of the drink gets added to the machine as the profit (money in report (current resources))
        add_money(cost)
        # If user has inserted too much money, refund the change (rounded to 2 decimals)
        if money_inserted - cost > 0:
            change = round(money_inserted - cost, 2)
            print(f"Here is ${change} dollars in change.")
            return True
    else:
        # Not enough? Print "Sorry that's not enough money. Money refunded"
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(type_of_coffee):
    """Ingredients to make the drink should be deducted from the resources"""
    for ingredient in MENU[type_of_coffee]['ingredients']:
        # For every ingredient in the necessary ingredients remove the value from the resources list
        necessary_resource = MENU[type_of_coffee]['ingredients'][ingredient]
        resources[ingredient] -= necessary_resource
    print(f"Here is your {type_of_coffee}. Enjoy!")


while is_on:
    # Ask for user input
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # If the user input is 'off' stop the machine
    if coffee_type == "off":
        is_on = False
    # Print the current resources
    elif coffee_type == "report":
        current_resources()
    # Check if user has put in a coffee type
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        # Check if there are enough resources to make the coffee
        if sufficient_resources(coffee_type):
            # Process coins
            quarters = float(input("How many quarters? "))
            dimes = float(input("How many dimes? "))
            nickles = float(input("How many nickles? "))
            pennies = float(input("How many pennies? "))
            total = calculate_total(quarters, dimes, nickles, pennies)
            # Check if the transaction is successful
            if check_transaction_successful(total, coffee_type):
                make_coffee(coffee_type)




