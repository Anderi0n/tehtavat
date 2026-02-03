kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu",
             "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu",
             "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

vuodenajannimet = ("Talvi", "Talvi", "Keväät",
             "Keväät", "Keväät", "Kesä", "Kesä", "Kesä",
             "Syksy", "Syksy", "Syksy", "Talvi")

vuodenajat = int(input("Anna kuukauden numero: "))
vuodenajannimet = vuodenajannimet[vuodenajat-1]

print(vuodenajannimet)



