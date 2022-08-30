import math

count_magnolii = int(input())
cout_zumbuli = int(input())
count_roses = int(input())
count_cactuses = int(input())
gift_price = float(input())

price_magnolii = count_magnolii * 3.25
price_zumbuli = cout_zumbuli * 4
price_roses = count_roses * 3.50
price_cactuses = count_cactuses * 8

total_flower_price = price_magnolii + price_zumbuli + price_roses + price_cactuses
total_profit = total_flower_price * 0.95
#diff_money = abs(gift_price - total_profit)

if total_profit >= gift_price:
    diff_money = abs(gift_price - total_profit)
    print(f"She is left with {math.floor(diff_money)} leva.")
else:
    diff_money = abs(gift_price - total_profit)
    print(f"She will have to borrow {math.ceil(diff_money)} leva.")