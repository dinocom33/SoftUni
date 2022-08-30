flower_type = input()
count_flower = int(input())
budget = int(input())

total_price = 0


if flower_type == "Roses":
    total_price = count_flower * 5
    if count_flower > 80:
        total_price = total_price * 0.90
elif flower_type == "Dahlias":
    total_price = count_flower * 3.80
    if count_flower > 90:
        total_price = total_price * 0.85
elif flower_type == "Tulips":
    total_price = count_flower * 2.80
    if count_flower > 80:
        total_price = total_price * 0.85
elif flower_type == "Narcissus":
    total_price = count_flower * 3
    if count_flower < 120:
        total_price = total_price * 1.15
elif flower_type == "Gladiolus":
    total_price = count_flower * 2.50
    if count_flower < 80:
        total_price = total_price * 1.20

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_flower} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")