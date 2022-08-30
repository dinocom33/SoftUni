sq_meters = float(input())
price_per_sq_meters = 7.61
price_without_disc = sq_meters * price_per_sq_meters
price_with_disc = price_without_disc * 0.82

final_price = (sq_meters * price_per_sq_meters)
print(f"The final price is {price_with_disc} lv.")
discount = (price_without_disc - price_with_disc)
print(f"The discount is {discount} lv.")
