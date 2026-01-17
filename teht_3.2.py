lux = input("Anna hyttiluokka: ")
upperlux = lux.upper()
if lux == ("lux"):
    print(f" {upperlux} on parvekkeellinen hytti yläkannella.")
elif lux == ("A"):
    print(f"{upperlux} on ikkunallinen hytti autokannen yläpuolella.")
elif lux == ("B"):
    print(f"{upperlux} on ikkunaton hytti autokannen yläpuolella.")
elif lux == ("C"):
    print(f"{upperlux} on ikkunaton hytti autokannen alapuolella.")
if lux not in ("lux", "A", "B", "C"):
    print("Virheellinen hyttiluokka.")


