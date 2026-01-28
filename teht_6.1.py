import random


def dice_roll():

    return random.randint(1,6)

order = 1
while True:
    results = dice_roll()
    if results == 6:
        print(f"This is the amount from the dice {results}. Try number {order}.")
        break
    print(f"This is the amount from the dice {results}. Try number {order}.")
    order = order + 1


