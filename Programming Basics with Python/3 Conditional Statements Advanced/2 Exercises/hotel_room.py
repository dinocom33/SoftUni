month = input()
sleep_count = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < sleep_count < 14:
        studio_price = studio_price * 0.95
    elif sleep_count > 14:
        studio_price = studio_price * 0.70
        apartment_price = apartment_price * 0.90
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if sleep_count > 14:
        studio_price = studio_price * 0.80
        apartment_price = apartment_price * 0.90
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if sleep_count > 14:
        apartment_price = apartment_price * 0.90

total_studio_expenses = studio_price * sleep_count
total_apartment_expenses = apartment_price * sleep_count

print(f"Apartment: {total_apartment_expenses:.2f} lv.")
print(f"Studio: {total_studio_expenses:.2f} lv.")