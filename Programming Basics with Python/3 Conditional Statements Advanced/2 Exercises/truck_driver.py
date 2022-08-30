season = input()
km_per_month = float(input())

salary = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.75) * 4
    elif season == "Summer":
        salary = (km_per_month * 0.90) * 4
    else:
        salary = (km_per_month * 1.05) * 4
elif km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.95) * 4
    elif season == "Summer":
        salary = (km_per_month * 1.10) * 4
    else:
        salary = (km_per_month * 1.25) * 4
elif km_per_month <= 20000:
    salary = (km_per_month * 1.45) * 4

salary = salary * 0.90

print(f"{salary:.2f}")