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


need_order = True
money = 0
order = ""

# TODO: 1. create report of coffee machine resources
def report():
    print(
        f"    The current resources are as follows:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")


# TODO: 7. calculate change and serve coffee
def calculate_change(order):
    change = round(money_given - MENU[order]["cost"], 2)
    print(f"You get ${change}change")


def make_coffee(order, resources):
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    return resources



# TODO: 3. Ask for the desired coffee
while need_order:
    sufficient_resources = True
    print("Hello, this is your coffee machine.")
    order = input("What would you like? (espresso/latte/cappuccino). Or enter 'report' to check resources: ").lower()
    need_order = False
    print(order)

    # TODO: 2. Print report of all coffee machine resources

    if order == "report":
        report()
        need_order = True
    elif order != "espresso" and order !="latte" and order !="cappuccino":
        print("invalid input")
        need_order = True
    else:
        for ingredient in (MENU[order]["ingredients"]):
            if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
                print(f"sorry, there is not enough {ingredient}")
                sufficient_resources = False
                need_order = True

                # TODO: 5. ask for money input
        if sufficient_resources:

            money_given = 0.25*int(input("How many quarters? ") or 0)
            money_given += 0.1*int(input("How many dimes? ") or 0)
            money_given += 0.05*int(input("How many nickels? ") or 0)
            money_given += 0.01*int(input("How many pennies? ") or 0)
            # TODO: 6. calculate if money is sufficient
            if money_given < MENU[order]["cost"]:
                print("Sorry, this is not enough money. Money refunded")
                need_order = True
            else:
                calculate_change(order)
                money += MENU[order]["cost"]
            make_coffee(order, resources)
            print(f"Here is your {order}. Thank you and see you again soon!")
            need_order = True






    # TODO: 4. calculate if amount of resources is sufficient/subtract resources




    # TODO: 8. make coffee and store money
