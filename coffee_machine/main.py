from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

machine_is_on = True
# put everything in a while loop
while machine_is_on:
    # Get user's choice
    choice = input(f"What would you like? {menu.get_items()[:-1]}: ").lower()
    if choice == 'off':
        # exit
        machine_is_on = False
    elif choice == 'report':
        coffee_machine.report()
        register.report()
    else:
        # check if item exists
        drink = menu.find_drink(choice)
        # if drink is valid
        # check if resources are available for this item
        if coffee_machine.is_resource_sufficient(drink) and register.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
