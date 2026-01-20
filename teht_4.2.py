tuuma = int(input("Anna tuuma: "))



while tuuma:
    print(f" {tuuma} tuuma on {tuuma * 2.54} cm")
    tuuma = int(input("Anna tuuma: "))
    if tuuma < 0:
        break