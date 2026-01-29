

def gas_prices(gallon):
    bensin_gallon = 3.785
    liter =  bensin_gallon * gallon
    return liter


while True:
    gas_station = float(input("How many gallons do you want to convert into liters? "))
    if gas_station < 0:
        print("Negatiivinen numero")
        break
    print(f"{gas_prices(gas_station)}")
