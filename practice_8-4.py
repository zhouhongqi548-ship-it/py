MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 140,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 160,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    try:
        total = int(input("How many NT$ 50?: ")) * 50
        total += int(input("How many NT$ 10?: ")) * 10
        total += int(input("How many NT$ 5?: ")) * 5
        return total
    except ValueError:
        print("Invalid input. Assuming 0 coins for this slot.")
        return 0


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is NT$ {change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: NT${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        # 檢查資源是否充足
        if is_resource_sufficient(drink["ingredients"]):
            # 處理投幣
            coins_inserted = process_coins()
            # 檢查交易是否成功
            if is_transaction_successful(coins_inserted, drink["cost"]):
                # 製作咖啡並扣除原料
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")