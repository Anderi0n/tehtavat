

user1 = ("python")
password1 = ("rules")
attempt = 1

while attempt <= 6:
    user = input("Anna käyttäjä tunnus: ")
    password = input("Anna salasana: ")
    if user1 == user and password1 == password:
        print("Tervetuloa")
        break
    attempt = attempt + 1
    print("Pääsy evätty, salasana tai käyttäjä tunnus on väärin")

