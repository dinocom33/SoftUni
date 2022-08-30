fuel_type = input()
tank_litres = int(input())

if tank_litres >= 25 and (fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"):
    print(f"You have enough {fuel_type.lower()}.")
elif tank_litres < 25 and (fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"):
    print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")