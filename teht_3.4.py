vuosi = int(input("Anna vuosiluku: "))

may = vuosi % 100

if vuosi % 4 == 0 and vuosi % 100 != 0 and vuosi % 400 == 0:
    print(f"{vuosi} On karkausvuosi")




else: print("Ei ole karkausvuosi")
