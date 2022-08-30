hall_rent = float(input())

cake_price = hall_rent * 0.20
drink_price = cake_price * 0.55
animator_price = hall_rent / 3

total_expenses = hall_rent + cake_price + drink_price + animator_price

print(total_expenses)