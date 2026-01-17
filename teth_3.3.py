
gender = input("Anna sukupuoli: ")
hemo =  int(input("Anna hemoglobiiniarvo: "))



if hemo < (134) and gender == "mies":
    print(f"{hemo} mies hemoglobiini matala")
if hemo < (117) and gender == "nainen":
    print (f"{hemo} nainen hemoglobiini on matala")
elif hemo > (195) and gender == "mies":
    print(f"{hemo} mies hemoglobiini korkea")
elif hemo > (175) and gender == "nainen":
    print(f"{hemo} nainen hemoglobiini korkea")

elif hemo in range(134, 195) and gender == "mies":
    print(f"{hemo} mies hemoglobiini on normaali")

elif hemo in range(117, 175) and gender == "nainen":
    print(f"{hemo} nainen hemoglobiini on normaali")