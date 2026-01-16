levi = float(input("Anna leivikisien määrä: "))
naula = float(input("Anna naulojen määrä: "))
luoti = float(input("Anna luotijen määrä: "))

levi1 = levi * 20
naula1 = naula + levi1
luoti1 = naula1 * 32 + 13.5
g = luoti1 * 13.3
kg = g / 1000
g2 = g % 1000

print(f"{str(kg)[:2]}, kilogrammaa eli {str(g2)[:6]} grammaa.")



