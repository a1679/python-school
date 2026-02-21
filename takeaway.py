#fix definition then once that is doen do phone number and other stuff like implimenting the def

import random
import sys
from word2number import w2n

def age_checker(min_val=15):
    while True:
        user_input = input("What is your age? ").lower()

        try:
            number = w2n.word_to_num(user_input)
        except ValueError:
            try:
                number = int(user_input)
            except ValueError:
                print("That's not a valid age. Try again.")
                continue

        if min_val <= number:
            return number
        else:
            print(f"Your number must be at least 15. Your too young.")
            sys.exit(0)

def checker_confirm():
    while True:
        continue1 = input(
            f"You have ordered {foods}, would you like anything else? "
            "Say 'Yes' or 'No': "
        ).lower()

        if continue1 == "yes":
            return True
        elif continue1 == "no":
            return False
        else:
            print("That is not a valid option. Please try again.")



age = age_checker()

print("Here is the menu:")

menu = {
    "Chicken": 12,
    "Beef": 15,
    "Pork": 13,
    "Rice": 5
}

order = []

print("Here is the menu:")

for food in menu:
    print(f"{food} - ${menu[food]}")



total_price = 0
while True:
    foods = input("What would you like? ")

    if foods in menu:
        order.append(foods)
        total_price += menu[foods]   # add price

        if not checker_confirm():
            break

    else:
        print(f"{foods} is not on the menu, please order again.")



print(f"You have ordered: {order}.")
print(f"Your order costs, ${total_price}. To confim please give your phone number and name.")
phone = int(input("Phone Number: "))
name = input("Name:")
print("ORDER CONFIRMED " + name + " !!!")
