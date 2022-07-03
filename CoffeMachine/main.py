from menu import MENU
from replit import clear


def report(elements):
    print(f"Water: {elements['Water']}ml: ")
    print(f"Milk: {elements['Milk']}ml: ")
    print(f"Coffee: {elements['Coffee']}g: ")
    print(f"Money: R${elements['Money']}: ")


def check_resources(choose, menu_in_function, resources_in_function):
    resources_ok = True
    for drink in menu_in_function:
        if choose == drink:
            for ingredient in menu_in_function[drink]['ingredients']:
                if menu_in_function[drink]['ingredients'][ingredient] > resources_in_function[ingredient]:
                    print(f'Sorry there is not enough {ingredient}.')
                    resources_ok = False
    return resources_ok


def process_coins(drink):
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < MENU[drink]['cost']:
        print('Sorry that is not enough money. Money refunded.')
        return 0
    elif total > MENU[drink]['cost']:
        change = total - MENU[drink]['cost']
        print(f'Here is ${change:.2f} dollars in change.')
        total = MENU[drink]['cost']
    return total


def do_drink(drink, resources_in_function):
    for ingredient in MENU[drink]['ingredients']:
        resources_in_function[ingredient] -= MENU[drink]['ingredients'][ingredient]
    print(f'Here is your {drink}!!! Enjoy!')
    return resources_in_function


def coffee_machine():
    resources = {'Water': 1000, 'Milk': 1000, 'Coffee': 500, 'Money': 0}
    while True:
        decision = input('What would you like? (espresso/latte/cappuccino): ')
        if decision in MENU:
            are_resources = check_resources(decision, MENU, resources)
            if are_resources:
                valor = process_coins(decision)
                if valor != 0:
                    resources['Money'] += valor
                    resources = do_drink(decision, resources)
        elif decision == 'report':
            report(resources)
        elif decision == 'off':
            print('Turning off.')
            break
        clear()


coffee_machine()
