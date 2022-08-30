budget = float(input())
statists_count = int(input())
outfit_price = float(input())

dekor_price = budget * 0.10
total_outfit_price = statists_count * outfit_price

if statists_count > 150:
    total_outfit_price = total_outfit_price * 0.90

total_sum = dekor_price + total_outfit_price
diff = abs(total_sum - budget)

if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

