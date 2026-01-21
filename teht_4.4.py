
import random
peli = int(input("Anna arpaus numero: "))
arpo = random.randint(1, 10)
while not peli == arpo:
    if peli < 1 or peli > 10:
        print(f"{peli} is not between 1-10")
    if peli < arpo:
        print(f"{peli} is too small ")
    elif peli > arpo:
        print(f"{peli} is too large")
    peli = int(input("Anna arpaus numero: "))

if peli == arpo:
        print("YOU HAVE WON")