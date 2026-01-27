prime = int(input("Give number: "))


for i in range(2, prime):
    if prime < 2:
        print("Not prime")
        break
    if prime % i == 0:
        is_prime = False
        print("Not prime")


else:
    print("Is prime")


