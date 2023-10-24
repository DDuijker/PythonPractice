from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


while turn_on:
    user_input = input("What would you like? (espresso/latte/cappucinno): ").lower()
    if user_input == "off":
        turn_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(user_input)
        # Check sufficient resources
        sufficient_resources = coffee_maker.is_resource_sufficient(coffee)
        if sufficient_resources and coffee is not None:
            success = money_machine.make_payment(coffee.cost)
            if success:
                coffee_maker.make_coffee(coffee)




