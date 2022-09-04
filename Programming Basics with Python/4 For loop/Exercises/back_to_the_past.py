start_money = float(input())
year_to_live = int(input())

money_left = start_money
ages = 18

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        money_left = money_left - 12000
    elif i % 2 != 0:
        money_left = money_left - (12000 + (ages * 50))
    ages = ages + 1

diff = abs(start_money - money_left)

if money_left < 0:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")
elif start_money >= money_left:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
