fuel_type = input()
fuel_liters = float(input())
club_card = input()

gasoline_price = 0
gas_price = 0
diesel_price = 0
total_sum = 0

if fuel_type == "Gasoline":
    if club_card == "Yes":
        gasoline_price = 2.04
        total_sum = gasoline_price * fuel_liters
    else:
        gasoline_price = 2.22
        total_sum = gasoline_price * fuel_liters
elif fuel_type == "Gas":
    if club_card == "Yes":
        gas_price = 0.85
        total_sum = gas_price * fuel_liters
    else:
        gas_price = 0.93
        total_sum = gas_price * fuel_liters
elif fuel_type == "Diesel":
    if club_card == "Yes":
        diesel_price = 2.21
        total_sum = diesel_price * fuel_liters
    else:
        diesel_price = 2.33
        total_sum = diesel_price * fuel_liters

if 20 <= fuel_liters <= 25:
    total_sum = total_sum * 0.92
elif fuel_liters > 25:
    total_sum = total_sum * 0.90

print(f"{total_sum:.2f} lv.")