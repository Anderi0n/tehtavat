number = []

while True:
    num = input("Anna numero: ")
    if num == "":
         break
    num_int = int(num)
    number.append(num_int)

print(f"{sorted(number)} lista")
