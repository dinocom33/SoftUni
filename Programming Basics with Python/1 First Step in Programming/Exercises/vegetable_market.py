veg_price = float(input())
fruit_price = float(input())
total_veg_kg = int(input())
total_fruit_kg = int(input())

veg_income = veg_price * total_veg_kg
fruit_income = fruit_price * total_fruit_kg
total_income = (veg_income + fruit_income) / 1.94

print(f"{total_income:.2f}")