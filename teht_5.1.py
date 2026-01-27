import random

times = int(input("Dice rolls how many?: "))
total = 0

for i in range(times):
    random_num = random.randint(1, 6)
    total = total + random_num
    order = i + 1
    print(f"{order}. roll = {random_num}")

print(f"Total = {total}")
