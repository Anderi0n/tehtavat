import random

darts = int(input("How many darts do you wanna throw?: "))

loops = 0
points = 0
while loops < darts:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        points = points + 1
    loops = loops + 1

tulos = 4 * points / darts
print(tulos)