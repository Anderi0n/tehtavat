import random

def dice_roll(side):
    return random.randint(1,side)

dice_amount = int(input("How many sides does your dice have? "))
side = dice_amount

order = 1

while 0 < dice_amount:
    results = dice_roll(side)

    if side == results:
        print(f"This is the amount from the dice {results}. It took {order} rolls!")
        break
    order = order + 1

